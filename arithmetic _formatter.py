# input for user to type
# we can add error statements afterwards another section for this
# first looking at the example there is 4 line of text so itll require 4 prints
# the 1st line is all numbers from the first line and spaces
# the 2nd line is the operation and the 2nd number
# the 3rd line is a number of dashes based of the indexes of the formula
# the 4th line is the answer
# just looking at it i see that i should organize it into 5 list
# split the input by the comma and make into individual formulas so input="x+x,y+y,..." becomes formulas=("x+x","y+y",...)
# split the list of formulas into 3 list first num,operations and 2nd num im thinking list to an index ill do a loop to locate the operant index and split it into three list base of that index
# in addition there may be issue with the input and spaces so i'll delete all spaces in the orignal input before
# so the first thing is determine the number of spaces needed for the first row so we are told there are 4 spaces in between each formula. and there most be a space between the operand  and the largest length number
# str are just formulas since there no operation in the first row i would set space=" " so 2*space+(number with the larger index - first num index)+first num index number+4*space
# to make the rows add up do a loop and row=row+2*space+(number with the larger index - index of first num)+smaller index number+4*space
# to find the max length between the two numbers just do an if then statement
# 2nd row will be same concept but since there is an operation symbol there so formula is so operation+space+(number with the larger index - first num index)+first num index number+4*space loop
# 3rd row will be even easier  met a variable dash="-" dash*(len of formula)+4*space then loop
# input to ask if the user wants the answers
# i would set variables to set each line equal so that it'll be if yes print=firstrow print+2ndrow,etc
# 4th row answer is the answer make a new list for answer= eval then str it
# same concept as before do space*(len of formula-len of answer)+answer loop it
x = 0
rowone = ""
rowtwo = ""
rowthree = ""
rowfour = ''
dash = "-"
math = ""
space = " "
seperation = "    "
listofoperandontop = []
listofoperandonbot = []
mathoperation = []
information = "111+1,2222-22,333+333,4+4444,5-55"
correct_length=True
Information_entered=True
numbers_r_digits=True
# if we were letting user input we would simply have an input then remove any spaces and read error if they type in non numbers
formulas = information.split(",")
answer = []
for operand in formulas:
    if operand.find("+") > 0:
        mathsym = (operand.find("+"))
    else:
        mathsym = (operand.find("-"))
    # elif operand.find("*")>0:
    # mathsym=(operand.find("*"))
    # else:
    # mathsym=(operand.find("/"))
    answer.append(str(eval(operand)))
    listofoperandontop.append(operand[0:mathsym])
    listofoperandonbot.append(operand[mathsym + 1:])
    mathoperation.append(operand[mathsym])
if len(formulas) > 5:
    print("Error: Too many problems.")
    Information_entered = False
for numbers in listofoperandonbot+listofoperandontop:
    if correct_length==False and numbers.isdigit()== False:
        break
    if correct_length==True and len(numbers) > 4:
        print("Error: Numbers cannot be more than four digits.")
        correct_length = False
        Information_entered = False
    if numbers.isdigit()== False and numbers_r_digits==True:
        print("Error: Numbers must only contain digits.")
        Information_entered = False
        numbers_r_digits = False
if information.find("*") > 0:
    print("Error: Operator must be '+' or '-'.")
    Information_entered = False
elif information.find("/") > 0:
    print("Error: Operator must be '+' or '-'.")
    Information_entered = False
if Information_entered == False:
    print("Wrong format for the problems you have entered ")
else:
    while x != (len(formulas)):
        if len(listofoperandontop[x]) > len(listofoperandonbot[x]):
            maxlen = len(listofoperandontop[x])
        else:
            maxlen = len(listofoperandonbot[x])
        # if we were to make a calculator for multiplication and division we would just compare the len to the answer too to find max len
        rowone += 2 * space + (maxlen - len(listofoperandontop[x])) * space + listofoperandontop[x] + seperation
        rowtwo += mathoperation[x] + space + (maxlen - len(listofoperandonbot[x])) * space + listofoperandonbot[
            x] + seperation
        rowthree += (maxlen + 2) * dash + seperation
        if float(answer[x])>=0:
            rowfour += space * 2 + (maxlen - len(answer[x])) * space + answer[x] + seperation
        else:
            rowfour += space + (maxlen - len(answer[x])) * space + answer[x] + seperation
        x += 1
    print(rowone)
    print(rowtwo)
    print(rowthree)
    response = input("Type yes to see the answers: ")
    if response == "yes":
        print(rowone)
        print(rowtwo)
        print(rowthree)
        print(rowfour)

# way to add division is to limit the decimal place by using float and limit the decimal
# if we use multiplication we can do if statement during the for loop so large numbers would be transformed to "number*E"  so it takes less space


