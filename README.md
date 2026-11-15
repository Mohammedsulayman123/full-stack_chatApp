<div align="center">

# 💬 Full-Stack Real-Time Chat App
### Enterprise-Grade Real-Time Messaging &bull; Cloud-Native DevOps Architecture &bull; Kubernetes &amp; Jenkins CI/CD

[![React](https://img.shields.io/badge/React-18-61DAFB?logo=react&logoColor=black&style=for-the-badge)](https://react.dev/)
[![Node.js](https://img.shields.io/badge/Node.js-18%2B-339933?logo=nodedotjs&logoColor=white&style=for-the-badge)](https://nodejs.org/)
[![Express](https://img.shields.io/badge/Express-4.x-000000?logo=express&logoColor=white&style=for-the-badge)](https://expressjs.com/)
[![Socket.io](https://img.shields.io/badge/Socket.io-4.x-010101?logo=socketdotio&logoColor=white&style=for-the-badge)](https://socket.io/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Latest-47A248?logo=mongodb&logoColor=white&style=for-the-badge)](https://www.mongodb.com/)
[![Docker](https://img.shields.io/badge/Docker-Multi--Stage-2496ED?logo=docker&logoColor=white&style=for-the-badge)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-K8s-326CE5?logo=kubernetes&logoColor=white&style=for-the-badge)](https://kubernetes.io/)
[![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?logo=jenkins&logoColor=white&style=for-the-badge)](https://www.jenkins.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

<br/>

<p align="center">
  A production-ready, full-stack real-time communication platform engineered with <strong>React</strong>, <strong>Node.js</strong>, <strong>Socket.io</strong>, and <strong>MongoDB</strong>. Powered by a cloud-native DevOps infrastructure featuring <strong>Docker multi-stage builds</strong>, <strong>Kubernetes (K8s) orchestration</strong>, <strong>Nginx Ingress</strong>, and an automated <strong>Jenkins CI/CD pipeline</strong> with continuous health monitoring.
</p>

[Explore Architecture](#-system-architecture--live-visualization) &bull;
[DevOps Pipeline](#-devops-cicd-pipeline-live-visualization) &bull;
[Quick Start](#-quick-start-with-docker-compose) &bull;
[Kubernetes Guide](#-kubernetes-k8s-cluster-deployment) &bull;
[API Docs](#-api-endpoints--contracts) &bull;
[Interactive Visualizer](docs/live-pipeline-visualizer.html)

</div>

---

## 🚀 DevOps CI/CD Pipeline (Live Visualization)

Below is the **live animated pipeline flow** depicting automated commits, webhook triggers, Jenkins build stages, smoke test health checks, Docker container image pushes, and Kubernetes rolling pod deployments.

> **💡 Live Moving Dots**: The animated glowing nodes and streaming dashed wires represent active telemetry streaming across each DevOps lifecycle stage.

<div align="center">
  <img src="assets/devops-pipeline.gif" alt="DevOps CI/CD Moving Dot Pipeline" width="100%" />
</div>

```mermaid
flowchart LR
    subgraph DEV["💻 Developer Environment"]
        A["Local Code"] -->|"git commit & push"| B["Branch: master"]
    end

    subgraph VCS["🐙 Version Control"]
        B -->|"Webhook Trigger"| C["GitHub Repository"]
    end

    subgraph CI["⚙️ Jenkins CI/CD Automation"]
        C --> D["1. Checkout Source"]
        D --> E["2. Smoke Test (/health)"]
        E --> F["3. Docker Multi-Stage Build"]
    end

    subgraph REG["🐳 Container Registry"]
        F -->|"Push Tag: latest"| G["Docker Hub"]
    end

    subgraph K8S["☸️ Kubernetes Cluster (chat-app)"]
        G -->|"Rolling Update"| H["Nginx Ingress (chat-tws.com)"]
        H -->|"Path: /"| I["Frontend Pod (React + Nginx)"]
        H -->|"Path: /api"| J["Backend Pod (Node + Socket.io)"]
        J -->|"mongodb-service:27017"| K[("MongoDB (PVC Persistent)")]
    end

    classDef dev fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef ci fill:#1e293b,stroke:#fbbf24,stroke-width:2px,color:#fff;
    classDef k8s fill:#0f172a,stroke:#34d399,stroke-width:2px,color:#fff;
    class DEV,VCS dev;
    class CI,REG ci;
    class K8S,I,J,K k8s;
```

<p align="center">
  🎮 <strong>Want an interactive simulation?</strong> Open the standalone <a href="docs/live-pipeline-visualizer.html"><strong>Live Pipeline Visualizer Dashboard (HTML)</strong></a> to pause/play packet delivery, trigger simulated Jenkins builds, inspect pod states, and stream real-time cluster telemetry logs in your browser!
</p>

---

## 🏛️ System Architecture &amp; Data Pipeline (Live Visualization)

The diagram below illustrates the end-to-end runtime architecture: dual client WebSocket synchronization, Nginx reverse proxy load-balancing, Express REST API controllers, MongoDB persistence, and Cloudinary media CDN.

<div align="center">
  <img src="assets/architecture-diagram.gif" alt="Real-Time Application Architecture Diagram" width="100%" />
</div>

```mermaid
flowchart TD
    subgraph CLIENTS["📱 Client Tier (React 18 + Vite + DaisyUI)"]
        A["Client A (Alice)"]
        B["Client B (Bob)"]
    end

    subgraph INGRESS["🛡️ Ingress & Proxy Tier"]
        NG["Nginx Reverse Proxy / Port 80"]
    end

    subgraph BACKEND["⚡ Application Tier (Port 5001)"]
        AUTH["Auth Controller (JWT)"]
        SOCK["Socket.io Cluster Engine (userSocketMap)"]
        MSG["Message Controller"]
    end

    subgraph DATA["💾 Persistence & Media CDN"]
        DB[("MongoDB (Users & Messages)")]
        CDN["Cloudinary CDN (Avatars & Media)"]
    end

    A <-->|"WebSocket Event Stream"| NG
    B <-->|"WebSocket Event Stream"| NG
    NG <--> SOCK
    A -->|"REST HTTP /api/auth"| NG --> AUTH
    AUTH --> DB
    SOCK --> MSG --> DB
    AUTH --> CDN
```

### 🔄 How Real-Time Data Flows:
1. **Connection &amp; Presence**: Upon client sign-in, the browser establishes a persistent WebSocket connection via Socket.io with the client's `userId`. The backend `userSocketMap` maintains online status and broadcasts `getOnlineUsers` to all active clients.
2. **Instant Messaging**: When Alice transmits a message to Bob, it travels as an encrypted payload over WebSocket to the Node.js backend.
3. **Concurrent Persistence**: The backend validates the JWT session, writes the chat document to **MongoDB**, and dispatches a targeted `newMessage` socket event directly to Bob's registered socket ID.
4. **Media &amp; Themes**: Profile photos and media attachments stream securely through **Cloudinary CDN**, while UI states and daisyUI themes persist locally via **Zustand**.

---

## ✨ Core Features

| Feature | Description |
| :--- | :--- |
| ⚡ **Instant Real-Time Chat** | Sub-millisecond peer-to-peer message delivery powered by Socket.io web-sockets. |
| 🟢 **Live Online/Offline Status** | Instant visual indicators showing when contacts enter or leave the chat. |
| 🔒 **Robust Authentication** | JSON Web Tokens (JWT) stored in secure, `httpOnly`, SameSite cookies + bcrypt password hashing. |
| 🎨 **32+ DaisyUI Themes** | Dynamic runtime theme switching with instant persistence across sessions. |
| 📸 **Cloud Image &amp; Media Uploads** | Profile photo customization and image messaging powered by Cloudinary. |
| 🐳 **Docker Multi-Stage Optimization** | Ultra-lean Alpine Linux containers running as non-root users (`appuser` / `nginx`). |
| ☸️ **Kubernetes Cloud Orchestration** | Complete K8s manifests including Ingress, Deployments, ClusterIP Services, and Persistent Volumes. |
| 🔄 **Continuous Integration &amp; Deployment** | Automated Jenkins pipeline featuring smoke tests (`/health`), image builds, and automated rollout. |
| 🩺 **Production Healthchecks** | Dedicated `/health` endpoint validating database connection readiness and pod health. |

---

## 🛠️ Technology Stack

```
┌────────────────────────────────────────────────────────────────────────┐
│                               TECH STACK                               │
├───────────────────┬────────────────────────────────────────────────────┤
│ Frontend          │ React 18, Vite, TailwindCSS, DaisyUI, Lucide React │
│ State Management  │ Zustand, React Hot Toast                           │
│ Backend Runtime   │ Node.js (v18+), Express.js (ES Modules)            │
│ Real-Time Engine  │ Socket.io (WebSocket with HTTP fallback)           │
│ Database          │ MongoDB (Mongoose ODM, Replica-ready)              │
│ Security & Auth   │ JSON Web Tokens (JWT), Cookie-Parser, Bcrypt.js    │
│ Media Storage     │ Cloudinary REST API & CDN                          │
│ Containerization  │ Docker, Docker Compose (Multi-stage Alpine images) │
│ Orchestration     │ Kubernetes (K8s Namespace, Deployments, PVC, Svc)  │
│ Reverse Proxy     │ Nginx, Nginx Ingress Controller                    │
│ CI/CD Automation  │ Jenkins (Jenkinsfile Pipeline as Code), Git        │
└───────────────────┴────────────────────────────────────────────────────┘
```

---

## 📂 Project Directory Structure

```plaintext
full-stack_chatApp/
├── .env                          # Global environment variables
├── docker-compose.yml            # Multi-container orchestration (FE, BE, Mongo)
├── Jenkinsfile                   # Declarative CI/CD pipeline script
├── package.json                  # Root scripts and workspace settings
│
├── assets/                       # Animated SVGs & visual assets
│   ├── devops-pipeline.svg       # Moving-dot DevOps CI/CD pipeline SVG
│   └── architecture-diagram.svg  # Moving-dot System Architecture SVG
│
├── docs/                         # Documentation & Interactive visualizers
│   └── live-pipeline-visualizer.html # Interactive HTML telemetry simulator
│
├── backend/                      # Node.js + Express Backend
│   ├── Dockerfile                # Multi-stage production container
│   ├── src/
│   │   ├── controllers/          # auth.controller.js, message.controller.js
│   │   ├── lib/                  # db.js (MongoDB), socket.js (Socket.io), cloudinary.js
│   │   ├── middleware/           # auth.middleware.js (JWT protectRoute)
│   │   ├── models/               # user.model.js, message.model.js
│   │   ├── routes/               # auth.route.js, message.route.js, health.route.js
│   │   └── index.js              # Server entry point & route registration
│   └── package.json
│
├── frontend/                     # React 18 + Vite SPA
│   ├── Dockerfile                # Multi-stage Vite build + Nginx runtime
│   ├── nginx.conf                # Nginx proxy config & SPA routing
│   ├── public/                   # Static images & UI screenshots
│   └── src/
│       ├── components/           # ChatContainer, MessageInput, Sidebar, Navbar
│       ├── store/                # useAuthStore.js, useChatStore.js, useThemeStore.js
│       ├── pages/                # HomePage, LoginPage, SignUpPage, ProfilePage
│       └── App.jsx
│
└── k8s/                          # Kubernetes Cloud Production Manifests
    ├── namespace.yml             # chat-app namespace
    ├── ingress.yml               # Nginx Ingress routing (chat-tws.com)
    ├── secrets.yml               # Base64 encoded secrets (JWT)
    ├── backend-deployment.yml    # Node.js backend Deployment (Port 5001)
    ├── backend-service.yml       # ClusterIP Service for backend
    ├── frontend-deployment.yml   # Nginx + React Deployment (Port 80)
    ├── frontend-service.yml      # ClusterIP Service for frontend
    ├── mongodb-deployment.yml    # MongoDB Deployment
    ├── mongodb-service.yml       # MongoDB ClusterIP
    ├── mongodb-pv.yml            # PersistentVolume for DB data
    └── mongodb-pvc.yml           # PersistentVolumeClaim (1Gi)
```

---

## ⚡ Quick Start with Docker Compose

The fastest way to spin up the entire application stack (Frontend, Backend, and MongoDB) is using Docker Compose:

### 1. Clone Repository & Setup Environment

```bash
git clone https://github.com/iemafzalhassan/full-stack_chatApp.git
cd full-stack_chatApp
```

Create or verify your `.env` file in the project root:

```env
# Database Configuration
MONGODB_URI=mongodb://root:admin@mongo:27017/chatApp?authSource=admin&retryWrites=true&w=majority

# Security
JWT_SECRET=super_secret_jwt_key_change_me_in_production

# Cloudinary CDN Configuration (Optional for photo uploads)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# Server Ports & Environment
PORT=5001
NODE_ENV=production
```

### 2. Launch the Application

```bash
# Build and run containers in detached mode
docker-compose up -d --build
```

### 3. Verify Container Status

```bash
docker-compose ps
```

| Service | Container Name | Internal Port | Host Port | URL |
| :--- | :--- | :--- | :--- | :--- |
| **Frontend** | `full-stack_chatapp-frontend-1` | 80 | 8080 | [http://localhost:8080](http://localhost:8080) |
| **Backend** | `full-stack_chatapp-backend-1` | 5001 | 5001 | [http://localhost:5001](http://localhost:5001) |
| **MongoDB** | `full-stack_chatapp-mongo-1` | 27017 | 27017 | `mongodb://localhost:27017` |

### 4. Verify Health Status

```bash
curl http://localhost:5001/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2026-11-15T19:40:00.000Z",
  "database": "connected",
  "environment": "production"
}
```

---

## ☸️ Kubernetes (K8s) Cluster Deployment

Deploying the stack to a production Kubernetes cluster (Minikube, EKS, GKE, AKS, or bare-metal K8s) is fully declarative using manifests in `k8s/`:

### 1. Apply All Manifests

```bash
# Create namespace
kubectl apply -f k8s/namespace.yml

# Apply configuration & secrets
kubectl apply -f k8s/secrets.yml

# Provision MongoDB Storage (PV & PVC)
kubectl apply -f k8s/mongodb-pv.yml
kubectl apply -f k8s/mongodb-pvc.yml

# Deploy Database
kubectl apply -f k8s/mongodb-deployment.yml
kubectl apply -f k8s/mongodb-service.yml

# Deploy Backend & Frontend Services
kubectl apply -f k8s/backend-deployment.yml
kubectl apply -f k8s/backend-service.yml
kubectl apply -f k8s/frontend-deployment.yml
kubectl apply -f k8s/frontend-service.yml

# Deploy Ingress Controller Routing
kubectl apply -f k8s/ingress.yml
```

Or apply all at once:
```bash
kubectl apply -f k8s/
```

### 2. Verify Cluster Resources

```bash
kubectl get all -n chat-app
```

Output:
```
NAME                                       READY   STATUS    RESTARTS   AGE
pod/backend-deployment-64d858597f-8n8pl    1/1     Running   0          45s
pod/frontend-deployment-7bb5df75c6-q2cql   1/1     Running   0          45s
pod/mongodb-deployment-55d644784b-74w7m    1/1     Running   0          50s

NAME                       TYPE        CLUSTER-IP       PORT(S)     AGE
service/backend            ClusterIP   10.108.120.14    5001/TCP    45s
service/frontend           ClusterIP   10.104.225.80    80/TCP      45s
service/mongodb-service    ClusterIP   10.111.45.19     27017/TCP   50s

NAME                                  CLASS    HOSTS          ADDRESS   PORTS   AGE
ingress.networking.k8s.io/chatapp-ingress   <none>   chat-tws.com             80      45s
```

### 3. Accessing via Ingress
Map `chat-tws.com` in your `/etc/hosts` (Linux/Mac) or `C:\Windows\System32\drivers\etc\hosts` (Windows):
```
127.0.0.1  chat-tws.com
```
Navigate to `http://chat-tws.com` in your browser.

---

## 🔄 Jenkins CI/CD Pipeline as Code

The project includes an enterprise declarative `Jenkinsfile` for continuous delivery.

```groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/iemafzalhassan/full-stack_chatApp.git'
            }
        }

        stage('Test') {
            steps {
                script {
                    sh '''
                        sleep 15
                        curl -f http://localhost:5001/health
                        curl -f http://localhost/ || exit 1
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker-compose up -d --build'
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment and tests completed successfully!'
        }
        failure {
            echo 'Deployment or tests failed.'
        }
    }
}
```

---

## 💻 Local Development Setup (Without Docker)

If you prefer running the code locally with hot module replacement (HMR):

### 1. Prerequisites
- **Node.js**: v18 or higher
- **MongoDB**: Local community server running on port `27017`

### 2. Backend Setup
```bash
cd backend
npm install

# Create backend/.env:
# PORT=5001
# MONGODB_URI=mongodb://localhost:27017/chatApp
# JWT_SECRET=mysecretkey
# NODE_ENV=development

npm run dev
# Server will start on http://localhost:5001
```

### 3. Frontend Setup
```bash
cd ../frontend
npm install
npm run dev
# Vite will serve at http://localhost:5173
```

---

## 📡 API Endpoints &amp; Contracts

### Authentication (`/api/auth`)
| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :---: |
| `POST` | `/api/auth/signup` | Register new user account | No |
| `POST` | `/api/auth/login` | Authenticate credentials &amp; issue JWT cookie | No |
| `POST` | `/api/auth/logout` | Invalidate session cookie | No |
| `PUT` | `/api/auth/update-profile` | Upload avatar &amp; update profile | Yes |
| `GET` | `/api/auth/check` | Validate current session cookie | Yes |

### Messages (`/api/messages`)
| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :---: |
| `GET` | `/api/messages/users` | Retrieve contact sidebar list | Yes |
| `GET` | `/api/messages/:id` | Fetch message history with user `:id` | Yes |
| `POST` | `/api/messages/send/:id` | Send text or image message to user `:id` | Yes |

### Health &amp; Telemetry (`/health`)
| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :---: |
| `GET` | `/health` | Kubernetes liveness/readiness probe &amp; DB status | No |

### WebSocket Events (Socket.io)
| Event Name | Direction | Payload | Description |
| :--- | :---: | :--- | :--- |
| `connection` | Client &rarr; Server | `{ query: { userId } }` | Client registers with socket engine |
| `getOnlineUsers` | Server &rarr; Client | `[ userId1, userId2, ... ]` | Broadcast active online users array |
| `newMessage` | Server &rarr; Client | `MessageObject` | Targeted message dispatched to receiver |
| `disconnect` | Client &rarr; Server | &mdash; | Triggered on socket close; updates online status |

---

## 📸 Application Screenshots

<div align="center">
  <img src="frontend/public/screenshot-for-readme.png" alt="Chat Application Full Preview" width="100%" />
</div>

<br/>

<div align="center">
  <table width="100%">
    <tr>
      <td width="50%" align="center">
        <strong>💬 Real-Time Messaging View</strong><br/><br/>
        <img src="frontend/public/chat.png" alt="Chat Window" width="100%" />
      </td>
      <td width="50%" align="center">
        <strong>🎨 32+ DaisyUI Themes Switcher</strong><br/><br/>
        <img src="frontend/public/settings.png" alt="Theme Settings" width="100%" />
      </td>
    </tr>
    <tr>
      <td width="50%" align="center">
        <strong>🔐 Secure Authentication</strong><br/><br/>
        <img src="frontend/public/login.png" alt="Login Page" width="100%" />
      </td>
      <td width="50%" align="center">
        <strong>🚪 Graceful Session Management</strong><br/><br/>
        <img src="frontend/public/logout.png" alt="Logout Modal" width="100%" />
      </td>
    </tr>
  </table>
</div>

---

## 🔒 Security Best Practices Implemented

- **Non-Root Containers**: Both frontend and backend Dockerfiles create unprivileged users (`appuser` in backend, `nginx` in frontend) to minimize host breach impact.
- **HTTP-Only Cookies**: JWTs are stored with `httpOnly: true`, preventing Client-Side Cross-Site Scripting (XSS) token theft.
- **Strict CORS Policy**: Whitelisted origin boundaries configured specifically between production ingress and development ports.
- **Kubernetes Secret Segregation**: Sensitive credentials and JWT keys are separated from code into `k8s/secrets.yml`.
- **Liveness &amp; Readiness Probes**: Built-in health checks automatically cycle unresponsive pods without downtime.

---

## 🤝 Contributing

Contributions are welcomed! Whether you are optimizing DevOps manifests, adding WebSocket typing indicators, or refining UI components:

1. **Fork** the repository: [https://github.com/iemafzalhassan/full-stack_chatApp/fork](https://github.com/iemafzalhassan/full-stack_chatApp/fork)
2. **Create your Feature Branch**:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your Changes**:
   ```bash
   git commit -m "feat: Add typing indicator broadcast event"
   ```
4. **Push to the Branch**:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**.

---

## 📜 License

This project is open-source and distributed under the [MIT License](LICENSE).

---

<div align="center">
  <strong>⭐ Star this repository if you find it helpful! ⭐</strong>
</div>