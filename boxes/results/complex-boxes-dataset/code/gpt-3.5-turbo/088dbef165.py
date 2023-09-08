# Initial state of boxes
boxes = {
    0: [],
    1: ['fridge', 'submarine'],
    2: [],
    3: ['charger', 'jungle'],
    4: ['fish', 'boot', 'bear', 'car'],
    5: ['telescope', 'branch', 'seaweed', 'bowl', 'bird']
}

# Remove the seaweed and the bowl from Box 5.
boxes[5].remove('seaweed')
boxes[5].remove('bowl')

# Remove the jungle and the charger from Box 3.
boxes[3].remove('jungle')
boxes[3].remove('charger')

# Swap the car in Box 4 with the branch in Box 5.
boxes[4].remove('car')
boxes[5].remove('branch')
boxes[4].append('branch')
boxes[5].append('car')

# Put the flute and the mixer into Box 4.
boxes[4].append('flute')
boxes[4].append('mixer')

# Remove the boot and the branch and the mixer from Box 4.
boxes[4].remove('boot')
boxes[4].remove('branch')
boxes[4].remove('mixer')

# Swap the submarine in Box 1 with the telescope in Box 5.
boxes[1].remove('submarine')
boxes[5].remove('telescope')
boxes[1].append('telescope')
boxes[5].append('submarine')

# Move the fridge from Box 1 to Box 2.
boxes[1].remove('fridge')
boxes[2].append('fridge')

# Move the fridge from Box 2 to Box 4.
boxes[2].remove('fridge')
boxes[4].append('fridge')

# Replace the telescope with the planet in Box 1.
boxes[1].remove('telescope')
boxes[1].append('planet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")