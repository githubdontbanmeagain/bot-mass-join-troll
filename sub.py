import discord, threading, os, argparse, time
from discord.ext import commands

intents=discord.Intents.default()
intents.message_content=True
intents.members=True

bot=commands.Bot(command_prefix="!", intents=intents, help_command=None)

message="you just got trolled!"
amount=5

parser=argparse.ArgumentParser()
parser.add_argument("-t", "--token")
token=parser.parse_args().token

@bot.listen("on_member_join")
async def dm(member):
    if not member.bot:
        for x in range(amount):
            await member.send(message)
            print(f"Sent message to {member.name}#{member.discriminator}")

if __name__ == "__main__":
    bot.run(token)