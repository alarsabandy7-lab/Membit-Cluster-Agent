🧠 Membit Context Agent

    

Mettzy_ — Context Agent for the Membit Half‑Hackathon

A lightweight, mobile-first Discord bot that performs Deep Hunts using Membit’s MCP / REST APIs and (optionally) Gemini for summarized AI insights. Built and iterated primarily on mobile (Replit). This repo contains the code, docs, and proofs used for the hackathon submission.


---

🚀 Project Overview

The agent turns plain queries into actionable context by combining:

v1/clusters/search — finds topical clusters and summaries

v1/posts/search — fetches example source posts

(Optional) Gemini — produces a concise human-style insight


Primary goals:

Demonstrate how real‑time social data can feed AI agents.

Provide a production-friendly, rate-limit-aware implementation that works with limited keys.

Ship a clear roadmap for MCP & deeper integration.



---

⚙️ Features

!hunt <keyword> — Deep Hunt (clusters + top related posts).

!trend <keyword> — Quick trend scan (positive vs risk indicators).

!analyze <text> — (Optional) Gemini sentiment analysis.

!whatis <term> — Short definition via Gemini.

!risk <text> — Local heuristic risk evaluation (keyword based).

!mcp <method[:payload]> — Safe MCP sandbox calls (read-only, heuristic helpers).


Embeds are color-coded (green / blue / red) based on heuristics to give instant risk/opp context.


---

🧩 System Architecture (high level)

User (Discord)
   ↓  (!hunt)
Membit API Layer
  ├─ /clusters/search
  └─ /posts/search
   ↓
Local Context Processor (cleaning, heuristics)
   ↓
(Optional) Gemini AI (1 call per hunt to reduce rate usage)
   ↓
Discord Embed Generator (color-coded)

Notes:

AI calls are minimized to avoid 429s and safety blocks.

MCP is simulated / sandboxed in the repository to demonstrate safe MCP-style interactions without exposing privileged operations.



---

🛠️ Tech stack

Python 3.10+

discord.py

aiohttp for async HTTP

google-generativeai (optional — Gemini)

python-dotenv for config



---

🧭 Quick Start — Install & Run

> Copy-paste box (works in Linux / macOS / Replit terminal). Modify .env with your keys.



# 1) Create & activate venv (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate

# 2) Install dependencies
pip install -U discord.py aiohttp google-generativeai python-dotenv

# 3) Create a .env file and add keys (example)
cat > .env <<EOF
DISCORD_TOKEN=your_discord_bot_token
MEMBIT_API_KEY=your_membit_key
GEMINI_API_KEY=your_gemini_key  # optional; leave blank to disable AI features
COOLDOWN_SECONDS=12
EOF

# 4) Run the bot
python main.py


---

✅ Environment Variables

DISCORD_TOKEN — required. Bot token.

MEMBIT_API_KEY — required. Membit API key.

GEMINI_API_KEY — optional. If provided, AI features enable.

COOLDOWN_SECONDS — optional. Per-user cooldown for rate-limiting commands.



---

📚 Usage (commands)

!help — show available commands

!hunt <keyword> — run Deep Hunt (clusters + sample posts + AI summary if available)

!trend <keyword> — quick trend scan

!analyze <text> — ask AI for sentiment (Gemini required)

!whatis <term> — quick definition (Gemini required)

!risk <text> — local heuristic risk scan (no AI needed)

!mcp <method[:payload]> — safe MCP sandbox (e.g. list_capabilities, cluster_risk:<short text>)



---

🔒 Safety & Limitations

Gemini safety: some prompts (financial advice, token price predictions) may be blocked; the bot handles "empty parts" and safety blocks gracefully.

Rate limits: the implementation minimizes AI calls (one AI call per hunt) and batches Membit queries to avoid hitting rate limits.

MCP behavior: the repo provides a sandboxed MCP (read-only heuristics). It does not call or execute privileged MCP commands — this keeps the hackathon submission safe and portable.



---

📁 Repo structure (recommended)

/ (root)
├─ main.py            # main bot implementation (async aiohttp + discord.py)
├─ README.md          # this file
├─ .env.example       # example env values
├─ proofs/            # screenshots used to demonstrate functionality
└─ LICENSE


---

🛠️ Development Notes & Tips

When developing on mobile/Replit, ensure proper SSL support in your environment. Some Replit instances require custom SSL tweaks.

If Gemini returns empty or SAFETY, rely on the local heuristic fallback (the bot already does this).

For MCP-style features, prefer read-only utilities that transform cluster data into safe metadata (risk score, short summary) instead of executing actions.



---

👥 Judges Summary (one-liner for the hackathon)

Membit Cluster Agent — a mobile-built, production-aware Discord prototype that demonstrates real-time data → human-ready context with a clear path to MCP-powered AI fusion.


---

📝 License

This repository is licensed under the MIT License — see LICENSE for full text.


---

❤️ Contributing

PRs and issues are welcome. If you want to help, try:

improving tests and edge-case handling for rate limits

adding unit tests for the heuristic risk engine

improving prompt designs for Gemini (optional keys required)



---

If you want, I can also:

generate a minimal .env.example file,

create the LICENSE (MIT) file,

produce a compact judges-ready submission (English).


Tell me which one to add next and I’ll update the README accordingly.
Clusterlusterluster
