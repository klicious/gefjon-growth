---
name: execute-postprocessing
description: Executes Python post-processing scripts to transform Gemini CLI outputs into final structured formats. Use this after AI generation steps to format and organize results.
---

# Execute Post-processing

This skill runs Python scripts to post-process AI-generated outputs from Gemini CLI.

## Instructions

1. **Execute Consolidation Script**
   - Run `scripts/consolidate_hiring_results.py` to organize scattered files:
     ```bash
     uv run python scripts/consolidate_hiring_results.py
     ```
   - This script:
     - Creates standardized candidate directory structure
     - Moves files from scattered locations to consolidated directories
     - Organizes by candidate_id and normalized name
     - Creates subdirectories: screening/, takehome/, interview/, evaluation/, communication/
   - Monitor execution for errors
   - Capture stdout/stderr for logging

2. **Execute Enhanced Materials Generation**
   - Run `scripts/generate_enhanced_materials.py` to create additional materials:
     ```bash
     uv run python scripts/generate_enhanced_materials.py
     ```
   - This script:
     - Generates missing candidate summaries
     - Creates evaluation frameworks
     - Fills gaps in interview materials
     - Ensures all candidates have complete documentation
   - Verify all materials were generated

3. **Execute Overall Summary Generation**
   - Run `scripts/generate_overall_summary.py` to create executive summary:
     ```bash
     uv run python scripts/generate_overall_summary.py
     ```
   - This script:
     - Aggregates all candidate data
     - Calculates statistics and distributions
     - Identifies standout candidates
     - Creates HIRING_SUMMARY_COMPLETE.md
     - Generates FINAL_WORKFLOW_SUMMARY.json
   - Verify summary files were created

4. **Validate Output Structure**
   - Verify consolidated directory structure exists:
     ```
     artifacts/public/hiring/candidates/{date}_consolidated/
     ├── HIRING_SUMMARY_COMPLETE.md
     ├── FINAL_WORKFLOW_SUMMARY.json
     └── {candidate_id}_{name}/
         ├── candidate_summary.md
         ├── screening/
         ├── takehome/
         ├── interview/
         ├── evaluation/
         └── communication/
     ```
   - Check that all expected files exist
   - Validate file content completeness
   - Report any missing or invalid files

5. **Generate Processing Log**
   - Create postprocessing_log.json with:
     - Timestamp of execution
     - Scripts executed and their status
     - Files created/moved
     - Any errors or warnings
     - Summary of operations performed

## Quality Gates

- ✅ Input files exist and are valid
- ✅ Python script executes without errors
- ✅ Output files created in correct locations
- ✅ Output format matches specifications
- ✅ Processing log updated

## Examples

```bash
# Complete post-processing workflow
🔄 Phase 6: Post-processing
   
📋 Step 1: Consolidating results...
   Running: uv run python scripts/consolidate_hiring_results.py
   ✅ Consolidated 13 candidates
   ✅ Created directory structure for all candidates
   ✅ Moved 156 files to correct locations

📋 Step 2: Generating enhanced materials...
   Running: uv run python scripts/generate_enhanced_materials.py
   ✅ Generated 13 candidate summaries
   ✅ Created 8 evaluation frameworks
   ✅ Filled 5 missing interview materials

📋 Step 3: Generating overall summary...
   Running: uv run python scripts/generate_overall_summary.py
   ✅ Created HIRING_SUMMARY_COMPLETE.md
   ✅ Created FINAL_WORKFLOW_SUMMARY.json
   ✅ Identified 3 standout candidates

✅ Post-processing completed successfully
📊 Output: artifacts/public/hiring/candidates/20250812_consolidated/
```

## Error Handling

- **Missing Input**: Report error, skip processing
- **Script Error**: Capture error message, log details, continue with next file
- **Invalid Output**: Report validation failure, mark for manual review
