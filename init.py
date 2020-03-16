# initialize the bot

from redis_model import RedisDb
from my_bot import MyClient
import CONFIG


TOKEN=CONFIG.TOKEN
if __name__=='__main__':
        redi_obj=RedisDb("localhost","6379")
        client = MyClient()
        client.run(TOKEN)