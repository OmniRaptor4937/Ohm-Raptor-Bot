# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits
import random

class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        if self.intent is not None:
            return
        ball_y_location = (self.ball.location.y)
        me_y_location = (self.me.location.y)
        ball_foe_goal = abs(ball_y_location - self.foe_goal.location.y)
        me_foe_goal_y = abs(self.me.location.y - self.foe_goal.location.y)
        me_foe_goal_x = abs(self.me.location.x - self.foe_goal.location.x)
        me_friend_goal_y = abs(self.me.location.y - self.friend_goal.location.y)
        is_in_front_of_ball = ball_foe_goal > me_foe_goal_y
        

        if self.kickoff_flag:
            self.set_intent(kickoff())
            print(self.intent)
            return
        #Goto closest Large Boost
        closest_boost = self.get_closest_large_boost()
        if closest_boost is not None:
            self.set_intent(goto(closest_boost.location))

        if self.is_in_front_of_ball():
            self.set_intent(goto(self.friend_goal.location, vector=self.get_closest_large_boost().location))


        target = {
            'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
            'away_from_our_net': (self.friend_goal.right_post, self.friend_goal.left_post)
        }
        hits = (find_hits(self, target))

        rando = []
        length = len(rando)
        for i in 'at_opponent_goal':
            rando.append(i)
        choice=random.randint(0, length)
        if len(hits['at_opponent_goal']) > 0:
 
            self.set_intent(hits['at_opponent_goal'][choice])
            print(0)
            return


        ronda = []
        gen = len(ronda)
        for i in 'away_from_our_net':
            ronda.append(i)
        noice=random.randint(0, gen)                                                          
        if len(hits['away_from_our_net']) > 0:

            self.set_intent(hits['away_from_our_net'][noice])
            print(1)
            return
        
        
       



