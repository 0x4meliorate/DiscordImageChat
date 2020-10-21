import discord
import time
from PIL import Image, ImageDraw, ImageFont
import textwrap
import asyncio

client = discord.Client()

token = "Discord-Token" # Enter Token here
myID = 1234567894012345678 # Enter Discord ID here

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.id == myID:
        if message.content.startswith("stego"):
                await StegoChat(message.channel.id)


async def StegoChat(channelid):
    channel = client.get_channel(channelid)
    while(True):
        text = input("Chat: ")
        if text.startswith("*"):
            normal = text[1:]
            await channel.send(normal)
        elif text == "":
            print("x")
        else:
            img = Image.open("black.jpg")
            pointsize = 30
            fillcolor = "white"
            shadowcolor = "black"
            font = ImageFont.truetype('Roboto-Bold.ttf', size=100)
            draw = ImageDraw.Draw(img)

            margin = offset = 40
            lines = textwrap.wrap(text, width=30)
            for line in lines:
                draw.text((margin, offset), line, font=font, fill=fillcolor)
                offset += font.getsize(line)[1]
             
            height = len(lines) * 100

            w = 1920
            h = 1080

            area = img.crop((0, 30, w, h-980+height))

            fname2 = "temp.png"
            area.save(fname2)

            await channel.send(file=discord.File(fname2))
            os.remove(fname2)

client.run(token, bot=False)
