---
name: gemini-deep-research
description: >
  Use when explicitly invoked to run a deep-research query against Google Gemini. Triggers when the user asks for deep research using Google Gemini or wants to investigate a complex topic in depth.
disable-model-invocation: true
user-invocable: true
argument-hint: "[complex query] [optional context file paths]"
---

# Google Gemini Deep Research

<context>

This tool-augmented skill triggers the Google Gemini deep-research API in the background. Deep research can take several minutes to run as the model performs multiple steps (searching the web, reasoning, evaluating) and gathers comprehensive background information. You can pass local workspace files to be uploaded as context to assist the research process. The terminal will stream intermediate thinking and action steps so you can monitor progress.
</context>

## Deep Research Task

<instructions>

Run the following terminal command (request permission first from the user if your environment requires it). Pass the user's query as the first argument, and any local file paths to be uploaded as context as subsequent arguments.
</instructions>

<command>

```bash
uv run scripts/deep-research.py "<query>" <file1> <file2>
```

</command>

<example_run>

Input: "Research the differences between FastMCP and full MCP SDK" src/server.py src/client.py
Output:
🔍 Starting Deep Research for: 'Research the differences between FastMCP and full MCP SDK'
📤 Uploading 2 context files...
   Uploading src/server.py...
   Uploading src/client.py...
⏳ Job ID \[interaction-123\] running. Polling Google API...
  \[Thinking\] The user wants to compare FastMCP and the full MCP SDK. I'll need to look at both codebases.
  \[Action\] google_search
  \[Thinking\] I see FastMCP is a higher-level abstraction...
✅ Research Complete!
</example_run>

<error_handling>

If the command fails with "GEMINI_API_KEY environment variable is missing", ask the user to provide their Gemini API key or set it in their terminal context before retrying.
If the API fails to process a file, check that the file path is correct and accessible.
</error_handling>

## Next Steps

<rules>

- Wait for the deep research job to complete in the terminal. Do not kill the terminal process unless the user explicitly asks to cancel it.
- After the output is printed, read the final markdown output and summarize it for the user, or offer to save it directly to a file like `research_report.md` if the research output is extensive.

</rules>
