# created redis model for data storage

import redis

class RedisDb:

        # Constructor will make connection to the redis db
        def __init__(self,host,port):
                self.obj=redis.StrictRedis(host=host,port=port)

        # add_recent_game is to add the game in db searched by user on bot (only related to games)
        def add_recent_game(self,game):
                self.obj.lpush("recent_game",game)

        # get_all_recent_game is to fetch out the recent searches made by user(only related to games)
        def get_all_recent_game(self,):
                return self.obj.lrange("recent_game",0,-1)