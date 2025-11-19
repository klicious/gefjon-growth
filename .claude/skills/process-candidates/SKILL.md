---
name: process-candidates
description: Normalizes and validates candidate resume data from JSON files, ensuring all required fields are present. Use this to prepare candidate data before AI screening.
---

# Process Candidates

This skill processes candidate JSON files from `data/public/hiring/resume/` and validates the data structure.

## Instructions

1. **Scan Resume Directory**
   - Read all JSON files from `data/public/hiring/resume/`
   - Skip files that don't match candidate pattern
   - Create a list of candidates to process

2. **Validate Candidate Data**
   - Check required fields exist:
     - `candidate_id` (format: atlas_XXX or similar)
     - `personal_info` (name, email, phone)
     - `experience` (work history)
     - `education`
     - `skills`
   - Validate data types and formats
   - Check for completeness of critical information

3. **Normalize Data Structure**
   - Ensure consistent field naming
   - Standardize date formats
   - Clean up formatting issues
   - Extract key metadata (years of experience, seniority level)

4. **Generate Processing Report**
   - List all candidates found
   - Report validation status for each
   - Identify any candidates with missing or invalid data
   - Create summary statistics

5. **Output Normalized Data**
   - Save normalized candidate data to `data/public/hiring/working/`
   - Create a processing log with timestamps
   - Prepare candidate list for next pipeline stage

## Quality Gates

- ✅ All candidate JSON files are valid
- ✅ Required fields present in all candidates
- ✅ No duplicate candidate IDs
- ✅ Normalized data saved successfully
- ✅ Processing log created

## Examples

```bash
# Processing output
📋 Found 13 candidates in data/public/hiring/resume/
✅ atlas_001_minseok_kim.json - Valid (Senior, 8 YOE)
✅ atlas_002_jiwon_park.json - Valid (Mid-level, 5 YOE)
⚠️  atlas_003_invalid.json - Missing experience field
📊 Processing complete: 12/13 valid candidates
```
