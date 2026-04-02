---
title: "How to Clone Only a Subdirectory in Git: Pull Specific Files or Directories with Alternative Commands"
source: "https://www.tutorialpedia.org/blog/cloning-only-a-subdirectory-with-git/#4-define-the-subdirectory-to-checkout"
author:
  - "[[tutorialpedia]]"
published: 2026-01-16
created: 2026-04-01
description: "Git is a powerful version control system, but its default behavior—cloning an entire repository—can be inefficient in certain scenarios. For example, if you’re working with a massive repository (e.g., containing thousands of files, large binaries, or multiple projects), cloning the entire repo may consume unnecessary bandwidth, storage, or time.What if you only need a specific subdirectory (e.g., `docs/`, `src/utils/`, or `assets/images/`)? Git doesn’t natively support \"cloning a subdirectory\" out of the box, but several workarounds let you achieve this. In this guide, we’ll explore **step-by-step methods** to clone only a subdirectory, along with alternatives for pulling specific files. We’ll cover everything from basic sparse checkout to advanced partial clones, ensuring you can choose the best approach for your use case."
tags:
  - "git"
  - "version control"
  - "cloning git repos"
  - "sparse checkout"
  - "git archive"
  - "partial clone"
  - "git show"
  - "tutorial"
---
1. [Why Clone Only a Subdirectory?](https://www.tutorialpedia.org/blog/cloning-only-a-subdirectory-with-git/#why-clone-only-a-subdirectory)
2. [Understanding Git’s Limitation: No "Direct Subdirectory Clone"](https://www.tutorialpedia.org/blog/cloning-only-a-subdirectory-with-git/#understanding-gits-limitation-no-direct-subdirectory-clone)
3. [Method 1: Sparse Checkout (Recommended for Ongoing Work)](https://www.tutorialpedia.org/blog/cloning-only-a-subdirectory-with-git/#method-1-sparse-checkout-recommended-for-ongoing-work)
4. [Method 2: Using `git archive` (Snapshot of a Subdirectory)](https://www.tutorialpedia.org/blog/cloning-only-a-subdirectory-with-git/#method-2-using-git-archive-snapshot-of-a-subdirectory)
5. [Method 3: Partial Clone with `--filter` (Git 2.19+)](https://www.tutorialpedia.org/blog/cloning-only-a-subdirectory-with-git/#method-3-partial-clone-with---filter-git-219)
6. [Alternative: Pulling Specific Files (Not Directories)](https://www.tutorialpedia.org/blog/cloning-only-a-subdirectory-with-git/#alternative-pulling-specific-files-not-directories)
7. [Troubleshooting Common Issues](https://www.tutorialpedia.org/blog/cloning-only-a-subdirectory-with-git/#troubleshooting-common-issues)
8. [Best Practices: Which Method to Choose?](https://www.tutorialpedia.org/blog/cloning-only-a-subdirectory-with-git/#best-practices-which-method-to-choose)
9. [Conclusion](https://www.tutorialpedia.org/blog/cloning-only-a-subdirectory-with-git/#conclusion)
10. [References](https://www.tutorialpedia.org/blog/cloning-only-a-subdirectory-with-git/#references)

## Why Clone Only a Subdirectory?

Before diving into methods, let’s clarify *why* you might need to clone only a subdirectory:

- **Large Repository Size**: Repos with gigabytes of data (e.g., containing binaries, datasets, or legacy code) take too long to clone entirely.
- **Bandwidth/Storage Constraints**: Limited internet or disk space makes full clones impractical.
- **Focused Workflow**: You only need a specific component (e.g., documentation, a microservice, or assets) and don’t care about the rest.
- **Avoid Clutter**: Cloning the entire repo adds unnecessary files to your local environment.

## Understanding Git’s Limitation: No "Direct Subdirectory Clone"

Git is designed to track entire repositories, not individual directories or files. The `git clone` command fetches the *entire* commit history, branches, and files by default. There’s no built-in `git clone --subdirectory=path` flag. However, Git provides tools like `sparse checkout`, `git archive`, and partial clones to simulate subdirectory cloning.

**Sparse checkout** is Git’s built-in feature to "filter" which files/directories are checked out locally, even if the repo contains thousands of others. It keeps the full Git history but only makes specific directories visible.

### Step-by-Step Guide

#### 1. Initialize a New Git Repository

Start by creating an empty local repo (we’ll pull the remote later):

```bash
mkdir my-sparse-repo && cd my-sparse-repo
git init
```

#### 2. Link to the Remote Repository

Add the URL of the remote repo you want to clone from:

```bash
git remote add origin https://github.com/username/your-repo.git
```

#### 3. Enable Sparse Checkout

Tell Git to use sparse checkout:

```bash
git config core.sparseCheckout true
```

#### 4. Define the Subdirectory to Checkout

Specify the subdirectory path in the `sparse-checkout` file (stored in `.git/info/`). Use relative paths from the repo root.

For example, to clone only `docs/tutorials/`:

```bash
echo "docs/tutorials/" >> .git/info/sparse-checkout
```

- **Important**: Trailing slashes (`/`) matter! Use `docs/tutorials/` for directories, not `docs/tutorials` (this avoids matching files named `tutorials`).
- **Multiple directories**: Add more lines to `sparse-checkout` (e.g., `src/utils/` on a new line).

#### 5. Pull the Remote Content

Fetch and checkout the files from the remote (e.g., `main` branch):

```bash
git pull origin main
```

Now, your local repo will only contain `docs/tutorials/` (and the hidden `.git/` directory).

#### 6. Updating the Subdirectory Later

To fetch updates from the remote for your sparse directory:

```bash
git pull origin main
```

Git will only update the files in `docs/tutorials/`.

## Method 2: Using git archive (Snapshot of a Subdirectory)

If you don’t need a full Git repository (e.g., no commit history, branches, or ability to push changes), `git archive` lets you download a **snapshot** of a subdirectory as a tar/zip file. This is ideal for one-time file retrieval.

### How It Works

`git archive` creates an archive (tar/zip) of specific files/directories from a Git repository. You can fetch this archive directly from a remote repo and extract it locally.

### Step-by-Step Guide

#### 1. Fetch the Subdirectory as an Archive

Use `git archive` with the remote URL, branch/tag, and subdirectory path. Pipe the output to `tar` to extract files:

```bash
# Syntax: git archive --remote=<remote-url> <branch/tag>:<subdirectory> | tar -x
git archive --remote=https://github.com/username/your-repo.git main:docs/tutorials | tar -x
```

- `<remote-url>`: URL of the remote repo (HTTPS or SSH).
- `<branch/tag>`: The branch (e.g., `main`) or tag (e.g., `v1.0`) to fetch from.
- `<subdirectory>`: Path to the subdirectory (e.g., `docs/tutorials`).
- `tar -x`: Extracts the tar archive (add `-v` for verbose output).

#### 2. Verify the Files

You’ll now have a `tutorials/` directory (or the subdirectory name) with all files from the remote.

### Limitations

- **No Git History**: The extracted files are just a snapshot—no `.git` directory, so you can’t commit/push changes.
- **No Remote Tracking**: You can’t update the directory later with `git pull`; you’d need to re-run `git archive`.

## Method 3: Partial Clone with --filter (Git 2.19+)

Introduced in Git 2.19 (2018), **partial clones** let you fetch only the *minimum* data needed to work with a repo. Combined with sparse checkout, this reduces the initial clone size significantly.

### How It Works

Partial clones use the `--filter` flag to exclude unnecessary data (e.g., blobs, trees) during cloning. The `--filter=tree:0` option fetches only metadata (commit history, branch names) but no file contents (blobs), resulting in a tiny initial clone. You then use sparse checkout to fetch the specific directory’s files.

### Step-by-Step Guide

#### 1. Clone with Partial Filter

Run `git clone` with `--filter=tree:0` to fetch minimal metadata:

```bash
git clone --filter=tree:0 https://github.com/username/your-repo.git
cd your-repo
```

The clone will be much smaller (e.g., 10MB instead of 1GB for large repos).

#### 2. Enable Sparse Checkout for the Subdirectory

Now, tell Git to checkout only your target subdirectory:

```bash
git sparse-checkout set docs/tutorials
```

Git will fetch the blobs (file contents) for `docs/tutorials/` and make them visible locally.

#### 3. (Optional) Update Later

To fetch updates, use `git pull` as usual—Git will only download changes for the checked-out subdirectory.

### Benefits

- **Small Initial Clone**: Metadata-only clone saves bandwidth/storage.
- **Full Git Functionality**: You retain history, branches, and can commit/push changes (if you have write access).

## Alternative: Pulling Specific Files (Not Directories)

Sometimes you need **individual files**, not entire directories. Git isn’t designed for this, but workarounds exist:

### Using git show

Fetch a single file from a remote repo using `git show`:

```bash
# Syntax: git show <remote>/<branch>:<file-path> > <local-file-name>
git show origin/main:docs/tutorials/intro.md > intro.md
```

- `<remote>/<branch>`: Remote and branch (e.g., `origin/main`).
- `<file-path>`: Path to the file in the repo (e.g., `docs/tutorials/intro.md`).
- `> <local-file-name>`: Saves the file locally (omit to print to terminal).

### Limitations

- No version tracking: The file isn’t part of a local Git repo, so you can’t commit changes or pull updates easily.

## Troubleshooting Common Issues

### "Subdirectory Not Showing Up After Sparse Checkout"

- **Incorrect Path**: Ensure the path in `.git/info/sparse-checkout` matches the remote repo’s structure (case-sensitive!).
- **Missing Trailing Slash**: For directories, always add a trailing slash (e.g., `docs/tutorials/`, not `docs/tutorials`).
- **Forgot to Pull**: Run `git pull origin <branch>` after setting up sparse checkout.
- The remote repo may not allow `git archive` (e.g., private repos require authentication). Use SSH instead of HTTPS, or clone the repo first (with sparse checkout) if you have access.

### "Partial Clone Fails: ‘fatal: remote does not support filter’"

- Some older Git servers (e.g., GitHub Enterprise pre-2.22) don’t support partial clones. Use sparse checkout (Method 1) instead.

## Best Practices: Which Method to Choose?

| Method | Use Case | Pros | Cons |
| --- | --- | --- | --- |
| Sparse Checkout | Ongoing work with a subdirectory | Full Git history, updateable | Initial clone may still fetch large metadata |
| `git archive` | One-time snapshot of a subdirectory | Fast, no Git overhead | No history, can’t push changes |
| Partial Clone | Large repos with ongoing work | Small initial clone, full Git features | Requires Git 2.19+, remote support |
| `git show` | Individual files (no directories) | Simple, no repo setup | No version tracking |

## Conclusion

While Git doesn’t natively support cloning subdirectories, tools like `sparse checkout`, `git archive`, and partial clones let you achieve this efficiently. Choose:

- **Sparse checkout** for ongoing work with a subdirectory.
- **git archive** for one-time file snapshots.
- **Partial clones** for large repos with limited bandwidth.

For individual files, use `git show` as a last resort. Always verify paths and remote access to avoid common pitfalls!

## References

- [Git Sparse Checkout Documentation](https://git-scm.com/docs/git-sparse-checkout)
- [Git Archive Documentation](https://git-scm.com/docs/git-archive)
- [Git Partial Clone Documentation](https://git-scm.com/docs/partial-clone)
- [GitHub: Sparse Checkout Guide](https://github.blog/2020-01-17-bring-your-monorepo-down-to-size-with-sparse-checkout/)
- [Stack Overflow: Clone a Subdirectory in Git](https://stackoverflow.com/questions/600079/how-do-i-clone-a-subdirectory-only-of-a-git-repository)
