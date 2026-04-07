Image Layer Optimization in a Startup
Scenario
A startup notices that its Docker images are very large and image builds are slow. The team wants a better Dockerfile strategy so images become smaller and rebuilds become faster. The main reason this is possible is that Docker images are made from layers, and Docker can reuse old layers from cache if the Dockerfile is written in a smart order.
This guide gives a complete step-by-step solution for a beginner. It explains every command, every file, the logic behind correct layer ordering, and a timer mechanism so image build time can be demonstrated and compared.
Learning Goals
By the end of this exercise, a beginner should be able to:
·	create a Dockerfile
·	understand what FROM, WORKDIR, COPY, RUN, and CMD do
·	understand what Docker layers are
·	understand why Docker layer order affects speed
·	use docker build and docker history
·	measure image build time with a timer
·	compare a bad Dockerfile with an optimized Dockerfile
Big Idea in One Line
Copy rarely changing files first and frequently changing files later, so Docker can reuse cached layers and avoid repeating expensive work.
What Is a Docker Image Layer?
A Docker image is not a single flat file. It is built as a stack of layers. Most important Dockerfile instructions create a new layer. Docker stores those layers and tries to reuse them on later builds.
For example:
·	FROM chooses the base image
·	RUN executes commands and usually creates a layer
·	COPY copies files into the image and usually creates a layer
If a layer has not changed, Docker can often reuse it. If an early layer changes, the later layers usually need to be rebuilt too. This is why the order of instructions matters so much.
Why Builds Become Slow
Many beginners write a Dockerfile like this:
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

This works, but it is inefficient.
Why it is inefficient:
1.	COPY . . copies everything first.
2.	Even a tiny change in the source code changes that layer.
3.	Once that layer changes, Docker cannot reuse the next install layer safely.
4.	So pip install -r requirements.txt runs again.
5.	Dependency installation is often the slowest part of the build.
So a tiny code change can trigger a large rebuild.
Better Strategy
A better Dockerfile should:
·	use a smaller base image
·	copy dependency files first
·	install dependencies before copying the full source code
·	avoid unnecessary files in build context
·	make Docker cache work in our favor
Project Structure
Create a folder like this:
optimizedapp/
├── app.py
├── requirements.txt
├── Dockerfile.bad
├── Dockerfile
└── .dockerignore

Step 1: Create a Project Folder
Open the terminal or command prompt and create a new folder.
mkdir optimizedapp
cd optimizedapp

Why this step matters
This creates a separate working directory so all files stay organized. A beginner should avoid mixing Docker demo files with unrelated files, because that creates confusion and may accidentally increase the Docker build context.
Step 2: Create the Application File
Create a file named app.py with the following content:
print("Hello from optimized Docker app")

Why this step matters
We are deliberately using a very small Python program so the focus stays on Docker concepts instead of application complexity. The goal here is to understand image optimization, not Python programming.
Step 3: Create the Dependency File
Create a file named requirements.txt:
flask==3.0.0
requests==2.31.0

Why this step matters
This file represents Python dependencies. In real projects, dependency installation is often one of the slowest build steps. That makes it the perfect example for demonstrating Docker layer cache behavior.
Step 4: Create a Bad Dockerfile for Comparison
Create a file named Dockerfile.bad:
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]

Line-by-line explanation
FROM python:3.11
This tells Docker to start from the official Python 3.11 base image.
Reasoning:
·	Docker needs a starting point.
·	A base image already contains an operating system layer and Python runtime.
·	The full python:3.11 image is larger than slim variants, so it increases image size.
WORKDIR /app
This sets /app as the working directory inside the image.
Reasoning:
·	It keeps files organized.
·	Later commands will run from this directory automatically.
·	It reduces the need to type full paths again and again.
COPY . .
This copies everything from the current host folder into the current directory inside the image.
Reasoning:
·	It is easy to write, but it is a common optimization mistake.
·	If even one source file changes, this layer changes.
·	That can force later layers to rebuild, including dependency installation.
RUN pip install -r requirements.txt
This installs all Python dependencies.
Reasoning:
·	It is an expensive step in many projects.
·	If Docker has to repeat it every time, builds become slow.
CMD ["python", "app.py"]
This defines the default command that runs when the container starts.
Reasoning:
·	It tells the container what to do at runtime.
·	It does not usually affect build optimization much, but it is needed to run the app.
Step 5: Create the Optimized Dockerfile
Create a file named Dockerfile:
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]

Why this Dockerfile is better
FROM python:3.11-slim
This uses a smaller version of the Python image.
Reasoning:
·	Smaller base image means smaller final image.
·	Smaller images are faster to download, store, and push to registries.
·	A startup benefits because deployments become quicker and storage costs can be lower.
WORKDIR /app
Same purpose as before.
Reasoning:
·	Maintains a clean directory structure inside the image.
COPY requirements.txt .
This copies only the dependency file first.
Reasoning:
·	Dependencies usually change less often than application code.
·	If only the source code changes later, this layer can stay cached.
·	That means the dependency installation layer may also stay cached.
RUN pip install --no-cache-dir -r requirements.txt
This installs dependencies without keeping pip's package cache.
Reasoning:
·	Installing dependencies early allows Docker to reuse this layer when requirements.txt has not changed.
·	--no-cache-dir prevents pip from storing unnecessary package cache files inside the image.
·	That reduces final image size.
COPY app.py .
This copies the application source after dependencies are installed.
Reasoning:
·	Source code changes more frequently.
·	Putting it later means only this layer needs rebuilding after code edits.
·	This is the heart of Docker layer optimization.
CMD ["python", "app.py"]
Same runtime command as before.
Step 6: Create .dockerignore
Create a file named .dockerignore:
__pycache__
*.pyc
*.pyo
*.pyd
.git
.gitignore
Dockerfile.bad
README.md

Why this tiny file matters
When Docker builds an image, it first sends the build context to the Docker daemon. The build context usually includes the files in the current folder.
If the folder contains unnecessary files, then:
·	more data is sent during build
·	builds may become slower
·	cache may break unnecessarily
·	unwanted files may get copied into the image
.dockerignore works like .gitignore, but for Docker build context. It tells Docker which files to ignore.
Step 7: Build the Bad Image
Run:
docker build -f Dockerfile.bad -t optimizedapp:bad .

What each part means
·	docker build tells Docker to build an image.
·	-f Dockerfile.bad says to use the file named Dockerfile.bad.
·	-t optimizedapp:bad gives the image a name and tag.
·	. means the current directory is the build context.
Why we build the bad image first
We want a comparison baseline. Without a baseline, it is hard to prove that optimization helped.
Step 8: Build the Optimized Image
Run:
docker build -t optimizedapp:v1 .

Why this step matters
Now we build the improved image. This is the version students are expected to defend conceptually. It uses better layer ordering and a smaller base image.
Step 9: Run the Images
Run the bad image:
docker run --rm optimizedapp:bad

Run the optimized image:
docker run --rm optimizedapp:v1

Expected output:
Hello from optimized Docker app

Why --rm is used
--rm tells Docker to automatically remove the container after it stops.
Reasoning:
·	keeps the system clean
·	avoids extra stopped containers
·	especially helpful for beginners during repeated testing
Step 10: Inspect Layers with docker history
Inspect the optimized image:
docker history optimizedapp:v1

Inspect the bad image:
docker history optimizedapp:bad

Why this step matters
docker history shows the layers used to create the image. This lets students see the practical result of the Dockerfile instructions.
What students should observe
They should look for:
·	the base image layer size
·	the dependency installation layer
·	the application copy layer
·	differences caused by using python:3.11 vs python:3.11-slim
This command helps connect theory to reality. Instead of merely hearing that images have layers, students can actually inspect them.
Step 11: Add a Timer to Measure Build Time
To prove optimization, students should measure build time.
Option A: Linux or macOS
Use the time command.
Bad image build timing:
time docker build -f Dockerfile.bad -t optimizedapp:bad .

Optimized image build timing:
time docker build -t optimizedapp:v1 .

aditya-2274@aditya-2274-IdeaPad-3-15IAU7 Docker/image_optimization (main) » time docker build -t optimizedapp:v1 .
[+] Building 0.5s (10/10) FINISHED                                                                                                                                               docker:default
 => [internal] load build definition from Dockerfile                                                                                                                                       0.0s
 => => transferring dockerfile: 189B                                                                                                                                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                                                        0.0s
 => [internal] load .dockerignore                                                                                                                                                          0.0s
 => => transferring context: 110B                                                                                                                                                          0.0s
 => [1/5] FROM docker.io/library/python:3.11-slim@sha256:9358444059ed78e2975ada2c189f1c1a3144a5dab6f35bff8c981afb38946634                                                                  0.0s
 => => resolve docker.io/library/python:3.11-slim@sha256:9358444059ed78e2975ada2c189f1c1a3144a5dab6f35bff8c981afb38946634                                                                  0.0s
 => [internal] load build context                                                                                                                                                          0.0s
 => => transferring context: 62B                                                                                                                                                           0.0s
 => CACHED [2/5] WORKDIR /myapp                                                                                                                                                            0.0s
 => CACHED [3/5] COPY requirements.txt .                                                                                                                                                   0.0s
 => CACHED [4/5] RUN pip install --no-cache -r requirements.txt                                                                                                                            0.0s
 => CACHED [5/5] COPY app.py .                                                                                                                                                             0.0s
 => exporting to image                                                                                                                                                                     0.4s
 => => exporting layers                                                                                                                                                                    0.0s
 => => exporting manifest sha256:66c17d39552674efaad73ceea5925d4cad33651afbd76fd5c65e92e6009b9bed                                                                                          0.0s
 => => exporting config sha256:246ead9f6930390d1e1dc044d4299929986441f43a8de160e7a443e5c309efd3                                                                                            0.0s
 => => exporting attestation manifest sha256:9c78e46e4d7b04b100f48a05c6ee7874b2b09fc0a9e0df31ee4ceebc27ad10bb                                                                              0.0s
 => => exporting manifest list sha256:ff281db503579f6e4e15a43b7cc2ce9d99c7b79d2567bfd56dbb0b03f1bd55f4                                                                                     0.0s
 => => naming to docker.io/library/optimizedapp:v1                                                                                                                                         0.0s
 => => unpacking to docker.io/library/optimizedapp:v1                                                                                                                                      0.3s
docker build -t optimizedapp:v1 .  0.14s user 0.07s system 30% cpu 0.689 total

Example output:
real    0m18.421s
user    0m0.520s
sys     0m0.250s

What these values mean
·	real is the total wall-clock time seen by the user.
·	user is CPU time spent in user mode.
·	sys is CPU time spent in system mode.
For beginners, the most important value is real, because it shows actual elapsed build time.
Option B: Windows PowerShell
Use Measure-Command.
Bad image build timing:
Measure-Command { docker build -f Dockerfile.bad -t optimizedapp:bad . }

Optimized image build timing:
Measure-Command { docker build -t optimizedapp:v1 . }

Example output:
Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 15
Milliseconds      : 120

Why the timer is important
Optimization should not remain a theoretical claim. The timer turns the result into measurable evidence. A startup cares about time because repeated builds happen many times every day.
Step 12: Demonstrate the Real Advantage with a Rebuild
The first build alone may not fully show the power of correct layer ordering, especially if Docker is still downloading base images or if nothing has been cached yet.
The real test is to change only the source code and rebuild.
Modify app.py like this:
print("Hello from optimized Docker app - updated version")

Rebuild the bad image
Linux or macOS:
time docker build -f Dockerfile.bad -t optimizedapp:bad2 .

Bad image build example:
aditya-2274@aditya-2274-IdeaPad-3-15IAU7 Docker/image_optimization (main) » time docker build -f Dockerfile.bad -t optimizedapp:bad .
[+] Building 73.2s (10/10) FINISHED                                                                                                                                              docker:default
 => [internal] load build definition from Dockerfile.bad                                                                                                                                   0.0s
 => => transferring dockerfile: 145B                                                                                                                                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.11                                                                                                                             4.2s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                              0.0s
 => [internal] load .dockerignore                                                                                                                                                          0.0s
 => => transferring context: 110B                                                                                                                                                          0.0s
 => [1/4] FROM docker.io/library/python:3.11@sha256:7076cc3363aeea9624548c01194745480602f173f3c528ec746affc4cd59f774                                                                      62.8s
 => => resolve docker.io/library/python:3.11@sha256:7076cc3363aeea9624548c01194745480602f173f3c528ec746affc4cd59f774                                                                       0.0s
 => => sha256:4e8ce30c1c4c3682691cd17dc5be39717cb0f67dc289254b69341b3bce681167 250B / 250B                                                                                                 0.8s
 => => sha256:0b4f6d60dcda26a8e3e7d6400d9d72a4a45228991b161cca93df7b35d594aeff 23.96MB / 23.96MB                                                                                          12.7s
 => => sha256:c30fe4e5a0d64ddeb396947cd40be87429b302568458241d99054360e7d757cb 6.09MB / 6.09MB                                                                                             4.7s
 => => sha256:1ecbddc58afba44ec9b55fb51ec8bfdee5112cd31b39b564f5abb4567d094ffc 236.08MB / 236.08MB                                                                                        57.9s
 => => sha256:5397da1d1537c4d725f3090c5688a582e14eeaf7743d75d9b38bad1649554987 67.78MB / 67.78MB                                                                                          33.0s
 => => sha256:f33970743aee750df25f6c661132b7401c8fefe930e5f4803f4c8b6f567a6b55 25.62MB / 25.62MB                                                                                          14.5s
 => => sha256:a7730063fcfe708b222d34c4f07d633dfe087a28c05c4daaab2fa9943854c155 49.30MB / 49.30MB                                                                                          22.0s
 => => extracting sha256:a7730063fcfe708b222d34c4f07d633dfe087a28c05c4daaab2fa9943854c155                                                                                                  0.9s
 => => extracting sha256:f33970743aee750df25f6c661132b7401c8fefe930e5f4803f4c8b6f567a6b55                                                                                                  0.4s
 => => extracting sha256:5397da1d1537c4d725f3090c5688a582e14eeaf7743d75d9b38bad1649554987                                                                                                  1.1s
 => => extracting sha256:1ecbddc58afba44ec9b55fb51ec8bfdee5112cd31b39b564f5abb4567d094ffc                                                                                                  4.0s
 => => extracting sha256:c30fe4e5a0d64ddeb396947cd40be87429b302568458241d99054360e7d757cb                                                                                                  0.2s
 => => extracting sha256:0b4f6d60dcda26a8e3e7d6400d9d72a4a45228991b161cca93df7b35d594aeff                                                                                                  0.5s
 => => extracting sha256:4e8ce30c1c4c3682691cd17dc5be39717cb0f67dc289254b69341b3bce681167                                                                                                  0.0s
 => [internal] load build context                                                                                                                                                          0.0s
 => => transferring context: 17.61kB                                                                                                                                                       0.0s
 => [2/4] WORKDIR /myapp                                                                                                                                                                   0.7s
 => [3/4] COPY . .                                                                                                                                                                         0.0s
 => [4/4] RUN pip install -r requirements.txt                                                                                                                                              4.1s
 => exporting to image                                                                                                                                                                     1.3s 
 => => exporting layers                                                                                                                                                                    0.8s 
 => => exporting manifest sha256:b4ffb2948d8e8e5c59414725fd3b3c3421411a54be4cfd89112e6d3cdcbf10b8                                                                                          0.0s 
 => => exporting config sha256:a551df6dc5903e3ba0853edeb75f340f7767b5e3011682de35f093314bfc1245                                                                                            0.0s 
 => => exporting attestation manifest sha256:75c6ed1295b005f7cdf00129542eab82c58120a3de5c284033e26d1eaa97aaac                                                                              0.0s 
 => => exporting manifest list sha256:8346c175d4ccf16d1354788ccba6fd6ba23dc12016521227acabfb3ef56c9eec                                                                                     0.0s 
 => => naming to docker.io/library/optimizedapp:bad                                                                                                                                        0.0s
 => => unpacking to docker.io/library/optimizedapp:bad                                                                                                                                     0.4s
docker build -f Dockerfile.bad -t optimizedapp:bad .  0.78s user 0.41s system 1% cpu 1:13.38 total

Windows PowerShell:
Measure-Command { docker build -f Dockerfile.bad -t optimizedapp:bad2 . }

Rebuild the optimized image
Linux or macOS:
time docker build -t optimizedapp:v2 .

Windows PowerShell:
Measure-Command { docker build -t optimizedapp:v2 . }

Why this rebuild comparison is the most important part
In the optimized Dockerfile:
·	requirements.txt was copied first
·	dependency installation happened before source code copy
·	if only app.py changes, Docker can reuse the dependency layer
In the bad Dockerfile:
·	COPY . . came before dependency installation
·	any source code change changes that copy layer
·	dependency installation likely runs again
·	rebuild takes longer
This is the clearest demonstration of layer optimization.
Step 13: Optional Direct Timer in Seconds
Some teachers prefer explicit timers in seconds.
aditya-2274@aditya-2274-IdeaPad-3-15IAU7 Docker/image_optimization (main) » /usr/bin/time -f "Bad Dockerfile build time: %e seconds" -o bad_time.txt \
docker build --no-cache -f Dockerfile.bad -t optimizedapp:bad .
[+] Building 7.3s (10/10) FINISHED                                                                                       docker:default
 => [internal] load build definition from Dockerfile.bad                                                                           0.0s
 => => transferring dockerfile: 145B                                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3.11                                                                     1.7s
 => [auth] library/python:pull token for registry-1.docker.io                                                                      0.0s
 => [internal] load .dockerignore                                                                                                  0.0s
 => => transferring context: 110B                                                                                                  0.0s
 => [1/4] FROM docker.io/library/python:3.11@sha256:7076cc3363aeea9624548c01194745480602f173f3c528ec746affc4cd59f774               0.0s
 => => resolve docker.io/library/python:3.11@sha256:7076cc3363aeea9624548c01194745480602f173f3c528ec746affc4cd59f774               0.0s
 => [internal] load build context                                                                                                  0.0s
 => => transferring context: 17.64kB                                                                                               0.0s
 => CACHED [2/4] WORKDIR /myapp                                                                                                    0.0s
 => [3/4] COPY . .                                                                                                                 0.0s
 => [4/4] RUN pip install -r requirements.txt                                                                                      4.2s
 => exporting to image                                                                                                             1.3s 
 => => exporting layers                                                                                                            0.8s 
 => => exporting manifest sha256:d62e8be78ff5d5d62476f4a5693528da83b193c2a113d0ed7a68370987f2a516                                  0.0s 
 => => exporting config sha256:b9b55d66566b127e934f1a0a1457837f087de0ee30f78e5d119d587646745fdb                                    0.0s 
 => => exporting attestation manifest sha256:1ee2ad29c2c42869e6e095286672e71027361eb68ce3e19db0784c975a48afd9                      0.0s 
 => => exporting manifest list sha256:6ef42dd324faab6247508897b5be4ab296b453da9d82544b1a227e60b8f3a52b                             0.0s 
 => => naming to docker.io/library/optimizedapp:bad                                                                                0.0s
 => => unpacking to docker.io/library/optimizedapp:bad                                                                             0.3s

Bad Dockerfile build time: 7.42 seconds

 aditya-2274@aditya-2274-IdeaPad-3-15IAU7 Docker/image_optimization (main) » /usr/bin/time -f "Good Dockerfile build time: %e seconds" -ogood_time.txt \
docker build --no-cache -t optimizedapp:v1 . 
[+] Building 5.4s (10/10) FINISHED                                                                                       docker:default
 => [internal] load build definition from Dockerfile                                                                               0.0s
 => => transferring dockerfile: 189B                                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                0.0s
 => [internal] load .dockerignore                                                                                                  0.0s
 => => transferring context: 110B                                                                                                  0.0s
 => [1/5] FROM docker.io/library/python:3.11-slim@sha256:9358444059ed78e2975ada2c189f1c1a3144a5dab6f35bff8c981afb38946634          0.0s
 => => resolve docker.io/library/python:3.11-slim@sha256:9358444059ed78e2975ada2c189f1c1a3144a5dab6f35bff8c981afb38946634          0.0s
 => [internal] load build context                                                                                                  0.0s
 => => transferring context: 62B                                                                                                   0.0s
 => CACHED [2/5] WORKDIR /myapp                                                                                                    0.0s
 => [3/5] COPY requirements.txt .                                                                                                  0.0s
 => [4/5] RUN pip install --no-cache -r requirements.txt                                                                           4.0s
 => [5/5] COPY app.py .                                                                                                            0.0s 
 => exporting to image                                                                                                             1.1s 
 => => exporting layers                                                                                                            0.7s 
 => => exporting manifest sha256:68eab8ae43dd595f738373bf93be9b510d5b76842ecb5dc28d93dcac14d8d275                                  0.0s 
 => => exporting config sha256:23b6106644ff0fe42dfedd75fb1bf5737570ffb0af934514fac747875d1c8e2f                                    0.0s 
 => => exporting attestation manifest sha256:4cc2e9e28ba9df100a889f17c63875e8f4ed0a89a8e702dcf7997bc97640c4de                      0.0s 
 => => exporting manifest list sha256:3ff77e42a05a50024754af8f6c03337b9f2b8c9254f47bed618dac8f7be4e55f                             0.0s
 => => naming to docker.io/library/optimizedapp:v1                                                                                 0.0s
 => => unpacking to docker.io/library/optimizedapp:v1                                                                              0.3s
 
 Good Dockerfile build time: 5.60 seconds

Linux or macOS
Bad image:
start=$(date +%s)
docker build -f Dockerfile.bad -t optimizedapp:bad .
end=$(date +%s)
echo "Bad Dockerfile build time: $((end-start)) seconds"

aditya-2274@aditya-2274-IdeaPad-3-15IAU7 Docker/image_optimization (main) » start=$(date +%s)
docker build -f Dockerfile.bad -t optimizedapp:bad .
end=$(date +%s)
echo "Bad Dockerfile build time: $((end-start)) seconds"
[+] Building 8.2s (10/10) FINISHED                                                                                       docker:default
 => [internal] load build definition from Dockerfile.bad                                                                           0.0s
 => => transferring dockerfile: 145B                                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3.11                                                                     1.8s
 => [auth] library/python:pull token for registry-1.docker.io                                                                      0.0s
 => [internal] load .dockerignore                                                                                                  0.0s
 => => transferring context: 110B                                                                                                  0.0s
 => [1/4] FROM docker.io/library/python:3.11@sha256:7076cc3363aeea9624548c01194745480602f173f3c528ec746affc4cd59f774               0.0s
 => => resolve docker.io/library/python:3.11@sha256:7076cc3363aeea9624548c01194745480602f173f3c528ec746affc4cd59f774               0.0s
 => [internal] load build context                                                                                                  0.0s
 => => transferring context: 35.88kB                                                                                               0.0s
 => CACHED [2/4] WORKDIR /myapp                                                                                                    0.0s
 => [3/4] COPY . .                                                                                                                 0.0s
 => [4/4] RUN pip install -r requirements.txt                                                                                      5.1s
 => exporting to image                                                                                                             1.2s
 => => exporting layers                                                                                                            0.8s
 => => exporting manifest sha256:8e768540e2ee666c9af696b9269ee3b8f249768a60b38aa6ac31014b7611bb77                                  0.0s
 => => exporting config sha256:f0fba713457326ea9a5453c71b2e84c1835a4cc6dc2929f6293e35ba4e28cea4                                    0.0s
 => => exporting attestation manifest sha256:bba42502b9a97965b11d9cda0684304bbc5cb794f57ecff9290f44b8f948e51e                      0.0s
 => => exporting manifest list sha256:d993f322aaf3f05e97a54d91508f10e11a70ebd70f3a1ddddd700121687da309                             0.0s
 => => naming to docker.io/library/optimizedapp:bad                                                                                0.0s
 => => unpacking to docker.io/library/optimizedapp:bad                                                                             0.2s
Bad Dockerfile build time: 9 seconds

Optimized image:
start=$(date +%s)
docker build -t optimizedapp:v1 .
end=$(date +%s)
echo "Optimized Dockerfile build time: $((end-start)) seconds"

aditya-2274@aditya-2274-IdeaPad-3-15IAU7 Docker/image_optimization (main) » start=$(date +%s)
docker build -t optimizedapp:v1 .
end=$(date +%s)
echo "Optimized Dockerfile build time: $((end-start)) seconds"
[+] Building 0.6s (10/10) FINISHED                                                                                       docker:default
 => [internal] load build definition from Dockerfile                                                                               0.0s
 => => transferring dockerfile: 189B                                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                0.0s
 => [internal] load .dockerignore                                                                                                  0.0s
 => => transferring context: 110B                                                                                                  0.0s
 => [1/5] FROM docker.io/library/python:3.11-slim@sha256:9358444059ed78e2975ada2c189f1c1a3144a5dab6f35bff8c981afb38946634          0.0s
 => => resolve docker.io/library/python:3.11-slim@sha256:9358444059ed78e2975ada2c189f1c1a3144a5dab6f35bff8c981afb38946634          0.0s
 => [internal] load build context                                                                                                  0.0s
 => => transferring context: 62B                                                                                                   0.0s
 => CACHED [2/5] WORKDIR /myapp                                                                                                    0.0s
 => CACHED [3/5] COPY requirements.txt .                                                                                           0.0s
 => CACHED [4/5] RUN pip install --no-cache -r requirements.txt                                                                    0.0s
 => CACHED [5/5] COPY app.py .                                                                                                     0.0s
 => exporting to image                                                                                                             0.4s
 => => exporting layers                                                                                                            0.0s
 => => exporting manifest sha256:68eab8ae43dd595f738373bf93be9b510d5b76842ecb5dc28d93dcac14d8d275                                  0.0s
 => => exporting config sha256:23b6106644ff0fe42dfedd75fb1bf5737570ffb0af934514fac747875d1c8e2f                                    0.0s
 => => exporting attestation manifest sha256:fcecdc1d5b3e2125403f9eab0fa1828bbabccada2d9adf58d8af4330be09cb35                      0.0s
 => => exporting manifest list sha256:34c5e299beaa8acef68e2cf49cbf7597f51fe7cb3f361f652c5e84a43a154f5e                             0.0s
 => => naming to docker.io/library/optimizedapp:v1                                                                                 0.0s
 => => unpacking to docker.io/library/optimizedapp:v1                                                                              0.3s
Optimized Dockerfile build time: 1 seconds

Windows PowerShell
Bad image:
$start = Get-Date
docker build -f Dockerfile.bad -t optimizedapp:bad .
$end = Get-Date
$duration = $end - $start
Write-Host "Bad Dockerfile build time: $($duration.TotalSeconds) seconds"

Optimized image:
$start = Get-Date
docker build -t optimizedapp:v1 .
$end = Get-Date
$duration = $end - $start
Write-Host "Optimized Dockerfile build time: $($duration.TotalSeconds) seconds"

Why use this method
This method is beginner-friendly because it prints one direct sentence in seconds.
Step 14: Save Timing Output for a Lab Report
Linux or macOS:
(time docker build -f Dockerfile.bad -t optimizedapp:bad .) 2> bad_time.txt
(time docker build -t optimizedapp:v1 .) 2> good_time.txt

Windows PowerShell:
Measure-Command { docker build -f Dockerfile.bad -t optimizedapp:bad . } | Out-File bad_time.txt
Measure-Command { docker build -t optimizedapp:v1 . } | Out-File good_time.txt

Why this matters
This helps students attach timing evidence in assignments, viva reports, or presentations.
Step 15: Observation Table
Students can fill an observation table like this:
Scenario	Command	Expected Result	Reason
First build of bad image	docker build -f Dockerfile.bad -t optimizedapp:bad .	Slower and larger	Full base image and poor layer ordering
First build of optimized image	docker build -t optimizedapp:v1 .	Better overall	Slim image and cleaner layer order
Rebuild after only code change, bad Dockerfile	docker build -f Dockerfile.bad -t optimizedapp:bad2 .	Slow rebuild	Dependency installation likely repeated
Rebuild after only code change, optimized Dockerfile	docker build -t optimizedapp:v2 .	Fast rebuild	Cached dependency layer reused

Step 16: Full Command Sequence for Classroom Demonstration
Create the project
mkdir optimizedapp
cd optimizedapp

Build and run the bad image
docker build -f Dockerfile.bad -t optimizedapp:bad .
docker run --rm optimizedapp:bad
docker history optimizedapp:bad

Build and run the optimized image
docker build -t optimizedapp:v1 .
docker run --rm optimizedapp:v1
docker history optimizedapp:v1

Time the builds on Linux or macOS
time docker build -f Dockerfile.bad -t optimizedapp:bad .
time docker build -t optimizedapp:v1 .

Time the builds on Windows PowerShell
Measure-Command { docker build -f Dockerfile.bad -t optimizedapp:bad . }
Measure-Command { docker build -t optimizedapp:v1 . }

Modify source code and rebuild
docker build -f Dockerfile.bad -t optimizedapp:bad2 .
docker build -t optimizedapp:v2 .

Step 17: Common Beginner Mistakes
Mistake 1: Copying everything too early
Using COPY . . before dependency installation often breaks cache too soon.
Mistake 2: Using very large base images by default
Bigger images increase storage, transfer time, and sometimes security surface.
Mistake 3: Forgetting .dockerignore
This can send unnecessary files into the build context.
Mistake 4: Judging performance only from the first build
The real benefit of layer ordering often appears during rebuilds.
Mistake 5: Not using docker history
Then the student misses the opportunity to inspect how the image was actually built.
Step 18: Conceptual Summary
A Dockerfile should be written in an order that matches how often things change.
A smart pattern is:
1.	start from a small base image
2.	set the working directory
3.	copy dependency file first
4.	install dependencies
5.	copy application code later
6.	run the application
That order reduces unnecessary rebuild work.
Viva Questions with Short Answers
Why is the optimized Dockerfile faster after a code change?
Because the dependency layer stays cached when only the source file changes.
Why is python:3.11-slim better than python:3.11 here?
It is smaller, so the final image is usually smaller and faster to transfer.
Why is COPY requirements.txt . done before COPY app.py .?
Because dependencies usually change less often than application code.
Why do we use .dockerignore?
To avoid sending unnecessary files into the build context.
Why use docker history?
To inspect image layers and understand how Dockerfile instructions translated into the final image.
Why use a timer in this activity?
To measure actual build performance and prove that optimization reduced build time.
Final Answer in One Paragraph
To reduce Docker image size and build time in a startup, the best strategy is to use a smaller base image, copy the dependency file before the application source code, install dependencies in a separate cached layer, and exclude unnecessary files using .dockerignore. This allows Docker to reuse cached layers when only source code changes, which speeds up rebuilds significantly. The result can be verified practically using docker build, docker history, and a timer mechanism such as time on Linux or Measure-Command in PowerShell.
Final Optimized Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]

Final One-Line Conclusion
Correct Docker layer ordering makes images smaller, rebuilds faster, and optimization measurable through timers.
