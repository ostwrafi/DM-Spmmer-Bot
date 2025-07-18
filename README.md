Repository: ostwrafi/dm-spmmer-bot
Files analyzed: 4

Estimated tokens: 1.7k

Directory structure:
└── ostwrafi-dm-spmmer-bot/
    ├── README.md
    ├── main.py
    ├── start.bat
    └── tokens.txt


================================================
FILE: README.md
================================================
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
install all requirements file with pip install 
```bash
git clone https://github.com/ostwrafi/DM-Spmmer-Bot.git
cd DM-Spmmer-
python main.py
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
├── tokens.txt         # Input token
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



================================================
FILE: main.py
================================================
import discord
import os
import asyncio
import time
from colorama import Fore
from pystyle import Colors, Colorate


if os.path.exists('tokens.txt'):
    with open('tokens.txt', 'r') as file:
        tokens = [line.strip() for line in file.readlines()]
    
    if not tokens:
        print(Colorate.Horizontal(Colors.red_to_white,"You need to add bot tokens."))
        time.sleep(5)
        exit()  
else:
    print(Colorate.Horizontal(Colors.red_to_white,"The tokens.txt file does not exist"))
    time.sleep(5)
    exit()
os.system('title ^| Nur Mohammad Rafi ^| Dm Spammer ^|')
os.system("mode con: cols=80 lines=20")
async def send_message(bot_token, user_id, message, count):
    intents = discord.Intents.default()
    intents.message_content = True 
    
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        try:
            user = await client.fetch_user(user_id)
            for _ in range(count):
                await user.send(message)
                print(Colorate.Horizontal(Colors.green_to_cyan,f" [+] Sent message successfully to user {user_id}"))
        except Exception as e:
            print(Fore.RED + f" [-] Failed to send message to user {user_id}: {e}")
        await client.close()

    try:
        await client.start(bot_token)
    except Exception:
        pass  


async def send_channel_message(bot_token, channel_id, message, count):
    intents = discord.Intents.default()
    intents.message_content = True
    
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        try:
            channel = client.get_channel(channel_id)
            for _ in range(count):
                await channel.send(message)
                print(Colorate.Horizontal(Colors.green_to_cyan,f" [+] Sent message successfully to channel {channel_id}"))
        except Exception as e:
            print(Fore.RED + f" [-] Failed to send message to channel {channel_id}: {e}")
        await client.close()

    try:
        await client.start(bot_token)
    except Exception:
        pass 


async def main():
    while True:
        print(Colorate.Horizontal(Colors.green_to_cyan,(r"""   
                    ██████╗░░█████╗░███████╗██╗ 
                    ██╔══██╗██╔══██╗██╔════╝██║
                    ██████╔╝███████║█████╗░░██║
                    ██╔══██╗██╔══██║██╔══╝░░██║
                    ██║░░██║██║░░██║██║░░░░░██║
                    ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
                                              """)))
        print()
        choice = input(Colorate.Horizontal(Colors.green_to_cyan,(" [$] U,C>> ")))

        if choice == 'u':
            user_id = int(input(Colorate.Horizontal(Colors.green_to_cyan,(" [$] Enter the user ID >> "))))
            message = input(Colorate.Horizontal(Colors.green_to_cyan,(" [$] Enter the message >> ")))
            count = int(input(Colorate.Horizontal(Colors.green_to_cyan,(" [$] Enter the number of messages to send >> "))))
            tasks = [send_message(token, user_id, message, count) for token in tokens]

        elif choice == 'c':
            channel_id = int(input(Colorate.Horizontal(Colors.green_to_cyan(" [$] Enter the channel ID >> "))))
            message = input(Colorate.Horizontal(Colors.green_to_cyan,(" [$] Enter the message >>")))
            count = int(input(Colorate.Horizontal(Colors.green_to_cyan(" [$] Enter the number of messages to send >> "))))
            tasks = [send_channel_message(token, channel_id, message, count) for token in tokens]

        else:
            print(Fore.RED + "Invalid choice.")
            continue


        await asyncio.gather(*tasks)


        print(Colorate.Horizontal(Colors.green_to_cyan,"\n [$] Spamming Complete Returing in 5 seconds!"))
        time.sleep(5)

        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    asyncio.run(main())






================================================
FILE: start.bat
================================================
python main.py
cls


================================================
FILE: tokens.txt
================================================
Token Here

