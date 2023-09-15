box_0 = ['leaf', 'elephant']
box_1 = []
box_2 = ['drum', 'beach', 'bracelet', 'microwave', 'forest']
box_3 = []
box_4 = ['motorcycle']
box_5 = ['telescope', 'key']
box_6 = ['butterfly', 'card', 'rocket']

# Put the battery, dog, and planet into Box 2
box_2.extend(['battery', 'dog', 'planet'])

# Move the planet from Box 2 to Box 3
box_2.remove('planet')
box_3.append('planet')

# Remove the key and the telescope from Box 5
box_5.remove('key')
box_5.remove('telescope')

# Put the piano, bowl, and tiger into Box 1
box_1.extend(['piano', 'bowl', 'tiger'])

# Move the card, butterfly, and rocket from Box 6 to Box 3
box_6.remove('card')
box_6.remove('butterfly')
box_6.remove('rocket')
box_3.extend(['card', 'butterfly', 'rocket'])

# Move the rocket, card, and butterfly from Box 3 to Box 6
box_3.remove('rocket')
box_3.remove('card')
box_3.remove('butterfly')
box_6.extend(['rocket', 'card', 'butterfly'])

# Put the horn and bird into Box 3
box_3.extend(['horn', 'bird'])

# Replace the horn, bird, and planet with the puzzle, bracelet, and shirt in Box 3
box_3.remove('horn')
box_3.remove('bird')
box_3.remove('planet')
box_3.extend(['puzzle', 'bracelet', 'shirt'])

# Replace the shirt and puzzle with the watch and laptop in Box 3
box_3.remove('shirt')
box_3.remove('puzzle')
box_3.extend(['watch', 'laptop'])

# Swap the dog in Box 2 with the rocket in Box 6
box_2.remove('dog')
box_6.remove('rocket')
box_2.append('rocket')
box_6.append('dog')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)