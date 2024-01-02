def calculate_percentages():
    while True:
        # Get user input
        num = input("Enter a number with decimal places (or 'q' to quit): ")
        
        # Check if the user wants to quit
        if num.lower() == 'q':
            break

        num = float(num)

        # Calculate percentages
        fifty_percent = num * 0.50
        thirty_percent = num * 0.30
        twenty_percent = num * 0.20

        # Output the results
        print("50% of the input number is: {:.2f}".format(fifty_percent))
        print("30% of the input number is: {:.2f}".format(thirty_percent))
        print("20% of the input number is: {:.2f}".format(twenty_percent))

# Call the function
calculate_percentages()
