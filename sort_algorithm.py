def bubble_sort(myList):
    for i in range(len(myList) - 1):
        for j in range(len(myList) - i - 1):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
    return myList


def selection_sort(myList):
    for i in range(len(myList) - 1):
        min_index = i
        for j in range(i + 1, len(myList)):
            if myList[j] < myList[min_index]:
                min_index = j
        # min_value = myList.pop(min_index)
        # myList.insert(i, min_value)
        myList[i], myList[min_index] = myList[min_index], myList[i]
    return myList


def insertion_sort(myList):
    for i in range(1, len(myList)):
        insert_index = i
        current_value = myList[i]
        for j in range(i - 1, -1, -1):
            if myList[j] > current_value:
                myList[j+1] = myList[j]
                insert_index = j
            else:
                break
        myList[insert_index] = current_value
    return myList


firstList = [1, 6, 4, 3, 6, 8, 3, 2, 1, 11, 3]
sorted_firstList = bubble_sort(firstList)
sorted_firstList2 = sorted(firstList)  # sorted_firstList2.sort()

for i in sorted_firstList:
    print(i, end="|")

print()

for i in sorted_firstList2:
    print(i, end="|")

print()

print(selection_sort(firstList))

print(insertion_sort(firstList))
