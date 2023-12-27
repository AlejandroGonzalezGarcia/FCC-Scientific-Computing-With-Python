import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)
    
    def draw(self, n):
        if n > len(self.contents):
            return self.contents
        else:
            count_contents = {}
            count_draw = {}
            new_list = []
            draw_list = random.sample(self.contents, n)
            for colour in draw_list:
                count_draw[colour] = count_draw.get(colour,0) + 1
            for colour in self.contents:
                count_contents[colour] = count_contents.get(colour,0) + 1
            for colour in set(draw_list):
                count_contents[colour] = count_contents[colour] - count_draw[colour]
            for key, value in count_contents.items():
                for _ in range(value):
                    new_list.append(key)
            self.contents = new_list
            return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        count = 0
        balls_list = {}
        balls = hat_copy.draw(num_balls_drawn)
        for colour in balls:
            balls_list[colour] = balls_list.get(colour,0) + 1
        for colour in expected_balls.keys():
            if colour in set(balls):
                if expected_balls[colour] <= balls_list[colour]:
                    count += 1
        if count == len(expected_balls.keys()):
            M += 1

    probability = M / num_experiments
    return probability
