A company is deploying a microservices-based web application using Docker Compose.
The architecture contains the following containers:

1. MySQL database service
2. Redis cache service
3. Backend API service
4. Nginx reverse proxy service

The API service depends on both MySQL and Redis, while Nginx forwards client requests to the API container.

Write a `docker-compose.yml` configuration to:

* Create and run all four containers
* Ensure MySQL and Redis start before the API service
* Configure Nginx as a reverse proxy for the API
* Use appropriate Docker Compose features such as:

  * `services`
  * `depends_on`
  * `ports`
  * `environment`
  * `build` and `image`

Also explain the purpose of:

* `depends_on`
* Docker networking between containers
* the role of Nginx in the architecture


Architecture:
                Client
                   ↓
                Nginx (reverse proxy)
                   ↓
                API container
                   ↓
                MySQL + Redis

So total 4 containers:
1)MySql
2)Redis
3)api backend
4)ngnix

and thewy wanted:
-service dependency ordering
-networking
-reverse proxy understanding
-multi-container orchestration

Full Mental Model:
    mysql
    redis
       ↓
    api
       ↓
    nginx
_Concepts hidden_ :
1. Service Discovery via DNS

Inside Docker Compose:

api can access mysql using hostname:
mysql

api can access redis using hostname:
redis

NOT localhost.

This is VERY commonly asked.

2. Why Nginx?

Nginx acts as:

reverse proxy
load balancer
frontend gateway

Flow:

Browser → Nginx → API
3. Why Redis?

Redis is usually:

caching
session storage
queue/pub-sub
4. Why MySQL?

Persistent relational storage.

5. build vs image

VERY COMMON QUESTION.

build	image
creates image from Dockerfile	pulls existing image
used for custom apps	used for ready-made apps

Example:

api:
  build: .

means:

use local Dockerfile

Whereas:

redis:
  image: redis

means:

pull official Redis image
6. depends_on Important Detail

BIG THEORY POINT:

depends_on only controls:

startup order

It does NOT guarantee:

database is fully ready
Real production systems use:
    healthchecks
    wait-for-it scripts
    retry logic

7. Networking Concept

All services automatically join same Compose network.

So:

api ↔ mysql
api ↔ redis
nginx ↔ api

can communicate internally.

8. Environment Variables

Very common:

environment:
  DB_HOST: mysql

Injects env vars into container.

9. Port Mapping
ports:
  - "80:80"

means:

host_port : container_port

Q)whether ngnix or api , either of them start first , doesn't matter??
Soln. Mostly yes — between Nginx and API, startup order usually does not matter much compared to DB → API dependency.

The critical dependency is: Mysql/Redis -> API
because:

API often crashes or fails if DB/cache unavailable.

Whereas:
        Ngnix -> API   , is softer coupling

Case 1 — Nginx Starts First
            Nginx starts
            ↓
            API not ready yet
            ↓
            Initial requests may fail (502 Bad Gateway)
            ↓
            API comes up
            ↓
            Nginx works normally
Usually nginx itself keeps running fine.

Case 2 — API Starts First
            API starts
            ↓
            Nginx starts
            ↓
            Everything works
Cleaner Startup

So Why Use depends_on for Nginx?

Mostly for:

cleaner orchestration
predictable startup
avoiding temporary 502 errors

NOT because nginx fundamentally requires API to exist before booting.

But DB Before API DOES Matter:
Example:
            API starts
            ↓
            tries DB connection
            ↓
            MySQL unavailable
            ↓
            API crashes
This is why:
api:
  depends_on:
    - mysql
    - redis

Real Production Truth

Modern systems are designed assuming:

services may restart anytime
order cannot be trusted completely

So applications should:

retry DB connections
handle unavailable upstreams gracefully

Docker Compose depends_on is only basic orchestration.

_Note_: The API service exposes port 5000 mainly for direct host access and testing.
Nginx forwards requests internally to the API container using Docker Compose networking and service discovery (api:5000).
Container-to-container communication inside Docker networks does not require ports mapping.

Final Output:
![alt text](image.png)