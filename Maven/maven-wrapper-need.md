the command mvn wrapper:wrapper, your computer must have native Maven installed to understand the word mvn.

To clear this up, you have to split the lifecycle of a project into two distinct phases: The Creator and The Consumers.
Phase 1: The Creator (Bootstrapping)

The very first developer who creates the repository from scratch—often the DevOps engineer or the lead developer—does need native Maven.

    They use native mvn to generate the archetype.

    They use native mvn to generate the wrapper.

Phase 2: The Consumers (The Rest of the World)

Once that first developer generates the wrapper, they commit those three files (mvnw, mvnw.cmd, .mvn/) to GitHub along with their code.

From that moment on, native Maven is never needed again.

    When Developer B joins the team and clones the repo, they don't need to install native Maven. They just run ./mvnw.

    When the CI/CD Server pulls the code to run tests, it doesn't need native Maven installed. It just runs ./mvnw.

The DevOps Win

In a company of 50 developers, only one person (The Creator) needs to bother installing and configuring native Maven on their machine. The other 49 developers, and all the cloud servers, get to skip the installation completely because they are just Consumers of the wrapper.