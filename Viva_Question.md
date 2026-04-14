Q)What is Devops Infrastructure??
Soln. Devops infrstrucutre means the tecnical foundation used to develop, build ,test and run software in a faster and automated with better collaboration between teams.
Q)What is a container?
Soln. A lightweight isolated environment that is used to run an application with all it's dependencies in a predictable way
Q)What was there before containers?
Soln. before containers became common,many teams used
 ->physical servers
 ->virtual machines
 ->manual software installation
 ->environment specific setup
Q)What is the origin of containers?
Soln.The idea of containers developed from older concepts such as:
    ->Process isolation
    ->chroot
    ->jails 
    ->namespaces
    ->cgroups
Q) Whaat is modern containerization
Soln.Modern containerization means:
    ->packagind application with dependencies
    ->running them in isolated environment
    ->using lightweight OS-level separation
    ->managing them with tools like Docker
Q)How are containers integrated into devops?
Soln.Containers fits devops very well because:
    ->they standaridized environments
    ->they support automation
    ->they help CI/CD pipelines
    ->they work well with cloud and microservices
Q) What is a container runtime?
Soln.A container runtime is a software that actually runs container
Q)What is process isolation?
Soln.Process isolation means ,one running process is separated from others, it caannot freely interfer with other processes,and it sees a very limited environment.
Q)What are namespaces?
Soln. Namespaces are linux features that gives processes it's own separate view of certain system resources.
Q)What are control groups(cgroups)?
Soln.They are linux features used to control and limit resource usage of processes.
In container,without cgroups:
->a container may consume too much RAM
->one app may slow down others
->host may become unstable
