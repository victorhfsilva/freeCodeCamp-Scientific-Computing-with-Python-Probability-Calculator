import copy
import random
# Consider using the modules imported above.

class Hat:
  contents = list()
  drawn_balls = list()

  # ** are used in named arguments
  def __init__(self, **kwargs):
    self.drawn_balls = list()
    self.contents = list()
    self.contents_dict = kwargs
    for key, value in kwargs.items():
      for number in range(value):
        self.contents.append(key)

  def draw(self,number_balls):
    if number_balls > len(self.contents):
      for drawn_ball in self.drawn_balls:
        self.contents.append(drawn_ball)
        self.drawn_balls.remove(drawn_ball)

    for i in range(number_balls):
      if number_balls > len(self.contents):
        raise Exception("Error: Not enough balls.")
      drawn_ball = random.choice(self.contents)
      self.contents.remove(drawn_ball)
      self.drawn_balls.append(drawn_ball)
    # print("Drawn Balls: ",self.drawn_balls)
    # print("Contents: ",self.contents)
    return(self.drawn_balls)
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_successful_experiments = 0

  for i in range(num_experiments):
    # Refill the hat before each experiment
    hat_copy = copy.deepcopy(hat)
    hat.draw(num_balls_drawn)
    experiment_successful = True
    for expected_ball, expected_number in expected_balls.items():
      if not expected_number <= hat.drawn_balls.count(expected_ball):
        experiment_successful = False
    if experiment_successful:
      num_successful_experiments += 1
    hat = hat_copy
  probability = num_successful_experiments / num_experiments
  
  return probability