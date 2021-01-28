import os
import random
import discord
import csv
import sys
import decimal
import pandas as pd
import aiohttp
import textwrap
import requests
from requests.auth import HTTPBasicAuth
import json
import time
import asyncio

from discord.ext import commands


msglist = []

#bot token
TOKEN = 'NzgyMzE1NjM1MzE2NDkwMjYw.X8KaNg.PHoknQtRhE6aw3dybOj0xhIidYM'

#check prefix
with open('prefix.txt', 'r') as pfx:
    prefix = pfx.readline()
    print('The prefix is', prefix)


bot = commands.Bot(command_prefix=prefix, help_command=None)

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



#on ready
@bot.event
async def on_ready():
    #set status from file
    with open('status.txt', 'r') as pfx:
        status = pfx.readline()
    await bot.change_presence(activity=discord.Game(name=status))
    print('Status is', status)
    
    print(f'{bot.user.name} has connected to Discord!')
    #send message in channel that the bot was restarted in
    with open('lastchannel.txt', 'r') as pfx:
        lastchannel = int(pfx.readline())
        channel = bot.get_channel(lastchannel)
    
    await channel.send('The bot is online!')


#test command
@bot.command(name='test')
async def test(ctx):
    
    await ctx.send('fuck off and leave me alone')



@bot.command(name='prefix')
async def prefixchange(ctx, new_pfx):

    #check prefix length
    if len(new_pfx) > 1:
        await ctx.send('The prefix must be only one character')
    else:
        #if prefix is valid, write to file and set status
        with open('prefix.txt', 'w') as pfx:
            pfx.seek(0)
            pfx.write(new_pfx)

        with open('prefix.txt', 'r') as pfx:
            prefix = pfx.readline()
        
        bot = commands.Bot(command_prefix=prefix, help_command=None)
        print('The prefix has been changed to', prefix)
        await ctx.send('The prefix has been changed.')


#gamestatus command
@bot.command(name='GameStatus')
async def statuschange(ctx, *, new_status):

    #write new status to file
    with open('status.txt', 'w') as pfx:
        pfx.truncate(0)
        pfx.seek(0)
        pfx.write(new_status)

    #read status from file just to check
    with open('status.txt', 'r') as pfx:
        status = pfx.readline()
    
    await bot.change_presence(activity=discord.Game(name=status))
    print('Status has been changed to', status)
    await ctx.send('Status has been changed.')


#wisdom command
@bot.command(name='wisdom')
async def wisdom(ctx):
    #check if server is nate's server
    id = ctx.message.guild.id
    if id == 729576520196161637:
        with open('wisdom.csv') as f:
            #pick wisdom
            reader = csv.reader(f)
            chosen_row = random.choice(list(reader))
            chosen_row = str(chosen_row)
            #replace unnescesary characters 
            chosen_row = chosen_row.replace("'",'')
            chosen_row = chosen_row.replace("[",'')
            chosen_row = chosen_row.replace("]",'')
            chosen_row = chosen_row.replace('"','')
            await ctx.send(chosen_row)
    #if not, use other wisdom file
    else:
        with open('wisdom2.csv') as f:
            reader = csv.reader(f)
            chosen_row = random.choice(list(reader))
            chosen_row = str(chosen_row)
            chosen_row = chosen_row.replace("'",'')
            chosen_row = chosen_row.replace("[",'')
            chosen_row = chosen_row.replace("]",'')
            chosen_row = chosen_row.replace('"','')
            await ctx.send(chosen_row)


#addwisdom command
@bot.command(name='addwisdom')
async def addwisdom(ctx, *, newentry):
    id = ctx.message.guild.id
    #check if server is nate's server
    print('received new wisdom "',newentry,'"')
    #write to file
    if id == 729576520196161637:
            with open('wisdom.csv','a') as fd:
                fd.write(f"\n{newentry}")
            await ctx.send(f'Added wisdom "{newentry}"')
    else:
        with open('wisdom2.csv','a') as fd:
            fd.write(f"\n{newentry}")
        await ctx.send(f'Added wisdom "{newentry}"')


#restart command
@bot.command(name='r')
async def restart(ctx):
    #output
    print('Received command to restart')
    await ctx.send('restarting...')
    print()

    #write channel id to file
    with open('lastchannel.txt', 'w') as pfx:
        pfx.truncate(0)
        pfx.seek(0)
        lastchannel = str(ctx.message.channel.id)
        pfx.write(lastchannel)
    
    #restart script
    os.system('main.py')
    exit()

#help command
@bot.command(name='help')
async def help(ctx):
    #define embed
        em = discord.Embed(title="Help", description="eat dick shitass", colour= 3447003)
        
        #add entries
        em.add_field(name=f"{prefix}test", value="Test if the bot is working correctly", inline=False)

        em.add_field(name=f"{prefix}prefix", value=f'Change the bot`s command prefix, currently "{prefix}"', inline=False)

        em.add_field(name=f"{prefix}GameStatus", value="Set the bot's current game status", inline=False)

        em.add_field(name=f"{prefix}wisdom", value='If you are ever in need of wisdom and direction in life, simply consult the Nut Bot.', inline=False)

        em.add_field(name=f"{prefix}addwisdom", value=f"Contribute to the bot's pool of knowledge ({prefix}addwisdom your wisdom here)", inline=False)

        em.add_field(name=f"{prefix}r", value='Restart the bot (for testing shit)', inline=False)

        em.add_field(name=f"{prefix}case", value='Open a fake CS:GO case and start down the path of crippling gambling addiction', inline=False)

        em.add_field(name=f"{prefix}femboy", value='Femboys are pog', inline=False)

        em.add_field(name=f"{prefix}subreddit", value=f'Grabs a random post from hot in a subreddit (ex: {prefix}subreddit dankmemes)', inline=False)

        em.add_field(name=f"{prefix}CSGOstats", value=f'Show everyone else on the server how much you suck at CS:GO. After {prefix}CSGOstats, put your Steam ID.', inline=False)

        em.add_field(name=f"{prefix}casestats", value=f"Gets your statistics from the $case command, such as the worth of all the skins you've gotten and your rarest skin.", inline=False)

        em.add_field(name=f"{prefix}connectfour", value='Play the classic game connect four, right in a discord channel!', inline=False)

        em.add_field(name=f"{prefix}store", value="Access the store to buy items and special roles (Currently the only ways to get money are to be active on the server or open cases, however I will add more ways to get money such as winning games of connect four and getting bonuses from admins for being helpful members, but you start with $100, and I'll add more items soon)", inline=False)

        em.add_field(name=f"{prefix}bank", value='Check your current balance as well as how much total money you have earned and spent', inline=False)

        em.add_field(name=f"{prefix}case", value='Open a CS:GO weapon case. (Yes, this is gambling, but I have tweaked the odds so they are mostly fair. You start with 10 free cases.)', inline=False)

        em.add_field(name=f"{prefix}pay @[user] [amount]", value='Send money to another member, no questions asked about what it is for.', inline=False)

        await ctx.send(embed=em)

chosen_skin = 'none'

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
        #print(''.join(result))
    
    await ctx.send(embed=em)


@bot.command(name='spam')
async def spam(ctx, num, *, id):
    for i in range(int(num)):
        await ctx.send(id)


@bot.command(name='dmspam')
async def dmspam(ctx, id, num, *, msg):
    id = str(id)
    id = id.replace('<','')
    id = id.replace('@','')
    id = id.replace('!','')
    id = id.replace('>','')
    id = id.replace('&','')
    id = int(id)
    user = bot.get_user(id)
    for i in range(int(num)):
        await user.send(msg)
        print('Msgs left:',(int(num) - i))

#@bot.command(name='pm')
#async def pm(ctx, users: Greedy[User], *, message):
    #for user in users:
        #await user.send(message)

@bot.command(name='connectfour')
async def connectfour(ctx):
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
        #print(topline)
        lines = ''
        for row in aGrid:
            line = "⠀ |  "
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

    

    grid = createGrid(noColumns, noRows)
    reciept = [grid, winLength]

    grid = reciept[0]
    winlength = reciept[1]
    printGrid(grid)
    message = await ctx.send(f"Red player's turn\n\n⠀ |  1️⃣  |  2️⃣  |  3️⃣  |  4️⃣  |  5️⃣  |  6️⃣  |  7️⃣  |  8️⃣  |  9️⃣  |  🔟  |\n{printGrid(grid)}")
    await message.add_reaction("1️⃣")
    await message.add_reaction("2️⃣")
    await message.add_reaction("3️⃣")
    await message.add_reaction("4️⃣")
    await message.add_reaction("5️⃣")
    await message.add_reaction("6️⃣")
    await message.add_reaction("7️⃣")
    await message.add_reaction("8️⃣")
    await message.add_reaction("9️⃣")
    await message.add_reaction("🔟")
    noColumns = len(grid[0])
    player = 0
    complete = False
    
    isbot = 1
    

    while(complete==False) :
        

        while True:
            try:
                reaction, user = await bot.wait_for("reaction_add", timeout=120)
                # waiting for a reaction to be added - times out after x seconds

                if isbot == 1:
                    isbot = 0
                    continue
                
                

                if str(reaction.emoji) == "1️⃣":
                    usermove = 0
                    await message.remove_reaction(reaction, user)
                    break

                elif str(reaction.emoji) == "2️⃣":
                    usermove = 1
                    await message.remove_reaction(reaction, user)
                    break
                    
                elif str(reaction.emoji) == "3️⃣":
                    usermove = 2
                    await message.remove_reaction(reaction, user)
                    break
                
                elif str(reaction.emoji) == "4️⃣":
                    usermove = 3
                    await message.remove_reaction(reaction, user)
                    break

                elif str(reaction.emoji) == "5️⃣":
                    usermove = 4
                    await message.remove_reaction(reaction, user)
                    break

                elif str(reaction.emoji) == "6️⃣":
                    usermove = 5
                    await message.remove_reaction(reaction, user)
                    break

                elif str(reaction.emoji) == "7️⃣":
                    usermove = 6
                    await message.remove_reaction(reaction, user)
                    break

                elif str(reaction.emoji) == "8️⃣":
                    usermove = 7
                    await message.remove_reaction(reaction, user)
                    break

                elif str(reaction.emoji) == "9️⃣":
                    usermove = 8
                    await message.remove_reaction(reaction, user)
                    break

                elif str(reaction.emoji) == "🔟":
                    usermove = 9
                    await message.remove_reaction(reaction, user)
                    break

                elif str(reaction.emoji) == "🔄":
                    await message.remove_reaction(reaction, user)
                    continue


            except asyncio.TimeoutError:
                break
                # ending the loop if user doesn't react after x seconds


        player = (player%2)+1
        if player == 1:
            pturn = "Yellow player's turn"
        else:
            pturn = "Red player's turn"
        #print("It is Player %d Turn!" % player)
        grid = dropCoin(noColumns, grid, player, usermove)
        complete = winCheck(player, selectedColumn, grid, winlength)
        
        if (complete==True):
            if player == 1:
                await ctx.send("Red player Wins!")
            else:
                await ctx.send("Yellow player Wins!")
            
        
        if (complete!=True):
            
            result = True
            for x in grid[0]:
                if x == 0:
                    result = False
                    break
            if result == True:
                print("The Game is a Draw!")
                await ctx.send
                pass
            
            complete = result
        
        
        topline = "|"
        #for n in range(0,len(aGrid)):
            #topline += "-" + str(n) + "-|"
        #print(topline)
        lines = ''
        for row in grid:
            line = "⠀ |  "
            for x in row:
                if (x == 0) :
                    x = "⬛️"
                elif (x == 1) :
                    x = "🔴"
                elif (x == 2) :
                    x = "🟡"
                line = line + str(x) + "  |  "
            lines += f'{line}\n'
            #print(lines)
        
        

        #boardem = discord.Embed(title="Connect Four", description=lines, colour= 3447003)
        await message.edit(content=f"{pturn}\n\n⠀ |  1️⃣  |  2️⃣  |  3️⃣  |  4️⃣  |  5️⃣  |  6️⃣  |  7️⃣  |  8️⃣  |  9️⃣  |  🔟  |\n{printGrid(grid)}")


chosen_skin = 'none'

#case command
@bot.command(name='case')
async def case(ctx):

    output(ctx)

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

    if cases == 0:
        await ctx.send('You are out of cases. You can buy more at the store.')
        print(cases)
    if cases > 0:
        print(cases)
        cases -= 1
        alldata[2] = f'{cases}\n'
        with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(alldata)

    
        #generate number
        probability = random.randrange(0, 174)

        rare = 0

        #probability = 164

        print(probability)

        loop = 0

        colors = [0xffffff, 0x0099cc, 0x0033cc, 0x6600cc, 0xff00ff, 0xff0000, 0xffcc00]

        

        #get rarity, remove unnessesary characters, skin name, and define embed with colors
        if probability < 50:
            rarity = 'consumer'
            with open('skins_consumer.csv') as f:
                reader = csv.reader(f)
                chosen_skin = random.choice(list(reader))
                chosen_skin = str(chosen_skin)
                chosen_skin = chosen_skin.replace("'",'')
                chosen_skin = chosen_skin.replace("[",'')
                chosen_skin = chosen_skin.replace("]",'')
            
            np = random.randrange(30,500)

            print(chosen_skin)

            skin_name = chosen_skin
            skin_name = skin_name.replace(".png",'')

            print(skin_name)

            
            colournum = 0
            em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour=colors[colournum])    
        elif probability < 130:
            rarity = 'industrial'
            with open(f'{rarity}.csv') as f:
                reader = csv.reader(f)
                chosen_skin = random.choice(list(reader))
                chosen_skin = str(chosen_skin)
                chosen_skin = chosen_skin.replace("'",'')
                chosen_skin = chosen_skin.replace("[",'')
                chosen_skin = chosen_skin.replace("]",'')

            np = random.randrange(30,500)

            print(chosen_skin)

            skin_name = chosen_skin
            skin_name = skin_name.replace(".png",'')

            print(skin_name)

            
            colournum = 1
            em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
        elif probability < 155:
            rarity = 'Mil-Spec'
            with open(f'{rarity}.csv') as f:
                reader = csv.reader(f)
                chosen_skin = random.choice(list(reader))
                chosen_skin = str(chosen_skin)
                chosen_skin = chosen_skin.replace("'",'')
                chosen_skin = chosen_skin.replace("[",'')
                chosen_skin = chosen_skin.replace("]",'')

            np = random.randrange(300,1000)
            print(chosen_skin)

            skin_name = chosen_skin
            skin_name = skin_name.replace(".png",'')

            print(skin_name)

            colournum = 2
            em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
            
        elif probability < 165:
            rarity = 'restricted'
            with open(f'{rarity}.csv') as f:
                reader = csv.reader(f)
                chosen_skin = random.choice(list(reader))
                chosen_skin = str(chosen_skin)
                chosen_skin = chosen_skin.replace("'",'')
                chosen_skin = chosen_skin.replace("[",'')
                chosen_skin = chosen_skin.replace("]",'')

            print(chosen_skin)

            skin_name = chosen_skin
            skin_name = skin_name.replace(".png",'')

            print(skin_name)

            colournum = 3
            em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
            
            np = random.randrange(700,2000)
        elif probability < 170:
            rarity = 'Classified'
            with open(f'{rarity}.csv') as f:
                reader = csv.reader(f)
                chosen_skin = random.choice(list(reader))
                chosen_skin = str(chosen_skin)
                chosen_skin = chosen_skin.replace("'",'')
                chosen_skin = chosen_skin.replace("[",'')
                chosen_skin = chosen_skin.replace("]",'')

            print(chosen_skin)

            skin_name = chosen_skin
            skin_name = skin_name.replace(".png",'')

            print(skin_name)

            colournum = 4
            em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
            
            np = random.randrange(1000,10000)

        elif probability < 173:
            rarity = 'Covert'
            with open(f'{rarity}.csv') as f:
                reader = csv.reader(f)
                chosen_skin = random.choice(list(reader))
                chosen_skin = str(chosen_skin)
                chosen_skin = chosen_skin.replace("'",'')
                chosen_skin = chosen_skin.replace("[",'')
                chosen_skin = chosen_skin.replace("]",'')

            print(chosen_skin)

            skin_name = chosen_skin
            skin_name = skin_name.replace(".png",'')

            print(skin_name)

            colournum = 5
            em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
            rare = 1
            
            np = random.randrange(5000,30000)

        elif probability < 174:
            rarity = 'Knife'
            with open(f'{rarity}.csv') as f:
                reader = csv.reader(f)
                chosen_skin = random.choice(list(reader))
                chosen_skin = str(chosen_skin)
                chosen_skin = chosen_skin.replace("'",'')
                chosen_skin = chosen_skin.replace("[",'')
                chosen_skin = chosen_skin.replace("]",'')
            
            np = random.randrange(30000,300000)

            print(chosen_skin)

            skin_name = chosen_skin
            skin_name = skin_name.replace(".png",'')

            print(skin_name)

            
            colournum = 6
            em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
            rare = 1
        else:
            print('bruh')


        
        

        price = 'No Price Available'


        #get price from file
        try:
            with open('fullprice.csv', 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    for j, column in enumerate(row):
                        if skin_name in column:
                            print((i,j))
                            price = row[1]
                            print(price)
        except:
            price = np

        if price == 'No Price Available':
            price = np


        #generate float and format price
        try:
            fl = random.randrange(0, 800000)

            finalfl = decimal.Decimal(fl)/1000000

            prfl = 1 - finalfl

            prfl = prfl * 1000000


            price = int(price)
            price= price * 3
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
        await ctx.send(embed=em, file=discord.File(f'{rarity}/{chosen_skin}'))
        #await ctx.send(file=discord.File(f'{rarity}/{chosen_skin}'))
        

        #price integer for storage
        if price != "No Price Available":
            intprice = price.replace('.','')
            intprice = intprice.replace('$','')
            intprice  = int(intprice)
            if intprice > 4000:
                rare = 1
        
        #rare skin in rare skin channel
        if rare == 1:
            chl = bot.get_channel(786751841374830604)
            await chl.send(f'{ctx.author.mention} got a {rarity} {skin_name} worth {price} in <#{ctx.message.channel.id}>', embed=em, file=discord.File(f'{rarity}/{chosen_skin}'))
        


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

            #print(newearnings[0])


            try:
                newearnings[0] = f'{int(newearnings[0]) + intprice}\n'
                newearnings[1] = f'{int(newearnings[1]) + intprice}\n'
            except:
                print('No Price')
                return

            with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                file.writelines(newearnings)


            with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
                totalwinnings = file.readlines()

            #print(totalwinnings[0])


            try:
                totalwinnings[0] = f'{int(totalwinnings[0]) + intprice}\n'
            except:
                print('No Price')
                return

            with open(f'data/{str(ctx.author.id)}.txt', 'w') as file:
                file.writelines(totalwinnings)





            with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
                mostvaluable = file.readlines()

            #print(mostvaluable[1])

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


        
@bot.command(name='casestats')
async def casestats(ctx):
    output(ctx)
    with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
        stats = file.readlines()
    
    print(stats)

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
    
    em.add_field(name=f"Current Balance", value=formatprice(currentbal), inline=False)
    em.add_field(name=f"Total Earnings", value=formatprice(totalearn), inline=False)
    em.add_field(name=f"Total Money Spent", value=formatprice(totalspent), inline=False)
    em.add_field(name=f"Inventory", value=f'Cases: {cases}', inline=False)

    await ctx.send(embed=em)

@bot.event
async def on_message(message):
    
    addbalance(message, 50)

    await bot.process_commands(message)


@bot.command(name='store')
async def store(ctx):
    em = discord.Embed(title="Store", description="Purchase items and and special roles", colour= 3447003)
    em.add_field(name=f"Current Balance:", value=balance(ctx), inline=False)
    em.add_field(name=f"⭐ - VIP Access ($1000)", value=f'Grants you access to the VIP lounge as well as other perks', inline=False)
    em.add_field(name=f"🎁 - CS:GO Case ($12)", value=f'1 CS:GO weapon case. (Yes, this is gambling, but I have tweaked the odds so they are mostly fair.)', inline=False)
    
    
    # getting the message object for editing and reacting

    message = await ctx.send(embed = em)

    
    await message.add_reaction("⭐")
    await message.add_reaction("🎁")

    def check(reaction, user):
        return user == ctx.author
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=120, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example
            
            usrbal = balance(ctx)

            formattedbalance = formatprice(usrbal)

            print(formatprice)

            em = discord.Embed(title="Store", description="Purchase items and and special roles", colour= 3447003)
            em.add_field(name=f"Current Balance:", value=formattedbalance, inline=False)
            em.add_field(name=f"⭐ - VIP Access ($1000)", value=f'Grants you access to the VIP lounge as well as other perks', inline=False)
            em.add_field(name=f"🎁 - CS:GO Case ($12)", value=f'1 CS:GO weapon case. (Yes, this is gambling, but I have tweaked the odds so they are mostly fair.)', inline=False)
            await message.edit(embed = em)
            
            
            if str(reaction.emoji) == "⭐":
                if usrbal < 100000:
                    await ctx.send('❌ You do not have enough money ($1000)')
                else:
                    role = discord.utils.get(ctx.author.guild.roles, name="★ VIP ★")
                    await ctx.author.add_roles(role)
                    subtractbalance(ctx, 100000)
                    await ctx.send('✅ Transaction succesful! You now have VIP access.')
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "🎁":
                if usrbal < 1200:
                    await ctx.send('❌ You do not have enough money ($12)')
                else:
                    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                        alldata = file.readlines()
                    
                    cases = int(alldata[2])

                    print(cases)
                    cases += 1
                    alldata[2] = f'{cases}\n'
                    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                        file.writelines(alldata)

                    subtractbalance(ctx, 1200)
                    await ctx.send(f'✅ Transaction succesful! You now have {cases} case(s).')
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            break
            # ending the loop if user doesn't react after x seconds

@bot.command(name='pay')
async def pay(ctx, member, amount):
    id = str(member)
    id = id.replace('<','')
    id = id.replace('@','')
    id = id.replace('!','')
    id = id.replace('>','')
    id = id.replace('&','')
    id = int(id)

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
    
    alldata[0] = f'{int(alldata[0]) + int(amount*100)}\n'
    alldata[1] = f'{int(alldata[1]) + int(amount*100)}\n'

    with open(f'bank/{str(id)}.txt', 'w') as file:
            file.writelines(alldata)

    subtractbalance(ctx, amount*100)

    await ctx.send(f'✅ Paid ${amount} to {member}')






bot.run(TOKEN)