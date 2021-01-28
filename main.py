import os
import random
import discord
import csv
import sys
import decimal
import pandas as pd
import aiohttp
import textwrap
import asyncio
import json
import requests
from requests.auth import HTTPBasicAuth
import pickle

from discord.ext import commands

admins = [256247035265548298]


msglist = []

class upgrades:
    def __init__(self, ctx):

        self.ctx = ctx

        with open(f'upgrades/auto.txt', 'r') as file:
            alldata = file.readlines()
            self.hasAuto = str(self.ctx.author.id) in str(alldata)
        
        with open(f'upgrades/auto1.txt', 'r') as file:
            alldata = file.readlines()
            self.hasAuto1 = str(self.ctx.author.id) in str(alldata)
        
        with open(f'upgrades/auto2.txt', 'r') as file:
            alldata = file.readlines()
            self.hasAuto2 = str(self.ctx.author.id) in str(alldata)
        
        with open(f'upgrades/bulk.txt', 'r') as file:
            alldata = file.readlines()
            self.hasBulk = str(self.ctx.author.id) in str(alldata)
    
    def give(self, role):
        with open(f'upgrades/{role}.txt', 'a') as file:
            file.write(f'\n{str(self.ctx.author.id)}')

TOKEN = 'put bot token here'

with open('prefix.txt', 'r') as pfx:
    prefix = pfx.readline()
    print('The prefix is', prefix)


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=prefix, help_command=None)

content = 0

rarechannel = 784126414956920893

nutcmds = True



autocooldown = []
async def opencase(ctx, auto):
    
    global autocooldown
    
    
    
    if auto and not upgrades(ctx).hasAuto:
        await ctx.send('❌ You must acquire the automatic case opening upgrade before you can use this command')
        return
    
    opening = True

    
    
    if autocooldown.count(ctx.author.id) == 0:
        autocooldown.append(ctx.author.id)
    else:
        if auto:
            print(autocooldown)
            await ctx.send('❌ Your monkeys are already opening cases.')
            return
    
    async def contopen():
        try:
            if ctx.channel.id != 785229090366029854 and ctx.channel.id != 783841388806406174 and ctx.channel.id != 784142409038561330:
                await ctx.send('❌ You can only open cases in <#785229090366029854>, <#783841388806406174>, or <#784142409038561330>')
                return True
            #output(ctx)

            try:
                with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                    pass
            except:
                newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
                with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                    file.writelines(newdata)
            

            with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                alldata = file.readlines()
            
            cases = int(alldata[2])

            testingtimelol = False

            if cases == 0:
                if auto:
                    await ctx.send(f'{ctx.author.mention} Your monkeys have finished opening cases.')
                else:
                    await ctx.send('You are out of cases. You can buy more at the store.')
                return True
            if cases > 0 or testingtimelol:
                cases -= 1
                alldata[2] = f'{cases}\n'
                with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                    file.writelines(alldata)

            
                #generate number
                probability = random.randrange(0, 383)

                rare = 0

                #probability = 191

                
                loop = 0

                colors = [0xffffff, 0x0099cc, 0x0033cc, 0x6600cc, 0xff00ff, 0xff0000, 0xffcc00]

                

                #get rarity, remove unnessesary characters, skin name, and define embed with colors
                if probability < 100:
                    rarity = 'consumer'
                    with open('skins_consumer.csv') as f:
                        reader = csv.reader(f)
                        chosen_skin = random.choice(list(reader))
                        chosen_skin = str(chosen_skin)
                        chosen_skin = chosen_skin.replace("'",'')
                        chosen_skin = chosen_skin.replace("[",'')
                        chosen_skin = chosen_skin.replace("]",'')
                    
                    np = random.randrange(30,500)


                    skin_name = chosen_skin
                    skin_name = skin_name.replace(".png",'')


                    
                    colournum = 0
                    em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour=colors[colournum])    
                elif probability < 200:
                    rarity = 'industrial'
                    with open(f'{rarity}.csv') as f:
                        reader = csv.reader(f)
                        chosen_skin = random.choice(list(reader))
                        chosen_skin = str(chosen_skin)
                        chosen_skin = chosen_skin.replace("'",'')
                        chosen_skin = chosen_skin.replace("[",'')
                        chosen_skin = chosen_skin.replace("]",'')

                    np = random.randrange(30,500)


                    skin_name = chosen_skin
                    skin_name = skin_name.replace(".png",'')


                    
                    colournum = 1
                    em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
                elif probability < 290:
                    rarity = 'Mil-Spec'
                    with open(f'{rarity}.csv') as f:
                        reader = csv.reader(f)
                        chosen_skin = random.choice(list(reader))
                        chosen_skin = str(chosen_skin)
                        chosen_skin = chosen_skin.replace("'",'')
                        chosen_skin = chosen_skin.replace("[",'')
                        chosen_skin = chosen_skin.replace("]",'')

                    np = random.randrange(300,1000)

                    skin_name = chosen_skin
                    skin_name = skin_name.replace(".png",'')


                    colournum = 2
                    em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
                    
                elif probability < 340:
                    rarity = 'restricted'
                    with open(f'{rarity}.csv') as f:
                        reader = csv.reader(f)
                        chosen_skin = random.choice(list(reader))
                        chosen_skin = str(chosen_skin)
                        chosen_skin = chosen_skin.replace("'",'')
                        chosen_skin = chosen_skin.replace("[",'')
                        chosen_skin = chosen_skin.replace("]",'')


                    skin_name = chosen_skin
                    skin_name = skin_name.replace(".png",'')


                    colournum = 3
                    em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
                    
                    np = random.randrange(700,2000)
                elif probability < 364:
                    rarity = 'Classified'
                    with open(f'{rarity}.csv') as f:
                        reader = csv.reader(f)
                        chosen_skin = random.choice(list(reader))
                        chosen_skin = str(chosen_skin)
                        chosen_skin = chosen_skin.replace("'",'')
                        chosen_skin = chosen_skin.replace("[",'')
                        chosen_skin = chosen_skin.replace("]",'')


                    skin_name = chosen_skin
                    skin_name = skin_name.replace(".png",'')


                    colournum = 4
                    em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
                    
                    np = random.randrange(1000,10000)

                elif probability < 382:
                    rarity = 'Covert'
                    with open(f'{rarity}.csv') as f:
                        reader = csv.reader(f)
                        chosen_skin = random.choice(list(reader))
                        chosen_skin = str(chosen_skin)
                        chosen_skin = chosen_skin.replace("'",'')
                        chosen_skin = chosen_skin.replace("[",'')
                        chosen_skin = chosen_skin.replace("]",'')


                    skin_name = chosen_skin
                    skin_name = skin_name.replace(".png",'')


                    colournum = 5
                    em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
                    
                    np = random.randrange(5000,30000)

                elif probability < 383:
                    rarity = 'Knife'
                    with open(f'{rarity}.csv') as f:
                        reader = csv.reader(f)
                        chosen_skin = random.choice(list(reader))
                        chosen_skin = str(chosen_skin)
                        chosen_skin = chosen_skin.replace("'",'')
                        chosen_skin = chosen_skin.replace("[",'')
                        chosen_skin = chosen_skin.replace("]",'')
                    
                    if random.randrange(1,20) == 15:
                        np = random.randrange(30000,1000000)
                    else:
                        np = random.randrange(30000,300000)


                    skin_name = chosen_skin
                    skin_name = skin_name.replace(".png",'')


                    
                    colournum = 6
                    em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
                else:
                    pass


                
                

                price = 'No Price Available'


                #get price from file
                try:
                    with open('fullprice.csv', 'r') as f:
                        reader = csv.reader(f)
                        for i, row in enumerate(reader):
                            for j, column in enumerate(row):
                                if skin_name in column:
                                    price = row[1]
                except:
                    price = np

                if price == 'No Price Available':
                    price = np

                price = str(price)

                price = price.replace(',','')

                price = int(price)

                #generate float and format price
                try:
                    fl = random.randrange(0, 800000)

                    finalfl = decimal.Decimal(fl)/1000000

                    prfl = 1 - finalfl

                    prfl = prfl * 1000000


                    price = int(price)
                    price= price * 2.5
                    price = int(str(str(price).split('.', 1)[0]))
                    price= price * prfl
                    price = decimal.Decimal(price)/100000000
                    price = round(price, 2)
                    price = str("${:,.2f}".format(price))
                    price = str(f'{price}')
                except:
                    pass
                else:
                    pass
                

                #add fields
                em.add_field(name="Rarity:", value=rarity, inline=False)
                em.add_field(name="Price:", value=price, inline=False)
                em.add_field(name="Wear:", value=finalfl, inline=False)
                em.add_field(name="Cases left:", value=cases, inline=False)
                if not auto:
                    await ctx.send(embed=em, file=discord.File(f'{rarity}/{chosen_skin}'))
                #await ctx.send(file=discord.File(f'{rarity}/{chosen_skin}'))
                
                price = price.replace(',','')

                #price integer for storage
                if price != "No Price Available":
                    intprice = price.replace(',','')
                    intprice = intprice.replace('.','')
                    intprice = intprice.replace('$','')
                    intprice  = int(intprice)
                    if intprice > 30000:
                        rare = 1
                

                prettyprice = formatprice(intprice)


                #rare skin in rare skin channel
                if rare == 1:
                    chl = bot.get_channel(rarechannel)
                    await chl.send(f'{ctx.author.display_name} got a {rarity} {skin_name} worth {prettyprice} in <#{ctx.message.channel.id}>', embed=em, file=discord.File(f'{rarity}/{chosen_skin}'))
                
                if rare == 1 and auto:
                    await ctx.send(embed=em, file=discord.File(f'{rarity}/{chosen_skin}'))

                #save data

                #setup file
                try:
                    with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
                        pass
                except:
                    newdata = ['0\n','0\n','0\n','0\n','0\n','0\n','0\n','0\n']
                    with open(f'data/{str(ctx.author.id)}.txt', 'w') as file:
                        file.writelines(newdata)
                else:

                    #add earnings to bank file
                    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                        newearnings = file.readlines()



                    try:
                        newearnings[0] = f'{int(newearnings[0]) + intprice}\n'
                        newearnings[1] = f'{int(newearnings[1]) + intprice}\n'
                    except:
                        print('No Price')
                        return True

                    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                        file.writelines(newearnings)


                    with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
                        totalwinnings = file.readlines()



                    try:
                        totalwinnings[0] = f'{int(totalwinnings[0]) + intprice}\n'
                    except:
                        print('No Price')
                        return True

                    with open(f'data/{str(ctx.author.id)}.txt', 'w') as file:
                        file.writelines(totalwinnings)





                    with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
                        mostvaluable = file.readlines()


                    if intprice > int(mostvaluable[1]):
                        mostvaluable[1] = f'{str(intprice)}\n'

                        with open(f'data/{str(ctx.author.id)}.txt', 'w') as file:
                            file.writelines(mostvaluable)

                        with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
                            storedat = file.readlines()

                        storedat[2] = str(f'{rarity}\n')
                        storedat[3] = str(f'{skin_name}\n')
                        storedat[4] = str(f'{chosen_skin}\n')
                        storedat[5] = str(f'{finalfl}\n')
                        storedat[7] = str(f'{colournum}\n')

                        with open(f'data/{str(ctx.author.id)}.txt', 'w') as file:
                            file.writelines(storedat)
                    
                    with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
                        totalcases = file.readlines()

                    totalcases[6] = f'{int(totalcases[6]) + 1}\n'
                    
                    with open(f'data/{str(ctx.author.id)}.txt', 'w') as file:
                        file.writelines(totalcases)
                    
                    return False
        except:
            pass

    if auto:
        await ctx.send("✅ We've dispatched a team of highly trained monkeys to open all of your cases and get your earnings to you as quickly as possible. (Case opening is headless to avoid rate limiting issues, but rare cases will still be shown)")

    

    if upgrades(ctx).hasAuto1:
        hasAuto1 = True
    else:
        hasAuto1 = False


    if upgrades(ctx).hasAuto2:
        hasAuto2 = True
    else:
        hasAuto2 = False

    if not auto:
        await contopen()

    elif hasAuto1 and not hasAuto2:
        while opening:
            await asyncio.sleep(1)
            if await contopen():
                break
    
    elif hasAuto2:
        while opening:
            await asyncio.sleep(0.01)
            if await contopen():
                break

    elif auto:
        while opening:
            await asyncio.sleep(3)
            if await contopen():
                break
    try:
        autocooldown.remove(ctx.author.id)
    except:
        pass
        


def balance(ctx):
    try:
        with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
            pass
    except:
        newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
        with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(newdata)

    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    usrbalance = alldata[0]
    return(int(usrbalance))


def writebalance(ctx, newbalance):
    try:
        with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
            pass
    except:
        newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
        with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(newdata)

    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    alldata[0] = f'{newbalance}\n'

    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(alldata)


def addbalance(ctx, newbalance):
    try:
        with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
            pass
    except:
        newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
        with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(newdata)

    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    alldata[0] = f'{int(alldata[0]) + newbalance}\n'
    alldata[1] = f'{int(alldata[1]) + newbalance}\n'

    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(alldata)

def subtractbalance(ctx, newbalance):
    try:
        with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
            pass
    except:
        newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
        with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(newdata)

    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    alldata[0] = f'{int(alldata[0]) - newbalance}\n'

    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(alldata)

def formatprice(oldprice):
    num = int(oldprice)
    num = decimal.Decimal(num)/100
    num = "${:,.2f}".format(num)
    num = str(f'{num}')
    return(num)

def output(ctx):
    print(f'Command {ctx.command.qualified_name} from {bot.get_user(ctx.author.id)} in {ctx.channel.name}')

def getbadge(ctx):
    try:
        with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
            pass
    except:
        newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
        with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(newdata)

    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    badgenum = alldata[3]
    return(int(badgenum))







@bot.event
async def on_ready():
    with open('status.txt', 'r') as pfx:
        status = pfx.readline()
    await bot.change_presence(activity=discord.Game(name=status))
    print('Status is', status)
    
    print(f'{bot.user.name} has connected to Discord!')

    with open('lastchannel.txt', 'r') as pfx:
        lastchannel = int(pfx.readline())
        channel = bot.get_channel(lastchannel)
    
    await channel.send('The bot is online!')



@bot.command(name='test')
async def test(ctx):
    output(ctx)
    
    await ctx.send('frick off and leave me alone')

@bot.command(name='autocase')
async def autocase(ctx):

    await opencase(ctx, True)

@bot.command(name='prefix')
async def prefixchange(ctx, new_pfx):
    output(ctx)

    if ctx.author.id in admins:
        if len(new_pfx) > 1:
            await ctx.send('The prefix must be only one character')
        else:

            with open('prefix.txt', 'w') as pfx:
                pfx.seek(0)
                pfx.write(new_pfx)

            with open('prefix.txt', 'r') as pfx:
                prefix = pfx.readline()
            
            bot = commands.Bot(command_prefix=prefix, help_command=None)
            print('The prefix has been changed to', prefix)
            await ctx.send('The prefix has been changed.')
    else:
        await ctx.send(f'You are not a bot administrator')

    



@bot.command(name='GameStatus')
async def statuschange(ctx, *, new_status):
    output(ctx)

    with open('status.txt', 'w') as pfx:
        pfx.truncate(0)
        pfx.seek(0)
        pfx.write(new_status)

    with open('status.txt', 'r') as pfx:
        status = pfx.readline()
    
    await bot.change_presence(activity=discord.Game(name=status))
    print('Status has been changed to', status)
    await ctx.send('Status has been changed.')



@bot.command(name='wisdom')
async def wisdom(ctx):
    output(ctx)
    with open('wisdom.csv') as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        chosen_row = str(chosen_row)
        chosen_row = chosen_row.replace("'",'')
        chosen_row = chosen_row.replace("[",'')
        chosen_row = chosen_row.replace("]",'')
        chosen_row = chosen_row.replace('"','')
        await ctx.send(chosen_row)


@bot.command(name='addwisdom')
async def addwisdom(ctx, *, newentry):
    output(ctx)
    added = 0
    with open('wisdom.csv', 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                for j, column in enumerate(row):
                    if newentry in column:
                        added = 1
    
    if added == 1:
        await ctx.send(f'That wisdom has already been added.')
    else:
        if '@' in newentry:
            await ctx.send(f'That wisdom is not allowed')
        else:
            print('received new wisdom "',newentry,'"')
            with open('wisdom.csv','a') as fd:
                fd.write(f"\n{newentry}")
            await ctx.send(f'Added wisdom "{newentry}"')



@bot.command(name='r')
async def restart(ctx):
    print('Received command to restart')
    await ctx.send('restarting...')
    print()

    with open('lastchannel.txt', 'w') as pfx:
        pfx.truncate(0)
        pfx.seek(0)
        lastchannel = str(ctx.message.channel.id)
        pfx.write(lastchannel)
    
    os.system('main.py')
    exit()


@bot.command(name='help')
async def pages(ctx):

    p1em=discord.Embed(title="General Help (Page 1/4)", description="eat dick shitass", color=0x7361ff)
    
    p1em.add_field(name="About", value="This is just a bot I made for fun on this server with some games and stuff.", inline=False)
    
    p1em.add_field(name=f"{prefix}help", value="Shows this message, use the arrow reactions to flip between pages.", inline=False)
    
    p1em.set_footer(text="Made by GoatInAHat")



    p2em=discord.Embed(title="Misc Commands (Page 2/4)", description="Random commands that don't fit any other category, but don't need a category of their own", color=0x7361ff)
    
    p2em.add_field(name=f"{prefix}GameStatus [new game status]", value="Change the bot's current in-game status to something funny", inline=False)

    p2em.add_field(name=f"{prefix}wisdom", value="With the new lauch of our crowd-sourced therapy initiative comes the wisdom command, If you are ever in need of wisdom and direction in life, simply consult the NUT.", inline=False)
    
    p2em.add_field(name=f"{prefix}addwisdom [new wisdom here]", value="Contribute to the NUT's pool of knowledge", inline=False)

    p2em.add_field(name=f"{prefix}connectfour", value="Play the classic game connect four with a friend, right in a discord channel! There is currently a $200 reward for winning, but betting on games is coming soon (or whenever I feel like implementing it, also currency is explained on the next page)", inline=False)

    p2em.add_field(name=f"{prefix}echo", value="Make the bot say something, idk it's funny sometimes if used correctly (Your message containing the command is automatically deleted right after you send it)", inline=False)

    p2em.add_field(name=f"{prefix}meme", value="memes... heh", inline=False)

    p2em.set_footer(text="Made by GoatInAHat")



    p3em=discord.Embed(title="Currency (Page 3/4)", description="The bot has a currency system. Money is passively gained for being active on the server, or can be earned through connect four or csgo cases. This money can be used to purchase more cases, buy upgrades to get money faster, purchase ranks and roles, and can be sent to other users.", color=0x7361ff)
    
    p3em.add_field(name=f"{prefix}store", value="Access the store to buy items, upgrades, and special roles.", inline=False)
    
    p3em.add_field(name=f"{prefix}bank", value="Check your current balance as well as how much total money you have earned and spent.", inline=False)

    p3em.add_field(name=f"{prefix}case", value="Open a CS:GO weapon case, purchased from the store. (Yes, this is gambling, but I have tweaked the odds so statistically you are likely to turn a profit. You start with 10 free cases.)", inline=False)

    p3em.add_field(name=f"{prefix}pay @[user] [amount]", value="Send money to another member, no questions asked about what it is for.", inline=False)

    p3em.add_field(name=f"{prefix}hitman @[user]", value="Hire a hitman to kick anyone from the server ($1,000,000)", inline=False)
    
    p3em.set_footer(text="Made by GoatInAHat")




    p4em=discord.Embed(title="Admin (Page 4/4)", description="These are commands for Council of C, for admin purposes", color=0x7361ff)
    
    p4em.add_field(name=f"{prefix}promote @[user]", value="Promote someone to Council of C", inline=False)
    
    p4em.add_field(name=f"{prefix}demote @[user]", value="Demote someone from Council of C, requires approval from one other Council of C member", inline=False)

    p4em.add_field(name=f"{prefix}votekick @[user]", value=f"Start a vote to kick someone from the server, other people vote by typing {prefix}votekick @[user] again.", inline=False)
    
    p4em.set_footer(text="Made by GoatInAHat")





    contents = [p1em, p2em, p3em, p4em]
    pages = 4
    cur_page = 1
    message = await ctx.send(embed=contents[cur_page-1])
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user.id == ctx.author.id and str(user.id) != '783766535658536981' and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=500, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(embed=contents[cur_page-1])
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(embed=contents[cur_page-1])
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            break
            # ending the loop if user doesn't react after x seconds

chosen_skin = 'none'



@bot.command(name='meme')
async def meme(ctx):
    output(ctx)
    subreddits = ['dankmemes','memes','memeeconomy']
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://www.reddit.com/r/{random.choice(subreddits)}/hot.json?sort=hot') as r:
            res = await r.json()
            post = random.randint(0, 25)
            header = res['data']['children'] [post]['data']['title']
            header = str(header)
            header = textwrap.fill(header, 38)
            embed = em = discord.Embed(title=header,description="", colour= 0xffffff)
            embed.set_image(url=res['data']['children'] [post]['data']['url'])
            await ctx.send(embed=embed)
            print('sent meme')

@bot.command(name='nuke')
async def nuke(ctx):
    output(ctx)
    if ctx.author.id in admins:
        await ctx.channel.clone(reason="none")
        await ctx.channel.delete()
    else:
        await ctx.send(f'You are not a bot administrator')

@bot.command(name='echo')
async def echo(ctx, *, content):
    output(ctx)
    if '@everyone' in content:
        await ctx.send(f'{ctx.author.mention} sucks donkey dick')
        return
    if '@here' in content:
        await ctx.send(f'{ctx.author.mention} sucks donkey dick')
        return
    await ctx.channel.purge(limit=1)
    await ctx.send(content)


#async def writedata():
    '''authordata[0] = f'{str(authorhp)}\n'
    authordata[1] = f'{str(authorslapcool)}\n'
    authordata[2] = f'{str(authorhealcool)}\n'

    slapdata[0] = f'{str(slaphp)}\n'
    slapdata[1] = f'{str(slapslapcool)}\n'
    slapdata[2] = f'{str(slaphealcool)}\n'

    with open(f'data/{author}.txt', 'w') as file:
            file.writelines(authordata)
    
    with open(f'data/{slapid}.txt', 'w') as file:
            file.writelines(slapdata)'''


gameison = False

@bot.command(name='connectfour')
async def connectfour(ctx):
    
    global gameison

    if gameison:
        await ctx.send('❌ Another game is already running')
        return
    else:
        gameison = True

    output(ctx)
    rows = 10
    columns = 10
    noColumns = 10
    noRows = 10
    winLength = 4

    def isInteger(n):
        result = True
        try:
            int(n)
            result = True
        except ValueError:
            print("That was not an Integer!")
            result = False
        return result

    def inputInLimitCheck(x,min, max):
        response = True
        if x < min:
            print("That is too low! Must be at least %d" % min)
            response = False
        elif x > max:
            print("That is too high! Cannot be higher than %d" % max)
            response = False
        return response

    def createGrid(columns, rows) :
        grid = []
        for row in range(0,rows):
            newRow = []
            for column in range(0,columns):
                newRow.append(0)
            grid.append(newRow)
        return grid

    def printGrid(aGrid) :
        topline = "|"
        #for n in range(0,len(aGrid)):
            #topline += "-" + str(n) + "-|"
        lines = ''
        for row in aGrid:
            line = "  ⠀ |  "
            for x in row:
                if (x == 0) :
                    x = "⬛️"
                elif (x == 1) :
                    x = "🔴"
                elif (x == 2) :
                    x = "🟡"
                line = line + str(x) + "  |  "
            lines += f'{line}\n'
        return lines

    def dropCoin(noColumns, grid, player, slotnum) :
        global selectedColumn
        selectedColumn =  slotnum
        if isValidCoinDrop(selectedColumn, grid)==False :
            newGrid = grid
        else :
            for x in range(1,len(grid)+1) :
                if (x==len(grid)):
                    grid[x-1][selectedColumn] = player
                    newGrid = grid
                elif (grid[x][selectedColumn]!=0):
                    grid[x-1][selectedColumn] = player
                    newGrid = grid
                    break
        return newGrid

    def isValidCoinDrop(columnNo, grid):
        result = True
        if (grid[0][columnNo]!=0) :
            print("Column is already full!")
            result = False
        return result

    def horizontalWinCheck(x,y,grid, player):
        streak = 0
        xleft = x
        xright = x + 1
        while (xleft>=0):
            if grid[y][xleft] == player:
                streak += 1
                xleft -= 1
            else:
                break
        while (xright<len(grid[0])):
            if grid[y][xright] == player:
                streak += 1
                xright += 1
            else:
                break
        return streak

    def verticalWinCheck(x,y,grid,player):
        streak = 0
        yup = y
        ydown = y + 1
        while (yup>=0):
            if grid[yup][x] == player:
                streak += 1
                yup -= 1
            else:
                break
        while (ydown<len(grid)):
            if grid[ydown][x] == player:
                streak += 1
                ydown += 1
            else:
                break
        return streak

    def NWSEWinCheck(x,y,grid,player):
        streak = 0
        yup = y
        ydown = y + 1
        xleft = x
        xright = x + 1
        while (yup>=0) and (xleft>=0):
            if grid[yup][xleft] == player:
                streak += 1
                yup -= 1
                xleft -= 1
            else:
                break
        while (ydown<len(grid)) and (xright<len(grid[0])):
            if grid[ydown][xright] == player:
                streak += 1
                ydown += 1
                xright += 1
            else:
                break
        return streak

    def NESWWinCheck(x,y,grid,player):
            streak = 1
            yup = y
            ydown = y + 1
            xleft = x - 1
            xright = x
            while (yup>=0) and (xright<len(grid[0])):
                if grid[yup][xleft] == player:
                    streak += 1
                    yup -= 1
                    xright += 1
                else:
                    break
            while (ydown<len(grid)) and (xleft>=0):
                if grid[ydown][xleft] == player:
                    streak += 1
                    ydown += 1
                    xleft -= 1
                else:
                    break
            return streak

    def winCheck(player, selectedColumn, grid, winlength):
        winner = 0
        x = selectedColumn
        y = findLastRow(selectedColumn, grid)
        win = False
        if (horizontalWinCheck(x,y, grid, player)>=winlength) :
            win = True
        elif (verticalWinCheck(x,y,grid,player)>=winlength) :
            win = True
        elif (NESWWinCheck(x,y,grid,player)>=winlength) :
            win = True
        elif (NWSEWinCheck(x,y,grid,player)>=winlength) :
            win = True
        if (win == True):
            print("Player %d Wins!" % player)
            
        return win

    def drawCheck(grid):
        result = True
        for x in grid[0]:
            if x == 0:
                result = False
                break
        if result == True:
            print("The Game is a Draw!")
            ctx.send("The Game is a Draw!")
        return result

    def findLastRow(selectedColumn, grid) :
        for n in range(0,len(grid)):
            if grid[n][selectedColumn] != 0:
                result = n
                break
        return result

    isbot = 1

    startmsg = ctx.message

    await startmsg.add_reaction("✅")

    hostid = str(ctx.author.id)

    grid = createGrid(noColumns, noRows)
    reciept = [grid, winLength]

    grid = reciept[0]
    winlength = reciept[1]
    printGrid(grid)

    confmessage = await ctx.send(f"Waiting for player to accept game...")

    def checkone(reaction, user):
        return user.id != ctx.author.id and ctx.message.id == reaction.message.id and str(user.id) != '783766535658536981'

    print('started checking reactions')

    
    try:
        reaction, user = await bot.wait_for("reaction_add", timeout=60, check=checkone)
        # waiting for a reaction to be added - times out after x seconds
        
        ('reaction received')


        if str(reaction.emoji) == "✅":
            guestid = str(user.id)


    except asyncio.TimeoutError:
        await ctx.send('❌ Player took too long to accept match')
        gameison = False
        return
        # ending the loop if user doesn't react after x seconds

    
    
    await confmessage.edit(content=f"<@!{guestid}> has accepted the match!")
    
    
    
    
    
    
    await confmessage.add_reaction("1️⃣")
    await confmessage.add_reaction("2️⃣")
    await confmessage.add_reaction("3️⃣")
    await confmessage.add_reaction("4️⃣")
    await confmessage.add_reaction("5️⃣")
    await confmessage.add_reaction("6️⃣")
    await confmessage.add_reaction("7️⃣")
    await confmessage.add_reaction("8️⃣")
    await confmessage.add_reaction("9️⃣")
    await confmessage.add_reaction("🔟")
    noColumns = len(grid[0])
    player = 2
    complete = False
    
    await confmessage.edit(content=f"<@!{hostid}>'s turn\n\n  ⠀ |  1️⃣  |  2️⃣  |  3️⃣  |  4️⃣  |  5️⃣  |  6️⃣  |  7️⃣  |  8️⃣  |  9️⃣  |  🔟  |\n{printGrid(grid)}")


    isbot = 1
    
    currentplayer  = hostid
    
    loop = 1

    while(complete==False) :
        
        try:

            
            while True:
                try:
                    
                    loop += 1

                    if loop > 100:
                        await ctx.send('Loop length exceeded, quitting game')
                        gameison = False
                        return
                    reaction, user = await bot.wait_for("reaction_add", timeout=120)
                    # waiting for a reaction to be added - times out after x seconds

                    #if isbot == 1:
                        #isbot = 0
                        #continue
                    if str(user.id) != str(currentplayer):
                        await ctx.send('❌ It is not your turn')
                        await confmessage.remove_reaction(reaction, user)
                        continue

                    if str(reaction.emoji) == "1️⃣":
                        usermove = 0
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "2️⃣":
                        usermove = 1
                        await confmessage.remove_reaction(reaction, user)
                        break
                        
                    elif str(reaction.emoji) == "3️⃣":
                        usermove = 2
                        await confmessage.remove_reaction(reaction, user)
                        break
                    
                    elif str(reaction.emoji) == "4️⃣":
                        usermove = 3
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "5️⃣":
                        usermove = 4
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "6️⃣":
                        usermove = 5
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "7️⃣":
                        usermove = 6
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "8️⃣":
                        usermove = 7
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "9️⃣":
                        usermove = 8
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "🔟":
                        usermove = 9
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "🔄":
                        await confmessage.remove_reaction(reaction, user)
                        continue

                        
                except asyncio.TimeoutError:
                    await ctx.send('❌ Player took too long to make a move')
                    break
                    # ending the loop if user doesn't react after x seconds


            
            grid = dropCoin(noColumns, grid, player, usermove)
            complete = winCheck(player, selectedColumn, grid, winlength)
            
            player = (player%2)+1
            if player == 1:
                currentplayer = guestid
                pturn = f"<@!{guestid}>'s turn"
            else:
                currentplayer = hostid
                pturn = f"<@!{hostid}>'s turn"
            
            if (complete==True):
                if player == 1:
                    await ctx.send(f"<@!{hostid}> won $200!")
                    await confmessage.edit(content=f"<@!{hostid}> won against <@!{guestid}>!\n\n  ⠀ |  1️⃣  |  2️⃣  |  3️⃣  |  4️⃣  |  5️⃣  |  6️⃣  |  7️⃣  |  8️⃣  |  9️⃣  |  🔟  |\n{printGrid(grid)}")
                    gameison = False
                    try:
                        with open(f'bank/{str(hostid)}.txt', 'r') as file:
                            pass
                    except:
                        newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
                        with open(f'bank/{str(hostid)}.txt', 'w') as file:
                            file.writelines(newdata)

                    with open(f'bank/{str(hostid)}.txt', 'r') as file:
                        alldata = file.readlines()
                    
                    alldata[0] = f'{int(alldata[0]) + 20000}\n'
                    alldata[1] = f'{int(alldata[1]) + 20000}\n'

                    with open(f'bank/{str(hostid)}.txt', 'w') as file:
                            file.writelines(alldata)
                else:
                    await ctx.send(f"<@!{guestid}> won $200!")
                    await confmessage.edit(content=f"<@!{guestid}> won against <@!{hostid}>!\n\n  ⠀ |  1️⃣  |  2️⃣  |  3️⃣  |  4️⃣  |  5️⃣  |  6️⃣  |  7️⃣  |  8️⃣  |  9️⃣  |  🔟  |\n{printGrid(grid)}")
                    try:
                        with open(f'bank/{str(guestid)}.txt', 'r') as file:
                            pass
                    except:
                        newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
                        with open(f'bank/{str(guestid)}.txt', 'w') as file:
                            file.writelines(newdata)

                    with open(f'bank/{str(guestid)}.txt', 'r') as file:
                        alldata = file.readlines()
                    
                    alldata[0] = f'{int(alldata[0]) + 20000}\n'
                    alldata[1] = f'{int(alldata[1]) + 20000}\n'

                    with open(f'bank/{str(guestid)}.txt', 'w') as file:
                            file.writelines(alldata)
                
            
            if (complete!=True):
                
                result = True
                for x in grid[0]:
                    if x == 0:
                        result = False
                        break
                if result == True:
                    await ctx.send('The Game is a Draw!')
                    gameison = False
                    pass
                
                complete = result
            
            
                topline = "|"
                #for n in range(0,len(aGrid)):
                    #topline += "-" + str(n) + "-|"
                lines = ''
                for row in grid:
                    line = "  ⠀ |  "
                    for x in row:
                        if (x == 0) :
                            x = "⬛️"
                        elif (x == 1) :
                            x = "🔴"
                        elif (x == 2) :
                            x = "🟡"
                        line = line + str(x) + "  |  "
                    lines += f'{line}\n'
                
                

                #boardem = discord.Embed(title="Connect Four", description=lines, colour= 3447003)
                await confmessage.edit(content=f"{pturn}\n\n  ⠀ |  1️⃣  |  2️⃣  |  3️⃣  |  4️⃣  |  5️⃣  |  6️⃣  |  7️⃣  |  8️⃣  |  9️⃣  |  🔟  |\n{printGrid(grid)}")
        except:
            pass
  

chosen_skin = 'none'

#case command
@bot.command(name='case')
async def case(ctx):

    await opencase(ctx, False)


       
@bot.command(name='casestats')
async def casestats(ctx):
    output(ctx)
    with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
        stats = file.readlines()
    

    colors = [0xffffff, 0x0099cc, 0x0033cc, 0x6600cc, 0xff00ff, 0xff0000, 0xffcc00]

    totalvalue = str(stats[0])
    rawtotal = int(stats[0])
    price= str(stats[1])
    rawprice = int(stats[1])
    rarity = str(stats[2])
    skin_name = str(stats[3])
    chosen_skin = str(stats[4])
    finalfl = str(stats[5])
    totalcases = str(stats[6])
    rawcases = int(stats[6])
    colournum = int(stats[7])


    price = decimal.Decimal(price)/100
    price = "${:,.2f}".format(price)
    price = str(f'{price}')


    totalvalue = decimal.Decimal(totalvalue)/100
    totalvalue = "${:,.2f}".format(totalvalue)
    totalvalue = str(f'{totalvalue}')

    luck = decimal.Decimal(rawtotal)/rawcases
    luck = str(luck)
    luck = str(luck.split('.', 1)[0])

    em2 = discord.Embed(title=f"{ctx.author}'s Case Stats",description='', colour= colors[1])
    em2.add_field(name="Total skin value", value=totalvalue, inline=False)
    em2.add_field(name="Amount of cases opened", value=totalcases, inline=False)
    em2.add_field(name="Most valueable skin", value=skin_name, inline=False)
    em2.add_field(name="Luck", value=luck, inline=False)



    em = discord.Embed(title="Most Valueable Skin⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
    
    
    
    em.add_field(name="Rarity:", value=rarity, inline=False)
    em.add_field(name="Price:", value=price, inline=False)
    em.add_field(name="Wear:", value=finalfl, inline=False)
    await ctx.send(embed=em2)
    path = str(f'{rarity}/{chosen_skin}').replace('\n','')
    await ctx.send(embed=em, file=discord.File(path))


@bot.command(name='bulkcase')
async def bulkcase(ctx, casenum):
    if not upgrades(ctx).hasBulk:
        await ctx.send('❌ You must acquire the bulk shipping upgrade before you can use this command')
        return


    casenum = int(casenum)
    usrbal = balance(ctx)
    caseprice = casenum * 1500
    caseprice = int(caseprice)
    caseprice = decimal.Decimal(caseprice)/100
    caseprice = "${:,.2f}".format(caseprice)
    caseprice = str(f'{caseprice}')

    if casenum > 0:
        if usrbal < 1500 * casenum:
            await ctx.send(f'❌ You do not have enough money ({caseprice})')
        else:
            with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                alldata = file.readlines()
            
            cases = int(alldata[2])


            cases += casenum
            alldata[2] = f'{cases}\n'
            with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                file.writelines(alldata)

            subtractbalance(ctx, 1500*casenum)
            await ctx.send(f'✅ Transaction successful! You now have {cases} case(s).')
    else:
        await ctx.send(f'❌ Invalid integer')





@bot.command(name='bank')
async def bank(ctx):
    output(ctx)
    currentbal = balance(ctx)

    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    cases = int(alldata[2])

    totalearn = int(alldata[1])
    totalspent = int(totalearn) - int(currentbal)

    em = discord.Embed(title="Bank Info", description="", colour= 3447003)

    potcases = str(currentbal/100/15).split('.')[0]
    
    em.add_field(name=f"Current Balance", value=formatprice(currentbal), inline=False)
    em.add_field(name=f"Total Earnings", value=formatprice(totalearn), inline=False)
    #em.add_field(name=f"Total Money Spent", value=formatprice(totalspent), inline=False)
    em.add_field(name=f"Inventory", value=f'Cases: {cases}\n(You can buy {potcases})', inline=False)

    await ctx.send(embed=em)

@bot.event
async def on_message(message):

    if message.content.startswith('audit'):
        print(message.author.display_name)

    addbalance(message, 250)
    if str(message.channel.id) != '788912941587628042' and str(message.channel.id) != '764239995003076640' and str(message.author) != 'Lois#4144'and str(message.channel.id) != '798986804837613568':
        try:
            channel = bot.get_channel(788912941587628042)
            attatchment = message.attachments[0].url

            await channel.send(attatchment)
            print('successfully sent in media channel')
        except IndexError:
            if 'discordapp' in str(message.content):
                await channel.send(message.content)
    if str(message.channel.id) == '798986804837613568':
        channel = bot.get_channel(798985608445296691)
        await channel.send(message.content)
    
    if balance(message) > 200000000:
        if random.randrange(1,500) == 5:
            await message.channel.send(f'{message.author.mention}, your case empire has been invaded, and you lost a significant portion of your wealth. However, all of your upgrades and purchases are still intact.')
            subtractbalance(message, int(balance(message)*0.75))
    
    '''
    if message.author.id == 461240802337751040 and '$' in message.content:
        await message.channel.send('Fuck off Frazzled no commands for you.')
    else:
    '''
    if message.content.startswith('$') and random.randrange(1,50) == 25:
        await message.send('No')
        return
        
    await bot.process_commands(message)




cooldown = []
@bot.command(name='store')
async def store(ctx):

    global cooldown

    if cooldown.count(ctx.author.id) == 0:
        cooldown.append(ctx.author.id)

        usrbal = balance(ctx)
                
        formattedbalance = formatprice(usrbal)


        em = discord.Embed(title="Store", description="Purchase items and and special roles", colour= 3447003)
        em.add_field(name=f"Current Balance:", value=formattedbalance, inline=False)
        em.add_field(name=f"🎁 - CS:GO Case ($15)", value=f'1 CS:GO weapon case. (Yes, this is gambling, but I have tweaked the odds so they are mostly fair.)', inline=False)
        
        

        check_role = discord.utils.get(ctx.guild.roles, name= '★ VIP ★')
        if check_role in ctx.author.roles:
            hasVIP = True
        else:
            hasVIP = False
            em.add_field(name=f"⭐ - VIP Access ($2000)", value=f'Grants you access to the VIP lounge as well as other perks', inline=False)


        if upgrades(ctx).hasBulk:
            hasBulk = True
        else:
            hasBulk = False
            em.add_field(name=f"📦 - Bulk Shipping Upgrade ($1500)", value=f'Unlocks the ability to buy cases in bulk ($bulkcase [number of cases])', inline=False)

        if upgrades(ctx).hasAuto:
            hasAuto = True
        else:
            hasAuto = False
            em.add_field(name=f"🐒 - Case Opening Monkeys ($12,000)", value=f'Outsource the opening of cases to an team of trained monkeys (No Refunds if unexpected monkey business occurs, the legality of this practice in your country is not guaranteed)', inline=False)


        if upgrades(ctx).hasAuto1:
            hasAuto1 = True
        else:
            hasAuto1 = False


        if upgrades(ctx).hasAuto2:
            hasAuto2 = True
        else:
            hasAuto2 = False

        if hasAuto and not hasAuto1:
            em.add_field(name=f"🤖 - Cyborg Monkeys ($60,000)", value=f'Hire robotically enhanced monkeys to work around the clock opening cases for you (Speeds up autocase by 3x)', inline=False)

        if hasAuto1 and not hasAuto2:
            em.add_field(name=f"💾 - Robot Monkey Army ($250,000)", value=f'Recruit an army of robot monkeys all opening cases for you to single-handedly start a global monkey slave trade fueled by an economy based around CSGO skins (The autocase command will work as fast as my computer can process the cases)', inline=False)

        if getbadge(ctx) == 0:
            em.add_field(name=f"<:Silver:791527610962280518> - Silver Badge ($100)", value=f'Grants you Silver badge.', inline=False)
        elif getbadge(ctx) == 1:
            em.add_field(name=f"<:Gold:791527610789396490> - Upgrade Badge to Gold ($500)", value=f'Grants you the Gold badge.', inline=False)
        elif getbadge(ctx) == 2:
            em.add_field(name=f"<:Platinum:791527610698039307> - Upgrade Badge to Platinum ($1,800)", value=f'Grants you the Platinum badge.', inline=False)
        elif getbadge(ctx) == 3:
            em.add_field(name=f"<:Mithril:791527613012639754> - Upgrade Badge to Mithril ($20,000)", value=f'Grants you the Mithril badge.', inline=False)
        elif getbadge(ctx) == 4:
            em.add_field(name=f"<:Ternion:791527612554936320> - Upgrade Badge to Ternion ($50,000)", value=f'Grants you the Ternion badge.', inline=False)

        # getting the message object for editing and reacting

        message = await ctx.send(embed = em)

        await message.add_reaction("🎁")

        if not hasVIP:
            await message.add_reaction("⭐")

        if not hasBulk:
            await message.add_reaction("📦")
        
        if not hasAuto:
            await message.add_reaction("🐒")
        
        if hasAuto and not hasAuto1:
            await message.add_reaction("🤖")
        
        if hasAuto1 and not hasAuto2:
            await message.add_reaction("💾")

        def check(reaction, user):
            return user == ctx.author
            # This makes sure nobody except the command sender can interact with the "menu"

        while True:
            
            try:
                with open(f'upgrades/bodyguard.txt', 'r') as file:
                    alldata = file.readlines()
                    hasBG = str(ctx.author.id) in str(alldata)

                if not hasBG:
                    await message.add_reaction('🕴')

                if getbadge(ctx) == 0:
                    await message.add_reaction('<:Silver:791527610962280518>')
                elif getbadge(ctx) == 1:
                    await message.add_reaction("<:Gold:791527610789396490>")
                elif getbadge(ctx) == 2:
                    await message.add_reaction("<:Platinum:791527610698039307>")
                elif getbadge(ctx) == 3:
                    await message.add_reaction("<:Mithril:791527613012639754>")
                elif getbadge(ctx) == 4:
                    await message.add_reaction("<:Ternion:791527612554936320>")
                
                if hasAuto and not hasAuto1:
                    await message.add_reaction("🤖")
                
                if hasAuto1 and not hasAuto2:
                    await message.add_reaction("💾")
                
                usrbal = balance(ctx)
                
                formattedbalance = formatprice(usrbal)

                print(formattedbalance)
                em = discord.Embed(title="Store", description="Purchase items and and special roles", colour= 3447003)
                em.add_field(name=f"Current Balance:", value=formattedbalance, inline=False)
                em.add_field(name=f"🎁 - CS:GO Case ($15)", value=f'1 CS:GO weapon case. (Yes, this is gambling, but I have tweaked the odds so they are in your favor.)', inline=False)
                
                

                if not hasVIP:
                    em.add_field(name=f"⭐ - VIP Access ($2,000)", value=f'Grants you access to the VIP lounge as well as other perks', inline=False)

                if not hasBulk:
                    em.add_field(name=f"📦 - Bulk Shipping Upgrade ($1500)", value=f'Unlocks the ability to buy cases in bulk ($bulkcase [number of cases])', inline=False)
                
                if not hasAuto:
                    em.add_field(name=f"🐒 - Case Opening Monkeys ($12,000)", value=f'Outsource the opening of cases to an army of trained monkeys (No Refunds if unexpected monkey business occurs, the legality of this practice in your country is not guaranteed)', inline=False)

                if hasAuto and not hasAuto1:
                    em.add_field(name=f"🤖 - Cyborg Monkeys ($60,000)", value=f'Hire robotically enhanced monkeys to work around the clock opening cases for you (Speeds up autocase by 3x)', inline=False)


                if hasAuto1 and not hasAuto2:
                    em.add_field(name=f"💾 - Robot Monkey Army ($250,000)", value=f'Recruit an army of robot monkeys all opening cases for you to single-handedly start a global monkey slave trade fueled by an economy based around CSGO skins (The autocase command will work as fast as my computer can process the cases)', inline=False)

                if not hasBG:
                    em.add_field(name=f"🕴 - Bodyguard ($10,000)", value=f'Hire a bodyguard to protect you from 1 attack from a hitman', inline=False)

                
                if getbadge(ctx) == 0:
                    em.add_field(name=f"<:Silver:791527610962280518> - Silver Badge ($100)", value=f'Grants you Silver badge.', inline=False)
                elif getbadge(ctx) == 1:
                    em.add_field(name=f"<:Gold:791527610789396490> - Upgrade Badge to Gold ($500)", value=f'Grants you the Gold badge.', inline=False)
                elif getbadge(ctx) == 2:
                    em.add_field(name=f"<:Platinum:791527610698039307> - Upgrade Badge to Platinum ($1,800)", value=f'Grants you the Platinum badge.', inline=False)
                elif getbadge(ctx) == 3:
                    em.add_field(name=f"<:Mithril:791527613012639754> - Upgrade Badge to Mithril ($20,000)", value=f'Grants you the Mithril badge.', inline=False)
                elif getbadge(ctx) == 4:
                    em.add_field(name=f"<:Ternion:791527612554936320> - Upgrade Badge to Ternion ($50,000)", value=f'Grants you the Ternion badge.', inline=False)


                await message.edit(embed = em)

                reaction, user = await bot.wait_for("reaction_add", timeout=120, check=check)


                if str(reaction.emoji) == "⭐":
                    usrbal = balance(ctx)
                    if usrbal < 200000:
                        await ctx.send('❌ You do not have enough money ($2,000)')
                    else:
                        role = discord.utils.get(ctx.author.guild.roles, name="★ VIP ★")
                        await ctx.author.add_roles(role)
                        hasVIP = True
                        subtractbalance(ctx, 200000)
                        await ctx.send('✅ Transaction successful! You now have VIP access.')
                    #await message.remove_reaction(reaction, user)
                    await message.clear_reaction("⭐")

                elif str(reaction.emoji) == "📦":
                    print('reaction received')
                    usrbal = balance(ctx)
                    if usrbal < 150000:
                        await ctx.send('❌ You do not have enough money ($1500)')
                    else:
                        upgrades(ctx).give('bulk')
                        hasBulk = True
                        subtractbalance(ctx, 150000)
                        await ctx.send('✅ Transaction successful! You can now use the $bulkcase command.')
                    #await message.remove_reaction(reaction, user)
                    await message.clear_reaction("📦")

                elif str(reaction.emoji) == "🐒":
                    print('reaction received')
                    usrbal = balance(ctx)
                    if usrbal < 1200000:
                        await ctx.send('❌ You do not have enough money ($12,000)')
                    else:
                        upgrades(ctx).give('auto')
                        hasAuto = True
                        subtractbalance(ctx, 1200000)
                        await ctx.send('✅ Transaction successful! You can now use the $autocase command.')
                    #await message.remove_reaction(reaction, user)
                    await message.clear_reaction("🐒")
                
                elif str(reaction.emoji) == "🤖":
                    print('reaction received')
                    usrbal = balance(ctx)
                    if usrbal < 6000000:
                        await ctx.send('❌ You do not have enough money ($60,000)')
                    else:
                        upgrades(ctx).give('auto1')
                        hasAuto1 = True
                        subtractbalance(ctx, 6000000)
                        await ctx.send('✅ Transaction successful! Your cyborg monkeys will be delivered shortly.')
                    #await message.remove_reaction(reaction, user)
                    await message.clear_reaction("🤖")
                
                elif str(reaction.emoji) == "💾":
                    print('reaction received')
                    usrbal = balance(ctx)
                    if usrbal < 25000000:
                        await ctx.send('❌ You do not have enough money ($250,000)')
                    else:
                        upgrades(ctx).give('auto2')
                        hasAuto2 = True
                        subtractbalance(ctx, 25000000)
                        await ctx.send('✅ Transaction successful! Your are well on your path to world domination.')
                    #await message.remove_reaction(reaction, user)
                    await message.clear_reaction("💾")


                elif str(reaction.emoji) == "<:Silver:791527610962280518>":
                    usrbal = balance(ctx)
                    if usrbal < 10000:
                        await ctx.send('❌ You do not have enough money ($100)')
                    else:
                        role = discord.utils.get(ctx.author.guild.roles, name="Silver")
                        await ctx.author.add_roles(role)
                        subtractbalance(ctx, 10000)
                        await ctx.send('✅ Transaction successful! You now have the Silver badge.')
                    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                        alldata = file.readlines()
                    
                    alldata[3] = f'{int(alldata[3]) + 1}\n'

                    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                            file.writelines(alldata)
                    await message.clear_reaction("<:Silver:791527610962280518>")

                elif str(reaction.emoji) == "<:Gold:791527610789396490>":
                    usrbal = balance(ctx)
                    if usrbal < 50000:
                        await ctx.send('❌ You do not have enough money ($500)')
                    else:
                        role = discord.utils.get(ctx.author.guild.roles, name="Gold")
                        await ctx.author.add_roles(role)
                        subtractbalance(ctx, 50000)
                        await ctx.send('✅ Transaction successful! You have upgraded your badge to Gold.')
                    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                        alldata = file.readlines()
                    
                    alldata[3] = f'{int(alldata[3]) + 1}\n'

                    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                            file.writelines(alldata)
                    await message.clear_reaction("<:Gold:791527610789396490>")

                elif str(reaction.emoji) == "<:Platinum:791527610698039307>":
                    usrbal = balance(ctx)
                    if usrbal < 180000:
                        await ctx.send('❌ You do not have enough money ($1,800)')
                    else:
                        role = discord.utils.get(ctx.author.guild.roles, name="Platinum")
                        await ctx.author.add_roles(role)
                        subtractbalance(ctx, 180000)
                        await ctx.send('✅ Transaction successful! You have upgraded your badge to Platinum.')
                    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                        alldata = file.readlines()
                    alldata[3] = f'{int(alldata[3]) + 1}\n'

                    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                            file.writelines(alldata)
                    await message.clear_reaction("<:Platinum:791527610698039307>")

                elif str(reaction.emoji) == "<:Mithril:791527613012639754>":
                    usrbal = balance(ctx)
                    if usrbal < 2000000:
                        await ctx.send('❌ You do not have enough money ($20,000)')
                    else:
                        role = discord.utils.get(ctx.author.guild.roles, name="Mithril")
                        await ctx.author.add_roles(role)
                        subtractbalance(ctx, 2000000)
                        await ctx.send('✅ Transaction successful! You have upgraded your badge to Mithril.')
                    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                        alldata = file.readlines()
                    alldata[3] = f'{int(alldata[3]) + 1}\n'

                    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                            file.writelines(alldata)
                    await message.clear_reaction("<:Mithril:791527613012639754>")

                elif str(reaction.emoji) == "<:Ternion:791527612554936320>":
                    usrbal = balance(ctx)
                    if usrbal < 5000000:
                        await ctx.send('❌ You do not have enough money ($50,000)')
                    else:
                        role = discord.utils.get(ctx.author.guild.roles, name="Ternion")
                        await ctx.author.add_roles(role)
                        subtractbalance(ctx, 5000000)
                        await ctx.send('✅ Transaction successful! You have upgraded your badge to Ternion.')
                    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                        alldata = file.readlines()
                    alldata[3] = f'{int(alldata[3]) + 1}\n'

                    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                            file.writelines(alldata)
                    await message.clear_reaction("<:Ternion:791527612554936320>")




                elif str(reaction.emoji) == "🕴":
                    usrbal = balance(ctx)
                    if usrbal < 1000000:
                        await ctx.send('❌ You do not have enough money ($10,000)')
                    else:
                        with open(f'upgrades/bodyguard.txt', 'a') as file:
                            file.write(f'\n{str(ctx.author.id)}')
                        subtractbalance(ctx, 1000000)
                        
                    await message.clear_reaction("🕴")




                    

                elif str(reaction.emoji) == "🎁":
                    usrbal = balance(ctx)
                    if usrbal < 1500:
                        await ctx.send('❌ You do not have enough money ($15)')
                    else:
                        with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                            alldata = file.readlines()
                        
                        cases = int(alldata[2])

                        print(cases)
                        cases += 1
                        alldata[2] = f'{cases}\n'
                        with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                            file.writelines(alldata)

                        subtractbalance(ctx, 1500)
                        await ctx.send(f'✅ Transaction successful! You now have {cases} case(s).')
                    await message.remove_reaction(reaction, user)

                else:
                    await message.remove_reaction(reaction, user)
                    # removes reactions if the user tries to go forward on the last page or
                    # backwards on the first page
            except asyncio.TimeoutError:
                break
                # ending the loop if user doesn't react after x seconds
        
        await asyncio.sleep(30)
        cooldown.remove(ctx.author.id)
    
    else:
        await ctx.send('❌ You cannot use this command again yet. You have to wait 30 seconds every time you open the store, but the old store message will still work until the cooldown is over.')


@bot.command(name='pay')
async def pay(ctx, member, amount):
    id = str(member)
    id = id.replace('<','')
    id = id.replace('@','')
    id = id.replace('!','')
    id = id.replace('>','')
    id = id.replace('&','')
    id = int(id)

    amount = amount.replace(',','')
    amount = amount.replace('$','')

    floatamount = float(amount)
    amount = floatamount * 100
    amount = int(amount)

    if amount < 1 or amount > balance(ctx):
        await ctx.send(f'❌ Invalid amount.')
        return

    if str(ctx.author.id) == str(id):
        await ctx.send(f"❌ You can't pay yourself.")
        return


    try:
        with open(f'bank/{str(id)}.txt', 'r') as file:
            pass
    except:
        await ctx.send(f'❌ User not found. If they have not sent any messages since the bot update, a file may not have been created for them.')
        return


    with open(f'bank/{str(id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    alldata[0] = f'{int(alldata[0]) + int(amount)}\n'
    alldata[1] = f'{int(alldata[1]) + int(amount)}\n'

    with open(f'bank/{str(id)}.txt', 'w') as file:
            file.writelines(alldata)

    subtractbalance(ctx, amount)

    await ctx.send(f'✅ Paid ${floatamount} to {member}')
    

@bot.command(name='add')
async def add(ctx, member, amount):
    if ctx.author.id in admins:
        id = str(member)
        id = id.replace('<','')
        id = id.replace('@','')
        id = id.replace('!','')
        id = id.replace('>','')
        id = id.replace('&','')
        id = int(id)

        amount = amount.replace(',','')
        amount = amount.replace('$','')

        floatamount = float(amount)
        amount = floatamount * 100
        amount = int(amount)

        if amount < 1:
            await ctx.send(f'❌ Invalid amount.')
            return


        try:
            with open(f'bank/{str(id)}.txt', 'r') as file:
                pass
        except:
            await ctx.send(f'❌ User not found. If they have not sent any messages since the bot update, a file may not have been created for them.')
            return
    
        with open(f'bank/{str(id)}.txt', 'r') as file:
            alldata = file.readlines()
        
        alldata[0] = f'{int(alldata[0]) + int(amount)}\n'
        alldata[1] = f'{int(alldata[1]) + int(amount)}\n'

        with open(f'bank/{str(id)}.txt', 'w') as file:
                file.writelines(alldata)
    
        await ctx.send(f'✅ Gave ${floatamount} to {member}')

    else:
        pass
        #await ctx.send(f'You are not a bot administrator')








if nutcmds:

    @bot.command(name='femboy')
    async def femboy(ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/femboy/hot.json?sort=hot') as r:
                res = await r.json()
                post = random.randint(0, 25)
                header = res['data']['children'] [post]['data']['title']
                header = str(header)
                header = textwrap.fill(header, 38)
                embed = em = discord.Embed(title=header,description="", colour= 0xffffff)
                embed.set_image(url=res['data']['children'] [post]['data']['url'])
                await ctx.send(embed=embed)

    @bot.command(name='subreddit')
    async def subreddit(ctx, subreddit):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://www.reddit.com/r/{subreddit}/hot.json?sort=hot') as r:
                res = await r.json()
                post = random.randint(0, 25)
                header = res['data']['children'] [post]['data']['title']
                header = str(header)
                header = textwrap.fill(header, 38)
                embed = em = discord.Embed(title=header,description="", colour= 0xffffff)
                embed.set_image(url=res['data']['children'] [post]['data']['url'])
                await ctx.send(embed=embed)

    @bot.command(name='CSGOstats')
    async def CSGOstats(ctx, *, id):
        await ctx.send('fetching data...')
        headers = {'TRN-Api-key': '69d87d1e-38f2-4537-87f7-a2e5d9625901'}

        response = requests.get(f"https://public-api.tracker.gg/v2/csgo/standard/profile/steam/{id}",headers=headers)

        data = json.loads(response.text)

        try:
            print(json.dumps(response.json(), indent=1))
            em = discord.Embed(title=f"CS:GO stats for {data['data']['platformInfo']['platformUserHandle']}", description="", colour= 3447003)
        except:
            await ctx.send('Could not find that user. Make sure you entered a valid Steam ID.')
        
        

        stats = data["data"]["segments"][0]["stats"]
        
        for key, item in stats.items():
            em.add_field(name=f"{item['displayName']}", value=f"{item['displayValue']} \n {item['percentile']}th Percentile", inline=False)
            #result = f"{item['displayName']}:      {item['displayValue']} \n {item['percentile']}"
        
        await ctx.send(embed=em)

    @bot.command(name='dmspam')
    async def dmspam(ctx, id, num, *, msg):
        try:
            id = str(id)
            id = id.replace('<','')
            id = id.replace('@','')
            id = id.replace('!','')
            id = id.replace('>','')
            id = id.replace('&','')
            id = int(id)
            user = bot.get_user(id)
            await ctx.send('ok')
            for i in range(int(num)):
                await asyncio.sleep(1)
                await user.send(msg)
                print('Msgs left:',(int(num) - i))
        except:
            await ctx.send('no worki')
        else:
            pass

    @bot.command(name='spam')
    async def spam(ctx, num, *, id):
        try:
                await ctx.send(id)
        except:
            await ctx.send('no worki')
        else:
            for i in range(int(num)):
                await asyncio.sleep(1)
                await ctx.send(id)


    @bot.command(name='faptime')
    async def material(ctx):
        subreddits = ['hentai','rule34','hentai4everyone','HentaiCity']
        async with aiohttp.ClientSession() as cs:
            for i in range(25):
                for subreddit in subreddits:
                    async with cs.get(f'https://www.reddit.com/r/{subreddit}/hot.json?sort=hot') as r:
                        res = await r.json()
                        post = i
                        url = res['data']['children'] [post]['data']['url']
                        endings = [".jpg", ".png"]
                        if any(x in url for x in endings) and 'imgur' not in url:
                            await ctx.send(url)
    
    @bot.command(name='faptimebutgay')
    async def faptimebutgay(ctx):
        subreddits = ['yaoi','femboys']
        async with aiohttp.ClientSession() as cs:
            for i in range(25):
                for subreddit in subreddits:
                    async with cs.get(f'https://www.reddit.com/r/{subreddit}/hot.json?sort=hot') as r:
                        res = await r.json()
                        post = i
                        url = res['data']['children'] [post]['data']['url']
                        endings = [".jpg", ".png"]
                        if any(x in url for x in endings) and 'imgur' not in url:
                            await ctx.send(url)

@bot.command(name='ppsize')
async def ppsize(ctx, member):
    if len(str(member)) != 22 and len(str(member)) != 21:
        await ctx.send('❌ Invalid user')
        return
    id = str(member)
    id = id.replace('<','')
    id = id.replace('@','')
    id = id.replace('!','')
    id = id.replace('>','')
    id = id.replace('&','')
    id = int(id)

    schlongth = id % 10

    print(schlongth)
    #<:balls:792956167995260978><:shaft:792956169429188628><:tip:792956169207414805> 
    shaftnum = int(str(schlongth/2).split('.')[0])
    
    shaft = '<:shaft:792956169429188628>' * shaftnum

    print(f"8{shaft}D")

    if schlongth < 3:
        comments = 'smol'
    elif schlongth < 7:
        comments = 'nice cock, bro'
    elif schlongth < 9:
        comments = 'damn bro'
    elif schlongth < 10:
        comments = '👀'

    usr = bot.get_user(id)

    embed = discord.Embed(title=f"{usr.display_name}'s pp",description=f"{schlongth + 1} inches\n<:balls:792956167995260978>{shaft}<:tip:792956169207414805>\n\n{comments}", color=0x9742ff)
    await ctx.send(embed=embed)

@bot.command(name='ust')
async def ust(ctx, user: discord.Member):
    if user.voice is not None:
        print('yes')

@bot.command(name='promote')
async def promote(ctx, user: discord.Member):
    check_role = discord.utils.get(ctx.guild.roles, name= 'Council of C')
    if check_role not in ctx.author.roles:
        await ctx.send('❌ Only Council of C members can promote other users to Council of C')
        return
    
    role = discord.utils.get(ctx.author.guild.roles, name="Council of C")
    await user.add_roles(role)
    await ctx.send(f'✅ {user.display_name} now has Council of C')

@bot.command(name='hitman')
async def hitman(ctx, user: discord.Member):
    with open(f'upgrades/bodyguard.txt', 'r') as file:
        alldata = file.readlines()
        hasBG = str(user.id) in str(alldata)
    
    if user.id == 782315635316490260:
        await ctx.send('No.')
        return
    
    if balance(ctx) < 100000000:
        await ctx.send('❌ You do not have enough money ($1,000,000)')
    
    elif user.voice is not None:
        await ctx.send(f"❌ You must wait until {user.display_name} isn't in voice call to assasinate them.")
    
    elif hasBG:
        await ctx.send(f'{user.display_name} survived but their himan was taken out, leaving them vulnerable to another attack.')
        infile = "upgrades/bodyguard.txt"
        outfile = "upgrades/bodyguard.txt"

        delete_list = [f"{user.id}"]
        with open(infile) as fin, open(outfile, "w+") as fout:
            for line in fin:
                for word in delete_list:
                    line = line.replace(word, "")
                fout.write(line)
        subtractbalance(ctx, 100000000)
    

    
    elif random.randrange(1,10) != 5:
        subtractbalance(ctx, 100000000)
        r_list = []
        res_list = []
        for role in user.roles:
            if str(role) != '@everyone':
                r_list.append(role)
                res_list.append(int(role.id))
        if len(r_list) == 0:
            await ctx.send('❌ That user is already dead.')
            return
        pickle.dump(res_list, open(f'member object dumps/{user.id}.p','wb'))
        await user.remove_roles(*r_list, reason=None, atomic=True)
        await ctx.send(f'✅ {user.display_name} has been taken out.')
        channel = bot.get_channel(803357135701278720)
        await channel.send(f'{user.mention}: you have been assassinated by {ctx.author.display_name}. You must wait for someone to revive you with {prefix}revive {user.mention}.')
    
    else:
        subtractbalance(ctx, 100000000)
        await ctx.send('❌ Your hitman missed. No refunds.')

@bot.command(name='revive')
async def revive(ctx, user: discord.Member):
    
    if ctx.channel.id == 803357135701278720:
        await ctx.send("❌ You can't use this command in this channel.")
        return
    
    try:
        res_list = pickle.load(open(f'member object dumps/{user.id}.p','rb'))
    except:
        await ctx.send('❌ That user does not have a file to restore roles from.')
        return
    
    for i in res_list:
        role = discord.utils.get(ctx.guild.roles, id=int(i))
        await user.add_roles(role, reason='Roles restored.', atomic=True)

    await ctx.send(f'✅ {user.display_name} has been revived.')


kicklist = {}
votedlist = {}

@bot.command(name='votekick')
async def votekick(ctx, user: discord.Member):
    check_role = discord.utils.get(ctx.guild.roles, name= 'Council of C')
    
    if user.id == 782315635316490260:
        await ctx.send('The NUT cannot be kicked.')
        return
    
    if check_role not in ctx.author.roles:
        await ctx.send('❌ Only Council of C members can vote to kick people')
        return
    
    if check_role not in user.roles:
        await ctx.send('❌ Vote kicking is only for Council of C members')
        return


    c_members = len(check_role.members)

    votes_needed = c_members - 3

    if ctx.author in votedlist: 
        if user in votedlist[ctx.author]:
            await ctx.send('❌ You have already voted.')
            return
        votedlist[ctx.author].append(user)
    else: 
        votedlist[ctx.author] = [user]
    
    

    if user in kicklist: 
        kicklist[user] += 1
    else: 
        kicklist[user] = 1
    
    await ctx.send(f'✅ Voted ({kicklist[user]}/5 votes).')

    if kicklist[user] == 5:
        await user.ban(reason=f"Vote kicked")
        votedlist[ctx.author].remove(user)
        kicklist[user] = 0
        await ctx.send(f'✅ {user.display_name} has been kicked.')



demkicklist = {}
demvotedlist = {}


@bot.command(name='demote')
async def demote(ctx, user: discord.Member):
    check_role = discord.utils.get(ctx.guild.roles, name= 'Council of C')
    if check_role not in ctx.author.roles:
        await ctx.send('❌ Only Council of C members can demote people')
        return
        

    if check_role not in user.roles:
        await ctx.send('❌ That person cannot be demoted, as they do not have Council of C')
        return


    if ctx.author in demvotedlist: 
        if user in demvotedlist[ctx.author]:
            await ctx.send(f'❌ You have already voted to demote {user.display_name}.')
            return
        demvotedlist[ctx.author].append(user)
    else: 
        demvotedlist[ctx.author] = [user]
    

    if user in demkicklist: 
        demkicklist[user] += 1
    else: 
        demkicklist[user] = 1
    
    

    if demkicklist[user] > 1:
        await user.remove_roles(check_role, reason='Demoted', atomic=True)
        await ctx.send(f'✅ {user.display_name} has been demoted.')
        demkicklist[user] = 0
        demvotedlist[ctx.author].remove(user)
    else:
        await ctx.send(f'✅ You need to wait for one other Council of C member to accept this demotion (with {prefix}demote {user.mention}).')

jkicklist = {}
jvotedlist = {}

@bot.command(name='jail')
async def jail(ctx, user: discord.Member):
    if user.id == 782315635316490260:
        await ctx.send('The NUT cannot be sent tp jail.')
        return


    if ctx.author in jvotedlist: 
        if user in jvotedlist[ctx.author]:
            await ctx.send('❌ You have already voted.')
            return
        jvotedlist[ctx.author].append(user)
    else: 
        jvotedlist[ctx.author] = [user]
    

    if user in jkicklist: 
        jkicklist[user] += 1
    else: 
        jkicklist[user] = 1
    
    await ctx.send(f'✅ Voted ({jkicklist[user]}/7 votes).')

    if jkicklist[user] == 7:
        r_list = []
        res_list = []
        for role in user.roles:
            if str(role) != '@everyone':
                r_list.append(role)
                res_list.append(int(role.id))
        
        role = discord.utils.get(ctx.author.guild.roles, name="jail")
        await user.add_roles(role)
        pickle.dump(res_list, open(f'member object dumps/{user.id}.p','wb'))
        await user.remove_roles(*r_list, reason=None, atomic=True)
        await ctx.send(f'✅ {user.display_name} has been sent to jail. BONK')
        jvotedlist[ctx.author].remove(user)
        jkicklist[user] = 0
        channel = bot.get_channel(804038846421008404)
        await channel.send(f'{user.mention}: you have sent to jail. However, someone not in jail can release you with {prefix}revive {user.mention}.')


@bot.command(name='release')
async def release(ctx, user: discord.Member):
    
    if ctx.channel.id == 804038846421008404 or ctx.channel.id == 803357135701278720:
        await ctx.send("❌ You can't use this command in this channel.")
        return
    
    try:
        res_list = pickle.load(open(f'member object dumps/{user.id}.p','rb'))
    except:
        await ctx.send('❌ That user does not have a file to restore roles from.')
        return
    await ctx.send(f'restoring roles...')
    for i in res_list:
        role = discord.utils.get(ctx.guild.roles, id=int(i))
        await user.add_roles(role, reason='Roles restored.', atomic=True)

    role = discord.utils.get(ctx.author.guild.roles, name="jail")
    await user.remove_roles(role)

    await ctx.send(f'✅ {user.display_name} has been released from jail.')


bot.run(TOKEN)
