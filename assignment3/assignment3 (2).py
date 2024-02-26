animal_dict = {'dog': 0, 'cat': 1, 'frog': 2}
labels = []
for _ in range(5):
    animal = input('Enter an animal (dog, cat, or frog): ')
    while animal not in animal_dict:
        print('Invalid animal. Please enter dog, cat, or frog.')
        animal = input('Enter an animal (dog, cat, or frog): ')
    labels.append(animal)
encoded_labels = [animal_dict[animal] for animal in labels]
print(f'Labels: {labels}')
print(f'Encoded Labels: {encoded_labels}')
