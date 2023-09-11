# Initial state of boxes
boxes = {
    0: ['cow', 'planet'],
    1: ['microscope', 'glove', 'helmet'],
    2: ['bell', 'shoe', 'desert', 'card', 'basket'],
    3: ['note', 'jungle', 'seaweed', 'toaster'],
    4: [],
    5: ['tiger', 'coin', 'tree'],
    6: ['sock', 'lipstick', 'river']
}

# Remove the sock and the lipstick and the river from Box 6.
boxes[6].remove('sock')
boxes[6].remove('lipstick')
boxes[6].remove('river')

# Swap the cow in Box 0 with the desert in Box 2.
boxes[0].remove('cow')
boxes[2].remove('desert')
boxes[0].append('desert')
boxes[2].append('cow')

# Put the shirt and the dolphin into Box 3.
boxes[3].append('shirt')
boxes[3].append('dolphin')

# Swap the toaster in Box 3 with the glove in Box 1.
boxes[3].remove('toaster')
boxes[1].remove('glove')
boxes[3].append('glove')
boxes[1].append('toaster')

# Remove the note from Box 3.
boxes[3].remove('note')

# Replace the planet with the shampoo in Box 0.
boxes[0].remove('planet')
boxes[0].append('shampoo')

# Remove the microscope and the toaster and the helmet from Box 1.
boxes[1].remove('microscope')
boxes[1].remove('toaster')
boxes[1].remove('helmet')

# Move the card from Box 2 to Box 3.
boxes[2].remove('card')
boxes[3].append('card')

# Swap the shampoo in Box 0 with the coin in Box 5.
boxes[0].remove('shampoo')
boxes[5].remove('coin')
boxes[0].append('coin')
boxes[5].append('shampoo')

# Remove the shoe from Box 2.
boxes[2].remove('shoe')

# Swap the cow in Box 2 with the coin in Box 0.
boxes[2].remove('cow')
boxes[0].remove('coin')
boxes[2].append('coin')
boxes[0].append('cow')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")