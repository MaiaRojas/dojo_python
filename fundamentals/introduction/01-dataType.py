#variable declaration
num1 = 42
# Data type_Primitive_Number
num2 = 2.3 
#Data type_Primitive_Boolean
boolean = True
#Data type_Primitive_String
string = 'Hello World'
#Data type_Composite_List_initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#Data type_Composite_Dictionary_initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#Data type_Composite_Tuple_initialize
fruit = ('blueberry', 'strawberry', 'banana')
# Type check
print(type(fruit))
# Data type _ Composite_ List_Access value
print(pizza_toppings[1])
# Data type _ Composite_ List_Add value
pizza_toppings.append('Mushrooms')
#Data type _ Composite_Dictionary_access value
print(person['name'])
# Data type _ Composite_ dictionary_change value
person['name'] = 'George'
# Data type _ Composite_ dictionary_add_value
person['eye_color'] = 'blue'
# Data type _ Composite_tuple_access value
print(fruit[2])
#Conditional_if /else
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#Conditional_else if
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# For Loop
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
#while loop
x = 0
while(x < 5):
    print(x)
    x += 1
#Data type _composite_List_delete value
pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
#Data type _composite_Dictionary_delete value
person.pop('eye_color')
print(person)

# For loop / continue
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
# Function
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()
# Function /parameter
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
# Function / argument
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) // NameError: name <variable name> is not defined
# num3 = 72 // 
# fruit[0] = 'cranberry' - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) // - KeyError: 'favorite_team'
# print(pizza_toppings[7]) - IndexError: list index out of range
#   print(boolean) - IndentationError: unexpected indent
# fruit.append('raspberry') - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'pop'