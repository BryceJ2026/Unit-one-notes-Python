print("supercalifragilisticexpialidocious!")

# Variables store data

lucky_num = 67 #int
my_name = "Machine" #str
cash = 5.50 #float
is_rain = True #boolean
is_Sunny = False


#ConCATENATE string literal + string variable
greeting = my_name + "... I will cut you down, break you apart, splay the gore of your profane form across the STARS! I will grind you down until the SPARKS SCREAM FOR MERCY!"
print(greeting)

other_greeting =           """
                        CHICKEN JOCKEY
                           """
print(other_greeting)

f_string = f"My name is {my_name} and my lucky number is {lucky_num}"
print(f_string)


#FUNCTIONS are reusable recipes/processes
#Use the keyword def to DEFINE a new function


def helloworld():


    print("hello world I am a function")

#UN-indent to signal the END of that block
#CALL a void function (no output)
helloworld()


#Define a function with ARGUEMENTS (input) + RETURN (output)
def  multiply(x, y):
    result = x * y
    return result

#CALL a non void function (handle the OUTPUT)

five_times_three = multiply(6,7)
print(five_times_three)
# you can also call the functio directly in another
print(multiply(1,67)) # funcs evaluated fromINSIDE to OUTSIDE

# LiStS
# ordered, mutable sequences
empty_list = list()
class_roster = ["Bryce", "Finny", "Jackson", "Kevin", "Maia", "Natalie", "Paige"]
print(class_roster)


# Indexes start at 0
first_item = class_roster[0]
print(first_item)

#Update an item in a list, access by index
class_roster[2] = "Jack"
print(class_roster)

lottery_nums = [13, 7, 89, 99, 67, 23, 4]
print(sorted(lottery_nums, reverse=True))
print(lottery_nums)#sorted() does not modify OG list
#Sort IN PLACE -> modifies OG list
lottery_nums.sort()
print(lottery_nums)
class_roster.sort(reverse=True)
print(class_roster)

#List operations
class_roster.append("Alex")
class_roster.insert(0, "Zoie")
class_roster.remove("Zoie")
class_roster.pop() #remove last item

#Check if item exists in a list
print(67 in lottery_nums)

# ***TUPLES***
# immutable - can't change items
# useful for "snapshot" of a row of data
student = ('Bryce', 17, 'Neuroscience', 0.0)
print(student)
#student[3] = 2.6 CANT RE-ASSIGN ITEM!


# *** SETS ***

songs = {'Stranger', '3005', '7', '3', 'Mutt', 'Freeze', '3005'}
print(songs)

colors = ['blue', 'green', 'red', 'orange', 'purple', 'green', 'green']
print(set(colors))
#you can add/remove items
songs.add('Gypsy')
songs.add('Stranger') # duplicate
print(songs)

# *** DICTIONARIES ***
# mutable, but the KEYS can only be immutable types
# { key: value } pairs Keys must be UNIQUE
# unordered(No index, can't sort in place)
characters = {'Aelin': 'Assasin queen',
              'Karate Kid': 'pupil',
              'Mr.Miyagi':'sensei',
              'Phil Dunphy': 'Dad',
              'WALL-E': 'robot',
              'Princess Peach': 'damsel in distress',
              'Dexter': 'Serial killer'
              }
print(len(characters))
# dictionary with numerical keys, list values
grade_requirements = {9:['Bio'],
                    10:['Chem'],
                     11:['Physics', 'Math', 'English', 'PE'],
                      12:['Math', 'English', 'PE'] 
                      }

print(10 > 5)# True
print(5 > 10)# False
print(10<= 10)# True
print(7<= 5)# False
print(5 == 5) #True
print(5 != 5)# False
print('A' > 'b')# False
print('cat' < 'cot') # o is GREATER because it comes later
print('T'=='t') # False (casesensitive)
print('T' < 't') # True, capital letters come first


# Checking equality vs. identity
list_a = (1,2,3)
list_b = (1,2,3)
print(list_a==list_b)
print(list_a is list_b)
# Typically only ise "is" when comparing to Nonoe, True, False
boolean_a = True
print(boolean_a is not False)

#Compound boolean operators
boolean_b = True
boolean_c = False
print(boolean_a and boolean_b)
print(boolean_b and boolean_c)
print(boolean_b or boolean_c)
print(boolean_a and boolean_b or boolean_c)

def can_drive(age):
        if (age >= 17):
             print('DRIVE DRIVE DRIVE')

        elif (age == 16) :
             print('PERMIT PERMIT PERMIT')

        else:
             print('DRIVE ANYWAYS HAHAHAHA')




can_drive(14)

#ITERATION (repetition)
# while loop: run until a condition is no longer True
max = 10
counter = 6
while counter <= max:
     print("67")
     counter += 1

#for-in loop: iterates through a collection
for student in class_roster:
     print('MAKE IT STOP.')

     #for-in range
     #prints 0 until 3
     for num in range(4):
          print(num)

     for num in range(1,5):
          print(num)

     for num in range(10, 50, 5):
          print(num)
#BTW, python has a help function
#help(range)

#enumerate() lets you loop through index AND items
for index, item in enumerate(class_roster):
     print(f'Item: {item} is at index {index}')

for character, description in characters.items():
     # character represents the KEYS of this dict
     # description represents the VALURES of the dict
     print(f'{character} is a {description}')


#review: setting up a dictionary
hex_colors = {
     'red':'#FF0000',
     'blue':'#008000',
     'blue':'#0000FF'

}











     max_num = 10
counter_num = 6
while counter_num <= max_num:
     print(' BALATRO. JOKERS. HANDS. BLINDS. ANTES. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. BALATRO. JOKERS. HANDS. BLINDS. ANTES. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. BALATRO. JOKERS. HANDS. BLINDS. ANTES. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. BALATRO. JOKERS. HANDS. BLINDS. ANTES. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. BALATRO. JOKERS. HANDS. BLINDS. ANTES. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. BALATRO. JOKERS. HANDS. BLINDS. ANTES. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. BALATRO. JOKERS. HANDS. BLINDS. ANTES. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. BALATRO. JOKERS. HANDS. BLINDS. ANTES. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. BALATRO. JOKERS. HANDS. BLINDS. ANTES. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING. GAMBLING.')