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