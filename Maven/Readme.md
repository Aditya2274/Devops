Maven Wrapper is a project-level mechanism that ensures a specific Maven version is used consistently across all environments, without requiring global installation.
✅ What Maven Wrapper actually is

The Maven Wrapper is project-scoped bootstrapping script.

👉 Think of it like:

“This project brings its own Maven version and ensures everyone uses it.”

Even if Maven is installed locally, I would still use Maven Wrapper to ensure version consistency across all developers and CI/CD environments. This eliminates discrepancies caused by different Maven versions and guarantees reproducible builds.

To create a new maven project ways:
1) Using maven on your system
mvn archetype:generate -DgroupId=com.example -DartifactId=my-new-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

2) using maven wrapper
It is basically "Wrapper Inception."

You are using the existing wrapper to build the new project, stepping inside the new project, and immediately building a new wrapper for it.

There is just one tiny terminal trick you have to use to make your pure-wrapper workflow happen without ever touching the global mvn command.

Here is exactly what your newly invented 4-step workflow looks like:

Step 1: Generate the project using your current wrapper (You are in the Q1 folder)

Bash
./mvnw archetype:generate -DgroupId=com.example -DartifactId=my-new-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
Step 2: Go into the new project folder

Bash
cd my-new-app
Step 3: Borrow the parent's wrapper to generate the new wrapper
(Since you don't have a wrapper inside my-new-app yet, and you don't want to use the global mvn, you just point backwards one folder by using ../)

Bash
../mvnw -N io.takari:maven:wrapper
Step 4: From now on, use your brand new local wrapper!

Bash
./mvnw clean package