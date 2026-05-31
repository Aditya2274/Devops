1. The compile Phase (Checking Syntax)
During this phase, Maven translates the human-readable .java source code into machine-readable .class bytecode. Passing this phase only proves that the code is syntactically correct. It confirms there are no missing semicolons, no invalid variable names, and that the Java grammar is flawless.

2. The test Phase (Checking Logic)
Occurring immediately after compilation, this phase uses the Maven Surefire Plugin to execute automated unit tests against the newly compiled bytecode. This phase verifies the actual business logic of the application (e.g., proving that a calculator function actually adds two numbers correctly).

3. Why Passing Compile Does Not Guarantee a Successful Build
The Maven build lifecycle is strictly sequential (validate → compile → test → package). Code can have perfect syntax but fundamentally broken logic. For example, a developer might write valid Java code that multiplies numbers instead of dividing them. It will compile perfectly, but it will fail the automated tests. Because a pipeline requires every lifecycle phase to succeed, a failure in the test phase immediately triggers a BUILD FAILURE and halts the pipeline, preventing broken logic from ever reaching production.

Output:
aditya-2274@aditya-2274-IdeaPad-3-15IAU7 Maven/Q3 (main) » cd three-app                                                                               1 ↵
aditya-2274@aditya-2274-IdeaPad-3-15IAU7 Q3/three-app (main) » mvn clean package   
[INFO] Scanning for projects...
[INFO] 
[INFO] ----------------------< three.example:three-app >-----------------------
[INFO] Building three-app 3.0.0
[INFO] --------------------------------[ jar ]---------------------------------
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-clean-plugin/3.4.0/maven-clean-plugin-3.4.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-clean-plugin/3.4.0/maven-clean-plugin-3.4.0.pom (5.5 kB at 4.3 kB/s)
[INFO] 
[INFO] --- maven-clean-plugin:3.4.0:clean (default-clean) @ three-app ---
[INFO] Deleting /home/aditya-2274/Storage/Documents/Devops/Maven/Q3/three-app/target
[INFO] 
[INFO] --- maven-resources-plugin:3.3.1:resources (default-resources) @ three-app ---
[INFO] skip non existing resourceDirectory /home/aditya-2274/Storage/Documents/Devops/Maven/Q3/three-app/src/main/resources
[INFO] 
[INFO] --- maven-compiler-plugin:3.13.0:compile (default-compile) @ three-app ---
[INFO] Recompiling the module because of changed source code.
[INFO] Compiling 1 source file with javac [debug release 17] to target/classes
[INFO] 
[INFO] --- maven-resources-plugin:3.3.1:testResources (default-testResources) @ three-app ---
[INFO] skip non existing resourceDirectory /home/aditya-2274/Storage/Documents/Devops/Maven/Q3/three-app/src/test/resources
[INFO] 
[INFO] --- maven-compiler-plugin:3.13.0:testCompile (default-testCompile) @ three-app ---
[INFO] Recompiling the module because of changed dependency.
[INFO] Compiling 1 source file with javac [debug release 17] to target/test-classes
[INFO] 
[INFO] --- maven-surefire-plugin:3.3.0:test (default-test) @ three-app ---
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-api/3.3.0/surefire-api-3.3.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-api/3.3.0/surefire-api-3.3.0.pom (3.5 kB at 32 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-logger-api/3.3.0/surefire-logger-api-3.3.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-logger-api/3.3.0/surefire-logger-api-3.3.0.pom (3.3 kB at 46 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-shared-utils/3.3.0/surefire-shared-utils-3.3.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-shared-utils/3.3.0/surefire-shared-utils-3.3.0.pom (4.1 kB at 63 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-api/3.3.0/surefire-extensions-api-3.3.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-api/3.3.0/surefire-extensions-api-3.3.0.pom (3.5 kB at 55 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/maven-surefire-common/3.3.0/maven-surefire-common-3.3.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/maven-surefire-common/3.3.0/maven-surefire-common-3.3.0.pom (7.8 kB at 101 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-booter/3.3.0/surefire-booter-3.3.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-booter/3.3.0/surefire-booter-3.3.0.pom (4.8 kB at 66 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-spi/3.3.0/surefire-extensions-spi-3.3.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-spi/3.3.0/surefire-extensions-spi-3.3.0.pom (1.8 kB at 22 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-api/3.3.0/surefire-api-3.3.0.jar
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-logger-api/3.3.0/surefire-logger-api-3.3.0.jar
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-shared-utils/3.3.0/surefire-shared-utils-3.3.0.jar
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-api/3.3.0/surefire-extensions-api-3.3.0.jar
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/maven-surefire-common/3.3.0/maven-surefire-common-3.3.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-logger-api/3.3.0/surefire-logger-api-3.3.0.jar (14 kB at 90 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-booter/3.3.0/surefire-booter-3.3.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-api/3.3.0/surefire-api-3.3.0.jar (171 kB at 793 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-spi/3.3.0/surefire-extensions-spi-3.3.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-api/3.3.0/surefire-extensions-api-3.3.0.jar (26 kB at 104 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-booter/3.3.0/surefire-booter-3.3.0.jar (118 kB at 420 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-spi/3.3.0/surefire-extensions-spi-3.3.0.jar (8.2 kB at 29 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/maven-surefire-common/3.3.0/maven-surefire-common-3.3.0.jar (308 kB at 989 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-shared-utils/3.3.0/surefire-shared-utils-3.3.0.jar (2.8 MB at 3.5 MB/s)
[INFO] Using auto detected provider org.apache.maven.surefire.junitplatform.JUnitPlatformProvider
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit-platform/3.3.0/surefire-junit-platform-3.3.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit-platform/3.3.0/surefire-junit-platform-3.3.0.pom (5.7 kB at 31 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-providers/3.3.0/surefire-providers-3.3.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-providers/3.3.0/surefire-providers-3.3.0.pom (2.6 kB at 23 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-java5/3.3.0/common-java5-3.3.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-java5/3.3.0/common-java5-3.3.0.pom (2.8 kB at 42 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit-platform/3.3.0/surefire-junit-platform-3.3.0.jar
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-java5/3.3.0/common-java5-3.3.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit-platform/3.3.0/surefire-junit-platform-3.3.0.jar (27 kB at 93 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-java5/3.3.0/common-java5-3.3.0.jar (18 kB at 60 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/junit/jupiter/junit-jupiter-engine/5.11.0/junit-jupiter-engine-5.11.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/jupiter/junit-jupiter-engine/5.11.0/junit-jupiter-engine-5.11.0.pom (3.2 kB at 40 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-engine/1.11.0/junit-platform-engine-1.11.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-engine/1.11.0/junit-platform-engine-1.11.0.pom (3.2 kB at 28 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/junit/jupiter/junit-jupiter-engine/5.11.0/junit-jupiter-engine-5.11.0.jar
Downloading from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-engine/1.11.0/junit-platform-engine-1.11.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-engine/1.11.0/junit-platform-engine-1.11.0.jar (238 kB at 1.9 MB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/jupiter/junit-jupiter-engine/5.11.0/junit-jupiter-engine-5.11.0.jar (260 kB at 879 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-launcher/1.11.0/junit-platform-launcher-1.11.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-launcher/1.11.0/junit-platform-launcher-1.11.0.pom (3.0 kB at 37 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-launcher/1.11.0/junit-platform-launcher-1.11.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-launcher/1.11.0/junit-platform-launcher-1.11.0.jar (189 kB at 2.1 MB/s)
[INFO] 
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running three.example.AppTest
[ERROR] Tests run: 2, Failures: 1, Errors: 0, Skipped: 0, Time elapsed: 0.097 s <<< FAILURE! -- in three.example.AppTest
[ERROR] three.example.AppTest.testAdd -- Time elapsed: 0.018 s <<< FAILURE!
org.opentest4j.AssertionFailedError: expected: <5> but was: <6>
        at org.junit.jupiter.api.AssertionFailureBuilder.build(AssertionFailureBuilder.java:151)
        at org.junit.jupiter.api.AssertionFailureBuilder.buildAndThrow(AssertionFailureBuilder.java:132)
        at org.junit.jupiter.api.AssertEquals.failNotEqual(AssertEquals.java:197)
        at org.junit.jupiter.api.AssertEquals.assertEquals(AssertEquals.java:150)
        at org.junit.jupiter.api.AssertEquals.assertEquals(AssertEquals.java:145)
        at org.junit.jupiter.api.Assertions.assertEquals(Assertions.java:531)
        at three.example.AppTest.testAdd(AppTest.java:22)
        at java.base/java.lang.reflect.Method.invoke(Method.java:580)
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)

[INFO] 
[INFO] Results:
[INFO] 
[ERROR] Failures: 
[ERROR]   AppTest.testAdd:22 expected: <5> but was: <6>
[INFO] 
[ERROR] Tests run: 2, Failures: 1, Errors: 0, Skipped: 0
[INFO] 
[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  6.731 s
[INFO] Finished at: 2026-05-31T22:19:04+05:30
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:3.3.0:test (default-test) on project three-app: There are test failures.
[ERROR] 
[ERROR] Please refer to /home/aditya-2274/Storage/Documents/Devops/Maven/Q3/three-app/target/surefire-reports for the individual test results.
[ERROR] Please refer to dump files (if any exist) [date].dump, [date]-jvmRun[N].dump and [date].dumpstream.
[ERROR] -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException
aditya-2274@aditya-2274-IdeaPad-3-15IAU7 Q3/three-app (main) » mvn clean package                                                                      1 ↵
[INFO] Scanning for projects...
[INFO] 
[INFO] ----------------------< three.example:three-app >-----------------------
[INFO] Building three-app 3.0.0
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] --- maven-clean-plugin:3.4.0:clean (default-clean) @ three-app ---
[INFO] Deleting /home/aditya-2274/Storage/Documents/Devops/Maven/Q3/three-app/target
[INFO] 
[INFO] --- maven-resources-plugin:3.3.1:resources (default-resources) @ three-app ---
[INFO] skip non existing resourceDirectory /home/aditya-2274/Storage/Documents/Devops/Maven/Q3/three-app/src/main/resources
[INFO] 
[INFO] --- maven-compiler-plugin:3.13.0:compile (default-compile) @ three-app ---
[INFO] Recompiling the module because of changed source code.
[INFO] Compiling 1 source file with javac [debug release 17] to target/classes
[INFO] 
[INFO] --- maven-resources-plugin:3.3.1:testResources (default-testResources) @ three-app ---
[INFO] skip non existing resourceDirectory /home/aditya-2274/Storage/Documents/Devops/Maven/Q3/three-app/src/test/resources
[INFO] 
[INFO] --- maven-compiler-plugin:3.13.0:testCompile (default-testCompile) @ three-app ---
[INFO] Recompiling the module because of changed dependency.
[INFO] Compiling 1 source file with javac [debug release 17] to target/test-classes
[INFO] 
[INFO] --- maven-surefire-plugin:3.3.0:test (default-test) @ three-app ---
[INFO] Using auto detected provider org.apache.maven.surefire.junitplatform.JUnitPlatformProvider
[INFO] 
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running three.example.AppTest
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.063 s -- in three.example.AppTest
[INFO] 
[INFO] Results:
[INFO] 
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0
[INFO] 
[INFO] 
[INFO] --- maven-jar-plugin:3.4.2:jar (default-jar) @ three-app ---
[INFO] Building jar: /home/aditya-2274/Storage/Documents/Devops/Maven/Q3/three-app/target/three-app-3.0.0.jar
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  2.633 s
[INFO] Finished at: 2026-05-31T22:21:35+05:30
[INFO] ------------------------------------------------------------------------