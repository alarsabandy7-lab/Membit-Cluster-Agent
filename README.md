# 🧠 **Membit Context Agent — V61 (Narrative Build + Stable Release)**

A dual-purpose submission for the **Membit Half-Hackathon**:

1. ✅ A stable, production-ready Discord bot powered by real-time Membit data  
2. ✅ A narrative-style roadmap showing the evolution toward full MCP integration  

V61 demonstrates what can be built **today**, while revealing a clear path for **V-Next**.

---

# 🚀 1. Introduction

**Membit Context Agent** transforms real-time cluster signals from the Membit API into contextual insights inside Discord.

This system combines:
- **Membit Real-Time Data (Clusters + Posts)**
- **Gemini AI Reasoning**
- **Async-first Python architecture**
- **Full sanitization & fallback logic**

> **Goal:** Give AI real-world awareness, not static training data.

---

# ✅ 2. Core Stable Features (Fully Working)

### **`!hunt <keyword>` — Real-Time Cluster Scanner**
- Fetches up to 6 live clusters from Membit  
- Sanitizes text  
- Runs a single optimized Gemini call (no rate-limit issues)  
- Outputs: AI insight, cluster summaries, related posts, color-coded risk level  

---

### **`!analyze <text>` — AI Sentiment Context**
- Short reasoning-based sentiment analysis  
- Includes fallback for Gemini “Empty parts” edge case  

---

### **`!whatis <term>` — AI Dictionary**
- 1–2 sentence definitions  
- Ideal for Web3, AI, and technical terms  

---

### **`!trend <keyword>` — Pure Data Trend Scan**
Counts positive / risk signals in real-time clusters.  
Zero AI usage = stable and fast.

---

### **`!context` — Hackathon Context Explainer**
A hardcoded explanation of why AI needs real-world context.

---

# 🔮 3. V-Next Roadmap (Narrative Build)

V61 contains 4 *intentionally disabled* commands.  
Each outputs a **Roadmap Explanation** showing technical limitations + future plans.

---

### **`!compare` — MCP Comparator (Future)**
Planned to use:
requires **cluster ids**, not labels → needs new data structure.

---

### **`!risk` — advanced risk scoring (future)**
blocked by `gemini-flash-latest` model limitations on negative logic.

---

### **`!hot` — real-time trending (future)**
requires sort/filter parameters not yet documented in the api.

---

### **`!dive <cluster_id>` — deep data dive (future)**
needs:
- label-to-id mapping  
- access to `/clusters/info`  

this shapes v-next into a **proactive context agent**.

---

# 🧩 4. architecture
### Core design decisions:
- Async-first (`aiohttp`)  
- One AI call per workflow  
- Text-cleaning on all inputs  
- Cooldown spam protection  
- Fallback logic for AI inconsistencies  

---

# ⚙️ 5. Installation

# Clone repository
git clone https://github.com/<your-username>/Membit-Cluster-Agent
cd Membit-Cluster-Agent

# Install dependencies
pip install -U discord.py aiohttp google-generativeai python-dotenv

# Create .env file
DISCORD_TOKEN=your_discord_token
MEMBIT_API_KEY=your_membit_api_key
GEMINI_API_KEY=your_gemini_api_key
COOLDOWN_SECONDS=12

# Run bot
python main.py

# Example commands
!hunt bitcoin
!whatis defi
!analyze the market feels unstable
!trend ethereum
!context

# Demo Video
https://youtu.be/your-demo-link-here
