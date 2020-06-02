import discord
from discord.ext import commands

class starboard(commands.Cog):
      def __init__(self, bot):
            self.bot = bot

description = '''A star bot.'''
bot = commands.Bot(command_prefix='vb!', description=description)
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name, bot.user.id)
    print('guilds: ', end='')
    for guild in bot.guilds:
        print(str('{0}, ').format(guild), end='')
    print()
    isrunning = False

# owner
owner = "509386354862456833"

@bot.event
async def on_raw_reaction_add(emoji, messageid, channelid, member):
    reactchannel = bot.get_channel(channelid)
    message = await reactchannel.get_message(messageid)
    await star_post_check(message)
isrunning = False

async def star_post_check(message):
    if str(message.id) in open('sent.txt').read():
        match = True
    else: 
        match = False
    if match:
        return
    isstar = False
    best_of = discord.utils.get(message.guild.channels, name= "stelle")
    for i in message.reactions:
        if i.emoji == ("⭐") and i.count >= 1 and message.channel != best_of:
            isstar = True
    if isstar:
        # embed message itself
        embed = discord.Embed(title='Starred post', description=message.content, colour=0xFFD700)
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        try:
            if message.content.startswith('https://'):
                embed.set_image(url=message.content)
        except:
            pass
        try:
            attach = message.attachments
            embed.set_image(url = attach[0].url)
        except:
            pass
        # sending actual embed
        await stelle.send(embed=embed)
        print ("* Starred "+str(message.id)+" by "+message.author.display_name)
        cache = open("sent.txt", "a")
        cache.write(str(message.id) + " ")
        cache.close()

@commands.command(help = "Rechecks all channels.")
@commands.is_owner()
async def recheck(ctx):
    messagecount = 0
    channelcount = 0
    guildcount = 0
    for guild in bot.guilds:
        print("\t Checking " + guild.name)
        for channel in guild.text_channels:
            print("Checked " + channel.name)
            try:
                async for message in channel.history(limit=1000, before=None, after=None, around=None, reverse=False):
                    await star_post_check(message)
                    messagecount += 1
                channelcount += 1
            except:
                channelcount += 1
                print("\t\tERROR: Skipped a channel")
        guildcount += 1
    print("Finished checking " + str(messagecount) + " messages in " + str(channelcount) + " channels and "
          + str(guildcount) + " guilds.")

def setup(bot):
      bot.add_cog(starboard(bot))
