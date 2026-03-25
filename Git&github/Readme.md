git filter-repo --path reports --invert-paths
🔍 1. git

👉 The Git CLI executable
This invokes the version control system itself.

🔍 2. filter-repo

👉 A history rewriting tool (modern replacement for git filter-branch)

What it does:
Traverses every commit in your repository
Applies filters (rules)
Rewrites a new clean history

👉 Think of it as:

“Rebuild my repo history, but remove/modify specific things”

🔍 3. --path reports

👉 This is a filter condition

Meaning:

Target the path named reports

Important details:
Matches folder/file named reports
Works across ALL commits
Relative to repo root
Examples:
reports/ → entire folder
reports/file.pdf → specific file
🔍 4. --invert-paths

👉 This is the key operator (most important part)

Without this flag:
git filter-repo --path reports

👉 Means:

“Keep ONLY the reports folder, remove everything else”

With --invert-paths:
git filter-repo --path reports --invert-paths

👉 Means:

“Remove reports, keep everything else”

🧠 Logical interpretation

You can think of it like:

Selected paths = reports

Normal mode:
    KEEP selected paths

Invert mode:
    REMOVE selected paths

Git rev-parse — Complete Notes
🔷 What is git rev-parse?

👉 A low-level (plumbing) Git command used to:

Resolve references (branches, HEAD, tags → commit hashes)
Extract repository metadata (paths, state)
Help in scripting and automation

Think: “Git’s internal resolver + info extractor”

🔹 1. Repository Location & Structure
✅ Get repo root
git rev-parse --show-toplevel

Output:

/home/aditya/Devops

✔ Use-case:

Ensure you're inside correct repo
Navigate to root in scripts
✅ Get .git directory
git rev-parse --git-dir

Output:

.git

✔ Use-case:

Access Git internals
Debug repo config/issues
✅ Get relative path inside repo
git rev-parse --show-prefix

Output (inside Docker/):

Docker/

✔ Use-case:

Know current position in repo
✅ Show path from root to current dir
git rev-parse --show-cdup

Output:

../

✔ Use-case:

Navigate back to repo root programmatically
🔹 2. Repository State Checks
✅ Check if inside repo
git rev-parse --is-inside-work-tree

Output:

true

✔ Use-case:

Script safety check
✅ Check if inside .git directory
git rev-parse --is-inside-git-dir

✔ Use-case:

Avoid running commands in wrong context
✅ Check if repo is bare
git rev-parse --is-bare-repository

✔ Use-case:

CI/CD or server repos
🔹 3. Commit / Reference Resolution
✅ Get current commit (HEAD)
git rev-parse HEAD

✔ Output:

a3f5c9d8e2b1f6...
✅ Get short commit hash
git rev-parse --short HEAD

✔ Output:

a3f5c9d
✅ Resolve branch → commit
git rev-parse main
✅ Resolve previous commit
git rev-parse HEAD~1
✅ Resolve nth parent
git rev-parse HEAD~3
✅ Resolve tag → commit
git rev-parse v1.0

✔ Use-case:

Logging
CI/CD versioning
Debugging commit history
🔹 4. Branch Information
✅ Get current branch name
git rev-parse --abbrev-ref HEAD

✔ Output:

main
⚠️ Detached HEAD case:
HEAD

✔ Means you're not on a branch

✔ Use-case:

Deployment scripts
Conditional logic based on branch
🔹 5. Object Path & Storage
✅ Get object directory
git rev-parse --git-path objects

✔ Use-case:

Advanced Git internals
Debug object storage
✅ Get hooks directory
git rev-parse --git-path hooks
🔹 6. Safe Argument Parsing (Important for scripts)
✅ Normalize revision input
git rev-parse --verify HEAD

✔ Use-case:

Ensure commit exists
Prevent script failures
❌ If invalid:
fatal: Needed a single revision
🔹 7. Path Conversion
✅ Convert relative → absolute path
git rev-parse --show-toplevel
✅ Combine with shell
cd $(git rev-parse --show-toplevel)

✔ Use-case:

Always operate from repo root
🔹 8. Hidden but Powerful (DevOps usage)
✅ Get repo root + run command
ROOT=$(git rev-parse --show-toplevel)
cd $ROOT && docker build .
✅ Use commit hash in Docker tagging
docker build -t app:$(git rev-parse --short HEAD) .

✔ Output:

app:a3f5c9d
✅ CI/CD versioning
VERSION=$(git rev-parse --short HEAD)
echo "Deploying version $VERSION"
🔹 9. Debugging Use Cases
✅ Confirm repo context
git rev-parse --is-inside-work-tree
✅ Find root when lost in nested folders
git rev-parse --show-toplevel
✅ Check current working directory in repo
git rev-parse --show-prefix
🔥 Summary Table
Category	Command	Purpose
Repo Root	--show-toplevel	Find repo root
Git Dir	--git-dir	Locate .git
Current Path	--show-prefix	Relative path
Repo Check	--is-inside-work-tree	Validate repo
Commit Hash	HEAD	Current commit
Short Hash	--short HEAD	Compact hash
Branch Name	--abbrev-ref HEAD	Current branch
Resolve Ref	main	Branch → commit
Previous Commit	HEAD~1	History traversal
Script Safety	--verify	Validate refs
🧠 Final Mental Model

git rev-parse is used for:

1. Where am I?
--show-toplevel
--show-prefix
2. What am I on?
HEAD
--abbrev-ref HEAD
3. What commit is this?
HEAD
main
HEAD~1
4. Is this a repo?
--is-inside-work-tree
🚀 When YOU should use it
Writing shell scripts
Building CI/CD pipelines
Debugging Git issues
Handling dynamic paths + versions