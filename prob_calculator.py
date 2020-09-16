import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.balls = kwargs
        self.contents = [key for key, value in kwargs.items() for _ in range(value)] #Double List Comprehension used here :)
        # print(self.contents)

    def draw(self, count: int):
        removed = []
        if count > len(self.contents):
            return self.contents
        
        for _ in range(count):
            remove_ball = random.choice(self.contents)
            self.contents.remove(remove_ball)
            removed.append(remove_ball)

        return removed        
        

def count_balls(removed: list):
    count = {}
    for ball in removed:
        count[ball] = count.get(ball, 0) + 1
    return count

        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count_M = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        removed = hat_copy.draw(num_balls_drawn)
        removed = count_balls(removed)
        result = True
        for key, value in expected_balls.items():
            if key not in removed or removed[key] < expected_balls[key]:
                result = False
                break

        if result:
            count_M += 1

    return count_M / num_experiments




