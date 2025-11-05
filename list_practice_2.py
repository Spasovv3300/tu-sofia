from random import randint  # Import randint for generating random numbers

try:
    # Ask user for the number of elements in the list
    n = int(input("Enter the number of elements between 10 and 50:"))
    if not (10 < n < 50):
        # Raise an error if input is not within the required range
        raise ValueError("Number of elements must be between 10 and 50.")

    mylst_1 = []  # First list
    # Generate random bounds for the interval [a, b]
    a = randint(-2500, -1300)
    b = randint(1111, 4444)

    counter = 0
    # Fill the list with numbers entered by the user
    while counter < n:
        number = int(input("Enter a number:"))
        # Only accept numbers within the random range
        if a <= number <= b:
            mylst_1.append(number)
            counter += 1
        else:
            print("Try again")

    # Count negative numbers whose tens digit is divisible by 4 or 5
    count_negative = 0
    for number in mylst_1:
        if number < 0:
            tens_digit = abs(number) // 10 % 10  # Extract tens digit
            if tens_digit % 4 == 0 or tens_digit % 5 == 0:
                count_negative += 1

    print("Count of negative numbers with tens digit divisible by 4 or 5:", count_negative)

    # Create a list of even two-digit numbers from mylst_1
    even_list = [number for number in mylst_1 if 9 <
                 abs(number) < 100 and number % 2 == 0]

    # Calculate average of these even numbers if any exist
    if even_list:
        average = sum(even_list) / len(even_list)
        print("Average:", average)
    else:
        print("There are no two-digit even numbers in mylst_1")

    # Create a second list with 3-digit numbers divisible by 3
    mylst_2 = [number for number in mylst_1 if 99 <
               abs(number) < 1000 and number % 3 == 0]

    print("New list:", mylst_2)

    # Count how many elements at even indices are odd numbers
    odd_counter = 0
    for i in range(0, len(mylst_2), 2):
        if mylst_2[i] % 2 == 1:
            odd_counter += 1

    print("The number of odd elements with even index is:", odd_counter)

    # Replace all elements at odd indices with 13
    for i in range(1, len(mylst_2), 2):
        mylst_2[i] = 13

    print("mylst_2 after the change:", mylst_2)

    # Compare the lengths of the two lists
    if len(mylst_1) != len(mylst_2):
        # If mylst_1 is longer, remove its first and last elements
        if len(mylst_1) > len(mylst_2):
            if len(mylst_1) > 2:  # Prevent error if list is too short
                del mylst_1[0]
                del mylst_1[-1]
        # If mylst_2 is longer, remove its first and last elements
        else:
            if len(mylst_2) > 2:
                del mylst_2[0]
                del mylst_2[-1]
    else:
        print("The two lists are equal in size")

    # Final output of both lists
    print("final mylst_1:", mylst_1)
    print("final mylst_2:", mylst_2)

# Error handling for invalid or unexpected inputs
except ValueError as ve:
    print("Value error:", ve)
except Exception as e:
    print("Unexpected error:", e)
