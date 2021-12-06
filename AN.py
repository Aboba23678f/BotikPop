import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = Bot(command_prefix ='?')
bot.remove_command('help')

@bot.event
async def on_ready():
	print(f'{bot.user} is connected! Лолл')

bot.run('OTE3MDAyOTQzNDExMTM0NDk0.YayXig.vNpEjoORsk_2b3LdwZqz_8jP2hE')

