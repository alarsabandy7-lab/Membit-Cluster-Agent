🧠 Membit Cluster Agent – Deep Hunt Bot

    

Membit Cluster Agent is a Discord bot that performs real-time data hunts using Membit’s MCP and API, allowing users to fetch live clusters and relevant posts directly from Discord.


---

🚀 Overview

This project was created for the Membit Half-Hackathon, demonstrating how Membit’s real-time contextual data can be integrated into chat-based environments.

With just a few simple commands, anyone can explore live data clusters, summaries, and posts from Membit — all inside Discord.


---

⚙️ Features

🔍 !hunt <keyword> — Deep Hunt Mode
Fetches clusters and related posts directly from Membit’s API.

💡 Dynamic Sentiment Color System

🟢 Green → positive/trending topics

🔴 Red → risk/scam/controversy

🔵 Blue → neutral/general context


🤖 Utility Commands

!ping → check bot status

!help → show available commands


🧩 Clean, Minimal, and Informative Output
Displays data in professional Discord embeds with direct links to source posts.



---

🛠️ Tech Stack

Component	Details

Language	Python 3
Libraries	discord.py, requests, json, os
APIs Used	Membit MCP / Membit REST API
Platform	Replit (Mobile Build)



---

🧪 How It Works

1. User types: !hunt <keyword>


2. The bot performs a dual Membit API query:

v1/clusters/search → Finds live clusters & summaries

v1/posts/search → Finds related source posts



3. The bot returns an embedded summary with colors and clickable source links.



Example:
📊 → Bot responds with clusters, summaries, and a relevant post link.


---

🧠 System Architecture (v37 Lite – Current Build)

User (Discord)
   ↓
!hunt <keyword>
   ↓
Membit API Layer
   ├── v1/clusters/search
   └── v1/posts/search
   ↓
Context Processor (Lite)
   ↓
Embed Builder (Color-coded)
   ↓
Discord Output


---

🚀 Final Vision (v38+ – Full Cluster Agent)

User (Discord)
   ↓
!hunt <keyword>
   ↓
Membit Dual API
   ↓
AI Insight Layer (Gemini 2.5 Pro)
      ├── Auto Context Summary
      ├── Trend & Risk Scoring
      └── Sentiment Intelligence
   ↓
Smart Embed Output

> Goal: Transform raw Membit clusters → one-block intelligence insight directly in Discord.




---

📸 Proof of Functionality

Due to deployment limitations, functionality is demonstrated with screenshots.
👉 Proofs folder link


---

📘 Notes

This project was coded 100% on a mobile phone via Replit, showing that Membit’s ecosystem enables lightweight, accessible, and creative real-world integrations.


---

🏁 Credits

Developed by Mettzy_
Built for the Membit Half-Hackathon 2025

> Vision Statement:
“From raw social data to actionable context — directly inside chat.”
— Mettzy_, 2025



