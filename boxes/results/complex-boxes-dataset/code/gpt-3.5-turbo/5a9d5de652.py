# Initial state of boxes
boxes = {
    0: ['leaf', 'elephant'],
    1: [],
    2: ['drum', 'beach', 'bracelet', 'microwave', 'forest'],
    3: [],
    4: ['motorcycle'],
    5: ['telescope', 'key'],
    6: ['butterfly', 'card', 'rocket']
}

# Put the battery and the dog and the planet into Box 2.
boxes[2].append('battery')
boxes[2].append('dog')
boxes[2].append('planet')

# Move the planet from Box 2 to Box 3.
boxes[2].remove('planet')
boxes[3].append('planet')

# Remove the key and the telescope from Box 5.
boxes[5].remove('key')
boxes[5].remove('telescope')

# Put the piano and the bowl and the tiger into Box 1.
boxes[1].append('piano')
boxes[1].append('bowl')
boxes[1].append('tiger')

# Move the card and the butterfly and the rocket from Box 6 to Box 3.
boxes[6].remove('card')
boxes[6].remove('butterfly')
boxes[6].remove('rocket')
boxes[3].append('card')
boxes[3].append('butterfly')
boxes[3].append('rocket')

# Move the rocket and the card and the butterfly from Box 3 to Box 6.
boxes[3].remove('rocket')
boxes[3].remove('card')
boxes[3].remove('butterfly')
boxes[6].append('rocket')
boxes[6].append('card')
boxes[6].append('butterfly')

# Put the horn and the bird into Box 3.
boxes[3].append('horn')
boxes[3].append('bird')

# Replace the horn and the bird and the planet with the puzzle and the bracelet and the shirt in Box 3.
boxes[3].remove('horn')
boxes[3].remove('bird')
boxes[3].remove('planet')
boxes[3].append('puzzle')
boxes[3].append('bracelet')
boxes[3].append('shirt')

# Replace the shirt and the puzzle with the watch and the laptop in Box 3.
boxes[3].remove('shirt')
boxes[3].remove('puzzle')
boxes[3].append('watch')
boxes[3].append('laptop')

# Swap the dog in Box 2 with the rocket in Box 6.
boxes[2].remove('dog')
boxes[6].remove('rocket')
boxes[2].append('rocket')
boxes[6].append('dog')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")