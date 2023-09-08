# Initial state of boxes
boxes = {
    0: [],
    1: ['usb', 'tiger'],
    2: ['game', 'shirt', 'glove', 'branch', 'fridge'],
    3: ['scissors', 'phone', 'makeup', 'dress'],
    4: ['shark', 'watch', 'guitar', 'vase', 'cow'],
    5: ['grass', 'pants', 'tie', 'sock', 'plate'],
    6: ['butterfly', 'pot'],
    7: ['magnet'],
    8: ['chair', 'lock', 'bell', 'book', 'telescope'],
    9: [],
    10: ['shorts', 'fork', 'puzzle', 'violin'],
    11: ['piano', 'mask', 'meteor', 'pen'],
    12: [],
    13: ['sandals', 'boot', 'towel']
}

# Swap the mask in Box 11 with the sandals in Box 13.
boxes[11].remove('mask')
boxes[13].remove('sandals')
boxes[11].append('sandals')
boxes[13].append('mask')

# Put the cloud into Box 1.
boxes[1].append('cloud')

# Swap the tie in Box 5 with the vase in Box 4.
boxes[5].remove('tie')
boxes[4].remove('vase')
boxes[5].append('vase')
boxes[4].append('tie')

# Move the bell from Box 8 to Box 7.
boxes[8].remove('bell')
boxes[7].append('bell')

# Swap the magnet in Box 7 with the towel in Box 13.
boxes[7].remove('magnet')
boxes[13].remove('towel')
boxes[7].append('towel')
boxes[13].append('magnet')

# Replace the scissors with the fridge in Box 3.
boxes[3].remove('scissors')
boxes[3].append('fridge')

# Remove the pot and the butterfly from Box 6.
boxes[6].remove('pot')
boxes[6].remove('butterfly')

# Swap the branch in Box 2 with the phone in Box 3.
boxes[2].remove('branch')
boxes[3].remove('phone')
boxes[2].append('phone')
boxes[3].append('branch')

# Swap the tie in Box 4 with the vase in Box 5.
boxes[4].remove('tie')
boxes[5].remove('vase')
boxes[4].append('vase')
boxes[5].append('tie')

# Remove the usb from Box 1.
boxes[1].remove('usb')

# Remove the meteor from Box 11.
boxes[11].remove('meteor')

# Put the flower and the bell into Box 12.
boxes[12].append('flower')
boxes[12].append('bell')

# Remove the boot from Box 13.
boxes[13].remove('boot')

# Put the lipstick and the sculpture into Box 10.
boxes[10].append('lipstick')
boxes[10].append('sculpture')

# Move the game from Box 2 to Box 1.
boxes[2].remove('game')
boxes[1].append('game')

# Put the meteor into Box 8.
boxes[8].append('meteor')

# Swap the game in Box 1 with the mask in Box 13.
boxes[1].remove('game')
boxes[13].remove('mask')
boxes[1].append('mask')
boxes[13].append('game')

# Remove the fridge from Box 2.
boxes[2].remove('fridge')

# Remove the piano and the pen and the sandals from Box 11.
boxes[11].remove('piano')
boxes[11].remove('pen')
boxes[11].remove('sandals')

# Put the mountain into Box 12.
boxes[12].append('mountain')

# Move the magnet from Box 13 to Box 8.
boxes[13].remove('magnet')
boxes[8].append('magnet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")