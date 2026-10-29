# Nurbek Abildaev

### Backend & Distributed Systems Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nurbek-abildaev-b1b277345)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=flat-square&logo=telegram&logoColor=white)](https://t.me/NURJAKS1)
[![Email](https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:nurbekabildaev89@gmail.com)

> Backend engineer specializing in **event-driven distributed systems**, **high-concurrency APIs**, and **production data pipelines**. Focused on database performance optimization, resilient worker topologies, and measurable business impact.

---

<!-- DYNAMIC_PROFILE:START -->
<div align="center">
  <kbd>📍 Almaty: +2°C (Patchy rain nearby)</kbd> • <kbd>⚡ Status: Engineering Scalable Systems</kbd> • <kbd>🔄 Synced: 29 Oct 2026, 03:40 UTC</kbd>
</div>

<br/>

> 💡 **Architectural Thought of the Day:**  
> *" Simplicity is prerequisite for reliability. (Edsger W. Dijkstra) "*

<br/>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=NURJAKS&show_icons=true&theme=radical&hide_border=true&count_private=true" height="150" alt="GitHub Stats"/>
  &nbsp;&nbsp;
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=NURJAKS&layout=compact&theme=radical&hide_border=true" height="150" alt="Top Languages"/>
</p>
<!-- DYNAMIC_PROFILE:END -->

---

### 🛠 Core Technical Stack

**Core Languages**  
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-CC292B?style=flat-square&logo=sqlite&logoColor=white)

**Backend Frameworks & Runtime**  
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![NestJS](https://img.shields.io/badge/NestJS-E0234E?style=flat-square&logo=nestjs&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)

**Databases, Cache & Asynchronous Queues**  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![BullMQ](https://img.shields.io/badge/BullMQ-FF5722?style=flat-square&logo=redis&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=flat-square&logo=rabbitmq&logoColor=white)

**Architecture, Protocols & DevOps**  
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![WebSockets](https://img.shields.io/badge/WebSockets-010101?style=flat-square&logo=socketdotio&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

---

### 🚀 Production & Engineering Highlights

* **Distributed Media Generation Pipeline ([ai-video-generator-saas](https://github.com/NURJAKS/ai-video-generator-saas)):**
  Architected an asynchronous video composition engine using **NestJS**, **BullMQ**, and **FFmpeg**. Quarantined compute-heavy AI rendering workflows into isolated worker queues, maintaining **sub-50ms API response latencies** while streaming bidirectional progress updates over WebSockets.

* **Database Optimization & Inventory State Machines (B2B SaaS WMS):**
  Engineered atomic FIFO/FEFO inventory allocation logic in PostgreSQL. Optimized complex relational queries and implemented **Redis pipelining** for high-load transaction paths, reducing P95 API response times from **2.5s down to 0.5s** (80% latency reduction).

* **Edge-Native Serverless Architecture ([edge-serverless-crm](https://github.com/NURJAKS/edge-serverless-crm)):**
  Engineered an edge-native CRM portal deployed across **Cloudflare Workers** and **Cloudflare D1** distributed SQL storage, leveraging Web Crypto JWT authentication for sub-10ms global edge execution.

* **Microservices Task Orchestration ([distributed-kanban-microservices](https://github.com/NURJAKS/distributed-kanban-microservices)):**
  Implemented a cloud-native Kanban platform enforcing the **Database-per-Service** pattern across decoupled PostgreSQL instances, orchestrated via **Kong API Gateway** (centralized JWT validation, rate limiting) with **Celery & Redis** asynchronous workers.

* **Real-Time Fleet Routing Engine ([smart-logistics-engine](https://github.com/NURJAKS/smart-logistics-engine)):**
  Developed a containerized routing backend composing OpenStreetMap road networks (**OSRM**), vehicle routing problem solvers (**VROOM**), and ML-based delay estimation with live WebSocket dispatch telemetry.

* **Threat Intelligence & LLM Security ([phishguard-threat-intelligence](https://github.com/NURJAKS/phishguard-threat-intelligence)):**
  Built a real-time anti-phishing engine combining lexical parsing, WHOIS/SSL telemetry, and multi-LLM security triage streaming live detections via Server-Sent Events (SSE).

* **AI Tooling & Codebase Intelligence ([zod-mcp-server](https://github.com/NURJAKS/zod-mcp-server)):**
  Created an extensible **Model Context Protocol (MCP)** server providing AST-based code transforms, hybrid semantic vector search, and persistent agent memory.

---

### 📂 Featured Architectural Repositories

| Repository | Architecture & Focus | Core Stack |
| :--- | :--- | :--- |
| [ai-video-generator-saas](https://github.com/NURJAKS/ai-video-generator-saas) | Event-driven media pipeline, worker pools, real-time telemetry | NestJS, BullMQ, Redis, FFmpeg, Angular |
| [distributed-kanban-microservices](https://github.com/NURJAKS/distributed-kanban-microservices) | Database-per-Service isolation, API Gateway pattern | Python, Flask, Kong, PostgreSQL, Celery |
| [smart-logistics-engine](https://github.com/NURJAKS/smart-logistics-engine) | Real-time vehicle routing solver & fleet dispatch engine | FastAPI, OSRM, VROOM, WebSockets, Docker |
| [zod-mcp-server](https://github.com/NURJAKS/zod-mcp-server) | Context protocol server for LLM agents & semantic search | TypeScript, MCP Protocol, Vector Search |
| [edge-serverless-crm](https://github.com/NURJAKS/edge-serverless-crm) | Edge-native distributed serverless CRM & client portal | Cloudflare Workers, D1 SQL, React 18 |
| [phishguard-threat-intelligence](https://github.com/NURJAKS/phishguard-threat-intelligence) | Threat intelligence & anti-phishing heuristic analysis engine | PHP, Python, LLM Security, SSE |
| [freelance-aggregator-pipeline](https://github.com/NURJAKS/freelance-aggregator-pipeline) | Resilient ingestion pipeline with deduplication & alert queues | Python, Asyncio, Telegram API, SQLite |
| [omnichannel-lead-router](https://github.com/NURJAKS/omnichannel-lead-router) | Omnichannel CRM & lead routing service with webhook pipelines | FastAPI, Aiogram 3, WhatsApp API, Sheets |

---

<div align="center">
  <sub>Engineered for reliability, scalability, and measurable performance.</sub>
</div>
