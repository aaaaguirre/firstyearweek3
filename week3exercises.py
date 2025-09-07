# Ex1

# Inputs
hours = int(input("hours:"))
minutes = int(input("minutes:"))
seconds = int(input("seconds: "))

# Constants
SECONDS_PER_MIN = 60
MINS_PER_HOUR = 60
HOURS_PER_DAY = 24

# Processing
time_in_seconds = hours + minutes + seconds *(HOURS_PER_DAY * MINS_PER_HOUR * SECONDS_PER_MIN)

# Output
print("Total number of seconds", time_in_seconds)

# Ex2

# Inputs
radius = int(input("radius:"))

# Constants
PI = 3.14159

# Processing
area_of_circle = (PI * radius * 2)

# Output
print("The radius is:", radius, "and the area of the circle is:", area_of_circle)

# Ex3

# Inputs
word1 = input("Please enter the first word: ")
word2 = input("Please enter the second number: ")
word3 = input("Please enter the third number: ")

# Processing
acronym = word1[0] + word2[0] + word3[0]
acronym = acronym.upper()

# Outputs
print("The acronym is", acronym)
