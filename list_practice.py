def listFill(myList):
    i = 0

    while i < 10:
        element = int(input("Enter your element:"))
        if element > 0:
            myList.append(element)
            i += 1
        else:
            print("you entered inccorrect value type")

    return myList


def listCountOdd(myList):
    count = 0
    for i in myList:
        if i % 2 == 1:
            count += 1
    print(count)


def listAverage(myList):
    sum = 0
    for i in myList:
        sum += i
    return sum / len(myList)


def listSort(myList):
    for i in range(len(myList)):
        for j in range(len(myList) - i - 1):
            if myList[j] < myList[j + 1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]

    return myList


def listDelete(myList):
    for k in range(len(myList) - 1, -1, -2):
        if k % 2 == 0:
            del myList[k]

    return myList


lst10 = []
lst5 = []
# filling the list
lst10 = listFill(lst10)

# printing the count of odd values
listCountOdd(lst10)

# calculating the average
print("Average:", listAverage(lst10))

# creating a list with the even elements and reverse sorting it
evenList = [k for k in lst10 if k % 2 == 0]
evenList = listSort(evenList)

# assigning the five biggest elements to lst5 from evenList
# lst5 = listSort(lst5)
lst5 = evenList[:5]

# deleteing the elements with an even index from lst5
# lst5 = lst5[1::2]
lst5 = listDelete(lst5)
print(lst5)
