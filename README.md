# 🧠 Membit Cluster Agent – Deep Hunt Bot  
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Discord.py](https://img.shields.io/badge/Discord.py-API-green?logo=discord)
![Membit](https://img.shields.io/badge/Membit-Data%20Agent-purple)
![Replit](https://img.shields.io/badge/Built%20on-Replit-orange)
![Hackathon](https://img.shields.io/badge/Hackathon-Submission✅-brightgreen)

**Membit Cluster Agent** is a Discord bot that performs real-time data hunts using **Membit’s MCP and API**, allowing users to fetch live clusters and relevant posts directly from Discord.

---

## 🚀 Overview
This project was created for the **Membit Half-Hackathon**, demonstrating how **Membit’s real-time contextual data** can be integrated into chat-based environments.

With just a few simple commands, anyone can explore *live data clusters, summaries, and posts* from Membit — all inside Discord.

---

## ⚙️ Features
- 🔍 **`!hunt <keyword>` — Deep Hunt Mode**  
  Fetches clusters and related posts directly from Membit’s API.  
- 💡 **Dynamic Sentiment Color System**  
  - 🟢 Green → positive/trending topics  
  - 🔴 Red → risk/scam/controversy  
  - 🔵 Blue → neutral/general context  
- 🤖 **Utility Commands**  
  - `!ping` → check bot status  
  - `!help` → show available commands  
- 🧩 **Clean, Minimal, and Informative Output**  
  Displays data in professional Discord embeds with direct links to source posts.

---

## 🛠️ Tech Stack
| Component | Details |
| :--- | :--- |
| **Language** | Python 3 |
| **Libraries** | `discord.py`, `requests`, `json`, `os` |
| **APIs Used** | Membit MCP / Membit REST API |
| **Platform** | Replit (Mobile Build) |

---

## 🧪 How It Works
1. User types: `!hunt <keyword>`  
2. The bot performs a dual Membit API query:  
   - `v1/clusters/search` → Finds live clusters & summaries  
   - `v1/posts/search` → Finds related source posts  
3. The bot returns an embedded summary with colors and clickable source links.  

Example:
📊 → Bot responds with clusters, summaries, and a relevant post link.

---

## 🧠 System Architecture & Final Vision

### 🧩 Current Build (v37 Lite)
```
User (Discord)
   ↓
!hunt <keyword>
   ↓
Membit API Layer
   ├── v1/clusters/search
   └── v1/posts/search
   ↓
Context Processor (Manual Analyze)
   ↓
Dynamic Embed Builder
   ↓
Discord Output (Color-coded Insight)
```
> 🔹 This version still runs **without direct Gemini integration**.  
> Sentiment is analyzed using **keyword-based logic** and structured output.  
> Despite limitations, it already reflects Membit’s data context potential.

---

### 🚀 Future Vision (v38+ / Final AI Stage)
```
User (Discord)
   ↓
!hunt <keyword>
   ↓
Membit Dual API
   ├── Contextual Clusters
   └── Real-time Posts
   ↓
AI Context Layer (Gemini 2.5 Pro)
   ├── Auto Insight Summarization
   ├── Sentiment Classification
   └── Risk/Trend Scoring
   ↓
Smart Embed Generator
   ↓
Discord Real-time Insight Stream
```
> 🧠 The goal is to let Membit’s data be **auto-analyzed by Gemini**, returning one cohesive “context intelligence block” inside Discord — an instant mini report combining raw data + human-like summary.

---

### 🔮 Why This Matters
This project isn’t just a bot — it’s a **prototype for a data-to-insight pipeline**:
- Shows how Membit data can power *real-time contextual agents.*
- Demonstrates a *mobile-only dev environment* achieving functional automation.
- Builds groundwork for a scalable AI layer that turns context → decision insight.

---

## 📸 Proof of Functionality
Due to deployment limitations, functionality is demonstrated with screenshots.  
👉 [View Proofs Folder](https://github.com/alarsabandy7-lab/Membit-Cluster-Agent/tree/proofs)

---

## 📘 Notes
This project was **coded 100% on a mobile phone via Replit**, showing that Membit’s ecosystem enables lightweight, accessible, and creative real-world integrations.

---

### 🏁 Credits
Developed by **Mettzy_**  
Built for the **Membit Half-Hackathon 2025**

> **Vision Statement:**  
> “From raw social data to actionable context — directly inside chat.”  
> — *Mettzy_, 2025*
