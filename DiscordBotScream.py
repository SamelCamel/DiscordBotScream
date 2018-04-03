import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

#READ PLS
#libraries that need to be installed using pip:
#PyNaCl, discord.py
#You will also need to download ffmpeg and add the ffmpeg.exe to your PATH variables
#This build uses Python 3

token = '' #put ur bot token here, received from Discord's developer portal
prefix = '!'  #character(s) before a command so the bot recognizes if a message is supposed to be a command

#opus is the library used to connect and play sound in voice channels
discord.opus.load_opus("C:\\") #file path to opus library goes here. In my computer it was called "libopus-0.x86.dll". It took me hours to find c:
if(discord.opus.is_loaded()):
    print("Opus loaded successfully!")
else:
    print("Opus failed to load. You shouldn't even see this message cause python will assault your eyes with error messages if opus doesnt load")


client = commands.Bot(command_prefix=prefix)
#--------------------------------------------------------------------------
@client.event
async def on_message(message):
        
    if(message.content == "owo"): #checks if any message sent in the server is "owo"
        for channel in client.get_all_channels(): #scrolls through all the channels, checks if they are voice channels, then plays the sound
            if(str(channel.type) == "voice"):
                voice = await client.join_voice_channel(channel)
                
                player = voice.create_ffmpeg_player("sounds\scream.wav") # file path to sound file
                player.start()
                while(player.is_playing()):
                    time.sleep(1)
                await voice.disconnect()

                #note: sound file can be any length, this code accounts for length and just waits until the entire thing is played


client.run(token)
