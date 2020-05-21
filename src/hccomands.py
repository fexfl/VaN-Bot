# This file features silly commands, do not judge!
from discord.ext import commands
import random


@commands.command()
async def penis(ctx):
    penis_variable = random.randint(0, 1)
    if penis_variable == 1:
        await ctx.send('Your penis is big')
    else:
        await ctx.send('Your penis is small')


@commands.command()
async def penis_l(ctx):
    rand_var = random.randint(1, 10)
    string_middle = ''
    for i in range(rand_var):
        string_middle += '='
    await ctx.send('8'+string_middle+'>')


@commands.command()
async def fufu(ctx):
    await ctx.send('https://i.ytimg.com/vi/m2GYLDZkzF0/hqdefault.jpg')


@commands.command()
async def build(ctx, arg):
    if arg == Jhin || jhin:
        jhinbuild = 'Jhin 10.10 Core Build: \n Stormrazor \n Infinity Edge \n Rapid Firecannon \n ---------------------------------------- \n Boots: Swiftness \n Keystone: Fleet Footwork'
        await ctx.send(Jhinbuild)
    if arg == Evelynn || evelynn:
        evelynnbuild = "Evelynn 10.10 Core Build: \n Enchantment: Runic Echoes \n Mejai's Soulstealer \n Lich Bane \n ---------------------------------------- \n Sorcerer's Shoes \n Keystone: Electocute"
    if arg == Irelia || irelia:
        ireliabuild = "Irelia 10.10 Core Build: \n Blade of the Ruined King \n Trinity Force (or Black Cleaver for Sinners) \n Sterak's Gage \n ---------------------------------------- \n Mercury's Treads \n Keystone: Conqueror/Press the Attack"
        
    
commands = [penis, penis_l, fufu, buildjhin]
