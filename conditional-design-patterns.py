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
