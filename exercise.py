import sys


def even_odd(myList):
    even = list()
    odd = list()

    for i in myList:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd


def show(myList):
    for i in myList:
        print(i, end=" | ")
    print()


try:
    user_input = input("Enter your list separated by spaces: ")
    myList = [int(i) for i in user_input.split()]

    evenList, oddList = even_odd(myList)

    show(evenList)
    show(oddList)

except Exception as e:
    print("Error occured!")
    print(e)
    sys.exit(0)
