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