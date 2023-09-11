# Initial state of boxes
boxes = {
    0: ['sock', 'controller', 'wig'],
    1: ['star', 'blender', 'drum'],
    2: [],
    3: ['chair', 'book', 'perfume', 'bell'],
    4: ['grass'],
    5: ['pillow'],
    6: ['shampoo', 'branch'],
    7: ['bird', 'tree'],
    8: ['freezer', 'mixer'],
    9: ['pants', 'river', 'tiger'],
    10: ['shoe']
}

# Move the tiger from Box 9 to Box 5.
boxes[9].remove('tiger')
boxes[5].append('tiger')

# Put the bowl and the violin and the submarine into Box 6.
boxes[6].append('bowl')
boxes[6].append('violin')
boxes[6].append('submarine')

# Put the fish and the console and the shampoo into Box 9.
boxes[9].append('fish')
boxes[9].append('console')
boxes[9].append('shampoo')

# Replace the tree with the soap in Box 7.
boxes[7].remove('tree')
boxes[7].append('soap')

# Remove the mixer from Box 8.
boxes[8].remove('mixer')

# Put the shoe and the dolphin and the freezer into Box 1.
boxes[1].append('shoe')
boxes[1].append('dolphin')
boxes[1].append('freezer')

# Replace the shoe with the battery in Box 10.
boxes[10].remove('shoe')
boxes[10].append('battery')

# Swap the soap in Box 7 with the book in Box 3.
boxes[7].remove('soap')
boxes[3].remove('book')
boxes[7].append('book')
boxes[3].append('soap')

# Swap the shampoo in Box 6 with the bird in Box 7.
boxes[6].remove('shampoo')
boxes[7].remove('bird')
boxes[6].append('bird')
boxes[7].append('shampoo')

# Move the bell and the perfume and the soap from Box 3 to Box 6.
items_to_move = ['bell', 'perfume', 'soap']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[6].append(item)

# Replace the shampoo with the lock in Box 7.
boxes[7].remove('shampoo')
boxes[7].append('lock')

# Remove the sock and the controller from Box 0.
boxes[0].remove('sock')
boxes[0].remove('controller')

# Move the freezer from Box 8 to Box 1.
boxes[8].remove('freezer')
boxes[1].append('freezer')

# Move the chair from Box 3 to Box 5.
boxes[3].remove('chair')
boxes[5].append('chair')

# Remove the battery from Box 10.
boxes[10].remove('battery')

# Swap the chair in Box 5 with the wig in Box 0.
boxes[5].remove('chair')
boxes[0].remove('wig')
boxes[5].append('wig')
boxes[0].append('chair')

# Replace the tiger and the pillow and the wig with the cow and the cloud and the bicycle in Box 5.
boxes[5].remove('tiger')
boxes[5].remove('pillow')
boxes[0].remove('wig')
boxes[5].append('cow')
boxes[5].append('cloud')
boxes[5].append('bicycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")