from random import randint

# Ask for a valid n between 25 and 45
while True:
    try:
        n = int(input("Enter n (between 25 and 45): "))
        if 25 <= n <= 45:
            break
        else:
            print("n must be between 25 and 45.")
    except ValueError:
        print("Invalid input! Please enter an integer.")
    except Exception as e:
        print("Unexpected error:", e)

# Generate random bounds for interval [p, q]
p = randint(-3700, -1600)
q = randint(2222, 3333)
print(f"Range for numbers: [{p}, {q}]")

lst_1 = []

# Fill lst_1 with n numbers within [p, q]
while len(lst_1) < n:
    try:
        num = int(input("Enter a whole number: "))
        if p <= num <= q:
            lst_1.append(num)
        else:
            print("Number out of range! Try again.")
    except ValueError:
        print("Invalid input, please enter an integer.")

# Count positive numbers whose hundreds digit is even
counter_positive = 0
for num in lst_1:
    if num > 0:
        hundreds_digit = abs(num) // 100 % 10
        if hundreds_digit % 2 == 0:
            counter_positive += 1

print("Positive numbers with even hundreds digit:", counter_positive)

# Find the index of the smallest number that gives remainder 3 when divided by 6
index_low_6 = None
for i in range(len(lst_1)):
    if lst_1[i] % 6 == 3:
        if index_low_6 is None or lst_1[i] < lst_1[index_low_6]:
            index_low_6 = i

if index_low_6 is not None:
    print("Index of smallest number with remainder 3 when divided by 6:", index_low_6)
else:
    print("No elements found with remainder 3 when divided by 6.")

# Create lst_2 with two-digit numbers divisible by 5
lst_2 = [i for i in lst_1 if 9 < abs(i) < 100 and i % 5 == 0]
print("List 2:", lst_2)

# Calculate the product of elements at odd indices
product = 1
for i in range(1, len(lst_2), 2):
    product *= lst_2[i]
print("Product of elements at odd indices in lst_2:", product)

# Delete all even elements with odd indexes from lst_2 (backward loop to avoid skipping)
for i in range(len(lst_2) - 1, -1, -1):
    if i % 2 == 1 and lst_2[i] % 2 == 0:
        del lst_2[i]

print("lst_2 after deleting even elements with odd indexes:", lst_2)

# Compare lengths and modify accordingly
if len(lst_1) > len(lst_2):
    if len(lst_1) >= 2:
        lst_1.insert(len(lst_1)//2, lst_1[0] + lst_1[-1])
elif len(lst_2) > len(lst_1):
    if len(lst_2) >= 2:
        lst_2.insert(len(lst_2)//2, lst_2[0] + lst_2[-1])
else:
    print("The two lists are equal in length.")

print("Final lst_1:", lst_1)
print("Final lst_2:", lst_2)
