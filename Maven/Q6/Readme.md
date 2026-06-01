6. A project depends on Library A, which itself depends on Library B. Developers never explicitly added Library B, yet it appears in the project classpath. Explain the concept of transitive dependencies and discuss one benefit and one risk of this feature.??
The Concept: Transitive Dependencies

In Maven, a transitive dependency is essentially a "dependency of a dependency."

When you tell Maven that your project needs Library A, Maven reaches out to the central repository and downloads it. However, before it finishes, Maven reads Library A's pom.xml file. If it sees that Library A requires Library B to function, Maven will automatically download Library B and add it to your project's classpath as well.

If Library B requires Library C, Maven downloads that too. This creates a deeply nested Dependency Tree. You only explicitly asked for one library, but Maven pulled in the entire underlying ecosystem required to make it work.
The Benefit: Massive Developer Productivity

The primary benefit of transitive dependencies is automation and ease of use.

Imagine you are building a modern web application and you want to use a massive framework like Spring Boot. Spring Boot relies on dozens of smaller libraries (for logging, web servers, security, JSON parsing, etc.).

    Without transitive dependencies: You would have to manually research, define, and version-match 50+ individual <dependency> tags in your pom.xml just to get a "Hello World" app running.

    With transitive dependencies: You add exactly one dependency (e.g., spring-boot-starter-web), and Maven instantly maps out and downloads the other 50 perfectly compatible libraries behind the scenes.

The Risk: "Dependency Hell" and Version Conflicts

The biggest risk of this automation is unpredictable classpath conflicts.

Because Maven is pulling in libraries invisibly, it is very easy to accidentally pull in two different, incompatible versions of the same underlying library.

    The Scenario: You import Library X (which transitively pulls in Library B version 1.0). Later, a teammate imports Library Y (which transitively pulls in Library B version 2.0).

    The Result: Your project now has two conflicting versions of Library B fighting in the background. Maven will attempt to resolve this using a "nearest definition" rule, but it often guesses wrong. The code will compile perfectly, but the moment you run the application, it crashes with a catastrophic NoSuchMethodError or ClassNotFoundException because the Java runtime grabbed the wrong version of the transitive file.

Another major risk is security: A severe vulnerability might exist in a transitive dependency hidden five layers deep in your tree, making it incredibly hard to spot until a security scanner flags your project.

💡 Pro-Tip for your DevOps Toolbelt

If you ever encounter a bizarre runtime error and suspect a transitive dependency is to blame, there is one ultimate command every DevOps engineer uses to visualize the invisible tree and see exactly what Library A brought with it:
Bash

./mvnw dependency:tree

_Output_:
aditya-2274@aditya-2274-IdeaPad-3-15IAU7 Q6/six.app (main) » ../mvnw dependency:tree                                                                  1 ↵
[INFO] Scanning for projects...
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-install-plugin/3.1.2/maven-install-plugin-3.1.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-install-plugin/3.1.2/maven-install-plugin-3.1.2.pom (8.5 kB at 17 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-deploy-plugin/3.1.2/maven-deploy-plugin-3.1.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-deploy-plugin/3.1.2/maven-deploy-plugin-3.1.2.pom (9.6 kB at 174 kB/s)
[INFO] 
[INFO] --------------------------< six.com:six.app >---------------------------
[INFO] Building six.app 1.0.0
[INFO] --------------------------------[ jar ]---------------------------------
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-web/3.0.0/spring-boot-starter-web-3.0.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-web/3.0.0/spring-boot-starter-web-3.0.0.pom (3.0 kB at 47 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter/3.0.0/spring-boot-starter-3.0.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter/3.0.0/spring-boot-starter-3.0.0.pom (3.1 kB at 50 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot/3.0.0/spring-boot-3.0.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot/3.0.0/spring-boot-3.0.0.pom (2.2 kB at 36 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-core/6.0.2/spring-core-6.0.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-core/6.0.2/spring-core-6.0.2.pom (2.0 kB at 39 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-jcl/6.0.2/spring-jcl-6.0.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-jcl/6.0.2/spring-jcl-6.0.2.pom (1.8 kB at 38 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-context/6.0.2/spring-context-6.0.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-context/6.0.2/spring-context-6.0.2.pom (2.6 kB at 47 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-aop/6.0.2/spring-aop-6.0.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-aop/6.0.2/spring-aop-6.0.2.pom (2.2 kB at 34 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-beans/6.0.2/spring-beans-6.0.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-beans/6.0.2/spring-beans-6.0.2.pom (2.0 kB at 33 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-expression/6.0.2/spring-expression-6.0.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-expression/6.0.2/spring-expression-6.0.2.pom (2.1 kB at 37 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-autoconfigure/3.0.0/spring-boot-autoconfigure-3.0.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-autoconfigure/3.0.0/spring-boot-autoconfigure-3.0.0.pom (2.1 kB at 32 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-logging/3.0.0/spring-boot-starter-logging-3.0.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-logging/3.0.0/spring-boot-starter-logging-3.0.0.pom (2.5 kB at 38 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/ch/qos/logback/logback-classic/1.4.5/logback-classic-1.4.5.pom
Downloaded from central: https://repo.maven.apache.org/maven2/ch/qos/logback/logback-classic/1.4.5/logback-classic-1.4.5.pom (12 kB at 149 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/ch/qos/logback/logback-parent/1.4.5/logback-parent-1.4.5.pom
Downloaded from central: https://repo.maven.apache.org/maven2/ch/qos/logback/logback-parent/1.4.5/logback-parent-1.4.5.pom (19 kB at 293 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/ch/qos/logback/logback-core/1.4.5/logback-core-1.4.5.pom
Downloaded from central: https://repo.maven.apache.org/maven2/ch/qos/logback/logback-core/1.4.5/logback-core-1.4.5.pom (5.0 kB at 88 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.4/slf4j-api-2.0.4.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.4/slf4j-api-2.0.4.pom (1.6 kB at 28 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/2.0.4/slf4j-parent-2.0.4.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/2.0.4/slf4j-parent-2.0.4.pom (16 kB at 274 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/logging/log4j/log4j-to-slf4j/2.19.0/log4j-to-slf4j-2.19.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/logging/log4j/log4j-to-slf4j/2.19.0/log4j-to-slf4j-2.19.0.pom (7.2 kB at 122 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/logging/log4j/log4j/2.19.0/log4j-2.19.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/logging/log4j/log4j/2.19.0/log4j-2.19.0.pom (71 kB at 1.2 MB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/logging/logging-parent/5/logging-parent-5.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/logging/logging-parent/5/logging-parent-5.pom (3.3 kB at 66 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/24/apache-24.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/24/apache-24.pom (20 kB at 358 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/logging/log4j/log4j-bom/2.19.0/log4j-bom-2.19.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/logging/log4j/log4j-bom/2.19.0/log4j-bom-2.19.0.pom (9.2 kB at 155 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.0/junit-bom-5.9.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.0/junit-bom-5.9.0.pom (5.6 kB at 95 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/logging/log4j/log4j-api/2.19.0/log4j-api-2.19.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/logging/log4j/log4j-api/2.19.0/log4j-api-2.19.0.pom (16 kB at 283 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/jul-to-slf4j/2.0.4/jul-to-slf4j-2.0.4.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/jul-to-slf4j/2.0.4/jul-to-slf4j-2.0.4.pom (954 B at 18 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/yaml/snakeyaml/1.33/snakeyaml-1.33.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/yaml/snakeyaml/1.33/snakeyaml-1.33.pom (39 kB at 633 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-json/3.0.0/spring-boot-starter-json-3.0.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-json/3.0.0/spring-boot-starter-json-3.0.0.pom (3.1 kB at 56 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-web/6.0.2/spring-web-6.0.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-web/6.0.2/spring-web-6.0.2.pom (2.4 kB at 44 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/io/micrometer/micrometer-observation/1.10.0/micrometer-observation-1.10.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/io/micrometer/micrometer-observation/1.10.0/micrometer-observation-1.10.0.pom (3.9 kB at 67 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/io/micrometer/micrometer-commons/1.10.0/micrometer-commons-1.10.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/io/micrometer/micrometer-commons/1.10.0/micrometer-commons-1.10.0.pom (3.2 kB at 60 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.14.1/jackson-databind-2.14.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.14.1/jackson-databind-2.14.1.pom (19 kB at 313 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-base/2.14.1/jackson-base-2.14.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-base/2.14.1/jackson-base-2.14.1.pom (10 kB at 183 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.14.1/jackson-annotations-2.14.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.14.1/jackson-annotations-2.14.1.pom (6.2 kB at 113 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.14.1/jackson-core-2.14.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.14.1/jackson-core-2.14.1.pom (7.0 kB at 132 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jdk8/2.14.1/jackson-datatype-jdk8-2.14.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jdk8/2.14.1/jackson-datatype-jdk8-2.14.1.pom (2.6 kB at 44 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/module/jackson-modules-java8/2.14.1/jackson-modules-java8-2.14.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/module/jackson-modules-java8/2.14.1/jackson-modules-java8-2.14.1.pom (3.1 kB at 58 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jsr310/2.14.1/jackson-datatype-jsr310-2.14.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jsr310/2.14.1/jackson-datatype-jsr310-2.14.1.pom (4.9 kB at 61 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/module/jackson-module-parameter-names/2.14.1/jackson-module-parameter-names-2.14.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/module/jackson-module-parameter-names/2.14.1/jackson-module-parameter-names-2.14.1.pom (4.4 kB at 68 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-tomcat/3.0.0/spring-boot-starter-tomcat-3.0.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-tomcat/3.0.0/spring-boot-starter-tomcat-3.0.0.pom (3.1 kB at 57 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/tomcat/embed/tomcat-embed-core/10.1.1/tomcat-embed-core-10.1.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/tomcat/embed/tomcat-embed-core/10.1.1/tomcat-embed-core-10.1.1.pom (1.8 kB at 31 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/tomcat/embed/tomcat-embed-el/10.1.1/tomcat-embed-el-10.1.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/tomcat/embed/tomcat-embed-el/10.1.1/tomcat-embed-el-10.1.1.pom (1.5 kB at 29 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/tomcat/embed/tomcat-embed-websocket/10.1.1/tomcat-embed-websocket-10.1.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/tomcat/embed/tomcat-embed-websocket/10.1.1/tomcat-embed-websocket-10.1.1.pom (1.8 kB at 32 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-webmvc/6.0.2/spring-webmvc-6.0.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-webmvc/6.0.2/spring-webmvc-6.0.2.pom (2.9 kB at 55 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-undertow/3.0.0/spring-boot-starter-undertow-3.0.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-undertow/3.0.0/spring-boot-starter-undertow-3.0.0.pom (2.7 kB at 4.2 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/io/undertow/undertow-core/2.3.0.Final/undertow-core-2.3.0.Final.pom
Downloaded from central: https://repo.maven.apache.org/maven2/io/undertow/undertow-core/2.3.0.Final/undertow-core-2.3.0.Final.pom (23 kB at 37 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/io/undertow/undertow-parent/2.3.0.Final/undertow-parent-2.3.0.Final.pom
Downloaded from central: https://repo.maven.apache.org/maven2/io/undertow/undertow-parent/2.3.0.Final/undertow-parent-2.3.0.Final.pom (26 kB at 67 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/jboss-parent/35/jboss-parent-35.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/jboss-parent/35/jboss-parent-35.pom (66 kB at 965 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/logging/jboss-logging/3.4.3.Final/jboss-logging-3.4.3.Final.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/logging/jboss-logging/3.4.3.Final/jboss-logging-3.4.3.Final.pom (15 kB at 294 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/xnio/xnio-api/3.8.8.Final/xnio-api-3.8.8.Final.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/xnio/xnio-api/3.8.8.Final/xnio-api-3.8.8.Final.pom (8.8 kB at 162 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/xnio/xnio-all/3.8.8.Final/xnio-all-3.8.8.Final.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/xnio/xnio-all/3.8.8.Final/xnio-all-3.8.8.Final.pom (7.1 kB at 148 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/wildfly/common/wildfly-common/1.5.4.Final/wildfly-common-1.5.4.Final.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/wildfly/common/wildfly-common/1.5.4.Final/wildfly-common-1.5.4.Final.pom (7.3 kB at 137 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/jboss-parent/34/jboss-parent-34.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/jboss-parent/34/jboss-parent-34.pom (65 kB at 1.1 MB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/wildfly/client/wildfly-client-config/1.0.1.Final/wildfly-client-config-1.0.1.Final.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/wildfly/client/wildfly-client-config/1.0.1.Final/wildfly-client-config-1.0.1.Final.pom (7.2 kB at 126 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/jboss-parent/23/jboss-parent-23.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/jboss-parent/23/jboss-parent-23.pom (35 kB at 656 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/logging/jboss-logging/3.3.1.Final/jboss-logging-3.3.1.Final.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/logging/jboss-logging/3.3.1.Final/jboss-logging-3.3.1.Final.pom (5.9 kB at 110 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/jboss-parent/15/jboss-parent-15.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/jboss-parent/15/jboss-parent-15.pom (32 kB at 553 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/xnio/xnio-nio/3.8.8.Final/xnio-nio-3.8.8.Final.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/xnio/xnio-nio/3.8.8.Final/xnio-nio-3.8.8.Final.pom (8.2 kB at 28 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/threads/jboss-threads/2.3.6.Final/jboss-threads-2.3.6.Final.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/threads/jboss-threads/2.3.6.Final/jboss-threads-2.3.6.Final.pom (4.6 kB at 76 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/jboss-parent/20/jboss-parent-20.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/jboss-parent/20/jboss-parent-20.pom (34 kB at 556 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/threads/jboss-threads/3.5.0.Final/jboss-threads-3.5.0.Final.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/threads/jboss-threads/3.5.0.Final/jboss-threads-3.5.0.Final.pom (7.3 kB at 93 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/logging/jboss-logging/3.4.1.Final/jboss-logging-3.4.1.Final.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/logging/jboss-logging/3.4.1.Final/jboss-logging-3.4.1.Final.pom (5.0 kB at 89 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/io/undertow/undertow-servlet/2.3.0.Final/undertow-servlet-2.3.0.Final.pom
Downloaded from central: https://repo.maven.apache.org/maven2/io/undertow/undertow-servlet/2.3.0.Final/undertow-servlet-2.3.0.Final.pom (19 kB at 29 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/jakarta/servlet/jakarta.servlet-api/6.0.0/jakarta.servlet-api-6.0.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/jakarta/servlet/jakarta.servlet-api/6.0.0/jakarta.servlet-api-6.0.0.pom (19 kB at 338 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/io/undertow/undertow-websockets-jsr/2.3.0.Final/undertow-websockets-jsr-2.3.0.Final.pom
Downloaded from central: https://repo.maven.apache.org/maven2/io/undertow/undertow-websockets-jsr/2.3.0.Final/undertow-websockets-jsr-2.3.0.Final.pom (9.8 kB at 19 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/jakarta/websocket/jakarta.websocket-api/2.1.0/jakarta.websocket-api-2.1.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/jakarta/websocket/jakarta.websocket-api/2.1.0/jakarta.websocket-api-2.1.0.pom (4.5 kB at 88 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/jakarta/websocket/jakarta.websocket-all/2.1.0/jakarta.websocket-all-2.1.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/jakarta/websocket/jakarta.websocket-all/2.1.0/jakarta.websocket-all-2.1.0.pom (11 kB at 198 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/jakarta/websocket/jakarta.websocket-client-api/2.1.0/jakarta.websocket-client-api-2.1.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/jakarta/websocket/jakarta.websocket-client-api/2.1.0/jakarta.websocket-client-api-2.1.0.pom (4.2 kB at 72 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-web/3.0.0/spring-boot-starter-web-3.0.0.jar
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter/3.0.0/spring-boot-starter-3.0.0.jar
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot/3.0.0/spring-boot-3.0.0.jar
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-autoconfigure/3.0.0/spring-boot-autoconfigure-3.0.0.jar
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-logging/3.0.0/spring-boot-starter-logging-3.0.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter/3.0.0/spring-boot-starter-3.0.0.jar (4.8 kB at 58 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/ch/qos/logback/logback-classic/1.4.5/logback-classic-1.4.5.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-web/3.0.0/spring-boot-starter-web-3.0.0.jar (4.8 kB at 31 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/ch/qos/logback/logback-core/1.4.5/logback-core-1.4.5.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-logging/3.0.0/spring-boot-starter-logging-3.0.0.jar (4.8 kB at 35 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.4/slf4j-api-2.0.4.jar
Downloaded from central: https://repo.maven.apache.org/maven2/ch/qos/logback/logback-classic/1.4.5/logback-classic-1.4.5.jar (266 kB at 1.5 MB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/logging/log4j/log4j-to-slf4j/2.19.0/log4j-to-slf4j-2.19.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.4/slf4j-api-2.0.4.jar (62 kB at 295 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/logging/log4j/log4j-api/2.19.0/log4j-api-2.19.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/logging/log4j/log4j-to-slf4j/2.19.0/log4j-to-slf4j-2.19.0.jar (19 kB at 80 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/jul-to-slf4j/2.0.4/jul-to-slf4j-2.0.4.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/jul-to-slf4j/2.0.4/jul-to-slf4j-2.0.4.jar (4.7 kB at 17 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-core/6.0.2/spring-core-6.0.2.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/logging/log4j/log4j-api/2.19.0/log4j-api-2.19.0.jar (318 kB at 865 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-jcl/6.0.2/spring-jcl-6.0.2.jar
Downloaded from central: https://repo.maven.apache.org/maven2/ch/qos/logback/logback-core/1.4.5/logback-core-1.4.5.jar (577 kB at 1.5 MB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/yaml/snakeyaml/1.33/snakeyaml-1.33.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-jcl/6.0.2/spring-jcl-6.0.2.jar (23 kB at 55 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-json/3.0.0/spring-boot-starter-json-3.0.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-json/3.0.0/spring-boot-starter-json-3.0.0.jar (4.7 kB at 9.8 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.14.1/jackson-databind-2.14.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/yaml/snakeyaml/1.33/snakeyaml-1.33.jar (332 kB at 608 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.14.1/jackson-annotations-2.14.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot/3.0.0/spring-boot-3.0.0.jar (1.5 MB at 2.4 MB/s)
Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.14.1/jackson-core-2.14.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.14.1/jackson-annotations-2.14.1.jar (76 kB at 120 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jdk8/2.14.1/jackson-datatype-jdk8-2.14.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-autoconfigure/3.0.0/spring-boot-autoconfigure-3.0.0.jar (1.6 MB at 2.6 MB/s)
Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jsr310/2.14.1/jackson-datatype-jsr310-2.14.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jdk8/2.14.1/jackson-datatype-jdk8-2.14.1.jar (35 kB at 49 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/module/jackson-module-parameter-names/2.14.1/jackson-module-parameter-names-2.14.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jsr310/2.14.1/jackson-datatype-jsr310-2.14.1.jar (122 kB at 165 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-tomcat/3.0.0/spring-boot-starter-tomcat-3.0.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/module/jackson-module-parameter-names/2.14.1/jackson-module-parameter-names-2.14.1.jar (9.5 kB at 12 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/tomcat/embed/tomcat-embed-core/10.1.1/tomcat-embed-core-10.1.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-tomcat/3.0.0/spring-boot-starter-tomcat-3.0.0.jar (4.8 kB at 6.0 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/tomcat/embed/tomcat-embed-websocket/10.1.1/tomcat-embed-websocket-10.1.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.14.1/jackson-core-2.14.1.jar (459 kB at 568 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-web/6.0.2/spring-web-6.0.2.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-core/6.0.2/spring-core-6.0.2.jar (1.8 MB at 2.2 MB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-beans/6.0.2/spring-beans-6.0.2.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/tomcat/embed/tomcat-embed-websocket/10.1.1/tomcat-embed-websocket-10.1.1.jar (277 kB at 281 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/io/micrometer/micrometer-observation/1.10.0/micrometer-observation-1.10.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.14.1/jackson-databind-2.14.1.jar (1.6 MB at 1.6 MB/s)
Downloading from central: https://repo.maven.apache.org/maven2/io/micrometer/micrometer-commons/1.10.0/micrometer-commons-1.10.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-beans/6.0.2/spring-beans-6.0.2.jar (841 kB at 732 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-webmvc/6.0.2/spring-webmvc-6.0.2.jar
Downloaded from central: https://repo.maven.apache.org/maven2/io/micrometer/micrometer-commons/1.10.0/micrometer-commons-1.10.0.jar (40 kB at 33 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-aop/6.0.2/spring-aop-6.0.2.jar
Downloaded from central: https://repo.maven.apache.org/maven2/io/micrometer/micrometer-observation/1.10.0/micrometer-observation-1.10.0.jar (66 kB at 54 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-context/6.0.2/spring-context-6.0.2.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-aop/6.0.2/spring-aop-6.0.2.jar (396 kB at 283 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/spring-expression/6.0.2/spring-expression-6.0.2.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-web/6.0.2/spring-web-6.0.2.jar (1.7 MB at 1.2 MB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-undertow/3.0.0/spring-boot-starter-undertow-3.0.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-webmvc/6.0.2/spring-webmvc-6.0.2.jar (1.0 MB at 660 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/io/undertow/undertow-core/2.3.0.Final/undertow-core-2.3.0.Final.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-expression/6.0.2/spring-expression-6.0.2.jar (291 kB at 187 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/logging/jboss-logging/3.4.3.Final/jboss-logging-3.4.3.Final.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/logging/jboss-logging/3.4.3.Final/jboss-logging-3.4.3.Final.jar (61 kB at 37 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/xnio/xnio-api/3.8.8.Final/xnio-api-3.8.8.Final.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/spring-context/6.0.2/spring-context-6.0.2.jar (1.2 MB at 691 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/wildfly/common/wildfly-common/1.5.4.Final/wildfly-common-1.5.4.Final.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/tomcat/embed/tomcat-embed-core/10.1.1/tomcat-embed-core-10.1.1.jar (3.4 MB at 1.9 MB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/wildfly/client/wildfly-client-config/1.0.1.Final/wildfly-client-config-1.0.1.Final.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/wildfly/common/wildfly-common/1.5.4.Final/wildfly-common-1.5.4.Final.jar (285 kB at 155 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/xnio/xnio-nio/3.8.8.Final/xnio-nio-3.8.8.Final.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/wildfly/client/wildfly-client-config/1.0.1.Final/wildfly-client-config-1.0.1.Final.jar (47 kB at 26 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/threads/jboss-threads/3.5.0.Final/jboss-threads-3.5.0.Final.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/xnio/xnio-api/3.8.8.Final/xnio-api-3.8.8.Final.jar (585 kB at 317 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/io/undertow/undertow-servlet/2.3.0.Final/undertow-servlet-2.3.0.Final.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-undertow/3.0.0/spring-boot-starter-undertow-3.0.0.jar (4.8 kB at 2.3 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/jakarta/servlet/jakarta.servlet-api/6.0.0/jakarta.servlet-api-6.0.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/xnio/xnio-nio/3.8.8.Final/xnio-nio-3.8.8.Final.jar (111 kB at 54 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/io/undertow/undertow-websockets-jsr/2.3.0.Final/undertow-websockets-jsr-2.3.0.Final.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/threads/jboss-threads/3.5.0.Final/jboss-threads-3.5.0.Final.jar (123 kB at 59 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/jakarta/websocket/jakarta.websocket-api/2.1.0/jakarta.websocket-api-2.1.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/jakarta/websocket/jakarta.websocket-api/2.1.0/jakarta.websocket-api-2.1.0.jar (24 kB at 11 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/jakarta/websocket/jakarta.websocket-client-api/2.1.0/jakarta.websocket-client-api-2.1.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/jakarta/servlet/jakarta.servlet-api/6.0.0/jakarta.servlet-api-6.0.0.jar (348 kB at 160 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/tomcat/embed/tomcat-embed-el/10.1.1/tomcat-embed-el-10.1.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/io/undertow/undertow-core/2.3.0.Final/undertow-core-2.3.0.Final.jar (2.3 MB at 1.1 MB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/jakarta/websocket/jakarta.websocket-client-api/2.1.0/jakarta.websocket-client-api-2.1.0.jar (42 kB at 19 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/tomcat/embed/tomcat-embed-el/10.1.1/tomcat-embed-el-10.1.1.jar (257 kB at 113 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/io/undertow/undertow-websockets-jsr/2.3.0.Final/undertow-websockets-jsr-2.3.0.Final.jar (178 kB at 70 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/io/undertow/undertow-servlet/2.3.0.Final/undertow-servlet-2.3.0.Final.jar (542 kB at 169 kB/s)
[INFO] 
[INFO] --- maven-dependency-plugin:2.8:tree (default-cli) @ six.app ---
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sink-api/1.0-alpha-10/doxia-sink-api-1.0-alpha-10.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sink-api/1.0-alpha-10/doxia-sink-api-1.0-alpha-10.pom (1.3 kB at 26 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia/1.0-alpha-10/doxia-1.0-alpha-10.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia/1.0-alpha-10/doxia-1.0-alpha-10.pom (9.2 kB at 191 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/6/maven-parent-6.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/6/maven-parent-6.pom (20 kB at 352 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/reporting/maven-reporting-impl/2.0.5/maven-reporting-impl-2.0.5.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/reporting/maven-reporting-impl/2.0.5/maven-reporting-impl-2.0.5.pom (4.2 kB at 77 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-core/1.0/doxia-core-1.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-core/1.0/doxia-core-1.0.pom (2.4 kB at 46 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/1.5.7/plexus-utils-1.5.7.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/1.5.7/plexus-utils-1.5.7.pom (8.1 kB at 155 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-site-renderer/1.0/doxia-site-renderer-1.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-site-renderer/1.0/doxia-site-renderer-1.0.pom (4.4 kB at 76 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sitetools/1.0/doxia-sitetools-1.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sitetools/1.0/doxia-sitetools-1.0.pom (9.6 kB at 196 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-i18n/1.0-beta-7/plexus-i18n-1.0-beta-7.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-i18n/1.0-beta-7/plexus-i18n-1.0-beta-7.pom (1.1 kB at 19 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-velocity/1.1.7/plexus-velocity-1.1.7.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-velocity/1.1.7/plexus-velocity-1.1.7.pom (2.0 kB at 40 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-container-default/1.0-alpha-20/plexus-container-default-1.0-alpha-20.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-container-default/1.0-alpha-20/plexus-container-default-1.0-alpha-20.pom (3.0 kB at 54 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-containers/1.0-alpha-20/plexus-containers-1.0-alpha-20.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-containers/1.0-alpha-20/plexus-containers-1.0-alpha-20.pom (1.9 kB at 34 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/1.3/plexus-utils-1.3.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/1.3/plexus-utils-1.3.pom (1.0 kB at 21 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-classworlds/1.2-alpha-7/plexus-classworlds-1.2-alpha-7.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-classworlds/1.2-alpha-7/plexus-classworlds-1.2-alpha-7.pom (2.4 kB at 44 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/1.0.9/plexus-1.0.9.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/1.0.9/plexus-1.0.9.pom (7.7 kB at 142 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity/1.5/velocity-1.5.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity/1.5/velocity-1.5.pom (7.8 kB at 132 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-decoration-model/1.0/doxia-decoration-model-1.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-decoration-model/1.0/doxia-decoration-model-1.0.pom (3.2 kB at 62 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-apt/1.0/doxia-module-apt-1.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-apt/1.0/doxia-module-apt-1.0.pom (2.3 kB at 42 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-modules/1.0/doxia-modules-1.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-modules/1.0/doxia-modules-1.0.pom (2.4 kB at 44 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-fml/1.0/doxia-module-fml-1.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-fml/1.0/doxia-module-fml-1.0.pom (2.7 kB at 56 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xdoc/1.0/doxia-module-xdoc-1.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xdoc/1.0/doxia-module-xdoc-1.0.pom (2.2 kB at 42 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xhtml/1.0/doxia-module-xhtml-1.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xhtml/1.0/doxia-module-xhtml-1.0.pom (1.6 kB at 31 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-doxia-tools/1.0.2/maven-doxia-tools-1.0.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-doxia-tools/1.0.2/maven-doxia-tools-1.0.2.pom (5.9 kB at 103 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/11/maven-shared-components-11.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/11/maven-shared-components-11.pom (8.3 kB at 164 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/1.4/commons-io-1.4.pom
Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/1.4/commons-io-1.4.pom (13 kB at 248 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/7/commons-parent-7.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/7/commons-parent-7.pom (17 kB at 318 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/commons-validator/commons-validator/1.2.0/commons-validator-1.2.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/commons-validator/commons-validator/1.2.0/commons-validator-1.2.0.pom (9.1 kB at 175 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/commons-logging/commons-logging/1.0.4/commons-logging-1.0.4.pom
Downloaded from central: https://repo.maven.apache.org/maven2/commons-logging/commons-logging/1.0.4/commons-logging-1.0.4.pom (5.3 kB at 107 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/xml-apis/xml-apis/2.0.2/xml-apis-2.0.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/xml-apis/xml-apis/2.0.2/xml-apis-2.0.2.pom (346 B at 7.2 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/2.3/plexus-archiver-2.3.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/2.3/plexus-archiver-2.3.pom (3.4 kB at 72 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/1.3/plexus-components-1.3.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/1.3/plexus-components-1.3.pom (3.1 kB at 66 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/3.3/plexus-3.3.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/3.3/plexus-3.3.pom (20 kB at 355 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.0.10/plexus-utils-3.0.10.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.0.10/plexus-utils-3.0.10.pom (3.1 kB at 56 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/2.0.6/plexus-io-2.0.6.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/2.0.6/plexus-io-2.0.6.pom (2.2 kB at 43 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/1.2/plexus-components-1.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/1.2/plexus-components-1.2.pom (3.1 kB at 61 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.0.9/plexus-utils-3.0.9.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.0.9/plexus-utils-3.0.9.pom (3.1 kB at 64 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/file-management/1.2.1/file-management-1.2.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/file-management/1.2.1/file-management-1.2.1.pom (3.9 kB at 73 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-io/1.1/maven-shared-io-1.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-io/1.1/maven-shared-io-1.1.pom (4.1 kB at 77 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/8/maven-shared-components-8.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/8/maven-shared-components-8.pom (2.7 kB at 51 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/7/maven-parent-7.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/7/maven-parent-7.pom (21 kB at 401 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/2.0.2/maven-artifact-2.0.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/2.0.2/maven-artifact-2.0.2.pom (765 B at 14 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven/2.0.2/maven-2.0.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven/2.0.2/maven-2.0.2.pom (13 kB at 263 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/1.1/plexus-utils-1.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/1.1/plexus-utils-1.1.pom (767 B at 16 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact-manager/2.0.2/maven-artifact-manager-2.0.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact-manager/2.0.2/maven-artifact-manager-2.0.2.pom (1.4 kB at 22 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-repository-metadata/2.0.2/maven-repository-metadata-2.0.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-repository-metadata/2.0.2/maven-repository-metadata-2.0.2.pom (1.3 kB at 24 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-provider-api/1.0-alpha-6/wagon-provider-api-1.0-alpha-6.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-provider-api/1.0-alpha-6/wagon-provider-api-1.0-alpha-6.pom (588 B at 11 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon/1.0-alpha-6/wagon-1.0-alpha-6.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon/1.0-alpha-6/wagon-1.0-alpha-6.pom (6.4 kB at 116 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/1.4.6/plexus-utils-1.4.6.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/1.4.6/plexus-utils-1.4.6.pom (2.3 kB at 50 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-dependency-analyzer/1.4/maven-dependency-analyzer-1.4.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-dependency-analyzer/1.4/maven-dependency-analyzer-1.4.pom (5.2 kB at 107 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/asm/asm/3.3.1/asm-3.3.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/asm/asm/3.3.1/asm-3.3.1.pom (266 B at 5.0 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/asm/asm-parent/3.3.1/asm-parent-3.3.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/asm/asm-parent/3.3.1/asm-parent-3.3.1.pom (4.3 kB at 82 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-project/2.0.5/maven-project-2.0.5.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-project/2.0.5/maven-project-2.0.5.pom (1.8 kB at 35 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven/2.0.5/maven-2.0.5.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven/2.0.5/maven-2.0.5.pom (5.7 kB at 121 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-settings/2.0.5/maven-settings-2.0.5.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-settings/2.0.5/maven-settings-2.0.5.pom (1.7 kB at 34 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-model/2.0.5/maven-model-2.0.5.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-model/2.0.5/maven-model-2.0.5.pom (2.7 kB at 52 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-profile/2.0.5/maven-profile-2.0.5.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-profile/2.0.5/maven-profile-2.0.5.pom (1.7 kB at 32 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact-manager/2.0.5/maven-artifact-manager-2.0.5.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact-manager/2.0.5/maven-artifact-manager-2.0.5.pom (1.8 kB at 35 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-repository-metadata/2.0.5/maven-repository-metadata-2.0.5.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-repository-metadata/2.0.5/maven-repository-metadata-2.0.5.pom (1.5 kB at 28 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/2.0.5/maven-artifact-2.0.5.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/2.0.5/maven-artifact-2.0.5.pom (727 B at 14 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-dependency-tree/2.1/maven-dependency-tree-2.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-dependency-tree/2.1/maven-dependency-tree-2.1.pom (6.8 kB at 131 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-project/2.2.0/maven-project-2.2.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-project/2.2.0/maven-project-2.2.0.pom (2.8 kB at 57 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven/2.2.0/maven-2.2.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven/2.2.0/maven-2.2.0.pom (22 kB at 458 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-settings/2.2.0/maven-settings-2.2.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-settings/2.2.0/maven-settings-2.2.0.pom (2.2 kB at 47 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-model/2.2.0/maven-model-2.2.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-model/2.2.0/maven-model-2.2.0.pom (3.2 kB at 66 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-profile/2.2.0/maven-profile-2.2.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-profile/2.2.0/maven-profile-2.2.0.pom (2.2 kB at 43 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact-manager/2.2.0/maven-artifact-manager-2.2.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact-manager/2.2.0/maven-artifact-manager-2.2.0.pom (3.1 kB at 62 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-repository-metadata/2.2.0/maven-repository-metadata-2.2.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-repository-metadata/2.2.0/maven-repository-metadata-2.2.0.pom (1.9 kB at 37 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/2.2.0/maven-artifact-2.2.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/2.2.0/maven-artifact-2.2.0.pom (1.6 kB at 32 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-plugin-registry/2.2.0/maven-plugin-registry-2.2.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-plugin-registry/2.2.0/maven-plugin-registry-2.2.0.pom (1.9 kB at 38 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/1.4/maven-common-artifact-filters-1.4.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/1.4/maven-common-artifact-filters-1.4.pom (3.8 kB at 71 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/2.0.8/maven-artifact-2.0.8.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/2.0.8/maven-artifact-2.0.8.pom (1.6 kB at 34 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven/2.0.8/maven-2.0.8.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven/2.0.8/maven-2.0.8.pom (12 kB at 233 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-model/2.0.8/maven-model-2.0.8.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-model/2.0.8/maven-model-2.0.8.pom (3.1 kB at 64 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-project/2.0.8/maven-project-2.0.8.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-project/2.0.8/maven-project-2.0.8.pom (2.7 kB at 53 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-settings/2.0.8/maven-settings-2.0.8.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-settings/2.0.8/maven-settings-2.0.8.pom (2.1 kB at 42 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-profile/2.0.8/maven-profile-2.0.8.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-profile/2.0.8/maven-profile-2.0.8.pom (2.0 kB at 38 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact-manager/2.0.8/maven-artifact-manager-2.0.8.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact-manager/2.0.8/maven-artifact-manager-2.0.8.pom (2.7 kB at 48 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-repository-metadata/2.0.8/maven-repository-metadata-2.0.8.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-repository-metadata/2.0.8/maven-repository-metadata-2.0.8.pom (1.9 kB at 35 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-plugin-registry/2.0.8/maven-plugin-registry-2.0.8.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-plugin-registry/2.0.8/maven-plugin-registry-2.0.8.pom (2.0 kB at 38 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-plugin-api/2.0.8/maven-plugin-api-2.0.8.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-plugin-api/2.0.8/maven-plugin-api-2.0.8.pom (1.5 kB at 28 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/2.1/plexus-utils-2.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/2.1/plexus-utils-2.1.pom (4.0 kB at 84 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-invoker/2.0.11/maven-invoker-2.0.11.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-invoker/2.0.11/maven-invoker-2.0.11.pom (5.1 kB at 110 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/commons-lang/commons-lang/2.6/commons-lang-2.6.pom
Downloaded from central: https://repo.maven.apache.org/maven2/commons-lang/commons-lang/2.6/commons-lang-2.6.pom (17 kB at 380 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/17/commons-parent-17.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/17/commons-parent-17.pom (31 kB at 611 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/reporting/maven-reporting-impl/2.0.5/maven-reporting-impl-2.0.5.jar
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-core/1.0/doxia-core-1.0.jar
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-doxia-tools/1.0.2/maven-doxia-tools-1.0.2.jar
Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/1.4/commons-io-1.4.jar
Downloading from central: https://repo.maven.apache.org/maven2/commons-validator/commons-validator/1.2.0/commons-validator-1.2.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/reporting/maven-reporting-impl/2.0.5/maven-reporting-impl-2.0.5.jar (21 kB at 349 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/commons-beanutils/commons-beanutils/1.7.0/commons-beanutils-1.7.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-doxia-tools/1.0.2/maven-doxia-tools-1.0.2.jar (41 kB at 587 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/commons-digester/commons-digester/1.6/commons-digester-1.6.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-core/1.0/doxia-core-1.0.jar (55 kB at 774 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/commons-logging/commons-logging/1.0.4/commons-logging-1.0.4.jar
Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/1.4/commons-io-1.4.jar (109 kB at 1.3 MB/s)
Downloading from central: https://repo.maven.apache.org/maven2/oro/oro/2.0.8/oro-2.0.8.jar
Downloaded from central: https://repo.maven.apache.org/maven2/commons-validator/commons-validator/1.2.0/commons-validator-1.2.0.jar (91 kB at 1.1 MB/s)
Downloading from central: https://repo.maven.apache.org/maven2/xml-apis/xml-apis/1.0.b2/xml-apis-1.0.b2.jar
Downloaded from central: https://repo.maven.apache.org/maven2/commons-logging/commons-logging/1.0.4/commons-logging-1.0.4.jar (38 kB at 284 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sink-api/1.0/doxia-sink-api-1.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/oro/oro/2.0.8/oro-2.0.8.jar (65 kB at 435 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-site-renderer/1.0/doxia-site-renderer-1.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/commons-beanutils/commons-beanutils/1.7.0/commons-beanutils-1.7.0.jar (189 kB at 1.2 MB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-i18n/1.0-beta-7/plexus-i18n-1.0-beta-7.jar
Downloaded from central: https://repo.maven.apache.org/maven2/commons-digester/commons-digester/1.6/commons-digester-1.6.jar (168 kB at 1.1 MB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-velocity/1.1.7/plexus-velocity-1.1.7.jar
Downloaded from central: https://repo.maven.apache.org/maven2/xml-apis/xml-apis/1.0.b2/xml-apis-1.0.b2.jar (109 kB at 675 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity/1.5/velocity-1.5.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sink-api/1.0/doxia-sink-api-1.0.jar (10 kB at 54 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-decoration-model/1.0/doxia-decoration-model-1.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-i18n/1.0-beta-7/plexus-i18n-1.0-beta-7.jar (11 kB at 51 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-apt/1.0/doxia-module-apt-1.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-site-renderer/1.0/doxia-site-renderer-1.0.jar (47 kB at 218 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-fml/1.0/doxia-module-fml-1.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-velocity/1.1.7/plexus-velocity-1.1.7.jar (7.7 kB at 36 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xdoc/1.0/doxia-module-xdoc-1.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-decoration-model/1.0/doxia-decoration-model-1.0.jar (49 kB at 200 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xhtml/1.0/doxia-module-xhtml-1.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-fml/1.0/doxia-module-fml-1.0.jar (19 kB at 69 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/2.3/plexus-archiver-2.3.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xdoc/1.0/doxia-module-xdoc-1.0.jar (28 kB at 104 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.0.9/plexus-utils-3.0.9.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-apt/1.0/doxia-module-apt-1.0.jar (47 kB at 173 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/file-management/1.2.1/file-management-1.2.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity/1.5/velocity-1.5.jar (392 kB at 1.3 MB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-io/1.1/maven-shared-io-1.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xhtml/1.0/doxia-module-xhtml-1.0.jar (22 kB at 73 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-provider-api/1.0-alpha-6/wagon-provider-api-1.0-alpha-6.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/file-management/1.2.1/file-management-1.2.1.jar (38 kB at 113 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/2.0.6/plexus-io-2.0.6.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/2.3/plexus-archiver-2.3.jar (186 kB at 544 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-dependency-analyzer/1.4/maven-dependency-analyzer-1.4.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-io/1.1/maven-shared-io-1.1.jar (39 kB at 113 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/asm/asm/3.3.1/asm-3.3.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.0.9/plexus-utils-3.0.9.jar (232 kB at 639 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-dependency-tree/2.1/maven-dependency-tree-2.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-provider-api/1.0-alpha-6/wagon-provider-api-1.0-alpha-6.jar (43 kB at 115 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/aether/aether-util/0.9.0.M2/aether-util-0.9.0.M2.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/2.0.6/plexus-io-2.0.6.jar (58 kB at 145 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/1.4/maven-common-artifact-filters-1.4.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-dependency-analyzer/1.4/maven-dependency-analyzer-1.4.jar (27 kB at 68 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-invoker/2.0.11/maven-invoker-2.0.11.jar
Downloaded from central: https://repo.maven.apache.org/maven2/asm/asm/3.3.1/asm-3.3.1.jar (44 kB at 106 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/commons-lang/commons-lang/2.6/commons-lang-2.6.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-dependency-tree/2.1/maven-dependency-tree-2.1.jar (60 kB at 140 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/commons-collections/commons-collections/3.2.1/commons-collections-3.2.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/aether/aether-util/0.9.0.M2/aether-util-0.9.0.M2.jar (134 kB at 302 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/1.4/maven-common-artifact-filters-1.4.jar (32 kB at 68 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-invoker/2.0.11/maven-invoker-2.0.11.jar (29 kB at 62 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/commons-lang/commons-lang/2.6/commons-lang-2.6.jar (284 kB at 570 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/commons-collections/commons-collections/3.2.1/commons-collections-3.2.1.jar (575 kB at 910 kB/s)
[INFO] six.com:six.app:jar:1.0.0
[INFO] +- org.junit.jupiter:junit-jupiter-api:jar:5.11.0:test
[INFO] |  +- org.opentest4j:opentest4j:jar:1.3.0:test
[INFO] |  +- org.junit.platform:junit-platform-commons:jar:1.11.0:test
[INFO] |  \- org.apiguardian:apiguardian-api:jar:1.1.2:test
[INFO] +- org.junit.jupiter:junit-jupiter-params:jar:5.11.0:test
[INFO] +- org.springframework.boot:spring-boot-starter-web:jar:3.0.0:compile
[INFO] |  +- org.springframework.boot:spring-boot-starter:jar:3.0.0:compile
[INFO] |  |  +- org.springframework.boot:spring-boot:jar:3.0.0:compile
[INFO] |  |  +- org.springframework.boot:spring-boot-autoconfigure:jar:3.0.0:compile
[INFO] |  |  +- org.springframework.boot:spring-boot-starter-logging:jar:3.0.0:compile
[INFO] |  |  |  +- ch.qos.logback:logback-classic:jar:1.4.5:compile
[INFO] |  |  |  |  +- ch.qos.logback:logback-core:jar:1.4.5:compile
[INFO] |  |  |  |  \- org.slf4j:slf4j-api:jar:2.0.4:compile
[INFO] |  |  |  +- org.apache.logging.log4j:log4j-to-slf4j:jar:2.19.0:compile
[INFO] |  |  |  |  \- org.apache.logging.log4j:log4j-api:jar:2.19.0:compile
[INFO] |  |  |  \- org.slf4j:jul-to-slf4j:jar:2.0.4:compile
[INFO] |  |  +- jakarta.annotation:jakarta.annotation-api:jar:2.1.1:compile
[INFO] |  |  +- org.springframework:spring-core:jar:6.0.2:compile
[INFO] |  |  |  \- org.springframework:spring-jcl:jar:6.0.2:compile
[INFO] |  |  \- org.yaml:snakeyaml:jar:1.33:compile
[INFO] |  +- org.springframework.boot:spring-boot-starter-json:jar:3.0.0:compile
[INFO] |  |  +- com.fasterxml.jackson.core:jackson-databind:jar:2.14.1:compile
[INFO] |  |  |  +- com.fasterxml.jackson.core:jackson-annotations:jar:2.14.1:compile
[INFO] |  |  |  \- com.fasterxml.jackson.core:jackson-core:jar:2.14.1:compile
[INFO] |  |  +- com.fasterxml.jackson.datatype:jackson-datatype-jdk8:jar:2.14.1:compile
[INFO] |  |  +- com.fasterxml.jackson.datatype:jackson-datatype-jsr310:jar:2.14.1:compile
[INFO] |  |  \- com.fasterxml.jackson.module:jackson-module-parameter-names:jar:2.14.1:compile
[INFO] |  +- org.springframework.boot:spring-boot-starter-tomcat:jar:3.0.0:compile
[INFO] |  |  +- org.apache.tomcat.embed:tomcat-embed-core:jar:10.1.1:compile
[INFO] |  |  \- org.apache.tomcat.embed:tomcat-embed-websocket:jar:10.1.1:compile
[INFO] |  +- org.springframework:spring-web:jar:6.0.2:compile
[INFO] |  |  +- org.springframework:spring-beans:jar:6.0.2:compile
[INFO] |  |  \- io.micrometer:micrometer-observation:jar:1.10.0:compile
[INFO] |  |     \- io.micrometer:micrometer-commons:jar:1.10.0:compile
[INFO] |  \- org.springframework:spring-webmvc:jar:6.0.2:compile
[INFO] |     +- org.springframework:spring-aop:jar:6.0.2:compile
[INFO] |     +- org.springframework:spring-context:jar:6.0.2:compile
[INFO] |     \- org.springframework:spring-expression:jar:6.0.2:compile
[INFO] \- org.springframework.boot:spring-boot-starter-undertow:jar:3.0.0:compile
[INFO]    +- io.undertow:undertow-core:jar:2.3.0.Final:compile
[INFO]    |  +- org.jboss.logging:jboss-logging:jar:3.4.3.Final:compile
[INFO]    |  +- org.jboss.xnio:xnio-api:jar:3.8.8.Final:compile
[INFO]    |  |  +- org.wildfly.common:wildfly-common:jar:1.5.4.Final:compile
[INFO]    |  |  \- org.wildfly.client:wildfly-client-config:jar:1.0.1.Final:compile
[INFO]    |  +- org.jboss.xnio:xnio-nio:jar:3.8.8.Final:runtime
[INFO]    |  \- org.jboss.threads:jboss-threads:jar:3.5.0.Final:compile
[INFO]    +- io.undertow:undertow-servlet:jar:2.3.0.Final:compile
[INFO]    |  \- jakarta.servlet:jakarta.servlet-api:jar:6.0.0:compile
[INFO]    +- io.undertow:undertow-websockets-jsr:jar:2.3.0.Final:compile
[INFO]    |  +- jakarta.websocket:jakarta.websocket-api:jar:2.1.0:compile
[INFO]    |  \- jakarta.websocket:jakarta.websocket-client-api:jar:2.1.0:compile
[INFO]    \- org.apache.tomcat.embed:tomcat-embed-el:jar:10.1.1:compile
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  17.914 s
[INFO] Finished at: 2026-06-01T22:47:35+05:30
[INFO] ------------------------------------------------------------------------
aditya-2274@aditya-2274-IdeaPad-3-15IAU7 Q6/six.app (main) » ../mvnw dependency:tree
[INFO] Scanning for projects...
[INFO] 
[INFO] --------------------------< six.com:six.app >---------------------------
[INFO] Building six.app 1.0.0
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] --- maven-dependency-plugin:2.8:tree (default-cli) @ six.app ---
[INFO] six.com:six.app:jar:1.0.0
[INFO] +- org.junit.jupiter:junit-jupiter-api:jar:5.11.0:test
[INFO] |  +- org.opentest4j:opentest4j:jar:1.3.0:test
[INFO] |  +- org.junit.platform:junit-platform-commons:jar:1.11.0:test
[INFO] |  \- org.apiguardian:apiguardian-api:jar:1.1.2:test
[INFO] +- org.junit.jupiter:junit-jupiter-params:jar:5.11.0:test
[INFO] +- org.springframework.boot:spring-boot-starter-web:jar:3.0.0:compile
[INFO] |  +- org.springframework.boot:spring-boot-starter:jar:3.0.0:compile
[INFO] |  |  +- org.springframework.boot:spring-boot:jar:3.0.0:compile
[INFO] |  |  +- org.springframework.boot:spring-boot-autoconfigure:jar:3.0.0:compile
[INFO] |  |  +- org.springframework.boot:spring-boot-starter-logging:jar:3.0.0:compile
[INFO] |  |  |  +- ch.qos.logback:logback-classic:jar:1.4.5:compile
[INFO] |  |  |  |  +- ch.qos.logback:logback-core:jar:1.4.5:compile
[INFO] |  |  |  |  \- org.slf4j:slf4j-api:jar:2.0.4:compile
[INFO] |  |  |  +- org.apache.logging.log4j:log4j-to-slf4j:jar:2.19.0:compile
[INFO] |  |  |  |  \- org.apache.logging.log4j:log4j-api:jar:2.19.0:compile
[INFO] |  |  |  \- org.slf4j:jul-to-slf4j:jar:2.0.4:compile
[INFO] |  |  +- jakarta.annotation:jakarta.annotation-api:jar:2.1.1:compile
[INFO] |  |  +- org.springframework:spring-core:jar:6.0.2:compile
[INFO] |  |  |  \- org.springframework:spring-jcl:jar:6.0.2:compile
[INFO] |  |  \- org.yaml:snakeyaml:jar:1.33:compile
[INFO] |  +- org.springframework.boot:spring-boot-starter-json:jar:3.0.0:compile
[INFO] |  |  +- com.fasterxml.jackson.core:jackson-databind:jar:2.14.1:compile
[INFO] |  |  |  +- com.fasterxml.jackson.core:jackson-annotations:jar:2.14.1:compile
[INFO] |  |  |  \- com.fasterxml.jackson.core:jackson-core:jar:2.14.1:compile
[INFO] |  |  +- com.fasterxml.jackson.datatype:jackson-datatype-jdk8:jar:2.14.1:compile
[INFO] |  |  +- com.fasterxml.jackson.datatype:jackson-datatype-jsr310:jar:2.14.1:compile
[INFO] |  |  \- com.fasterxml.jackson.module:jackson-module-parameter-names:jar:2.14.1:compile
[INFO] |  +- org.springframework:spring-web:jar:6.0.2:compile
[INFO] |  |  +- org.springframework:spring-beans:jar:6.0.2:compile
[INFO] |  |  \- io.micrometer:micrometer-observation:jar:1.10.0:compile
[INFO] |  |     \- io.micrometer:micrometer-commons:jar:1.10.0:compile
[INFO] |  \- org.springframework:spring-webmvc:jar:6.0.2:compile
[INFO] |     +- org.springframework:spring-aop:jar:6.0.2:compile
[INFO] |     +- org.springframework:spring-context:jar:6.0.2:compile
[INFO] |     \- org.springframework:spring-expression:jar:6.0.2:compile
[INFO] \- org.springframework.boot:spring-boot-starter-undertow:jar:3.0.0:compile
[INFO]    +- io.undertow:undertow-core:jar:2.3.0.Final:compile
[INFO]    |  +- org.jboss.logging:jboss-logging:jar:3.4.3.Final:compile
[INFO]    |  +- org.jboss.xnio:xnio-api:jar:3.8.8.Final:compile
[INFO]    |  |  +- org.wildfly.common:wildfly-common:jar:1.5.4.Final:compile
[INFO]    |  |  \- org.wildfly.client:wildfly-client-config:jar:1.0.1.Final:compile
[INFO]    |  +- org.jboss.xnio:xnio-nio:jar:3.8.8.Final:runtime
[INFO]    |  \- org.jboss.threads:jboss-threads:jar:3.5.0.Final:compile
[INFO]    +- io.undertow:undertow-servlet:jar:2.3.0.Final:compile
[INFO]    |  \- jakarta.servlet:jakarta.servlet-api:jar:6.0.0:compile
[INFO]    +- io.undertow:undertow-websockets-jsr:jar:2.3.0.Final:compile
[INFO]    |  +- jakarta.websocket:jakarta.websocket-api:jar:2.1.0:compile
[INFO]    |  \- jakarta.websocket:jakarta.websocket-client-api:jar:2.1.0:compile
[INFO]    \- org.apache.tomcat.embed:tomcat-embed-el:jar:10.1.1:compile
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  1.127 s
[INFO] Finished at: 2026-06-01T22:47:46+05:30
[INFO] ------------------------------------------------------------------------