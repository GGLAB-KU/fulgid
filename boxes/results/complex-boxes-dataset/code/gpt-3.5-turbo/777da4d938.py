# Initial state of boxes
boxes = {
    0: ['river', 'blender'],
    1: ['storm', 'boot'],
    2: ['grass', 'glasses', 'helmet'],
    3: [],
    4: ['boat', 'clock', 'shirt'],
    5: ['thread', 'brush'],
    6: [],
    7: ['button', 'sun'],
    8: [],
    9: ['toothpaste', 'magnet'],
    10: ['wallet', 'book', 'lightning', 'vase', 'perfume']
}

# Put the scissors into Box 2.
boxes[2].append('scissors')

# Remove the vase and the lightning from Box 10.
boxes[10].remove('vase')
boxes[10].remove('lightning')

# Move the button from Box 7 to Box 6.
boxes[7].remove('button')
boxes[6].append('button')

# Move the shirt and the boat from Box 4 to Box 2.
boxes[4].remove('shirt')
boxes[4].remove('boat')
boxes[2].append('shirt')
boxes[2].append('boat')

# Move the thread from Box 5 to Box 4.
boxes[5].remove('thread')
boxes[4].append('thread')

# Move the river from Box 0 to Box 9.
boxes[0].remove('river')
boxes[9].append('river')

# Remove the shirt and the boat from Box 2.
boxes[2].remove('shirt')
boxes[2].remove('boat')

# Put the comb and the boat into Box 5.
boxes[5].append('comb')
boxes[5].append('boat')

# Move the button from Box 6 to Box 1.
boxes[6].remove('button')
boxes[1].append('button')

# Move the button from Box 1 to Box 0.
boxes[1].remove('button')
boxes[0].append('button')

# Put the comet and the fridge into Box 5.
boxes[5].append('comet')
boxes[5].append('fridge')

# Move the boot and the storm from Box 1 to Box 10.
boxes[1].remove('boot')
boxes[1].remove('storm')
boxes[10].append('boot')
boxes[10].append('storm')

# Swap the wallet in Box 10 with the button in Box 0.
boxes[0].remove('button')
boxes[10].remove('wallet')
boxes[0].append('wallet')
boxes[10].append('button')

# Put the mixer and the starfish into Box 4.
boxes[4].append('mixer')
boxes[4].append('starfish')

# Move the sun from Box 7 to Box 6.
boxes[7].remove('sun')
boxes[6].append('sun')

# Swap the storm in Box 10 with the wallet in Box 0.
boxes[0].remove('wallet')
boxes[10].remove('storm')
boxes[0].append('storm')
boxes[10].append('wallet')

# Swap the starfish in Box 4 with the toothpaste in Box 9.
boxes[4].remove('starfish')
boxes[9].remove('toothpaste')
boxes[4].append('toothpaste')
boxes[9].append('starfish')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")