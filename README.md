🧠 Membit Cluster Agent – Deep Hunt Bot

    

Membit Cluster Agent is a Discord bot designed for real-time contextual intelligence. It integrates Membit’s MCP and API to fetch live clusters, summaries, and related posts directly into Discord.


---

🚀 Overview

Built for the Membit Half-Hackathon, this project demonstrates how Membit’s real-time data can be transformed into actionable insights in chat environments.

With simple commands, users can explore:

Live clusters

Context summaries

Related posts

Color-coded risk signals



---

⚙️ Features

🔍 !hunt <keyword> – Deep Hunt Mode
Retrieves clusters and related posts directly from Membit.

💡 Dynamic Sentiment Color System

🟢 Positive / trending topics

🔴 Risk / scam / controversy

🔵 Neutral / general context


🤖 Utility Commands

!ping – Bot status check

!help – List of commands


🧩 Clean Output Professional Discord embeds with source links and structured context.



---

🛠️ Tech Stack

Component	Details

Language	Python 3
Libraries	discord.py, requests, json, os
APIs	Membit MCP / Membit REST API
Platform	Replit (Mobile Development)



---

🧪 How It Works

1. User types: !hunt <keyword>


2. Bot triggers a dual Membit API query:

v1/clusters/search – Retrieves live clusters and summaries

v1/posts/search – Retrieves related source posts



3. Bot generates a structured, color-coded Discord embed.




---

🧠 System Architecture & Vision

✅ Current Build (v37 Lite)

User (Discord)
   ↓
!hunt <keyword>
   ↓
Membit API Layer
   ├── v1/clusters/search
   └── v1/posts/search
   ↓
Context Processor (Keyword Logic)
   ↓
Embed Builder
   ↓
Discord Output

Notes:

No Gemini auto-insight due to key/payment limitations.

Sentiment uses keyword-based detection.

Fully functional and stable for real-time hunting.



---

🚀 Future Vision (v38+)

User (Discord)
   ↓
!hunt <keyword>
   ↓
Membit Dual API
   ↓
AI Context Layer (Gemini 2.5 Pro)
   ├── Auto Insight Summary
   ├── Trend & Risk Scoring
   └── Context Fusion
   ↓
Smart Embed Generator
   ↓
Discord Real-time Insight

This transforms Membit’s raw data → structured insight → user-friendly intelligence.


---

📸 Proof of Functionality

Screenshots provided due to environment limitations.
👉 proofs/ folder in GitHub repository.


---

⚠️ Known Limitations

Gemini 2.5 Pro not integrated (key/paywall restrictions)

Replit SSL patching required in some environments

AI Insight still handled manually via !analyze



---

📘 Development Notes

This entire project was built 100% on a mobile phone using Replit.
Despite constraints, it demonstrates that Membit enables lightweight yet powerful integrations.


---

🏁 Credits

Developed by Mettzy_
Submission for Membit Half-Hackathon 2025

> Vision:
“From raw social data to actionable context — directly inside chat.”



