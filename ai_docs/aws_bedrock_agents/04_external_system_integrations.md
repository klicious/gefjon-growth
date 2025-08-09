# External System Integration Specifications

## Executive Summary

This document details the specific integrations required to connect the AI hiring automation system with existing external systems: Dooray Task for candidate submissions, Outlook for email-based resumes, and HR communication via email. Each integration includes authentication methods, API specifications, data formats, and error handling procedures.

---

## Integration Architecture Overview

```mermaid
graph LR
    A[Dooray Task] --> B[Intake Agent]
    C[Outlook Email] --> B
    B --> D[Candidate Processing Pipeline]
    D --> E[Communication Agent]
    E --> F[hr@dunamiscap.com]
    
    B --> G[S3 Bucket]
    B --> H[DynamoDB]
    E --> I[SES Email Service]
```

---

## 1. Dooray Task Integration

### Overview
Automated monitoring of Dooray Task projects for new candidate submissions with resume attachments.

### Authentication Configuration

```python
class DoorayTaskConfig:
    """Dooray Task API Configuration"""
    BASE_URL = "https://api.dooray.com"
    API_VERSION = "v2"
    
    # Authentication
    TOKEN_TYPE = "Bearer"
    TOKEN_ENDPOINT = "https://api.dooray.com/oauth2/token"
    
    # Project Configuration
    HIRING_PROJECT_ID = "your-project-id"
    TASK_FILTER_LABELS = ["candidate", "resume", "hiring"]
    
    # Polling Configuration
    POLL_INTERVAL_SECONDS = 300  # 5 minutes
    LOOKBACK_HOURS = 24
```

### API Integration Implementation

```python
import requests
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class DoorayTaskIntegration:
    def __init__(self, access_token: str, project_id: str):
        self.access_token = access_token
        self.project_id = project_id
        self.base_url = "https://api.dooray.com/v2"
        self.headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
    
    def get_new_candidate_tasks(self) -> List[Dict]:
        """
        Retrieve new tasks with candidate submissions
        Returns list of tasks with resume attachments
        """
        try:
            # Calculate lookback time
            since_time = datetime.now() - timedelta(hours=24)
            since_timestamp = since_time.isoformat() + 'Z'
            
            # API endpoint for tasks
            url = f"{self.base_url}/projects/{self.project_id}/tasks"
            
            # Query parameters
            params = {
                'createdAt': f'since:{since_timestamp}',
                'hasAttachment': True,
                'state': 'registered',  # Only new tasks
                'size': 100  # Max tasks per request
            }
            
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            
            tasks = response.json().get('result', [])
            
            # Filter tasks with resume-like attachments
            candidate_tasks = []
            for task in tasks:
                if self._has_resume_attachment(task):
                    candidate_tasks.append(self._process_task(task))
                    
            return candidate_tasks
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Dooray API error: {str(e)}")
            raise
    
    def _has_resume_attachment(self, task: Dict) -> bool:
        """Check if task has resume-like attachments"""
        attachments = task.get('attachments', [])
        resume_extensions = {'.pdf', '.doc', '.docx'}
        
        for attachment in attachments:
            filename = attachment.get('fileName', '').lower()
            if any(filename.endswith(ext) for ext in resume_extensions):
                return True
        return False
    
    def _process_task(self, task: Dict) -> Dict:
        """Process and normalize task data"""
        return {
            'taskId': task['id'],
            'title': task['subject'],
            'content': task['body'],
            'createdDate': task['createdAt'],
            'submitterEmail': task['createdBy']['emailAddress'],
            'attachments': [
                {
                    'fileName': att['fileName'],
                    'fileSize': att['size'],
                    'downloadUrl': att['downloadUrl'],
                    'mimeType': att.get('mimeType', 'application/octet-stream')
                }
                for att in task.get('attachments', [])
            ],
            'source': 'dooray_task'
        }
    
    def download_attachment(self, download_url: str) -> bytes:
        """Download attachment file"""
        response = requests.get(download_url, headers=self.headers)
        response.raise_for_status()
        return response.content
    
    def mark_task_processed(self, task_id: str) -> bool:
        """Mark task as processed to avoid reprocessing"""
        try:
            url = f"{self.base_url}/projects/{self.project_id}/tasks/{task_id}"
            
            # Add processed label or update status
            update_data = {
                'milestone': {'id': 'processed'},
                'tags': [{'name': 'ai-processed'}]
            }
            
            response = requests.put(url, headers=self.headers, json=update_data)
            response.raise_for_status()
            return True
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error marking task processed: {str(e)}")
            return False
```

### Webhook Integration (Optional)

```python
# Flask webhook endpoint for real-time notifications
from flask import Flask, request, jsonify
import hmac
import hashlib

app = Flask(__name__)

@app.route('/dooray-webhook', methods=['POST'])
def dooray_webhook():
    """Handle real-time notifications from Dooray"""
    
    # Verify webhook signature
    signature = request.headers.get('X-Dooray-Signature')
    if not verify_dooray_signature(request.data, signature):
        return jsonify({'error': 'Invalid signature'}), 401
    
    payload = request.json
    event_type = payload.get('eventType')
    
    if event_type == 'task.created':
        task_data = payload.get('task')
        if _has_resume_attachment(task_data):
            # Trigger immediate processing
            trigger_candidate_processing(task_data)
    
    return jsonify({'status': 'received'}), 200

def verify_dooray_signature(payload: bytes, signature: str) -> bool:
    """Verify webhook signature"""
    expected_signature = hmac.new(
        DOORAY_WEBHOOK_SECRET.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(f"sha256={expected_signature}", signature)
```

---

## 2. Outlook/Exchange Integration

### Overview
Microsoft Graph API integration for monitoring hiring email accounts and processing resume attachments.

### Authentication Setup

```python
class OutlookConfig:
    """Microsoft Graph API Configuration"""
    AUTHORITY = "https://login.microsoftonline.com"
    TENANT_ID = "your-tenant-id"
    CLIENT_ID = "your-client-id"
    CLIENT_SECRET = "your-client-secret"
    
    # Graph API Configuration
    GRAPH_API_BASE = "https://graph.microsoft.com/v1.0"
    SCOPES = ["https://graph.microsoft.com/.default"]
    
    # Email Configuration
    HIRING_MAILBOX = "hiring@dunamiscap.com"
    SHARED_MAILBOX = True
    
    # Processing Configuration
    EMAIL_POLL_INTERVAL = 300  # 5 minutes
    MAX_ATTACHMENT_SIZE = 10 * 1024 * 1024  # 10MB
```

### Graph API Integration Implementation

```python
import requests
from msal import ConfidentialClientApplication
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class OutlookIntegration:
    def __init__(self, tenant_id: str, client_id: str, client_secret: str):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.token_expires_at = None
        
        # Initialize MSAL client
        self.app = ConfidentialClientApplication(
            client_id=client_id,
            client_credential=client_secret,
            authority=f"https://login.microsoftonline.com/{tenant_id}"
        )
    
    def _get_access_token(self) -> str:
        """Get valid access token"""
        if (self.access_token and self.token_expires_at and 
            datetime.now() < self.token_expires_at):
            return self.access_token
        
        # Get new token
        result = self.app.acquire_token_silent(
            scopes=["https://graph.microsoft.com/.default"],
            account=None
        )
        
        if not result:
            result = self.app.acquire_token_for_client(
                scopes=["https://graph.microsoft.com/.default"]
            )
        
        if "access_token" in result:
            self.access_token = result["access_token"]
            self.token_expires_at = datetime.now() + timedelta(
                seconds=result.get("expires_in", 3600) - 300  # 5min buffer
            )
            return self.access_token
        else:
            raise Exception(f"Failed to acquire token: {result.get('error_description')}")
    
    def get_hiring_emails(self, mailbox: str = None) -> List[Dict]:
        """Get recent emails with resume attachments"""
        mailbox = mailbox or "hiring@dunamiscap.com"
        token = self._get_access_token()
        
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        
        # Calculate time filter (last 24 hours)
        since_time = datetime.utcnow() - timedelta(hours=24)
        since_iso = since_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        
        # Build query filter
        filter_query = (
            f"hasAttachments eq true and "
            f"receivedDateTime ge {since_iso} and "
            f"(subject/any(s:contains(s,'resume')) or "
            f"subject/any(s:contains(s,'cv')) or "
            f"subject/any(s:contains(s,'application')))"
        )
        
        # API request
        url = f"https://graph.microsoft.com/v1.0/users/{mailbox}/messages"
        params = {
            '$filter': filter_query,
            '$expand': 'attachments',
            '$select': 'id,subject,body,from,receivedDateTime,attachments',
            '$top': 50
        }
        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            
            emails = response.json().get('value', [])
            processed_emails = []
            
            for email in emails:
                if self._has_resume_attachment(email):
                    processed_emails.append(self._process_email(email))
            
            return processed_emails
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Graph API error: {str(e)}")
            raise
    
    def _has_resume_attachment(self, email: Dict) -> bool:
        """Check if email has resume-like attachments"""
        attachments = email.get('attachments', [])
        resume_extensions = {'.pdf', '.doc', '.docx'}
        resume_keywords = {'resume', 'cv', 'curriculum'}
        
        for attachment in attachments:
            filename = attachment.get('name', '').lower()
            
            # Check file extension
            if any(filename.endswith(ext) for ext in resume_extensions):
                return True
            
            # Check filename keywords
            if any(keyword in filename for keyword in resume_keywords):
                return True
        
        return False
    
    def _process_email(self, email: Dict) -> Dict:
        """Process and normalize email data"""
        return {
            'emailId': email['id'],
            'subject': email['subject'],
            'body': email['body']['content'],
            'fromEmail': email['from']['emailAddress']['address'],
            'fromName': email['from']['emailAddress']['name'],
            'receivedDate': email['receivedDateTime'],
            'attachments': [
                {
                    'attachmentId': att['id'],
                    'fileName': att['name'],
                    'fileSize': att['size'],
                    'contentType': att['contentType'],
                    'isInline': att['isInline']
                }
                for att in email.get('attachments', [])
                if not att['isInline']  # Skip inline images
            ],
            'source': 'outlook_email'
        }
    
    def download_attachment(self, mailbox: str, email_id: str, 
                          attachment_id: str) -> bytes:
        """Download email attachment"""
        token = self._get_access_token()
        headers = {'Authorization': f'Bearer {token}'}
        
        url = (f"https://graph.microsoft.com/v1.0/users/{mailbox}/messages/"
               f"{email_id}/attachments/{attachment_id}/$value")
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.content
    
    def mark_email_processed(self, mailbox: str, email_id: str) -> bool:
        """Mark email as processed"""
        try:
            token = self._get_access_token()
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            
            # Add category or flag to indicate processing
            url = f"https://graph.microsoft.com/v1.0/users/{mailbox}/messages/{email_id}"
            
            update_data = {
                'categories': ['AI-Processed'],
                'isRead': True
            }
            
            response = requests.patch(url, headers=headers, json=update_data)
            response.raise_for_status()
            return True
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error marking email processed: {str(e)}")
            return False
```

---

## 3. HR Email Communication Integration

### Overview
Automated email communication to HR team using Amazon SES for hiring decisions and notifications.

### SES Configuration

```python
class HREmailConfig:
    """HR Email Communication Configuration"""
    HR_EMAIL = "hr@dunamiscap.com"
    SENDER_EMAIL = "hiring-automation@dunamiscap.com"
    REPLY_TO_EMAIL = "hiring@dunamiscap.com"
    
    # SES Configuration
    SES_REGION = "us-east-1"  # SES region
    
    # Email Templates
    TEMPLATE_BUCKET = "hiring-automation-templates"
    TEMPLATE_PREFIX = "email-templates/"
    
    # Notification Types
    NOTIFICATION_TYPES = {
        'screening_complete': 'Candidate Screening Complete',
        'assessment_complete': 'Assessment Evaluation Complete',
        'interview_complete': 'Interview Process Complete',
        'final_decision': 'Final Hiring Decision',
        'process_error': 'Hiring Process Error'
    }
```

### SES Integration Implementation

```python
import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from jinja2 import Template
import json

class HREmailIntegration:
    def __init__(self, region: str = 'us-east-1'):
        self.ses_client = boto3.client('ses', region_name=region)
        self.s3_client = boto3.client('s3')
        self.hr_email = "hr@dunamiscap.com"
        self.sender_email = "hiring-automation@dunamiscap.com"
    
    def send_screening_notification(self, candidate_data: Dict, 
                                  decision: str, details: Dict) -> bool:
        """Send screening completion notification to HR"""
        
        template_data = {
            'candidate_name': candidate_data.get('name', 'Unknown'),
            'candidate_email': candidate_data.get('email', 'Unknown'),
            'position': candidate_data.get('position', 'Unknown'),
            'decision': decision.upper(),
            'screening_score': details.get('score', 0),
            'key_strengths': details.get('strengths', []),
            'concerns': details.get('concerns', []),
            'recommendation': details.get('recommendation', ''),
            'process_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'next_steps': self._get_next_steps(decision)
        }
        
        subject = f"Candidate Screening Complete - {candidate_data.get('name')} - {decision.upper()}"
        
        return self._send_templated_email(
            template_name='screening_notification',
            subject=subject,
            template_data=template_data,
            attachments=details.get('attachments', [])
        )
    
    def send_final_decision_notification(self, candidate_data: Dict, 
                                       final_decision: Dict) -> bool:
        """Send final hiring decision to HR"""
        
        template_data = {
            'candidate_name': candidate_data.get('name'),
            'candidate_email': candidate_data.get('email'),
            'position': candidate_data.get('position'),
            'final_decision': final_decision['decision'].upper(),
            'overall_score': final_decision.get('overall_score', 0),
            'confidence_level': final_decision.get('confidence', 'Medium'),
            'screening_score': final_decision.get('screening_score', 0),
            'assessment_score': final_decision.get('assessment_score', 0),
            'interview_score': final_decision.get('interview_score', 0),
            'key_strengths': final_decision.get('strengths', []),
            'areas_of_concern': final_decision.get('concerns', []),
            'salary_recommendation': final_decision.get('salary_band', 'TBD'),
            'start_date_recommendation': final_decision.get('start_date', 'TBD'),
            'additional_notes': final_decision.get('notes', ''),
            'process_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        subject = f"FINAL HIRING DECISION - {candidate_data.get('name')} - {final_decision['decision'].upper()}"
        
        # Attach comprehensive evaluation report
        attachments = [
            {
                'filename': f"{candidate_data.get('name', 'candidate')}_evaluation_report.json",
                'content': json.dumps(final_decision, indent=2),
                'mimetype': 'application/json'
            }
        ]
        
        return self._send_templated_email(
            template_name='final_decision',
            subject=subject,
            template_data=template_data,
            attachments=attachments
        )
    
    def send_process_error_notification(self, candidate_data: Dict, 
                                      error_details: Dict) -> bool:
        """Send error notification when automated process fails"""
        
        template_data = {
            'candidate_name': candidate_data.get('name', 'Unknown'),
            'error_stage': error_details.get('stage', 'Unknown'),
            'error_message': error_details.get('message', 'Unknown error'),
            'error_timestamp': error_details.get('timestamp'),
            'candidate_data': json.dumps(candidate_data, indent=2),
            'requires_manual_review': True
        }
        
        subject = f"URGENT: Hiring Process Error - {candidate_data.get('name')} - Manual Review Required"
        
        return self._send_templated_email(
            template_name='process_error',
            subject=subject,
            template_data=template_data,
            priority='high'
        )
    
    def _send_templated_email(self, template_name: str, subject: str, 
                            template_data: Dict, attachments: List = None,
                            priority: str = 'normal') -> bool:
        """Send email using HTML template"""
        try:
            # Load email template from S3
            template_html = self._load_email_template(f"{template_name}.html")
            template_text = self._load_email_template(f"{template_name}.txt")
            
            # Render templates
            html_content = Template(template_html).render(**template_data)
            text_content = Template(template_text).render(**template_data)
            
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = self.hr_email
            msg['Reply-To'] = "hiring@dunamiscap.com"
            
            if priority == 'high':
                msg['X-Priority'] = '1'
                msg['X-MSMail-Priority'] = 'High'
            
            # Add text and HTML parts
            msg.attach(MIMEText(text_content, 'plain'))
            msg.attach(MIMEText(html_content, 'html'))
            
            # Add attachments
            if attachments:
                for attachment in attachments:
                    self._add_attachment(msg, attachment)
            
            # Send email
            response = self.ses_client.send_raw_email(
                Source=self.sender_email,
                Destinations=[self.hr_email],
                RawMessage={'Data': msg.as_string()}
            )
            
            logger.info(f"Email sent successfully. MessageId: {response['MessageId']}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}")
            return False
    
    def _load_email_template(self, template_name: str) -> str:
        """Load email template from S3"""
        try:
            response = self.s3_client.get_object(
                Bucket='hiring-automation-templates',
                Key=f'email-templates/{template_name}'
            )
            return response['Body'].read().decode('utf-8')
        except Exception as e:
            logger.error(f"Failed to load template {template_name}: {str(e)}")
            return self._get_default_template(template_name)
    
    def _add_attachment(self, msg: MIMEMultipart, attachment: Dict):
        """Add attachment to email message"""
        if isinstance(attachment['content'], str):
            content = attachment['content'].encode('utf-8')
        else:
            content = attachment['content']
        
        part = MIMEApplication(content)
        part.add_header(
            'Content-Disposition',
            'attachment',
            filename=attachment['filename']
        )
        msg.attach(part)
    
    def _get_next_steps(self, decision: str) -> str:
        """Get next steps based on screening decision"""
        next_steps = {
            'PASS': 'Candidate will receive take-home assessment automatically',
            'FAIL': 'Candidate has been sent rejection email with feedback',
            'MANUAL_REVIEW': 'Candidate requires manual review before proceeding'
        }
        return next_steps.get(decision.upper(), 'Please review candidate manually')
```

### Email Templates

```html
<!-- screening_notification.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Candidate Screening Complete</title>
</head>
<body>
    <h2>Candidate Screening Complete</h2>
    
    <h3>Candidate Information</h3>
    <ul>
        <li><strong>Name:</strong> {{ candidate_name }}</li>
        <li><strong>Email:</strong> {{ candidate_email }}</li>
        <li><strong>Position:</strong> {{ position }}</li>
        <li><strong>Decision:</strong> <span style="color: {% if decision == 'PASS' %}green{% else %}red{% endif %}">{{ decision }}</span></li>
    </ul>
    
    <h3>Evaluation Summary</h3>
    <ul>
        <li><strong>Screening Score:</strong> {{ screening_score }}/100</li>
        <li><strong>Recommendation:</strong> {{ recommendation }}</li>
    </ul>
    
    <h3>Key Strengths</h3>
    <ul>
        {% for strength in key_strengths %}
        <li>{{ strength }}</li>
        {% endfor %}
    </ul>
    
    {% if concerns %}
    <h3>Areas of Concern</h3>
    <ul>
        {% for concern in concerns %}
        <li>{{ concern }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    
    <h3>Next Steps</h3>
    <p>{{ next_steps }}</p>
    
    <hr>
    <p><em>Processed by Dunamis Capital Hiring Automation System on {{ process_date }}</em></p>
</body>
</html>
```

---

## 4. Error Handling & Monitoring

### Integration Health Monitoring

```python
class IntegrationMonitor:
    def __init__(self):
        self.cloudwatch = boto3.client('cloudwatch')
        self.sns = boto3.client('sns')
        
    def monitor_dooray_health(self) -> Dict:
        """Monitor Dooray Task integration health"""
        try:
            # Test API connectivity
            dooray = DoorayTaskIntegration(DOORAY_TOKEN, DOORAY_PROJECT_ID)
            test_result = dooray.get_new_candidate_tasks()
            
            # Send success metric
            self._send_metric('DoorayIntegration', 'Health', 1)
            return {'status': 'healthy', 'last_check': datetime.now()}
            
        except Exception as e:
            # Send failure metric
            self._send_metric('DoorayIntegration', 'Health', 0)
            self._send_alert('Dooray integration failure', str(e))
            return {'status': 'unhealthy', 'error': str(e)}
    
    def monitor_outlook_health(self) -> Dict:
        """Monitor Outlook integration health"""
        try:
            outlook = OutlookIntegration(TENANT_ID, CLIENT_ID, CLIENT_SECRET)
            test_result = outlook.get_hiring_emails()
            
            self._send_metric('OutlookIntegration', 'Health', 1)
            return {'status': 'healthy', 'last_check': datetime.now()}
            
        except Exception as e:
            self._send_metric('OutlookIntegration', 'Health', 0)
            self._send_alert('Outlook integration failure', str(e))
            return {'status': 'unhealthy', 'error': str(e)}
    
    def _send_metric(self, namespace: str, metric_name: str, value: float):
        """Send custom metric to CloudWatch"""
        self.cloudwatch.put_metric_data(
            Namespace=f'HiringAutomation/{namespace}',
            MetricData=[
                {
                    'MetricName': metric_name,
                    'Value': value,
                    'Unit': 'Count',
                    'Timestamp': datetime.utcnow()
                }
            ]
        )
    
    def _send_alert(self, subject: str, message: str):
        """Send alert notification"""
        self.sns.publish(
            TopicArn='arn:aws:sns:region:account:hiring-automation-alerts',
            Subject=f'Hiring Automation Alert: {subject}',
            Message=message
        )
```

This comprehensive integration specification provides all the technical details needed to connect the AI hiring system with your existing external systems, ensuring seamless data flow and reliable communication channels.