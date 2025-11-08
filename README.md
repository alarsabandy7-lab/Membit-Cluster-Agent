# 🧠 **Membit Context Agent — V62 (Local Risk Engine)**

A dual-purpose submission for the **Membit Half-Hackathon**:

1.  ✅ **A stable, production-ready Discord bot** (V67) using real-time Membit data.
2.  ✅ **A narrative build** (V67) showing a clear architectural roadmap for full MCP integration.

V67 demonstrates what can be built **today**, and *proves* we have a clear vision for what comes **next**.

> **“Context isn't data — it's awareness. Membit gives AI its eyes.”**

---

# 🚀 **1. Introduction**

**Membit Context Agent** transforms real-time cluster data from the **Membit API** into actionable insights inside Discord.

Unlike static AI bots, this agent uses:
- **Real-time social signals** (Membit Clusters & Posts)
- **Gemini AI reasoning** (for sentiment & summarization)
- **A 100% Stable *Local* Risk Engine** (for `!risk` and `!hunt` coloring)
- **Clean, latency-safe processing** (`aiohttp`)

This combination equips AI with something it normally doesn’t have: **Awareness of what is happening *right now*.**

---

# ✅ **2. Core Features (Stable & Fully Working)**

These are the 6 core features shipped in **V67** and tested for reliability.

### **`!hunt <keyword>` — Real-Time Cluster Hunting**
Searches for up to 6 clusters using Membit’s Search API, cleans the text, and performs **one optimized Gemini call** to avoid rate-limits. Outputs include:
- Cluster summaries & AI-generated overall insight
- Related posts (X/Twitter or Web)
- Color-coded risk/opportunity classifier

### **`!analyze <text>` — AI Sentiment Analyzer**
Provides a short, reasoning-based sentiment analysis (Positive/Negative/Neutral) using Gemini AI.

### **`!risk <text>` — Local Risk Scanner (100% Stable)**
This is our **local, heuristic (keyword-based) risk engine**. It does **NOT** call the AI, meaning it's 100% stable and will **never** fail with `Empty parts`. It provides instant risk recommendations (High Risk / Opportunity / Neutral).

### **`!whatis <term>` — AI Dictionary**
Simple, fast definitions for Web3, tech, and AI terms using Gemini AI.

### **`!trend <keyword>` — Data-Driven Trend Scanner**
Pure Membit data analysis. Counts Positive/Risk indicators from the top 8 clusters.

### **`!context` — Hackathon Context Command**
A "hardcoded" stable command that explains the purpose of Membit’s real-time context and how it powers AI systems.

---

# 🔮 **3. V-Next Roadmap (Narrative Build)**

V67 includes **1 intentionally disabled "experimental" command**.
It replies with a **Roadmap Explanation** to show the limitations encountered and the clear vision for V-Next.

### **`!compare <a> vs <b>` — MCP Cluster Comparator**
* **Goal:** Use the official `/v1/clusters/compare` endpoint for native, data-driven comparisons (instead of AI guesses).
* **Status:** Paused. Our tests (V51) failed, indicating we need to read the documentation more closely for the correct parameters (e.g., `topicA`, `topicB`).
* **Roadmap:** Integrate the *real* Membit compare endpoint for superior results.

*(We also paused exploration of `!hot` and `!dive` (MCP) due to API/model limitations documented in our V1-V60 debug journey.)*

---

# 🧩 **4. Architecture Overview**
- **Async-first:** Uses `aiohttp` for non-blocking API calls.
- **Optimized:** One AI call per workflow (in `!hunt`) to avoid 429 rate limits.
- **Robust:** Strong sanitization filters (`clean_text`) and a **Local Risk Engine** (anti-`Empty parts`).
- **Community-Ready:** Full cooldown system to prevent spam.

---

# ⚙️ **5. Installation**

### 1. Clone
```bash
git clone https://github.com/alarsabandy7-lab/Membit-Cluster-Agent.git
cd Membit-Cluster-Agent
```
2. Install Dependencies
```bash
pip install -U discord.py aiohttp google-generativeai python-dotenv
```
3.Create .env file
​Create a file named .env in the folder and add your keys:
```bash
DISCORD_TOKEN=your_discord_token
MEMBIT_API_KEY=your_membit_key
GEMINI_API_KEY=your_gemini_key
COOLDOWN_SECONDS=12
```
4.Run
```bash
python main.py
```
​💬 6. Example Commands
```bash
!hunt bitcoin
!whatis deflation
!analyze the market looks unstable
!risk The devs are anonymous and the liquidity is locked for only 3 days.
!trend ethereum
!context
```
​
🔥 7. The "Grit Story"

This entire V67 build—from the initial V1 debug hell (404s, 429s, Empty parts, Falsbachink typos) to the final V67 "Local Risk Engine"—was coded, tested, and debugged 100% on a Realme Narzo 20 mobile phone.


```bash
>“If you want one thing, you have to risk everything.”
```


​🎥 8. Demo Video
​Add your demo link here:Coming soon


​👤 9. Author
​Mettzy_ 
AI Integrator • Context Systems Builder
Bot Version: V67 - Local Risk Engine


​📜 10. License
​MIT License
Copyright (c) 2025 Mettzy_
