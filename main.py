# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits

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
        available_large_boosts = [boost for boost in self.boosts if boost.large and boost.active]
        available_boosts = [boost for boost in self.boosts if boost.active]

        closest_large_boost = None
        closest_large_distance = 10000
        closest_distance = 10000

        closest_boost = None
        for boost in available_large_boosts:
            distance = (self.me.location - boost.location).magnitude()
            # print(distance)
            if closest_large_boost == None or distance < closest_large_distance:
                closest_large_boost = boost
        
        for boost in available_boosts:
            distance = (self.me.location - boost.location).magnitude()
            if closest_boost == None or distance < closest_distance:
                closest_boost = boost
        
        if self.me.boost =< 90 and closest_large_boost is not None:
            self.set_intent(goto(closest_large_boost.location))
            print("I want boost")
            return
        # if we're in front of the ball, retreat
        if is_in_front_of_ball:
            self.set_intent(goto(self.friend_goal.location))
            return

        target = {
            'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
            'away_from_our_net': (self.friend_goal.right_post, self.friend_goal.left_post)
        }
        hits = (find_hits(self, target))
        if len(hits['at_opponent_goal']) > 0:
            self.set_intent(hits['at_opponent_goal'][0])
            print(self.me.velocity)
            return
            
        if len(hits['away_from_our_net']) > 0:
            self.set_intent(hits['away_from_our_net'][0])
            print(self.me.velocity)
            return
        
       



