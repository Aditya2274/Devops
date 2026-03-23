Docker is a containerization platform used for developing, packaging, shipping, and running applications.
It allows an application to run in an isolated environment called a container.
Docker makes development and deployment efficient.
The document addresses the common development issue of an application working on one machine but failing on another,proposing Docker as the solution.
Containers
A container is a way to package an application with all necessary dependencies and configuration.
Containers can be easily shared.
Unlike VMs which encapsulate the whole machine, Docker containers encapsulate applications, leading to a low impact on the OS, faster performance, and low disk space usage.
-----------------------------Docker Components------------------------

The main components of Docker are:
DockerFile: A simple text file with instructions to build an image.
Docker Image: A single file with all the dependencies and libraries needed to run the program.
Docker Container: An instance of an image.
Docker Registry: A central repository for storing and distributing Docker images, such as Docker Hub or a Private Registry.
--------------------------------Docker commands---------------------

-> docker build . to build an image of the file in working directory
-> docker image ls  to see all the images that have been created
-> docker run <image-id>  to create an instance of image(i.e container)
-> docker ps  to check the process status like what all containers are running
-> docker ps -a  shows all the containers that are and were running
-> docker stop <container-name> to stop the running container, container-name u can customize , if u don't docker gives a random name to it
-> docker rm <conatiner-name> to remove that specific container
 docker build . 
 docker image ls  
 docker run <image-id>
 if u just do this much and expect to create a container , but u won't get an output on the browser,even though the container is created u  can't access it to the browser, i.e outside of the container
 So we do port binding when we create a run it listens at a certain port inside the container, and for it be used on web outside the container we use port binding.
 Why Port Binding is Necessary
When you run a web application, it listens on a port inside the container’s network. To see that app in your browser (which lives on your host machine), you have to create a bridge between the two.

The Port Mapping Syntax
We use the -p (or --publish) flag during the docker run command:

docker run -p [Host Port]:[Container Port] image_name
_Breaking Down the Logic_
Let’s say you have a Node.js app listening on port 3000 inside the container:
The Container Port (3000): This is where the application is actually listening. You cannot change this via the command line; it's defined in your code or Dockerfile.

The Host Port (8080): This is the port you type into your browser (e.g., localhost:8080). You can choose almost any number here.

Command Example: docker run -p 8080:3000 my-web-app

Browser: You go to localhost:8080.

Docker: It catches traffic on 8080 and tunnels it to port 3000 inside the container.

App: The app receives the request, processes it, and sends it back through the tunnel.
![](Portforwarding.md)
_Running Container in Detached Mode_
->docker run -d -p <outside-container-port-no>:<inside-container-port-no> <Image-id>  this way we can run containers in detached mode so that terminal is not occupied by the running container
->docker run -d -p <outside-container-port-no>:<inside-container-port-no> <Image-id> if the outside-container-port-no is same for another container, it will give error
so just change outside-container-port-no and then u can run multiple containers
Just a convinience cmd:
->docker run -d --rm -p <outside-container-port-no>:<inside-container-port-no> <Image-id>  runs the container in detached mode but will be removed as soon as the container stops
_Custom naming of container_
->docker run -d --rm --name "Name" -p <outside-container-port-no>:<inside-container-port-no> <Image-id>
just a convinience step, u can stop containers with copying imageid or random names docker assigns you
->docker stop Name

_Managing Docker Images_
We build images and for its reference we have imageID only , that's what we've seen until now, so what 
about a name that we can give to it, so it'd be easy for even us to refer to..
->docker build -t Name:<version> . here -t is tagging that version_id is tagged with the name
The use of version is , if u just change the version , u can still use the same name for building images.Real life scenarios , like an app upgraded version we want to containerise and for that we won't just create a new image so we just change the version number
-> docker rmi Name:<version> to remove a specific image tagged with a specific version  
aditya-2274@aditya-2274-IdeaPad-3-15IAU7:~/Documents/devops/Docker/demo$ docker image ls
i Info →   U  In Use
IMAGE     ID             DISK USAGE   CONTENT SIZE   EXTRA
demo:01   61dc64ca8cdf        1.7GB          429MB      

aditya-2274@aditya-2274-IdeaPad-3-15IAU7:~/Documents/devops/Docker/demo$ docker run -d --rm --name "demo" -p 3001:5173 demo:
01
099dba7dc599d86a791feed53e09a69b096a62b04538968470d4d47464473347
aditya-2274@aditya-2274-IdeaPad-3-15IAU7:~/Documents/devops/Docker/demo$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                         NAMES
099dba7dc599   demo:01   "docker-entrypoint.s…"   5 seconds ago   Up 5 seconds   0.0.0.0:3001->5173/tcp, [::]:3001->5173/tcp   demo
This right here is my example , a react app created using vite , running on container name demo version 1

_Pre-defined Images_
 ->docker pull Image_Name
 -> docker run -d -p <your_custom_port>:<image_default_port> image_name:latest
 This way you can use pre-defined images for you use
 One more thing , before using docker pull <Image-name> make sure to login via cli , by docker login

 _Docker-Container-With-Interactive-Mode_
 docker run -it -p <your_custom_port>:<image_default_port> image_name 

 _Pushing_an _image_to_docker_
 1)docker login
 2)rename the image with username/imagename
 3)docker push username/imagename:tagname

 image renaming: docker tag <image_name>:tagname  <user_name>/<image_name>:tagname

->Docker volume
1)A Docker volume is the preferred and most robust mechanism for persisting data generated by and used by Docker containers.
2)When you run a container, any data it creates is usually stored in its temporary "writable layer." If the container is deleted, that data is lost forever. Volumes solve this by storing the data outside the container's lifecycle, directly on the host machine's file system, but managed entirely by Docker.
# docker run -it --rm -v myvolume:/myapp --name interactive-python-container itcontainer:01
# docker run -it --rm -v myvolume:/myapp/ cff4e11724d4

->Bind Mounts
Docker offers two main ways to store data on the host machine, and it's important to know the difference:FeatureDocker VolumesBind MountsManagementManaged entirely by Docker.Managed by the host's operating system.Host LocationStored in a specific Docker directory (e.g., /var/lib/docker/volumes/ on Linux).Can be anywhere on the host system.Use CaseDatabases, persistent app data, sharing data between containers.Sharing configuration files (like DNS) or source code during local development.
in bind_mount folder
# docker run -v /home/aditya-2274/Storage/Documents/devops/Docker/bind_mount/servers.txt:/myapp/servers.txt --rm bind_mount:01
Q)so bind mount is use to make changes in a specific file of an image so that we don't have to make image again and again after creating the change in file in that project which we have dockerized and had to mke small changes??
Soln: How it works in practice:
Instead of copying your code into the image during the docker build process, you use a bind mount to tell Docker: "Take this specific folder on my laptop, and mirror it directly inside the container."

Because the container is looking directly at the files on your host machine, any change you make in your local code editor is instantly reflected inside the running container.

A Quick Example
Imagine you are working on a web app and your source code is in C:\Users\Me\my-project.

Instead of rebuilding, you run the container like this:

Bash
docker run -d -p 8080:80 \
  -v /C/Users/Me/my-project:/var/www/html \
  my_web_image
-v /C/Users/Me/my-project:/var/www/html: This is the bind mount. It connects your local folder to the /var/www/html folder inside the container.

Now, if you edit index.html on your laptop and hit save, you just refresh your browser. The container serves the new file instantly. No rebuild required!

The Golden Rule: Development vs. Production
Because of this behavior, there is a golden rule in Docker:

Use Bind Mounts for Local Development: For instant feedback loops and live-reloading code.

Use Copies/Images for Production: When you deploy to a live server, you generally do not use bind mounts for your code. You want your code baked securely into the image so that the container is entirely self-contained, predictable, and immutable (unchangeable).

Q)so are those changes automatically saved or we have create them as an image afterwards??
Soln:Docker images are read-only (immutable).

The short answer is: The changes are saved safely to your local computer's hard drive, but they are not automatically saved into the Docker image.

Yes, to make those changes a permanent part of the image, you have to build a new image afterwards.

Here is a breakdown of exactly what happens to your files:

1. Where the changes are saved
When you are using a bind mount and you hit "save" in your code editor (like VS Code), the file is saved directly to your laptop's hard drive, just like normal.
Because the container is "looking" at that exact folder on your laptop through the bind mount, the container instantly runs the updated code.

If you stop or delete the container, your code is perfectly safe on your laptop.

2. Why it doesn't change the image
A Docker image is like a snapshot or a blueprint. Once it is created, it cannot be changed. The bind mount is simply a temporary bridge between your laptop and the running container; it completely bypasses the underlying image.

If you were to stop your container and send that exact image to a coworker right now, they would not see your new code. They would only see the old code that was originally baked into the image.

3. The "Afterwards" Step (Building for Production)
Once you have finished making all your small changes and the app is working perfectly via the bind mount, you are ready to finalize it.

To "save" those changes into a distributable format, you must tell Docker to take your newly updated local files and bake them into a brand new image. You do this by running the build command again:

Bash
docker build -t my_web_image:v2 .
Now, my_web_image:v2 contains all your new changes hardcoded into it, and you can deploy it to a server or share it without needing a bind mount!

->__.dockerignore__
The things you don't want in the image build up just simply put into this .dockerignore, and they won't be build into the images