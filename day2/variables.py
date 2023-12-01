# Day 2: 30 Days of python programming

# Exercise 1

first_name = "Ganiu"
last_name = "Quadri"
full_name = "Quadri Ganiu"
country = "Nigeria"
city = "Kano"
age = 25
year = 2023
is_married = False
is_true = True
is_light_on = False

# Multiple variables on a single line
religion, gender, academy_level = "islam", "male", 400


# Exercise 2
# 1
print(type(first_name))     # string
print(type(last_name))      # string
print(type(full_name))      # string
print(type(country))        # string
print(type(city))           # string
print(type(age))            # int
print(type(year))           # int
print(type(is_married))     # boolean
print(type(is_true))        # boolean
print(type(is_light_on))    # boolean

# 2
print('First name length:', len(first_name))

# 3
print('Compare length of first to last name')
print('equals:',len(first_name) == len(last_name))
print('greater:',len(first_name) > len(last_name))
print('less:',len(first_name) < len(last_name))

# 4
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# 5
radius = float(input("Enter radius of a circle: "))
area_of_circle = 3.14 * radius ** 2     # πr²
circum_of_circle = 2 * 3.14 * radius    # 2πr

# 6
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

# 7
help('keywords')