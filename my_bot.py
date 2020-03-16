# created my client class for discord bot

import discord
from discord.ext import commands
from googlesearch import search
from redis_model import RedisDb

redis_obj=RedisDb("localhost","6379")

class MyClient(discord.Client):
    # on ready function will print the user who logged in
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # on_message will reply to user on some specific commands.
    # also i have put a condition if the author is sending message bot won't reply to that

    async def on_message(self, message):
        if message.author == client.user:
                return

        if message.content.startswith('hi'):
                await message.channel.send("hey")

        if message.content.startswith('!google'):
                query=message.content.replace("!google","").strip()
                for result in search(query,tld='co.in', num =5 ,start=0,stop=5,pause=2):
                        await message.channel.send(result)
                if "game" in query.lower():
                                redis_obj.add_recent_game(query)
        if message.content.startswith('!recent'):
                result_set=redis_obj.get_all_recent_game()
                for result in result_set:
                        await message.channel.send(result.decode('utf-8'))
