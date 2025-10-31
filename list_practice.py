# Function to fill a list with 10 positive integer elements
def listFill(myList):
    i = 0
    while i < 10:
        # Ask the user for input and convert it to an integer
        element = int(input("Enter your element:"))
        
        # Check if the entered number is positive
        if element > 0:
            myList.append(element)  # Add the element to the list
            i += 1  # Move to the next iteration
        else:
            print("You entered an incorrect value type")  # Error message for non-positive numbers

    return myList  # Return the filled list


# Function to count and print how many odd numbers are in the list
def listCountOdd(myList):
    count = 0
    for i in myList:
        if i % 2 == 1:  # Check if the number is odd
            count += 1
    print(count)  # Print the total number of odd elements


# Function to calculate the average of all numbers in the list
def listAverage(myList):
    sum = 0
    for i in myList:
        sum += i  # Add all elements
    return sum / len(myList)  # Return average value


# Function to sort the list in descending order using bubble sort
def listSort(myList):
    for i in range(len(myList)):
        for j in range(len(myList) - i - 1):
            # Swap elements if the left one is smaller than the right one
            if myList[j] < myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
    return myList  # Return the sorted list


# Function to delete elements that have even indices (starting from 0)
def listDelete(myList):
    # Loop backwards to safely delete elements without index shifting issues
    for k in range(len(myList) - 1, -1, -2):
        if k % 2 == 0:
            del myList[k]  # Delete element at even index
    return myList  # Return the updated list


# Initialize two empty lists
lst10 = []
lst5 = []

# Fill lst10 with 10 user-provided positive numbers
lst10 = listFill(lst10)

# Print how many odd numbers are in lst10
listCountOdd(lst10)

# Calculate and print the average of the numbers in lst10
print("Average:", listAverage(lst10))

# Create a new list with only even numbers from lst10
evenList = [k for k in lst10 if k % 2 == 0]

# Sort the even numbers in descending order
evenList = listSort(evenList)

# Take the first 5 biggest even elements and assign them to lst5
lst5 = evenList[:5]

# Delete elements with even indices from lst5
lst5 = listDelete(lst5)

# Print the final list
print(lst5)
