from keep_alive import keep_alive
from phasmo_functions import * 
import discord
from discord.ext import tasks
import get_token
import logging
from os import system

# Logging
logging.basicConfig(filename="discord.log", level=logging.DEBUG, format= "| {asctime} | {levelname:<8} > {message}", style="{",filemode="w")

def debug(msg):
    logging.debug(msg)
def error(msg):
    logging.debug(msg)

# Token
def open_token():
    return get_token.open_token()
      
# Documentaton : https://discordpy.readthedocs.io/en/stable/search.html
BOT_USER_ID = 953791444726976584
MY_ID = 183743234084700160
command_prefix = ">>"
class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")
        self.bot_user : discord.User = await client.fetch_user(BOT_USER_ID)
      
    async def on_message(self, msg:discord.Message):
        if msg.author.id == self.bot_user.id:
          return
      
        print(f"Message from guild \"{msg.channel.guild.name}\" -> {msg.author}: {msg.content}")
        
        # Check messages
        msg_lower = str(msg.content).lower()
        
        # Check if is command
        if msg_lower.startswith(command_prefix):
            # Is command
            command_arguments = msg_lower.split(" ")
            number_of_arguments = len(command_arguments)
            
            if msg_lower.startswith(f"{command_prefix}help") == True:
                await self.send_message(msg.channel.id, f"**Commands:**\
                                                        \n      **>>help** ~> Generates this menu.\n\
                                                        \n      **>>generatepartialosu (name) (type)** ~> Mixes osu/phasmophobia names. You can set the name/surname by typing what name you want at the **(name) argument** and name/surname at the **(type) argument**\n\
                                                        \n      **>>generatefullphasmo** ~> Generate full phasmophobia name.\n\
                                                        \n      **>>roll (max_number)** ~> Generates random number between 1 and **(max_number) argument**. **(max_number) argument** defaults to 100")
                
            elif msg_lower.startswith(f"{command_prefix}generatepartialosu") == True:
                # Check arguments
                if number_of_arguments == 1:
                    name, err = generate_partial_osu(first_name="", second_name="")
                if number_of_arguments == 2:
                    await self.send_error_message(msg.channel.id , "No **(type)** specified!")
                    return
                elif number_of_arguments >= 3:
                    if command_arguments[2] == "name":
                        name, err = generate_partial_osu(first_name=command_arguments[1].title(), second_name="")
                    elif command_arguments[2] == "surname":
                        name, err = generate_partial_osu(first_name="", second_name=command_arguments[1].title())
                    else:
                        await self.send_error_message(msg.channel.id , "Invalid **(type)**!")
                        return
                        
                if err != None:
                    await self.send_message(msg.channel.id, f"**Error:** {err}")
                    return
                    
                await self.send_message(msg.channel.id, f"**Name generated:** {name}")
                
            elif msg_lower.startswith(f"{command_prefix}generatefullphasmo") == True:
                name, err = generate_full_phasmo()
                await self.send_message(msg.channel.id, f"**Name generated:** {name}")
                
            elif msg_lower.startswith(f"{command_prefix}roll") == True:
                if number_of_arguments >= 2:
                    roll_result, err = osu_roll(command_arguments[1])
                else:
                    roll_result, err = osu_roll()
                    
                if err != None:
                    await self.send_error_message(msg.channel.id, f"{err}")
                    return
                
                await self.send_message(msg.channel.id, f"**Number generated:** {roll_result}")
                if roll_result == 727:
                    await self.send_message(msg.channel.id, f"**THE FUCKING FUNNY**")
                    await self.send_message(msg.channel.id, f"**NOOOOOOOOOOOOOOOO**")
                
            else:
                await self.send_error_message(msg.channel.id, f"Unknown command, type **{command_prefix}help** to list all commands!")
            
            
        
           
    # Use this Function with await, Ex: await send_message(id, msg) 
    async def send_message(self, channel_id, msg):
        channel = self.get_channel(channel_id)
        await channel.send(msg)

    async def send_error_message(self, channel_id, msg):
        await self.send_message(channel_id, f"**Error:** {msg}")
# Keep bot alive when using repl.it
keep_alive()

TOKEN = open_token()

client = MyClient()

try:
    client.run(TOKEN)
except:
    print("Restarting")
    system("python restarter.py")
    system("kill 1")