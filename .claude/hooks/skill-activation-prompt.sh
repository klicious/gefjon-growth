#!/usr/bin/env bash
#
# Skill Activation Prompt Hook - Bash Wrapper
#
# This script wraps the TypeScript implementation and executes it via npx tsx.
# It passes stdin to the TypeScript file and returns the output.

set -e

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "$SCRIPT_DIR"

# Execute the TypeScript implementation
npx tsx skill-activation-prompt.ts
