# Conditional design patterns (Khan Academy Python, Unit 2)

# capturing a range
percent = int(input("Enter quiz score (out of 100): "))

if percent == 100:
    print("Stellar!")
elif percent >= 90:
    print("Excellent work!")
elif percent >= 75:
    print("Nice job!")
else: 
    print("Great effort!")


# validating inputs
filename = input("What would you like to name the photo?")

if len(filename) < 3 or len(filename) > 20: 
    # clear out the filename if it's invalid.
    filename = ""
    print("Filename must be between 3 and 20 characters.")
else: 
    # photos are stored as JPEGs, so we add the file extension.
    filename = filename + ".jpeg"
    print("The file has been renamed to " + filename)


# Overwriting a default value
vehicle = input("Pick a vehicle: ")

speed = 5
acceleration = 5

# Players unlock mega vehicles by winning a race on every course.
if vehicle == "mega cycle":
    acceleration = acceleration + 4
elif vehicle == "mega kart":
    speed = speed + 2
    acceleration = acceleration + 2

print(
    "The " + vehicle + "has " + str(speed) + str(acceleration) + " acceleration."
)


# A program with two independent conditionals
purchase_price = 42.70
sale_price = float(input("How much did you sell for? "))

price_diff = round(abs(sale_price - purchase_price), 2)
if price_diff > purchase_price: 
    print("There was a huge change in value.")