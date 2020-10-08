import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for key,val in kwargs.items():
            for i in range(val):
                self.contents.append(key)

    def draw(self, num):
        removed = []
        num = len(self.contents) if num > len(self.contents) else num
        for i in range(num):
            chosen_item = self.contents[random.randint(0,len(self.contents)-1)]
            removed.append(chosen_item)
            self.contents.remove(chosen_item)
        return removed

#test = Hat(yellow=3, blue=2, green=6)

#print (test.draw(3))
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = {}
        for item in (hat_copy.draw(num_balls_drawn)):
            if item in drawn:
                drawn[item] += 1
            else:
                drawn[item] = 1
        #print(drawn)
        passes = 0
        for key in expected_balls:
            if key in drawn:
                if expected_balls[key] <= drawn[key]:
                    passes += 1
                    #print(passes)
        if passes == len(expected_balls):
            count += 1
    return count/num_experiments

    #print(hat_copy.contents)


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)