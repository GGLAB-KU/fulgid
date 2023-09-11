# Initial state of boxes
boxes = {
    0: ['button', 'gloves'],
    1: ['needle', 'headphone', 'tiger', 'submarine'],
    2: ['wallet'],
    3: ['sandals'],
    4: ['comet', 'bracelet', 'dress', 'grass', 'microscope'],
    5: ['branch'],
    6: ['car', 'rock', 'usb'],
    7: ['glove', 'cup', 'fridge'],
    8: ['shoes', 'pan', 'skirt']
}

# Remove the glove and the cup and the fridge from Box 7.
boxes[7].remove('glove')
boxes[7].remove('cup')
boxes[7].remove('fridge')

# Remove the branch from Box 5.
boxes[5].remove('branch')

# Empty Box 0.
boxes[0] = []

# Move the tiger from Box 1 to Box 4.
boxes[1].remove('tiger')
boxes[4].append('tiger')

# Remove the usb from Box 6.
boxes[6].remove('usb')

# Swap the wallet in Box 2 with the rock in Box 6.
boxes[2].remove('wallet')
boxes[6].remove('rock')
boxes[2].append('rock')
boxes[6].append('wallet')

# Remove the rock from Box 2.
boxes[2].remove('rock')

# Move the needle from Box 1 to Box 5.
boxes[1].remove('needle')
boxes[5].append('needle')

# Put the dress and the fork into Box 6.
boxes[6].append('dress')
boxes[6].append('fork')

# Swap the skirt in Box 8 with the wallet in Box 6.
boxes[8].remove('skirt')
boxes[6].remove('wallet')
boxes[8].append('wallet')
boxes[6].append('skirt')

# Move the shoes and the pan and the wallet from Box 8 to Box 2.
items_to_move = ['shoes', 'pan', 'wallet']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[2].append(item)

# Replace the tiger with the shampoo in Box 4.
boxes[4].remove('tiger')
boxes[4].append('shampoo')

# Empty Box 5.
boxes[5] = []

# Remove the shampoo and the microscope from Box 4.
boxes[4].remove('shampoo')
boxes[4].remove('microscope')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")