---
id: visual_elements_specifications
type: design_specifications
domain: presentation
created_date: 2025-08-12
author: Claude Code
priority: high
tags: [visual-design, diagrams, charts, google-slides]
visibility: public
version: 1.0
---

# 🎨 VISUAL ELEMENTS SPECIFICATIONS

**PURPOSE**: Detailed design specifications for creating professional diagrams, charts, and infographics in Google Slides.

---

## 🏗️ ARCHITECTURAL DIAGRAMS

### **1. 7-Stage Pipeline Diagram (Slide 6)**

#### **Design Specifications**
```
LAYOUT: Horizontal flow, left-to-right
DIMENSIONS: 12" width × 3" height
SPACING: Equal spacing between stages (1.5" apart)
```

#### **Stage Elements**
- **Shape**: Rounded rectangles (0.5" corner radius)
- **Size**: 1.5" width × 0.8" height each
- **Color Gradient**: 
  - Stage 1-2: Deep Blue (#1E40AF)
  - Stage 3-4: Medium Blue (#2563EB)
  - Stage 5-6: Blue-Green (#0D9488)
  - Stage 7: Success Green (#10B981)

#### **Stage Content**
```
STAGE 1: "Pre-Flight Validation" + checklist icon
STAGE 2: "Candidate Screening" + magnifying glass icon  
STAGE 3: "Assignment Generation" + document icon
STAGE 4: "Evaluation & Scoring" + star rating icon
STAGE 5: "Interview Kit Creation" + speech bubble icon
STAGE 6: "Assessment & Recommendations" + thumbs up icon
STAGE 7: "Executive Summary" + presentation icon
```

#### **Connecting Elements**
- **Arrows**: Right-pointing chevrons between stages
- **Quality Gates**: Diamond shapes (0.3" × 0.3") with green checkmarks
- **Context Callout**: "90% Context Requirement" badge on Stage 1

#### **Implementation Steps**
1. Insert 7 rounded rectangles in horizontal line
2. Apply gradient colors from blue to green
3. Add icons from Google Slides icon library
4. Insert arrows between each stage
5. Add diamond quality gates with checkmarks
6. Create "90%" badge with callout line to Stage 1

---

### **2. MCP Agent Network (Slide 12b)**

#### **Design Specifications**
```
LAYOUT: Hub-and-spoke network
CENTER: "MCP Protocol" hub (2" diameter circle)
AGENTS: 4 surrounding circles (1.2" diameter each)
POSITIONING: Cardinal directions (N, E, S, W)
```

#### **Agent Specifications**
- **EXA/Google (North)**: Green circle (#10B981) + search icon
- **Sequential Thinking (East)**: Blue circle (#2563EB) + brain icon
- **Playwright (South)**: Orange circle (#F97316) + browser icon
- **Fetch (West)**: Purple circle (#8B5CF6) + download icon

#### **Connection Design**
- **Lines**: 2pt weight, dashed style
- **Color**: Match destination agent color
- **Flow Indicators**: Small arrows showing data direction
- **Capability Boxes**: Small text boxes with 2-3 key features each

#### **Implementation Steps**
1. Create central circle with "MCP Protocol" text
2. Add 4 agent circles in cardinal positions
3. Insert appropriate icons in each circle
4. Draw connecting lines with flow arrows
5. Add capability text boxes near each agent
6. Apply color coding throughout

---

### **3. Security Layers Model (Slide 12c)**

#### **Design Specifications**
```
LAYOUT: Concentric circles (4 layers)
OUTER DIAMETER: 6" (Compliance layer)
RING WIDTHS: 0.8" each layer
CENTER: 2" diameter (Protected data)
```

#### **Layer Specifications**
- **Layer 1 (Outer)**: Compliance & Governance
  - Color: Light gray (#F3F4F6)
  - Icons: GDPR badge, SOC 2 badge, audit symbols
- **Layer 2**: Security Controls  
  - Color: Security blue (#1E40AF)
  - Icons: Shield, lock, key, monitor symbols
- **Layer 3**: Data Protection
  - Color: Trust green (#059669)
  - Icons: Classification, access control, encryption symbols
- **Layer 4 (Center)**: Protected HR Data
  - Color: Vault gold (#F59E0B)
  - Icon: Data vault or safe symbol

#### **Implementation Steps**
1. Create 4 concentric circles with transparency
2. Apply layer colors with 70% transparency
3. Add icons and labels for each layer
4. Insert center vault icon
5. Add security indicators (shields, checkmarks)

---

## 📊 DATA VISUALIZATIONS

### **4. ROI Dashboard (Slide 22)**

#### **Main ROI Display**
```
ELEMENT: Large circular badge
SIZE: 3" diameter
COLOR: Investment gold (#F59E0B)
TEXT: "286%-563% ROI"
POSITION: Top-right prominence
```

#### **Value Streams Chart**
- **Type**: Stacked horizontal bar chart
- **Data**:
  - Time Savings: $21K-$61K (Blue #2563EB)
  - Quality Improvement: $563K (Green #10B981)  
  - Speed Advantage: $150K-$375K (Orange #F97316)
- **Total Bar**: $734K-$998K range
- **Labels**: Clear value descriptions

#### **Time Comparison Visual**
- **Design**: Clock icons with dramatic size difference
- **Before**: Large clock (3") showing "6-10 hours"
- **After**: Small clock (1") showing "10-15 minutes"  
- **Arrow**: Large "97%" with downward arrow
- **Colors**: Red for before, green for after

---

### **5. Success Metrics Dashboard (Slide 10)**

#### **Donut Chart Specifications**
```
TYPE: Donut chart (thick ring)
SIZE: 4" diameter  
DATA: 100% success (3/3 candidates)
COLOR: Success green (#10B981)
CENTER TEXT: "3/3 HIRED" (large, bold)
POSITION: Left side of slide
```

#### **Quality Gauge Design**
- **Shape**: Semi-circle (180-degree arc)
- **Scale**: 0-10 with tick marks
- **Industry Line**: Red line at 6.2 with "Industry Average" label
- **Our Needle**: Green arrow pointing to 8.7
- **Background**: Gradient from red (low) to green (high)

#### **Zero Errors Badge**
- **Design**: Circular badge with checkmark
- **Size**: 2" diameter
- **Color**: Success green with white checkmark
- **Text**: "ZERO ERRORS" around perimeter
- **Shadow**: Subtle drop shadow for prominence

---

### **6. Competitive Matrix (Slide 18d)**

#### **Table Design**
```
COLUMNS: 5 (Capability, Us, Traditional ATS, AI Screening, Custom Dev)
ROWS: 8 capability categories
CELL SIZE: 1.2" width × 0.6" height
HEADER COLOR: Professional blue (#2563EB)
```

#### **Status Icons**
- **Full Capability**: Green checkmark (✅) with circle background
- **Missing/Poor**: Red X (❌) with circle background  
- **Partial/Warning**: Yellow triangle (⚠️) with circle background
- **Icon Size**: 0.4" diameter for visibility

#### **Our Column Highlight**
- **Background**: Light blue tint (#EBF8FF)
- **Border**: 2pt blue border (#2563EB)
- **Text**: Bold formatting for emphasis

---

## 💰 FINANCIAL VISUALIZATIONS

### **7. Investment Allocation Pie Chart (Slide 28c)**

#### **Chart Specifications**
```
TYPE: Pie chart with exploded segments
SIZE: 5" diameter
SEGMENTS: 4 with different colors
LABELS: Outside with leader lines
```

#### **Segment Details**
- **Product Development (40%)**: Blue (#2563EB) - $6M
- **Sales & Marketing (33%)**: Green (#10B981) - $5M
- **Market Expansion (17%)**: Orange (#F97316) - $2.5M
- **Operations (10%)**: Gray (#6B7280) - $1.5M

#### **Breakdown Tables**
- **Position**: Four corners around pie chart
- **Size**: 2" × 1.5" each table
- **Content**: Specific allocation details for each segment
- **Color**: Header matches segment color

---

### **8. Return Scenarios Chart (Slide 28d)**

#### **Bar Chart Design**
```
TYPE: Clustered column chart
CATEGORIES: Conservative, Base, Upside scenarios
COLORS: Blue (#2563EB), Green (#10B981), Gold (#F59E0B)
Y-AXIS: Exit valuation ($0-$1.5B)
```

#### **Return Multipliers**
- **Position**: Above each bar
- **Format**: Large text (24pt) with "x" suffix
- **Values**: 8x, 10x, 16x
- **Color**: Match bar color

#### **Timeline Element**
- **Design**: Horizontal timeline below chart
- **Start**: "Series A 2025"
- **Milestones**: Revenue markers at years 2, 3, 4, 5
- **End**: "Exit 2029-2031"
- **Arrows**: Show progression from investment to exit

---

## 🎨 DESIGN SYSTEM ELEMENTS

### **Icon Library**
- **Source**: Google Slides built-in icons + Feather icon set
- **Style**: Outline style for consistency
- **Size**: Standard 0.3" for inline, 0.5" for emphasis
- **Colors**: Match slide color scheme

### **Typography Scale**
- **Mega Headlines**: 48pt (slide titles)
- **Headlines**: 36pt (section headers)
- **Subheadings**: 24pt (subsection headers)
- **Body Text**: 18pt (main content)
- **Captions**: 14pt (chart labels, footnotes)

### **Spacing Grid**
- **Margins**: 0.5" from slide edges
- **Section Spacing**: 0.75" between major sections
- **Element Spacing**: 0.25" between related elements
- **Line Height**: 1.2x for readability

### **Color Applications**
- **Backgrounds**: White or light gray (#F9FAFB)
- **Text**: Dark gray (#374151) for readability
- **Accent**: Use brand colors sparingly for emphasis
- **Charts**: Distinct colors from palette for data series

---

## ✅ IMPLEMENTATION CHECKLIST

### **Before Starting**
- [ ] Review all content files for accuracy
- [ ] Gather high-resolution logos and images
- [ ] Set up color palette in Google Slides
- [ ] Install consistent font (Inter or Roboto)

### **During Creation**
- [ ] Maintain consistent spacing and alignment
- [ ] Use slide master for typography consistency
- [ ] Test readability at presentation size
- [ ] Ensure color accessibility (contrast ratios)

### **Quality Review**
- [ ] All charts display correctly
- [ ] Text is readable from back of room
- [ ] Visual hierarchy guides attention
- [ ] Professional appearance throughout

---

**READY FOR IMPLEMENTATION**: These specifications provide complete guidance for creating professional, visually engaging slides that enhance audience understanding and retention.