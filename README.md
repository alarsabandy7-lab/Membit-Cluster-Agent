# 🧠 Membit Context Agent — V55 (Stable Release)

### 🚀 Overview
**Membit Context Agent** is a Discord bot powered by **Membit’s Real-Time Clusters** and **Gemini AI**, designed to deliver contextual insights about real-world social data — from crypto and tech to human behavior.

Built for the **Membit Half-Hackathon**, this project demonstrates how AI can *see beyond static data* by tapping into Membit’s living, breathing context signals.

---

### 🎯 Core Features

| Command | Description |
|----------|-------------|
| `!hunt <keyword>` | Searches Membit clusters for real-time data and generates AI-powered insights |
| `!analyze <text>` | Performs quick sentiment and context analysis |
| `!whatis <term>` | Returns concise definitions of Web3 or AI terms |
| `!trend <keyword>` | Summarizes trending topics from Membit’s real-time clusters |
| `!compare <A> vs <B>` | (Experimental) Compares two topics based on Membit data and Gemini reasoning |
| `!help` | Displays all available commands |

---

### 🧩 Architecture
```
User → Discord Bot → Membit API → Gemini AI → Contextual Insight → Discord Channel
```

Membit Context Agent acts like a **digital detective**, combining Membit’s 3,000+ real-time clusters (including 900 crypto-related) with Gemini’s reasoning to create short, analytical stories — *AI with awareness.*

---

### ⚙️ Tech Stack

- **Language:** Python 3.10+
- **Framework:** `discord.py`
- **Libraries:** `requests`, `google-generativeai`, `python-dotenv`
- **APIs:**
  - Membit API (Real-Time Cluster & Post Search)
  - Google Gemini API
- **Integration:** Discord Bot

---

### 🧱 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/membit-context-agent.git
   cd membit-context-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -U discord.py requests google-generativeai python-dotenv
   ```

3. **Create a `.env` file**
   ```
   DISCORD_TOKEN=your_discord_bot_token
   MEMBIT_API_KEY=your_membit_api_key
   GEMINI_API_KEY=your_gemini_api_key
   COOLDOWN_SECONDS=12
   ```

4. **Run the bot**
   ```bash
   python main.py
   ```

---

### 🧠 Vision
> “AI without real-world context is just prediction.  
> Membit gives it understanding.”

This project showcases why **AI must learn from real data** — not frozen datasets.  
By merging Membit’s live context streams with reasoning models, we aim to build **adaptive intelligence** that responds to evolving trends, human emotions, and market behaviors.

---

### 🎥 Demo Video
See Membit Context Agent in action:  
👉 [Watch the Demo](https://youtu.be/your-demo-link-here)

*(Replace this link with your actual YouTube or Drive demo video once ready.)*

---

### 🏆 Hackathon Relevance
✅ Uses Membit MCP / API directly  
✅ Real-world, interactive AI application  
✅ Demonstrates why “AI needs real data”  
✅ Strong storytelling and creative presentation  

---

### 💬 Example Commands
```
!hunt bitcoin
!analyze Market seems unstable lately
!whatis DeFi
!trend ethereum
!compare Solana vs Avalanche
```

---

### 🔮 Future Roadmap
- Membit Dashboard Integration  
- Context memory for trend evolution  
- Visual sentiment timeline per cluster  
- Adaptive insight threading  
- Lightweight caching for API optimization  

---

### 🔒 Notes
- Experimental commands (`!compare`) may produce variable outputs.  
- This bot **does not store user data**.  
- Outputs are AI-generated for educational and analytical purposes.

---

### 👤 Author
**@maybeitsmet**  
AI integrator | Story-driven builder | Membit Hunter  
Discord Bot Version: **V55 — Stable**

---

### 📜 License

```
MIT License

Copyright (c) 2025 maybeitsmet

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

> 🧠 *“Context isn’t just data — it’s awareness. Membit gives AI its eyes.”*  
> — Membit Context Agent (V55)
