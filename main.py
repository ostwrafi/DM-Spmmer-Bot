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



