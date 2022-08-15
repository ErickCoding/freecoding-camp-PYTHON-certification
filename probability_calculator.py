import random


class Frontend:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"

    @classmethod
    def new_or_old_hat(cls):
        new_old_hat = int(input("Would you like to create a new hat or choose and old one?\n1. New\n2. Old\n"))
        return new_old_hat

    @classmethod
    def color_question(cls):
        user_input_color = input("What color of the ball would you like?\n")
        return user_input_color

    @classmethod
    def number_of_balls_question(cls):
        user_input_ball_quantity = int(input("How many of balls would you want?\n"))
        return user_input_ball_quantity

    @classmethod
    def expected_color(cls):
        print("what color ball and quantity are you trying to get?")
        user_input_color = input("What color of the ball would you like?\n")
        return user_input_color

    @classmethod
    def done_with_hat(cls):
        are_you_done = int(input("Would you like to add more balls?\n1. Yes\n2. No\n"))
        return are_you_done

    @classmethod
    def action_question(cls):
        user_action = int(input("What would you like to?\n1. Draw random ball(s)\n2. Test the combination possibility\n"))   #yea i know bad wording
        return user_action

    @classmethod
    def draw_amount(cls):
        how_many_draws = int(input("How many times would you like to draw from the hat?\n"))
        return how_many_draws

    @classmethod
    def number_of_experiments(cls):
        experiment_quantity = int(input("How many times would you like to experiment?\n"))
        return experiment_quantity

    @classmethod
    def choose_old_hat(cls):
        choices = "Which hat would you like?\n"
        for object in Hat.all_hats:
            choices = choices+str(object.id)+"."+object.name+" "+str(object.composition)+" \n"
        print(choices)
        user_choice = int(input())
        print(Hat.id_search(user_choice))
        return Hat.id_search(user_choice)


class App:
    @classmethod
    def system_procedure(cls):
        while True:
            print("hello welcome to Hats and Balls Probability Tester")
            if Frontend.new_or_old_hat() == 1:
                if Frontend.action_question() == 1:
                    print(App.drawing_from_hat(App.hat_creation(App.hat_detail()), Frontend.draw_amount()))
                else:
                    print(App.experiment(App.hat_creation(App.hat_detail()), Frontend.draw_amount(), Frontend.number_of_experiments(), App.expected_balls()))
            else:
                if Frontend.action_question() == 1:
                    print(App.drawing_from_hat(Frontend.choose_old_hat(), Frontend.draw_amount()))
                else:
                    print(App.experiment(Frontend.choose_old_hat(), Frontend.draw_amount(), Frontend.number_of_experiments(), App.expected_balls()))

    @staticmethod
    def hat_detail():
        hat_ball_dictionary = {}
        hat_completed = False
        while hat_completed != True:
            color = Frontend.color_question()
            quantity = Frontend.number_of_balls_question()
            hat_ball_dictionary[color] = quantity
            if Frontend.done_with_hat() == 2:
                hat_completed = True
        return hat_ball_dictionary

    @staticmethod
    def hat_creation(hat_detail):
        new_hat = Hat(**hat_detail)
        print(new_hat)
        return new_hat

    @staticmethod
    def drawing_from_hat(hat_creation, draw_amount):
        return hat_creation.draw(draw_amount)+"ball(s) was drawn in this order."

    @staticmethod
    def expected_balls():
        print("what color ball and quantity are you hoping to get?")
        expectations_dictionary = {}
        expectations_complete = False
        while expectations_complete != True:
            color = Frontend.color_question()
            quantity = Frontend.number_of_balls_question()
            expectations_dictionary[color] = quantity
            if Frontend.done_with_hat() == 2:
                expectations_complete = True
        return expectations_dictionary

    @staticmethod
    def experiment(hat, draw_amount, number_experiments, expected_balls):
        if sum(expected_balls.values()) > draw_amount:
            return "0%"
        else:
            expected_is_true = 0
            for experiment in range(number_experiments):
                balls_drawn_completely = True
                for key, value in expected_balls.items():
                    draw_result = hat.draw(draw_amount)
                    print(draw_result)
                    if draw_result.count(key) < value:
                        balls_drawn_completely = False
                        continue
                if balls_drawn_completely == True:
                    expected_is_true += 1
            experiment_percent = f"{expected_is_true*100/number_experiments}%"
            return experiment_percent


class Hat:
    id = 0
    all_hats = []

    @classmethod
    def id_assignment(cls):
        cls.id += 1
        return cls.id

    @staticmethod
    def balls(**kwargs):
        color_quantity = {}
        for color, quantity in kwargs.items():
            color_quantity[color] = quantity
        return color_quantity

    def __init__(self, **kwargs):
        self.name = f"hat{Hat.id_assignment()}"
        self.composition = Hat.balls(**kwargs)
        self.id = Hat.id
        Hat.all_hats.append(self)

    def __repr__(self):
        return f"{self.name, self.composition}"

    def content(self):
        content_list = []
        for key, value in self.composition.items():
            for number in range(value):
                content_list.append(key)
        return content_list

    def draw(self, number_of_draws):
        remaining_balls = self.content()
        draw_balls = ""
        if number_of_draws % len(remaining_balls) == 0:
            for count in range(number_of_draws):
                random.shuffle(remaining_balls)
                draw_balls = draw_balls + remaining_balls.pop() + " "
        else:
            for count in range(number_of_draws % len(remaining_balls)):
                random.shuffle(remaining_balls)
                draw_balls = draw_balls + remaining_balls.pop() + " "
        return draw_balls

    @staticmethod
    def id_search(id):
        for object in Hat.all_hats:
            if object.id == id:
                return object


object_one = Hat(blue=1, red=2)
object_two = Hat(green=1, orange=2, yellow=1)
App.system_procedure()
#dictionary={}
#dictionary["blue"]=1
#dictionary["red"]=2


#object = Hat(blue=1, red=2)
#print(object.name)
#print(object.composition)
#print(object.id - 1)
#print(object.content())
#print(object.draw(4))
#object_two=Hat(**dictionary)
#print(object_two.name)
