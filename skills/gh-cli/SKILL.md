---
name: gh-cli
description: |
  Use this skill for any GitHub operation from the command line using the gh CLI. Triggers on: "use gh to...", "create a PR", "list issues", "merge this pull request", "trigger a workflow", "gh cli command for...", "how do I use gh to...", "create a GitHub release", "manage projects with gh", "clone a repo with gh", "gh auth", "list my repos". Covers repositories, issues, pull requests, GitHub Actions, projects, releases, gists, codespaces, organizations, search, labels, secrets, extensions, and the gh API. Includes output formatting, jq filtering, and common multi-step workflows.
argument-hint: "[operation to perform, e.g. 'create PR from current branch' or 'list open issues assigned to me']"
user-invocable: true
---

# GitHub CLI (gh) Reference

Comprehensive reference for GitHub CLI (gh) — work seamlessly with GitHub from the command line.

**Version:** 2.85.0 (current as of January 2026)

## Quick Start

```bash
# Install (macOS)
brew install gh

# Authenticate
gh auth login

# Verify
gh auth status
```

**Other platforms:** Linux (apt), Windows (`winget install --id GitHub.cli`) — see [references/auth-repos-browse.md](references/auth-repos-browse.md) for full install commands.

---

## Reference Files

Load the relevant file based on the operation requested. Each file contains complete command syntax and examples.

| Topic | File | Commands Covered |
|---|---|---|
| Authentication, Browse, Repositories | [references/auth-repos-browse.md](references/auth-repos-browse.md) | `gh auth`, `gh browse`, `gh repo` |
| Issues & Pull Requests | [references/issues-prs.md](references/issues-prs.md) | `gh issue`, `gh pr` |
| Actions, Projects, Releases | [references/actions-projects-releases.md](references/actions-projects-releases.md) | `gh run`, `gh workflow`, `gh project`, `gh release` |
| Gists, Codespaces, Orgs, Config, Extensions, Aliases, Search, Secrets | [references/gists-codespaces-misc.md](references/gists-codespaces-misc.md) | `gh gist`, `gh codespace`, `gh org`, `gh config`, `gh extension`, `gh alias`, `gh search`, `gh secret`, `gh label`, `gh ssh-key`, `gh api` |
| Flags, Output Formatting, Workflows, Best Practices | [references/flags-formatting-workflows.md](references/flags-formatting-workflows.md) | Global flags, `--json`, `--jq`, `--template`, common multi-step workflows |

---

## Most Common Commands

```bash
# Repos
gh repo create my-repo --public       # Create repo
gh repo clone owner/repo              # Clone repo
gh repo view --web                    # Open in browser

# Issues
gh issue create --title "Bug" --body "..."
gh issue list --assignee @me
gh issue close 42

# Pull Requests
gh pr create --title "Feature" --base main
gh pr list --state open
gh pr merge 12 --squash
gh pr checkout 12                     # Checkout PR branch locally

# Actions
gh workflow run ci.yml
gh run list --limit 5
gh run watch                          # Live-tail latest run

# Release
gh release create v1.0.0 --notes "Initial release"
```

---

## Output Formatting & Filtering

```bash
# JSON output (pipe to jq for filtering)
gh pr list --json number,title,author
gh issue list --json number,title --jq '.[] | select(.title | contains("bug"))'

# Table template
gh pr list --template '{{range .}}{{.number}}: {{.title}}{{"\n"}}{{end}}'

# Pagination
gh issue list --state all --paginate
```

---

## Gotchas

- **Authentication scope**: Some commands (e.g., `gh secret set`, `gh org list`) require additional OAuth scopes. Run `gh auth refresh --scopes <scope>` to add them.
- **Default repo**: In a git repo, `gh` auto-detects the remote. Outside one, set `GH_REPO=owner/repo` or `gh repo set-default owner/repo`.
- **Enterprise**: Pass `--hostname enterprise.internal` or set `GH_HOST` for GitHub Enterprise Server.
- **JSON parsing**: Use `--jq` for simple filters inline; pipe to `jq` for complex queries.
- **Paginate large results**: Always use `--paginate` when listing issues/PRs in active repos to avoid missing items.

---

## Environment Variables

```bash
export GH_TOKEN=ghp_xxxxxxxxxxxx   # Auth token for automation
export GH_HOST=github.com           # Hostname (for GHE)
export GH_REPO=owner/repo           # Default repository
export GH_PROMPT_DISABLED=true      # Disable interactive prompts (CI)
export GH_PAGER=less                # Custom pager
```

---

## Getting Help

```bash
gh --help
gh pr --help
gh issue create --help
gh help environment    # Environment variables
gh help formatting     # Output format options
```

**Official docs:** https://cli.github.com/manual/
