---
name: cloning-subdirectories-with-git
description: Use this skill when the user wants to clone, download, or fetch only a specific folder or file from a Git repository without cloning the entire repo. Triggers on "clone a subdirectory", "clone only a folder", "download specific folder from git", "pull a specific directory from GitHub", "sparse checkout", "clone part of a repo", "get only one file from git", "clone a subfolder", "how do I clone just the docs folder", "fetch specific path from repo".
argument-hint: "[repo URL] [path to subdirectory or file] [branch/tag]"
user-invocable: true
---

# Cloning Subdirectories with Git

Git has no native `git clone --subdirectory` flag. This skill selects and executes the correct workaround based on the user's situation.

## Step 1: Determine which method to use

Ask (or infer from context):

1. **Ongoing work or one-time snapshot?** — If the user plans to pull updates or push changes, use Sparse Checkout or Partial Clone. If it's a one-time download, use `git archive`.
2. **Directory or single file?** — Single file → `git show`. Directory → Methods 1–3.
3. **Large repo or bandwidth-constrained?** — Large repo with Git 2.19+ support → Partial Clone (Method 3). Standard repo → Sparse Checkout (Method 1).

Quick decision table:

| Situation | Method |
|---|---|
| Ongoing work, any repo size | **Method 1**: Sparse Checkout |
| One-time snapshot, no history needed | **Method 2**: `git archive` |
| Large repo, ongoing work, Git 2.19+ remote | **Method 3**: Partial Clone |
| Single file only | **Alternative**: `git show` |

---

## Method 1: Sparse Checkout (recommended for ongoing work)

Use when the user needs to pull updates later or push commits back.

```bash
mkdir <local-dir> && cd <local-dir>
git init
git remote add origin <repo-url>
git config core.sparseCheckout true
echo "<path/to/subdirectory>/" >> .git/info/sparse-checkout
git pull origin <branch>
```

**Working example** — clone only `docs/tutorials/` from `main`:

```bash
mkdir my-docs && cd my-docs
git init
git remote add origin https://github.com/username/your-repo.git
git config core.sparseCheckout true
echo "docs/tutorials/" >> .git/info/sparse-checkout
git pull origin main
```

**To add more directories later:**

```bash
echo "src/utils/" >> .git/info/sparse-checkout
git pull origin main
```

**To pull updates:**

```bash
git pull origin <branch>
```

---

## Method 2: `git archive` (one-time snapshot)

Use when the user only needs the files, not the Git history or the ability to push.

```bash
git archive --remote=<repo-url> <branch>:<path/to/subdirectory> | tar -x
```

**Working example** — download `docs/tutorials/` from `main`:

```bash
git archive --remote=https://github.com/username/your-repo.git main:docs/tutorials | tar -x
```

The files are extracted into the current directory. No `.git/` folder is created — this is a plain file download.

> **Limitation**: Many public hosting platforms (GitHub, GitLab SaaS) block `git archive` over HTTPS for remote repos. If it fails with `fatal: operation not supported by protocol`, use Method 1 instead.

---

## Method 3: Partial Clone + Sparse Checkout (large repos, Git 2.19+)

Use when the repo is very large and the user wants to minimize initial download size while keeping full Git functionality.

```bash
git clone --filter=tree:0 <repo-url>
cd <repo-name>
git sparse-checkout set <path/to/subdirectory>
```

**Working example** — clone only `src/utils/` from a large repo:

```bash
git clone --filter=tree:0 https://github.com/username/large-repo.git
cd large-repo
git sparse-checkout set src/utils
```

Git fetches only the metadata on clone, then lazily fetches blob contents for `src/utils/` on checkout.

**To pull updates later:**

```bash
git pull origin <branch>
```

>[!note]
> **Requirement**: Both your local Git and the remote server must support partial clones (Git 2.19+). GitHub.com and GitLab.com support this. Self-hosted servers may not.

---

## Alternative: Fetch a single file with `git show`

Use when the user needs exactly one file and already has the repo cloned (or can do a quick fetch).

```bash
# Requires the remote to be added or already cloned
git show <remote>/<branch>:<path/to/file> > <local-filename>
```

**Working example:**

```bash
git show origin/main:docs/tutorials/intro.md > intro.md
```

> This writes a plain copy of the file. It is not tracked — you cannot `git pull` updates to it later.

---

## Gotchas

- **Trailing slash is required for directories in sparse-checkout**: Write `docs/tutorials/`, not `docs/tutorials`. Without the slash, Git may match files *named* `tutorials` instead of the directory.
- **Path is case-sensitive**: The path in `sparse-checkout` or `git archive` must exactly match the repo's path casing. On Linux hosts this will silently fail if the case is wrong.
- **`git archive` is blocked on most GitHub repos**: GitHub does not support `git archive --remote` over HTTPS for public repos. Use SSH (with a valid key) or use Method 1/3 instead.
- **`--filter=tree:0` requires server support**: If the server doesn't support it, `git clone` fails with `fatal: remote does not support filter`. Fall back to Method 1.
- **Sparse checkout does not materialize new files automatically**: After updating `.git/info/sparse-checkout`, run `git checkout HEAD` to pull the newly included paths.

---

## Full reference

For deeper details on each method, troubleshooting steps, and the full comparison table, see [references/cloning-git-subdirectories.md](references/cloning-git-subdirectories.md).

```md
### Searching Commands

Linux offers various commands to search for files, directories, and text. Use these commands to search for files and directories on the system and filter the search using various patterns.

| Command | Description |
| --- | --- |
| **`find [path] -name [search_pattern]`** | [Find files and directories](https://phoenixnap.com/kb/guide-linux-find-command) that match the specified pattern in a specified location. |
| **`find [path] -size [+100M]`** | See files and directories larger than a specified size in a directory. |
| **`fdfind [pattern] [path]`**[^fd-find] | Find files and directories, but much faster |
| **`fdfind -s +100M [path]`**[^fd-find] | Find files and directories that match the specified pattern in a specified location. |
| **`find . -type d -name "neovim"`** | Find a directory named `neovim` |
| **`fdfind -t d neovim`** | Same, but much faster |
| **`grep [search_pattern] [file_name]`** | [Search for a specific pattern](https://phoenixnap.com/kb/grep-multiple-strings) in a [file](https://phoenixnap.com/glossary/what-is-a-file) with [grep](https://phoenixnap.com/kb/grep-command-linux-unix-examples). |
| **`grep -r [search_pattern] [directory_name]`** | Recursively search for a pattern in a directory. |
| **`rg -r [search_pattern] [directory_name]`** | Recursively search for a pattern in a directory. |
| **`locate [name]`** | [Locate all files and directories](https://phoenixnap.com/kb/locate-command-in-linux) related to a particular name. |
| **`which [command]`** | [Search the command path](https://phoenixnap.com/kb/which-command-linux) in the **`$PATH`** environment variable. |
| **`whereis [command]`** | Use the [whereis command](https://phoenixnap.com/kb/whereis-command-linux) to find the source, binary, and manual page for a command. |
| **`awk '[search_pattern] {print $0}' [file_name]`** | [Print all lines matching a pattern](https://phoenixnap.com/kb/awk-command-in-linux) in a file. See also the [gawk command](https://phoenixnap.com/kb/gawk-linux), the [GNU](https://phoenixnap.com/glossary/what-is-gnu) version of **`awk`**. |
| **`sed 's/[old_text]/[new_text]/' [file_name]`** | [Find and replace text](https://phoenixnap.com/kb/sed-replace) in a specified file. |

[^fd-find]: Download this package with `sudo apt install fd-find`, but calling it with `fdfind` command. This is a faster version of `find` command. I deeply recommend using it in your workflows.

### Directory Navigation Commands

Directory navigation commands provide shortcuts to navigate to the desired location quickly. Below are several crucial shortcuts to remember when navigating directories in Linux through the terminal.

| Directory Navigation Commands | Description |
| --- | --- |
| **`ls`** | [List files and directories](https://phoenixnap.com/kb/linux-ls-commands) in the current directory. |
| **`ls -a`** | List all files and directories in the current directory ([shows hidden files](https://phoenixnap.com/kb/show-hidden-files-linux)). |
| **`ls -l`** | List files and directories in long format. |
| **`pwd`** | [Show the directory](https://phoenixnap.com/kb/pwd-linux) you are currently working in. |
| **`cd`**   **`cd ~`** | [Change directory](https://phoenixnap.com/kb/linux-cd-command) to **`$HOME`**. |
| **`cd ..`** | Move up one directory level. |
| **`cd -`** | Change to the previous directory. |
| **`cd [directory_path]`** | Change location to a specified directory. |
| **`dirs`** | Show current directory stack. |
```
