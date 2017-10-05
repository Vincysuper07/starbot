import discord
from discord.ext import commands
import asyncio
import re
import sys
import os, random


#scriptpath = "../modules/commandmodule.py" #relative path dont DO a n y  Funny business
#sys.path.append(os.path.abspath(scriptpath))

description = '''A star bot.'''
bot = commands.Bot(command_prefix='!', description=description)
@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name, bot.user.id)
	print('Servers: ', end='')
	for server in bot.servers:
		print(str('{0}, ').format(server), end='')
	print()
	print('----------------')
	#global starnumber
	#starnumber = 4
	isrunning = False
	
#fn = os.path.join(os.path.dirname(__file__), 'starbot.py')
#dir = os.path.dirnam(__file__)


#owner 
owner = "141695444995670017"

#channels
#best_of = 332172659863453697
#bot-bot = 332229780797652992

#roles
#shut up = 329705402021183488

def getRandomFile(path):
  """
  Returns a random filename, chosen among the files of the given path.
  """
  files = os.listdir(path)
  index = random.randrange(0, len(files))
  return files[index]

###starboard code### 

#@bot.event
#async def on_member_join(member):
#	if member.id == ("289588477492723712"):
#		muterole = discord.utils.get(message.server.roles, id='329705402021183488')
#		await bot.add_roles(member, muterole)
	
@bot.event
async def on_reaction_add(reaction, member):
	print ("detected")
	if reaction.emoji == ("⭐"):
		if reaction.count == 5:
			nsfw = bot.get_channel("nsfw-garbage-bin")
			if reaction.message.channel != nsfw:	
				best_of = discord.utils.get(reaction.message.server.channels, name= "best_of")
				
			#embed message itself
				em = discord.Embed(title='Starred post', description=reaction.message.content, colour=0xFFD700)
				em.set_author(name=reaction.message.author, icon_url=reaction.message.author.avatar_url)
				
			#embed url images
				if reaction.message.content.endswith(('.png', '.jpg', '.gif', '.gifv', '.webm')):
					em.set_image(url = reaction.message.content)

			#modifying reaction.message.attachments
				attach = reaction.message.attachments
				detector = str(attach)
				if detector.startswith('[{'):
					modify2 = str(attach)
					junk, junk2 = modify2.split("'url': '")
					websitelink, junk3 = junk2.split("',", 1)
					em.set_image(url = websitelink)
			#sending actual embed
				await bot.send_message(best_of, embed=em)
				await bot.clear_reactions(reaction.message)
				
		else:
			pass

isrunning = False

'''commands'''
@bot.event
async def on_message(message):
#check the message
	global isrunning
	#global commanduser
	#commanduser = ("null")
	
	
	#terobot v2
	
	terobotchance=random.randrange(200)
	if terobotchance == 1:
		if message.channel.is_private == True:
			return
		if message.channel.server.id == "351885259199086593" or message.channel.server.id == "308265490877382656": #consider refactoring to check a list
			return
		else:
			this_dir = os.path.dirname(__file__) 
			pastaraw = os.path.realpath("{0}/copypastas".format(this_dir))
			choosepasta = getRandomFile(pastaraw)
			copypastaaa = open(pastaraw+"\\"+choosepasta, "r",encoding="utf8")
			selectedcopypasta = copypastaaa.read()
			await bot.send_message(message.channel, "<@{}> {}".format(message.author.id, selectedcopypasta))
	
	
#dablist command
	if message.content.startswith('!listdabs'):
		#dablist = os.listdir("starbot\\dabs")
		
		this_dir = os.path.dirname(__file__) 
		dabpath = os.path.realpath("{0}/dabs".format(this_dir))
		dablist = os.listdir(dabpath)
		liststr = '\n'.join(dablist)
		em = discord.Embed(title='a list of dabs for people with terrible memories', description=liststr, colour=0xFFD700)
		await bot.send_message(message.channel, embed=em)
#dablist command
	if message.content.startswith('!dab'):
	#checks for command !story

		if not isrunning:
			isrunning = True
			#commanduser = message.author
			try:
				storycommand = message.content.split("!dab ",1)[1]
			except IndexError:
				kill3 = await bot.send_message(message.channel, "wtf it's empty what do you want me to do")
				await asyncio.sleep(1)
				await bot.delete_message(kill3)
				await bot.delete_message(message)
				isrunning = False
				if message.author == ("☭Liar☭#0946"):
					return
				print(message.author, "was unable to type properly")
				return
			try:
				this_dir = os.path.dirname(__file__) 
				storypath = os.path.realpath("{0}/dabs".format(this_dir))
				story = open(storypath+"\\"+storycommand+".txt", "r",encoding="utf8")
			except IOError:
				isrunning = False
				kill2=await bot.send_message(message.channel, "Choose a real file you nigger")
				await asyncio.sleep(2)
				await bot.delete_message(kill2)	
				await bot.delete_message(message)
				if message.author == ("☭Liar☭#0946"):
					return
				print(message.author, "was unable to find a file.")
				return
			msg = await bot.send_message(message.channel, story.readline())
			this_dir = os.path.dirname(__file__) 
			pathstory2 = os.path.realpath("{0}/dabs/".format(this_dir))
			story = open(pathstory2+"\\"+storycommand+".txt", "r",encoding="utf8")
			await asyncio.sleep(.1)
			#waits 3 second (I think 3 seconds, not sure)
			dabstop = False
			for chunk in iter(lambda: story.readline(), ''):
			#loops until end of file
				await bot.edit_message(msg, chunk)
				#edits message to add next line
				#if dabstop == True:
					#return
				await asyncio.sleep(1)
				#waits 3 seconds
			await bot.delete_message(msg)
			await bot.delete_message(message)
			#deletes the message 
			story.close() 
			#closes the file
			isrunning = False
			if message.author == ("☭Liar☭#0946"): 
					return
			print(message.author, "used !dab successfully.")
				
		else:
			kill = await bot.send_message(message.channel,"REEEEEEEEEEEEEEE WAIT YOUR TURN")
			await asyncio.sleep(2)
			await bot.delete_message(kill)
			await bot.delete_message(message)
			if message.author == ("☭Liar☭#0946"):
				return
			print (message.author, "was unable to wait his turn.")
#help command
	if message.content.startswith("!help"):
		this_dir = os.path.dirname(__file__) 
		helppath = os.path.realpath("{0}".format(this_dir))
		helptext=open(helppath+"\\"+"help.txt", "r", encoding="utf8")
		helptextactual=helptext.read()
		em = discord.Embed(title='Help', description=helptextactual, colour=0xFFD700)
		await bot.send_message(message.channel, embed=em)
		print(message.author, "asked for help!")
		helptext.close()
		
#echo command			
	if message.content.startswith("!echo"):
		if message.author != bot.user:
			try:
				echoecho = message.content.split("!echo ",1)[1]
			except IndexError:
				kill3 = await bot.send_message(message.channel, "I can't echo silence")
				if message.author == ("☭Liar☭#0946"):
					return
				print(message.author, "is unable to speak properly")
				await asyncio.sleep(1)
				await bot.delete_message(kill3)
				await bot.delete_message(message)
				return
			await bot.send_message(message.channel, echoecho)
			try:
				print(message.author, "echoed: ", echoecho)
			except UnicodeEncodeError:
				print ("invalid characters for the console")
			await bot.delete_message(message)
			
#superecho command			
	'''if message.content.startswith("!superecho"):
		if message.author != bot.user:
			try:
				echoecho = message.content.split("!superecho ",1)[1]
			except IndexError:
				kill3 = await bot.send_message(message.channel, "I can't echo silence")
				if message.author == ("☭Liar☭#0946"):
					return
				print(message.author, "is unable to speak properly")
				await asyncio.sleep(1)
				await bot.delete_message(kill3)
				await bot.delete_message(message)
				return
			echonumber = 100
			while echonumber != 0:
				await bot.send_message(message.channel, "@everyone "+echoecho)
				echonumber = echonumber - 1
			try:
				print(message.author, "echoed: ", echoecho)
			except UnicodeEncodeError:
				print ("invalid characters for the console")
			await bot.delete_message(message)'''
	
#status command
	if message.content.startswith("!status"):
		oldstatus = message.content
		newstatus = oldstatus.replace("!status", "")
		await bot.change_presence(game=discord.Game(name=newstatus))
		print(message.author,"changed status.")
	
	if message.content.startswith("!wormhole"):
		rawwormholemsg = message.content
		refinedwrmmsg= rawwormholemsg.replace("!wormhole", "")
		await bot.send_message(message.channel, "<@127296623779774464> wormhole send"+refinedwrmmsg)
		
#hotdog command
	if message.content.startswith("!hotdog"):
		await bot.send_message(message.channel, "https://cdn.discordapp.com/attachments/322415222004514827/333425912932728832/image.jpg")
	
#4chan
	if message.channel.is_private == True:
		chan = bot.get_channel("347242341632835584")
		await bot.send_message(chan, message.content)
		print(message.author)
#rename command
	
#joke command - not really working
	if message.content.startswith("!joke"):
		this_dir = os.path.dirname(__file__) 
		jokepath = os.path.realpath("{0}".format(this_dir))
		with open(jokepath+"\\"+"jokes.txt", 'r') as infile:
			randomlinecount = random.randrange(2,6,2)
			print (randomlinecount)
			lines = [line for line in [infile.readline() for _ in range(randomlinecount)] if len(line) ]
			await  bot.send_message(message.channel, '\n'.join(lines))

#trap
	#if message.content.startswith("!delet"):
		deletcount=0
		deletcount+=1
		deletmessage=logs_from(message.channel, limit = 1)
		if deletcount == 2:
			await bot.delete_message(deletmessage)
		

bot.run('get your own token')
