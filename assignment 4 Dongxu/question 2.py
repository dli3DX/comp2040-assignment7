input_string = input("Please enter a string:")

char_dict = {}

for char in input_string:
    if char in char_dict:
        char_dict[char] += 1
    else:
        char_dict[char] = 1

sorted_char_dict = dict(sorted(char_dict.items()))

for key, value in sorted_char_dict.items():
    print(key, ":", value)
