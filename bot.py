import discord
import aiohttp
from random import randint
from keep_alive import keep_alive
import pandas as pd
import random
import requests
import json
import datetime
import pytz
import wikipedia

client = discord.Client()

# TOKEN removed for security purposes
TOKEN = 'Your_bot_token'

trivia_api = [
              "https://opentdb.com/api.php?amount=1&category=15" # Video Games
              "https://opentdb.com/api.php?amount=1&category=18", # Science Computer
              "https://opentdb.com/api.php?amount=1&category=30" # Science & Gadgets
             ]

user_input = ["tgb hello", "tgb hii", "tgb hi", "tgb bro", "tgb yo", "tgb yoohoo", "tgb hey", "tgb ola", "tgb wassup", "tgb dude", "tgb what up dude", "tgb ciao", "tgb buddy"]

bot_reply = ["Hello", "Heya", "Ciao", "Hey", "Heya, how's it going", "Hey, wassup", "Good to see you", "Great to see you", "Glad to see you", "Look who it is! It's a bird... it's a plane... it's ", "Nice to see you again", "Hi there","Long time no see","Howdy", "Hiya", "Yoohoo", "Ola", "Bonjour","What's going on","Look who it is. It's"]

wish_morning = ["Rise and shine!", "Top of the morning to you!", "Goos day to you", "Have a great day", "Wishing you the best for the day ahead", "How are you this fine morning?",
                "Isn't it a beatuiful day today?", "Look alive!", "What a pleasant morning we are doing", "Morning!", "Good morning", "Good day"]

wish_afternoon = ["Have a good afternoon and a great day!", "You are as bright as the afternoon sun", "Have an awesome afternoon! thank you for sharing a piece of your heart", "Wishing you a splendid afternoon my one and only!",
                  "This afternoon is a beauty, just like you", "Half of the day is over; have a marvelous afternoon and enjoy the rest of the day!", "i Would like to wish you a good afternoon and an even better evening",
                  "Today, there will be a beautiful sunset after you have a good afternoon!"]

wish_evening = ["Have a nice evening", "Good evening", "Good evening Mayank", "Evening boss", "I hope you are having a refreshing evening as i am having here thinking of you"]

wish_night = ["It was nice to meet you, goodnight!", "Goodnight! see you tomorrow", "It was good to meet you", "I'll catch up with you later", "I'll will see you seen", "Ta-Ta for now"]

li = ['bio of', 'details of', 'about', 'who is']
nishant = ['nishant gandhi', 'nishant']
sarthak = ['sarthak khandelwal', 'sarthak']
samarth = ['samarth sharma', 'samarth']
vipin = ['vipin']
ishika = ['ishika shahaney', 'ishika']
mayank = ['mayank verma', 'mayank']
anushka = ['anushka', 'anushka jain']
aditi_d = ['aditi dandawate', 'aditi d']
aditi_m = ['aditi mandlik', 'aditi m']
raj = ['raj soni', 'raj']
prateeti = ['prateeti jain', 'prateeti']
suchismita = ['suchismita', 'suchismita']
tanisha = ['tanisha', 'tanisha jain']
jassi = ['jassi', 'jaspreet op', 'jaspreet singh saini', 'jaspreet']
saud = ['saud hashmi', 'saud']

def quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.content)
    quo = "*" + json_data[0]['q'] + "*\n-**" + json_data[0]['a'] + "**"
    return quo


@client.event
async def on_ready():
    print('Ready {0.user}'.format(client))


@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    msge = message.content.lower()
    if any(word in msge for word in user_input):  # BOT WILL RESPOND TO HI HELLO MESSAGES
        await message.channel.send(random.choice(bot_reply) + '   {0.author.mention}'.format(message))

    if message.content.lower() == 'tgb help':
        embed = discord.Embed(
            title="***TGB Help/Command list***",
            description=f"{user_input}\ntgb event\ntgb council\ntgb core\ntgb exec\ntgb contacts\ntgb trivia\ntgb meme\ntgb quote\n",
            colour=discord.Colour.random()
        )
        await message.channel.send(embed=embed)

    if message.content.lower() == "tgb event":
        embed = discord.Embed(title="*** \t\t\t\t\t:computer: :computer: CP and DS***",

        description="**Medi-Caps University ACM Student Chapter (MUACM)** brings you a super interesting & informative session in collaboration with Prepbytes,   :regional_indicator_c:   **How to Master Competitive Programming** and opportunity to delve deep into the   :map: :map: **World of Data Science and become Industry Ready**",
                                                                
                              color=discord.Color.random()
                              )

        embed.add_field(name="**\t\t\t\t\tCompetitive Programming**\n*4th September ( :timer:  8 PM)*",

         value="[Registration Form](https://webinar.prepbytes.com/how-to-master-competitive-programming?utm_source=Webinar_Medicap_University&utm_medium=College_Specific&utm_campaign=CP)")

        embed.add_field(name="***\t\t\t\t\t\t\t\t\tData Science***\n*5th September ( :timer:  11 AM)*",
         value="[Type Form](https://yhqovll6z83.typeform.com/to/jGfylXgA)", inline=False)

        embed.set_image(url="https://i.ibb.co/48nmSCN/IMG-20210829-WA0033.jpg")

        embed.set_image(url="https://i.ibb.co/0y87KcW/20210901-004833.jpg")
        #await message.reply(embed=embed)

    msg_content = message.content.lower()
    code = ['1228401632', '1777366558', '2377004904', '1545327834', '2377004904', '7853253329', '5955586652', '9224255213', '1895696588', '9068240223']

    if any(word in msg_content for word in code):
        await message.delete()
        embed = discord.Embed(
            title="***Warning!!!***",
            description=" {0.author.mention}   ".format(message) + "**Don't share the code with anyone, otherwise your attendance won't be counted**",
            colour=discord.Colour.random()
        )
        await message.channel.send(embed=embed)
        
    if message.content.lower() == 'tgb council':
        embed = discord.Embed(
            title="***\t\t\t\t\tCouncil Members***",
            description="***Nishant Gandhi*** >>> Mentor\n***Sarthak Khandelwal*** >>> Mentor\n***Samarth Sharma*** >>> Chairman\n***Vipin Gupta*** >>> Vice-Chairman\n***Saud Hashmi*** >>> Membership Chairperson\n***Ishika Shahaney***  >>> Treasurer & Secretary",
            colour=discord.Colour.from_rgb(138,43,226)
        )
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb core':
        embed = discord.Embed(
            title="***\t\t\t\t\tHead Members***"
            ,
            description="***Aditi Dandawate*** -->  Content & Ideation\n"
                        "***Aditi Mandlik*** -->  Social Media & Outreach\n"
                        "***Anushka Jain*** -->  Management\n"
                        "***Jaspreet Singh Saini --> Graphics\n"
                        "***Mayank Verma*** -->  Technical\n"
                        "***Prateeti Jain*** -->  Junior Coordinator\n"  
                        "***Raj Soni*** -->  Marketing\n"
                        "***Suchismita Nanda*** -->  Documentation\n"
                        "***Tanisha Jain*** -->  Graphics\n",
                 
        
            colour=discord.Colour.from_rgb(0, 255, 255)
        )
        await message.channel.send(embed=embed)

    if message.content.lower() == "tgb contacts":
        embed = discord.Embed(
            title='***\t\t\t\t\tConnect us on*** !',
            description='**[Instagram](https://instagram.com/mu_acm?utm_medium=copy_link)**\n\n'
                        '**[LinkedIn](https://www.linkedin.com/company/acm-student-chapter-medicaps/)**'
                        '\n\n**[YouTube](https://www.youtube.com/channel/UC5kQv1TB5GVNuttr2LuSKhA)**',
            colour=discord.Colour.orange()
        )
        embed.set_image(url='https://i.ibb.co/YWV5Bx0/Mu-ACMlogo.png')
        await message.channel.send(embed=embed)

    if message.content.lower() == "tgb trivia":
        res = requests.get(random.choice(trivia_api))
        data = res.json()
        val = data["results"][0]["question"] + "\n**Answer: **" + data["results"][0]["correct_answer"]
        embed = discord.Embed(colour=discord.Colour.random())
        embed.add_field(name="**Trivia**", value=val)
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb meme':
        await message.channel.send(embed=await pyrandmeme())

    if message.content.lower() == "tgb quote":
        quo = quote()
        embed = discord.Embed(color=discord.Color.random())
        embed.add_field(name="Quote:", value=quo)
        embed.set_footer(text="Requested by {0.author.name}".format(message))
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb bio':
        await message.channel.send(tgb_bio(message))

    if 'tgb bio: ' in message.content.lower() and message.content[9] != None:

      code = message.content[9:]
      userid = int(code[3:len(code) - 1])
      await message.channel.send(tgb_bio_with_user(message, userid))

    if ("tgb add bio: " in message.content.lower()) and (message.content[13] != None):
      await message.channel.send(add_bio(message))

    if ("tgb change bio: " in message.content.lower()) and (message.content[16] != None):

      await message.channel.send(change_bio(message))

    query = message.content.lower()
    # query = input("- ").lower()

    if any(word in query for word in li) and any(word in query for word in nishant):
      embed = discord.Embed(title="Nishant Gandhi, Ex-Chairman and Founder of MUACM who flies over the cloud", colour=discord.Colour.red())
      await message.reply(embed=embed)

    if any(word in query for word in li) and any(word in query for word in saud):
        embed = discord.Embed(title='Membership Chairperson at MUACM\nFounder @CSCult\nLoves STEM, Economics and Philosophy\nSpends time building stuff and jamming', colour=discord.Colour.red())
        await message.reply(embed=embed)

    if any(word in query for word in li) and any(word in query for word in samarth):
        embed = discord.Embed(title="Founder & Mentor at MUACM\nCloud Enthusiast\nWorking for my goals", colour=discord.Colour.red())
        await message.reply(embed=embed)

    if any(word in query for word in li) and any(word in query for word in sarthak):
        embed = discord.Embed(title="Founder & Mentor at MUACM\nMachine Learning Geek, Zealot Researcher", colour=discord.Colour.red())
        await message.reply(embed=embed)
    

    if "wikipedia" in query:
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        embed = discord.Embed(title="According to Wikipedia", description=results, colour=discord.Colour.random())
        await message.reply(embed=embed)

    if "google" in query:
        query = query.replace("google", "")
        results = wikipedia.summary(query, sentences=2)
        embed = discord.Embed(title="According to Google", description=results, colour=discord.Colour.random())
        await message.reply(embed=embed)

    

async def pyrandmeme():
    pymeme = discord.Embed(title="Tech Meme requested", description="Here you go!", color=0x84d4f4)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/TechMemes/new.json?sort=new') as r:
            res = await r.json()
            pymeme.set_image(url=res['data']['children'][randint(0, 25)]['data']['url'])
            return pymeme
        await pyrandmeme()

def tgb_bio(message):
  df = pd.read_csv(r'bio.csv')
  user = str(message.author)
  users = list(df['user'].values)
  userid = message.author.id
  if user in users:
      return df[df['userid'] == userid].bio.values[0]
  else:
      rtn = f"No bio found for {user}"
      return rtn

def tgb_bio_with_user(message, userid):

  df = pd.read_csv(r'bio.csv')
  user = str(message.author)
  users = list(df['user'].values)
  userid = message.author.id
  if user in users:
      return df[df['userid'] == userid].bio.values[0]
  else:
      rtn = f"No bio found for {user}"
      return rtn

def add_bio(message):
  df = pd.read_csv(r'bio.csv')
  bio = str(message.content[13:])
  user = str(message.author)
  userid = message.author.id
  users = list(df['user'].values)
  if user in users:
      return 'You already have a bio!'
  df.loc[len(df.index)] = [userid, user, bio]
  df.to_csv(r'bio.csv', index=False)
  return 'Bio added!'

def change_bio(message):
  df = pd.read_csv(r'bio.csv')
  new_bio = str(message.content[16:])
  user = str(message.author)
  userid = str(message.author.id)
  users = list(df['user'].values)
  if user in users:
      df.loc[df.userid == userid, 'bio'] = new_bio
      df.to_csv(r'bio.csv', index=False)
      return 'Bio changed!'
  else:
      rtn = f"No bio found for {user}"
      return rtn

keep_alive()
client.run(TOKEN)
