# Initial state of boxes
boxes = {
    0: ['grinder'],
    1: ['planet', 'toy', 'toaster', 'star'],
    2: [],
    3: ['note', 'microscope', 'coat', 'butterfly', 'bowl'],
    4: ['dolphin', 'phone', 'rain', 'bell', 'button'],
    5: ['river'],
    6: ['clock', 'pants', 'towel', 'train', 'submarine']
}

# Remove the phone and the bell from Box 4.
boxes[4].remove('phone')
boxes[4].remove('bell')

# Swap the grinder in Box 0 with the note in Box 3.
boxes[0].remove('grinder')
boxes[3].remove('note')
boxes[0].append('note')
boxes[3].append('grinder')

# Put the paint and the candle into Box 2.
boxes[2].append('paint')
boxes[2].append('candle')

# Put the thunder and the earring into Box 0.
boxes[0].append('thunder')
boxes[0].append('earring')

# Remove the toy from Box 1.
boxes[1].remove('toy')

# Replace the planet and the toaster with the helmet and the storm in Box 1.
boxes[1].remove('planet')
boxes[1].remove('toaster')
boxes[1].append('helmet')
boxes[1].append('storm')

# Move the coat from Box 3 to Box 6.
boxes[3].remove('coat')
boxes[6].append('coat')

# Remove the river from Box 5.
boxes[5].remove('river')

# Remove the pants and the coat and the train from Box 6.
boxes[6].remove('pants')
boxes[6].remove('coat')
boxes[6].remove('train')

# Put the magnet into Box 2.
boxes[2].append('magnet')

# Put the table and the key and the bicycle into Box 2.
boxes[2].append('table')
boxes[2].append('key')
boxes[2].append('bicycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")