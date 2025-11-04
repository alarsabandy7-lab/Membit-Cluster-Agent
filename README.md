# 🤖 Context Agent - Membit Hackathon Submission

**Project by: Mettzy_

---

### 💡 Project Description 

This is an advanced **Data Intelligence Agent** built for Discord, leveraging the Membit API to bring real-time social context directly to the user's chat.

The agent transforms general search inquiries into "Deep Hunts," providing users with not only data trends but also specific, relevant source material.

### 🔥 Key Features and Implementation (Fitur Utama & Implementasi)

| Feature | Implementation Details |
| :--- | :--- |
| **Deep Hunt (`!hunt <topic>`)** | The bot executes a multi-step query: it first calls `v1/clusters/search` for trends, and then calls `v1/posts/search` for *specific content* relevant to each found cluster. This ensures highly contextual results. |
| **Dynamic Sentiment Analysis** | The result Embeds automatically change color (Red/Green/Blue) based on keywords (e.g., "scam," "win," "controversy") found in the data, giving users an immediate context/risk level. |
| **Clean UI & Traceability** | Results are displayed in clean Discord Embeds, with all titles and footers professionalized. Crucially, each finding includes a clickable link to the original source post. |
| **Bot Presence** | Displays the status `Watching !help for info` for improved professionalism. |

### 🛠️ Technical Stack (Tumpukan Teknologi)

* **Language:** Python 3+
* **Libraries:** `discord.py`, `requests` (for API calls)
* **Platform:** Deployed on Replit

### 🥇 The Story Behind the Build

This entire project, including all coding, debugging, and testing of the dual-API workflow, was executed **100% using a mobile phone** and the Replit platform. This demonstrates the high accessibility and power of the Membit ecosystem.

### 📜 How to Use

1.  **`!help`**: Displays the clean help menu.
2.  **`!hunt <search_term>`**: Performs a Deep Hunt.
    * Example: `!hunt airdrop`
    * Example: `!hunt band protocol`

---
*Thank you for reviewing my submission.*
