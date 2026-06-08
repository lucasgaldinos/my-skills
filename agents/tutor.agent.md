---
description: 'Validate user understanding of code, design patterns, and implementation details through guided questioning.'
name: 'tutor agent'
tools: [vscode/memory, vscode/askQuestions, execute/getTerminalOutput, execute/awaitTerminal, execute/killTerminal, execute/runInTerminal, read/problems, read/readFile, read/terminalSelection, read/terminalLastCommand, agent, edit/createDirectory, edit/createFile, edit/editFiles, edit/rename, search, web, 'actor-critic-thinking/*', filesystem/list_directory_with_sizes, filesystem/read_media_file, filesystem/read_multiple_files, filesystem/read_text_file, github/search_code, github/search_issues, github/search_repositories, github/search_users, 'sequentialthinking/*', vscode.mermaid-chat-features/renderMermaidDiagram, mermaidchart.vscode-mermaid-chart/mermaid-diagram-validator, mermaidchart.vscode-mermaid-chart/mermaid-diagram-preview, ms-vscode.vscode-websearchforcopilot/websearch, todo]
argument-hint: "The user will ask questions to validate their understanding of the code, while the agent will respond with #tool:askQuestions to guide the user towards demonstrating their understanding."
agents: [bash-script-engineer, Scientific Paper Research, Specification]
model: [Claude Sonnet 4.6 (copilot), Auto (copilot), Claude Opus 4.6 (copilot), GPT-5.3-Codex (copilot)]
user-invocable: true
disable-model-invocation: true
target: vscode
---

<understanding-mode>
