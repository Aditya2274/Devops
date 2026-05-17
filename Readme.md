# DevOps Learning Repo

This repository is a hands-on collection of small examples and notes you can use to upskill your DevOps knowledge. The content is organized by folder name; most folders contain ready-to-run examples or short documentation. Use this README as a quick map and a suggested learning path.

## How to use this repo

1. Clone the repo locally and open it in your editor of choice.
2. Read the `Readme.md` inside each folder when present (some folders have a single README). If a folder has no README but contains files, open those files — their names usually describe the content.
3. Try the examples locally (many are small Docker/Python demos). Run one example end-to-end, then read and tweak the code or Dockerfile to learn how changes affect behavior and the image.
4. Repeat: pick a different folder and try a new exercise. Track what you learned in a personal notes file or a PR-style change in the repo.

## Folder overview

- `Docker/` — Practical Docker examples and notes. This is the most content-rich area right now.
	- `Portforwarding.md` — A focused document that explains port forwarding with Docker containers (read this to understand host<->container networking basics).
	- subfolders include container examples such as `bind_mount`, `Container_with_localDB`, `demo`, `interactive-mode`, `multiple_container`, `userinfo`, and `working_with_api` — each contains a `Dockerfile` and small demo scripts like `myapp.py` or `sql_demo.py`.
	- Suggested exercises: build and run each Docker example, inspect image layers, experiment with `--no-cache-dir` for pip installs, and try Docker BuildKit cache mounts for faster iterative builds.

- `Git&github/` — A folder with `Readme.md` containing Git and GitHub notes/exercises. Start here if you want to strengthen your source-control workflows (branches, PRs, rebasing, tags, hooks).

- `yaml/` — Various YAML and related config examples. There is no `Readme.md` here yet, but the filenames are descriptive:
	- `datatypes.yml`, `advanceDatatype.yml`, `hello.yaml`, `school.yml` and also `school.json` / `school.xml` for format comparison.
	- Suggested exercises: validate YAML with `yamllint`/`yq`, convert JSON↔YAML, write a small Kubernetes manifest based on these examples, and try templating with Helm or Kustomize.

## Quick learning path (suggested)

1. Git fundamentals: open `Git&github/Readme.md` and follow the exercises there. Practice branching, committing, pushing, and making PRs.
2. Docker basics: read `Docker/Portforwarding.md` then build and run `Docker/demo` and `Docker/userinfo` examples to get comfortable with Dockerfiles, volumes, and ports.
3. Intermediate Docker: try `Container_with_localDB` and `multiple_container` to learn about multi-container setups, bind mounts, and networking between containers.
4. Configuration and manifests: use `yaml/` to practice writing and validating configuration files and transform them into simple Kubernetes manifests.
5. Automation & CI: once comfortable, add a GitHub Actions workflow to build and test one Docker example on push.

## Commands to try (zsh / Linux)
Open a terminal and run these from the repo root:

```bash
# list top-level folders
ls -la

# explore Docker examples
cd Docker
ls -la

# build a specific example (adjust the path to the folder you want)
docker build -f Container_with_localDB/Dockerfile -t my-sql-demo ./Container_with_localDB

# run the image interactively (if the demo supports it)
docker run --rm -it my-sql-demo

# validate a YAML file (install yamllint or yq first)
yamllint yaml/hello.yaml
``` 

Note: some examples use Python. If a Dockerfile installs Python packages, you may see `--no-cache-dir` used with pip to avoid leaving pip's download cache in the final image (this keeps images smaller).

## Prerequisites

- Docker installed and running
- (Optional) Python 3.11+ for running local scripts outside containers
- (Optional) `yamllint` / `yq` if you want to validate and manipulate YAML locally

## Next steps and ideas

- Add `Readme.md` files for the `yaml/` folder and for other Docker subfolders that don't have one, describing how to run each demo.
- Add simple GitHub Actions workflows that build Docker images for `Docker/demo` and run any included tests.
- Convert a few `yaml/` examples into Kubernetes manifests and add `kubectl --dry-run=client -f` checks.

---

If you'd like, I can:
- create missing `Readme.md` files inside `yaml/` and other folders with run instructions, or
- add a minimal GitHub Actions workflow that builds one of the Docker examples.

Tell me which follow-up you'd prefer and I'll implement it.

__Port managing(in linux)__:
Once you understand ports properly, debugging servers becomes 10x easier.

Let’s make this crystal clear.

🧠 What Is A Port?

Think of your system like:

IP Address = Building
Ports = Room numbers

Example:

localhost:3000

means:

your computer → room 3000

A process/app binds itself to a port.

🚨 Why Port Conflicts Happen

Suppose:

Node app uses 3000

Then another app also tries:

listen on 3000

Linux says:

Port already in use

because:

only ONE process can bind to a port at a time.

🔥 MOST IMPORTANT COMMANDS

These are the REAL commands you must know.

1️⃣ See Which Process Uses A Port
Modern command:
sudo lsof -i :3000

Example output:

node    12345 user   23u  IPv4 ...

Meaning:

Node app
PID = 12345
using port 3000
2️⃣ Kill Process Using Port
kill -9 12345

Now port becomes free.

🚀 Faster One-Liner
sudo kill -9 $(sudo lsof -t -i:3000)

Kills whatever uses port 3000.

VERY useful.

3️⃣ See All Listening Ports
sudo ss -tulnp

Modern replacement for netstat.

Shows:

TCP
UDP
listening ports
process names
4️⃣ Filter Specific Port
sudo ss -tulnp | grep 8080

Useful for:

Jenkins
Node
Docker
nginx
🧠 Common Dev Ports
Service	Port
React/Vite	5173
Node/Express	3000
MongoDB	27017
MySQL	3306
Jenkins	8080
nginx	80
HTTPS	443
SSH	22
Docker Registry	5000
🚀 Changing Ports
Node/Express
app.listen(5000)
React/Vite
npm run dev -- --port 4000
Jenkins

Edit:

/etc/default/jenkins

Find:

HTTP_PORT=8080

Change to:

HTTP_PORT=9090

Restart:

sudo systemctl restart jenkins
Docker Port Mapping

VERY important.

Example:

docker run -p 8081:8080 image

Meaning:

Host	Container
8081	8080

So browser uses:

localhost:8081

while app inside container still uses:

8080
🚨 VERY Common Problem

You close terminal but app still runs.

Example:

Node server still alive
Vite still alive
Docker container still alive

Then next run:

EADDRINUSE

means:

address already in use.

🔥 How To Debug Properly
Step 1

Check port:

sudo lsof -i :3000
Step 2

See process:

PID
Step 3

Kill:

kill -9 PID
Step 4

Restart app.

🧠 Docker Port Understanding
Container Port vs Host Port

Example:

docker run -p 9000:8080 jenkins

means:

Machine	Container
localhost:9000	container:8080

Browser:

localhost:9000

Container internally:

8080

VERY important concept.

🔥 How To See Docker Containers Using Ports
docker ps

Example:

0.0.0.0:8080->8080/tcp

means:

host 8080
mapped to container 8080
🚀 Stop Docker Container
docker stop container_id

or:

docker stop container_name
🧠 Best Practices
Development

Use:

3000
5173
8080
Multiple Apps

Use:

3001
3002
8081
8082
Production

Usually:

nginx → 80/443
backend internal ports hidden
🚀 MOST IMPORTANT DEVOPS UNDERSTANDING

Port conflict means:

two processes trying to occupy same network socket.

That’s all.

🏆 Commands You ABSOLUTELY Must Remember
Find process using port
sudo lsof -i :PORT
Kill process
kill -9 PID
See listening ports
sudo ss -tulnp
Docker running containers
docker ps