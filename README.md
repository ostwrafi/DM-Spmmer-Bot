# DM‑Spmmer‑Bot 🤖

A simple Discord bot (Python + Go) designed to send bulk direct messages (DMs) — for testing, automation, or notifications.  
⚠️ **Intended for educational use only. Misuse may violate Discord’s Terms of Service.**

---

## Features

- ✅ Bulk DM sending via Python
- ⚙️ High-performance messaging through Go shared library
- 🐍 Python + Go integration for speed and flexibility

---

## Prerequisites

Make sure you have the following installed:

- Python 3.8+  
- Git  
- Go (for building the `spammer.so` shared library)  
- GCC (for c-shared build mode)  
- Docker & Docker Compose (optional)

---

## 📥 Installation

```bash
git clone https://github.com/ostwrafi/DM-Spmmer-Bot.git
cd DM-Spmmer-Bot
```

1. Copy `.env.example` to `.env`, then edit:
   ```env
   DISCORD_TOKEN=your_bot_token_here
   ```
2. Add your target tokens in `tokens.txt`, one per line.

---

## ⚙️ Build

### 🐳 Using Docker:

```bash
docker compose build
docker compose up -d
```

### ❌ Without Docker:

1. (Optional) Build Go shared library:
   ```bash
   cd go_spammer
   go build -o ../shared/spammer.so -buildmode=c-shared main.go
   cd ..
   ```
2. Install Python dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the bot:
   ```bash
   python main.py
   ```

---

## 🚀 Usage

- Place user IDs or Discord tokens in `tokens.txt`.
- Configure any settings via `.env`.
- Run the bot as shown above.
- For performance, ensure `spammer.so` is present in `shared/`.

---

## 🗂 Project Structure

```
DM-Spmmer-Bot/
├── go_spammer/        # Go code for spammer.so
├── shared/            # Contains the built spammer.so
├── main.py            # Python entrypoint
├── requirements.txt
├── tokens.txt         # Input targets
├── .env.example
├── docker-compose.yml
└── README.md
```

---

## ⚠️ Warning & Disclaimer

This bot is provided **for educational and GDPR-compliant testing purposes only**. Misuse (e.g. spamming real users) of this tool:

- May breach Discord’s Terms of Service  
- May lead to suspension or banning of your accounts

**Use responsibly!**

---

## 🔧 Contributing

Contributions are welcome! To contribute:

1. Fork the repo  
2. Create a new branch (`git checkout -b fix/feature`)  
3. Commit your changes (`git commit -m "Add description"`)  
4. Push (`git push origin fix/feature`)  
5. Open a Pull Request — improvements appreciated!

---

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE) for details.
