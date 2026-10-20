# Nurbek Abildaev

### Backend & Distributed Systems Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nurbek-abildaev-b1b277345)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=flat-square&logo=telegram&logoColor=white)](https://t.me/NURJAKS1)
[![Email](https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:nurbekabildaev89@gmail.com)

> Backend engineer specializing in **event-driven distributed systems**, **high-concurrency APIs**, and **production data pipelines**. Focused on database performance optimization, resilient worker topologies, and measurable business impact.

---

### 🚀 Production & Engineering Highlights

* **Distributed Media Generation Pipeline ([ai-video-generator-saas](https://github.com/NURJAKS/ai-video-generator-saas)):**
  Architected an asynchronous video composition engine using **NestJS**, **BullMQ**, and **FFmpeg**. Quarantined compute-heavy AI rendering workflows into isolated worker queues, maintaining **sub-50ms API response latencies** while streaming bidirectional progress updates over WebSockets.

* **Database Optimization & Inventory State Machines (B2B SaaS WMS):**
  Engineered atomic FIFO/FEFO inventory allocation logic in PostgreSQL. Optimized complex relational queries and implemented **Redis pipelining** for high-load transaction paths, reducing P95 API response times from **2.5s down to 0.5s** (80% latency reduction).

* **Edge-Native Serverless Architecture ([crm-website](https://github.com/NURJAKS/crm-website)):**
  Engineered an edge-native CRM portal deployed across **Cloudflare Workers** and **Cloudflare D1** distributed SQL storage, leveraging Web Crypto JWT authentication for sub-10ms global edge execution.

* **Microservices Task Orchestration ([Mini-Trello](https://github.com/NURJAKS/Mini-Trello)):**
  Implemented a cloud-native Kanban platform enforcing the **Database-per-Service** pattern across decoupled PostgreSQL instances, orchestrated via **Kong API Gateway** (centralized JWT validation, rate limiting) with **Celery & Redis** asynchronous workers.

* **Real-Time Fleet Routing Engine ([smart_logistics](https://github.com/NURJAKS/smart_logistics)):**
  Developed a containerized routing backend composing OpenStreetMap road networks (**OSRM**), vehicle routing problem solvers (**VROOM**), and ML-based delay estimation with live WebSocket dispatch telemetry.

* **AI Tooling & Codebase Intelligence ([ZOD-mcp-server](https://github.com/NURJAKS/ZOD-mcp-server)):**
  Created an extensible **Model Context Protocol (MCP)** server providing AST-based code transforms, hybrid semantic vector search, and persistent agent memory.

---

### 🛠 Core Technical Stack

| Domain | Technologies & Patterns |
| :--- | :--- |
| **Languages** | TypeScript, JavaScript, Python, Go, SQL |
| **Backend & Frameworks** | Node.js (NestJS, Express), Python (FastAPI, Flask), Go (Fiber) |
| **Distributed Systems & Queues** | BullMQ, Celery, Redis (Caching, Pub/Sub, Pipelines), RabbitMQ concepts |
| **Databases & Storage** | PostgreSQL (Indexing, Partitioning, ACID), Cloudflare D1, MongoDB, MinIO (S3) |
| **Architecture Patterns** | Microservices, Event-Driven Architecture, Database-per-Service, CQRS principles |
| **Infrastructure & DevOps** | Docker, Docker Compose, Kong API Gateway, Linux / Bash, Nginx, GitHub Actions |
| **Protocols & Networking** | RESTful APIs, WebSockets, Server-Sent Events (SSE), Webhooks, gRPC principles |

---

### 📂 Featured Architectural Repositories

| Repository | Architecture & Focus | Core Stack |
| :--- | :--- | :--- |
| [ai-video-generator-saas](https://github.com/NURJAKS/ai-video-generator-saas) | Event-driven media pipeline, worker pools, real-time telemetry | NestJS, BullMQ, Redis, FFmpeg, Angular |
| [Mini-Trello](https://github.com/NURJAKS/Mini-Trello) | Database-per-Service isolation, API Gateway pattern | Python, Flask, Kong, PostgreSQL, Celery |
| [smart_logistics](https://github.com/NURJAKS/smart_logistics) | Real-time vehicle routing solver & fleet dispatch engine | FastAPI, OSRM, VROOM, WebSockets, Docker |
| [ZOD-mcp-server](https://github.com/NURJAKS/ZOD-mcp-server) | Context protocol server for LLM agents & semantic search | TypeScript, MCP Protocol, Vector Search |
| [freelance-aggregator-pipeline](https://github.com/NURJAKS/freelance-aggregator-pipeline) | Resilient ingestion pipeline with deduplication & alert queues | Python, Asyncio, Telegram API, SQLite |
| [crm-website](https://github.com/NURJAKS/crm-website) | Edge-native distributed serverless CRM & client portal | Cloudflare Workers, D1 SQL, React 18 |

---

<div align="center">
  <sub>Engineered for reliability, scalability, and measurable performance.</sub>
</div>
