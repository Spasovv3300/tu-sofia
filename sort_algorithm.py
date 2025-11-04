# --- Bubble Sort Function ---
def bubble_sort(myList):
    # Outer loop runs for each element except the last one
    for i in range(len(myList) - 1):
        # Inner loop compares adjacent elements
        for j in range(len(myList) - i - 1):
            # If the current element is greater than the next one, swap them
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
    # Return the sorted list (ascending order)
    return myList


# --- Selection Sort Function ---
def selection_sort(myList):
    # Loop through each element in the list
    for i in range(len(myList) - 1):
        # Assume the current index has the minimum value
        min_index = i
        # Search for the smallest value in the remaining unsorted part
        for j in range(i + 1, len(myList)):
            if myList[j] < myList[min_index]:
                min_index = j  # Update the index of the new minimum
        # Swap the smallest found value with the current position
        myList[i], myList[min_index] = myList[min_index], myList[i]
    # Return the sorted list
    return myList


# --- Insertion Sort Function ---
def insertion_sort(myList):
    # Start from the second element (index 1)
    for i in range(1, len(myList)):
        insert_index = i
        current_value = myList[i]  # Value to be placed in correct position

        # Move elements greater than current_value one position ahead
        for j in range(i - 1, -1, -1):
            if myList[j] > current_value:
                myList[j + 1] = myList[j]
                insert_index = j  # Remember the new position
            else:
                break  # Stop when a smaller element is found

        # Place the current value at its correct position
        myList[insert_index] = current_value
    # Return the sorted list
    return myList


# --- Main Program ---

# Example list of numbers
firstList = [1, 6, 4, 3, 6, 8, 3, 2, 1, 11, 3]

# Sort the list using bubble sort
sorted_firstList = bubble_sort(firstList)

# Sort the list using Python’s built-in sorted() function (for comparison)
sorted_firstList2 = sorted(firstList)

# Print the list sorted by bubble sort
for i in sorted_firstList:
    print(i, end="|")
print()  # new line

# Print the list sorted by the built-in sorted() function
for i in sorted_firstList2:
    print(i, end="|")
print()  # new line

# Print the result of selection sort
print(selection_sort(firstList))

# Print the result of insertion sort
print(insertion_sort(firstList))
