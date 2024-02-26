word = input('Enter a word: ').lower()
reversed_word = word[::-1]
is_palindrome = word == reversed_word
print(f'Forward: {word}')
print(f'Backward: {reversed_word}')
print(f'Is palindrome: {is_palindrome}')