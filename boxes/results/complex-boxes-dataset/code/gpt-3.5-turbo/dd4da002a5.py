# Initial state of boxes
boxes = {
    0: ['rain', 'controller', 'necklace', 'flute'],
    1: ['grass', 'oven'],
    2: ['keyboard', 'book'],
    3: ['thunder', 'train', 'frame', 'fork'],
    4: ['microscope', 'mirror', 'boot', 'charger', 'wallet'],
    5: ['shark', 'earring', 'piano', 'tiger'],
    6: ['pan', 'submarine', 'towel', 'harmonica', 'shirt'],
    7: [],
    8: ['bowl', 'cloud', 'toy', 'telescope'],
    9: ['apple'],
    10: ['camera', 'belt', 'coat', 'shoes'],
    11: ['mask', 'speaker', 'river'],
    12: ['note', 'candle']
}

# Put the key and the button and the crown into Box 12.
boxes[12].extend(['key', 'button', 'crown'])

# Swap the apple in Box 9 with the book in Box 2.
boxes[9].remove('apple')
boxes[2].remove('book')
boxes[9].append('book')
boxes[2].append('apple')

# Put the coin and the oven into Box 1.
boxes[1].extend(['coin', 'oven'])

# Replace the telescope and the bowl and the toy with the apple and the chair and the toaster in Box 8.
boxes[8].remove('telescope')
boxes[8].remove('bowl')
boxes[8].remove('toy')
boxes[8].extend(['apple', 'chair', 'toaster'])

# Swap the apple in Box 8 with the thunder in Box 3.
boxes[8].remove('apple')
boxes[3].remove('thunder')
boxes[8].append('thunder')
boxes[3].append('apple')

# Remove the speaker and the mask and the river from Box 11.
boxes[11].remove('speaker')
boxes[11].remove('mask')
boxes[11].remove('river')

# Move the oven from Box 1 to Box 0.
boxes[1].remove('oven')
boxes[0].append('oven')

# Replace the ocean and the grass and the coin with the controller and the needle and the mixer in Box 1.
boxes[1].remove('grass')
boxes[1].remove('coin')
boxes[1].extend(['controller', 'needle', 'mixer'])

# Remove the piano and the tiger from Box 5.
boxes[5].remove('piano')
boxes[5].remove('tiger')

# Replace the boot and the microscope with the dress and the bear in Box 4.
boxes[4].remove('boot')
boxes[4].remove('microscope')
boxes[4].extend(['dress', 'bear'])

# Remove the dress from Box 4.
boxes[4].remove('dress')

# Remove the pan from Box 6.
boxes[6].remove('pan')

# Remove the cloud and the toaster from Box 8.
boxes[8].remove('cloud')
boxes[8].remove('toaster')

# Put the blanket and the sculpture into Box 8.
boxes[8].extend(['blanket', 'sculpture'])

# Remove the shark and the earring from Box 5.
boxes[5].remove('shark')
boxes[5].remove('earring')

# Remove the frame from Box 3.
boxes[3].remove('frame')

# Move the keyboard and the apple from Box 2 to Box 0.
boxes[2].remove('keyboard')
boxes[2].remove('apple')
boxes[0].extend(['keyboard', 'apple'])

# Swap the button in Box 12 with the book in Box 9.
boxes[12].remove('button')
boxes[9].remove('book')
boxes[12].append('book')
boxes[9].append('button')

# Move the belt from Box 10 to Box 7.
boxes[10].remove('belt')
boxes[7].append('belt')

# Put the soap into Box 1.
boxes[1].append('soap')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")