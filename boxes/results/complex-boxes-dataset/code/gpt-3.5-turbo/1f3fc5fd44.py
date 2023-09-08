# Initial state of boxes
boxes = {
    0: ['horn', 'coin', 'motorcycle'],
    1: ['note'],
    2: ['keyboard', 'elephant', 'truck', 'paint'],
    3: ['ring', 'toaster'],
    4: ['scarf', 'spoon', 'necklace', 'flute', 'camera'],
    5: ['rocket'],
    6: ['laptop', 'gloves', 'glove', 'coral'],
    7: [],
    8: ['glasses'],
    9: ['boat', 'console', 'shoes']
}

# Swap the note in Box 1 with the motorcycle in Box 0.
boxes[0].remove('motorcycle')
boxes[1].remove('note')
boxes[0].append('note')
boxes[1].append('motorcycle')

# Swap the glasses in Box 8 with the note in Box 0.
boxes[0].remove('note')
boxes[8].remove('glasses')
boxes[0].append('glasses')
boxes[8].append('note')

# Put the tie into Box 1.
boxes[1].append('tie')

# Remove the flute and the necklace from Box 4.
boxes[4].remove('flute')
boxes[4].remove('necklace')

# Remove the keyboard and the elephant and the truck from Box 2.
boxes[2].remove('keyboard')
boxes[2].remove('elephant')
boxes[2].remove('truck')

# Put the chair into Box 9.
boxes[9].append('chair')

# Move the rocket from Box 5 to Box 3.
boxes[5].remove('rocket')
boxes[3].append('rocket')

# Replace the coral with the charger in Box 6.
boxes[6].remove('coral')
boxes[6].append('charger')

# Put the beach into Box 2.
boxes[2].append('beach')

# Remove the ring and the toaster from Box 3.
boxes[3].remove('ring')
boxes[3].remove('toaster')

# Remove the note from Box 8.
boxes[8].remove('note')

# Swap the rocket in Box 3 with the motorcycle in Box 1.
boxes[1].remove('motorcycle')
boxes[3].remove('rocket')
boxes[1].append('rocket')
boxes[3].append('motorcycle')

# Remove the tie and the rocket from Box 1.
boxes[1].remove('tie')
boxes[1].remove('rocket')

# Move the coin and the glasses from Box 0 to Box 6.
boxes[0].remove('coin')
boxes[0].remove('glasses')
boxes[6].append('coin')
boxes[6].append('glasses')

# Move the paint and the beach from Box 2 to Box 6.
boxes[2].remove('paint')
boxes[2].remove('beach')
boxes[6].append('paint')
boxes[6].append('beach')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")