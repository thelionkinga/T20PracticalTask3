# Declare a variable to store the total sum of numbers
total = 0

# Continue looping until the user enters -1 or non-numeric input
while True:
    # Request user to enter a number
    number_input = input("Please enter a number (type -1 to stop): ")

    # Check if the entered number is -1 to exit the loop
    if number_input == "-1":
        break

    try:
        # Convert user input to an integer
        number = int(number_input)

        # Add the entered number to the total sum
        total += number

    except ValueError:
        # Handle the case when non-numeric input is entered
        print("Invalid input. Please enter a valid number.")

# Print the total sum when the loop exits
print(f"The sum of the entered numbers is: {total}.")
