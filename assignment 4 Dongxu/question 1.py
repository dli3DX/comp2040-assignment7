print("Please enter five integers:")

input_numbers = []

while len(input_numbers) < 5:
    try:
        number = int(input())
        input_numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter an integer.")

original_numbers = input_numbers.copy()

for i in range(len(input_numbers)):
    for j in range(i + 1, len(input_numbers)):
        if input_numbers[i] > input_numbers[j]:
            input_numbers[i], input_numbers[j] = input_numbers[j], input_numbers[i]

print("Original list:", original_numbers)
print("Sorted list:", input_numbers)
