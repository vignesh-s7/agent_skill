---
name: rtk
description: Input interception and output stream compaction for AI coding agents to reduce token usage.
license: MIT
---

# RTK — Stream Compaction & Input Interception

**Origin:** https://github.com/rtk-ai/rtk  
**License:** MIT License  

## Summary
RTK intercepts verbose command outputs (such as `git log`, build outputs, test runner reports) and collapses repetitive streams down to essential errors, status signals, and tail lines before feeding the text to the AI model context.

## Two-Way Compaction Architecture
1. **Input Interception**: When an AI coding agent executes shell commands, RTK intercepts stdout/stderr, filters out repetitive progress lines, extracts tracebacks/failures, and preserves head/tail context.
2. **Output Compaction (with Caveman)**: When generating responses, conversational prose is stripped down to structured findings, code diffs, and exact status receipts, preventing token waste on return trips.
