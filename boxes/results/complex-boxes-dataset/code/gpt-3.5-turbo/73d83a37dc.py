# Initial state of boxes
boxes = {
    0: ['butterfly', 'speaker'],
    1: ['grass', 'fish'],
    2: ['microwave', 'glove', 'leaf'],
    3: ['scarf', 'shark', 'glasses'],
    4: ['pot', 'sock', 'card', 'earring', 'thunder']
}

# Put the polish and the dog into Box 0.
boxes[0].append('polish')
boxes[0].append('dog')

# Put the beach and the controller and the truck into Box 3.
boxes[3].append('beach')
boxes[3].append('controller')
boxes[3].append('truck')

# Put the starfish into Box 1.
boxes[1].append('starfish')

# Remove the pot and the card from Box 4.
boxes[4].remove('pot')
boxes[4].remove('card')

# Swap the earring in Box 4 with the truck in Box 3.
boxes[4].remove('earring')
boxes[3].remove('truck')
boxes[4].append('truck')
boxes[3].append('earring')

# Replace the starfish and the fish and the grass with the dress and the console and the blender in Box 1.
boxes[1].remove('starfish')
boxes[1].remove('fish')
boxes[1].remove('grass')
boxes[1].append('dress')
boxes[1].append('console')
boxes[1].append('blender')

# Replace the glove with the skirt in Box 2.
boxes[2].remove('glove')
boxes[2].append('skirt')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")