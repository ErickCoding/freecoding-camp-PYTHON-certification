import math
import datetime
class App:
    id=0
    all=[]
    def id_assignment(cls):
        cls.id+=1
        return cls.id

    def __init__(self,name):
        self.name=name
        self.id=App.id_assignment
        self.date=datetime
        App.all.append(self)

    def __repr__(self):
        return f"{self.name}"

    @classmethod
    def first_question(cls):
        name=input("What is Your Name?\n")
        return cls(name)
    @staticmethod
    def height_question():
        height=int(input("What is the Height of your Rectange? Only Whole numbers everything will be rounded down\n"))
        return (height)

    @staticmethod
    def width_question():
        width = int(input("What is the width of your Rectange? Only Whole numbers everything will be rounded down\n"))
        return (width)

    @staticmethod
    def recording_info():
        width=App.width_question()
        height=App.height_question()
        Rectangle(width,height)
        return(Rectangle.id)

    @staticmethod
    def second_shape_comparison(id):
        second_width = int(input("Tell us the width of the rectangle you want to see fit inside the original square"))
        second_height = int(input("Tell us the height of the rectangle you want to see fit inside the original square"))
        return Rectangle.get_amount_inside(id,second_width,second_height)

    @staticmethod
    def first_step():
        first_response = int(input("Hello what do you need assistance with? Please enter the number corresponding with the options.\n1. Find Area \n2. Find Perimeter \n3. Find Diagonal \n4. Draw Shape \n5. Compare Rectangles\n6. Exit\n"))
        return first_response

    @staticmethod
    def system_step(user_selection):
        if user_selection == 1:
            print(Rectangle.area_by_id(App.recording_info()))
        elif user_selection == 2:
            print(Rectangle.perimeter_by_id(App.recording_info()))
        elif user_selection == 3:
            print(Rectangle.diaganol_by_id(App.recording_info()))
        elif user_selection == 4:
            print(Rectangle.draw_a_rectangle_by_id(App.recording_info()))
        elif user_selection == 5:
            print(App.second_shape_comparison(App.recording_info()))
        else:
            exit()


    @classmethod
    def run_thru(cls):
        print("Hello this is Friendly Rectangle Helper Who Should Be Asleep Too but Its Not.")
        while True:
            App.system_step(App.first_step())


class Rectangle:
    id = 0
    all=[]
    @classmethod

    def id_assignment(cls):
        cls.id+=1
        return cls.id

    def __init__(self, width, height):
        self.width=int(width)
        self.height=int(height)
        if self.height == self.width:
            self.shape = "Square"
        else:
            self.shape = "Rectangle"
        self.id = Rectangle.id_assignment()
        Rectangle.all.append(self)

    def __repr__(self):
        return f"{self.shape}(width={self.width}, height={self.height})"

    @staticmethod
    def dimensions_by_id(id):
        for dimension in Rectangle.all:
            if dimension.id==id:
                return dimension


    @staticmethod
    def area_by_id(id):
        area=Rectangle.dimensions_by_id(id).width*Rectangle.dimensions_by_id(id).height
        return area

    @staticmethod
    def perimeter_by_id(id):
        if Rectangle.dimensions_by_id(id).shape == "Square":
            perimeter = Rectangle.dimensions_by_id(id).width * 2
        else:
            perimeter = Rectangle.dimensions_by_id(id).width * 2 +2* Rectangle.dimensions_by_id(id).height
        return perimeter

    @staticmethod
    def diaganol_by_id(id):
        diagnol = math.sqrt(Rectangle.dimensions_by_id(id).width ** 2 + Rectangle.dimensions_by_id(id).height**2)
        return diagnol

    @staticmethod
    def draw_a_rectangle_by_id(id):
        if Rectangle.dimensions_by_id(id).height>50 or Rectangle.dimensions_by_id(id).width>50:
            return "Shape to big to create image."
        else:
            shape=''
            current_height=1
            while current_height <= Rectangle.dimensions_by_id(id).height:
                shape+="*  "*Rectangle.dimensions_by_id(id).width+"\n"
                current_height += 1
            return shape

    @staticmethod
    def get_amount_inside(id,second_width,second_height):
        if second_height==second_width:
            second_shape = "square"
        else:
            second_shape = "rectangle"
        how_many_widths = int(Rectangle.dimensions_by_id(id).width/second_width)
        how_many_heights = int(Rectangle.dimensions_by_id(id).height/second_height)
        return f"{how_many_heights*how_many_widths} of the {second_shape}(width={second_width}, height={second_height}) will fit inside the {Rectangle.dimensions_by_id(id)})"

App.run_thru()


