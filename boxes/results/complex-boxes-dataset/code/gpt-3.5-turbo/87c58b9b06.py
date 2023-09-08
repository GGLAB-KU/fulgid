# Initial state of boxes
boxes = {
    0: ['horse', 'lamp', 'book'],
    1: [],
    2: ['frame', 'chair', 'coin', 'boat'],
    3: ['mountain', 'shirt', 'glasses', 'tape', 'thread'],
    4: ['spoon', 'camera', 'submarine', 'pot', 'pan'],
    5: ['lightning', 'rock', 'coral'],
    6: [],
    7: ['charger'],
    8: ['vase'],
    9: ['pillow', 'boot', 'truck', 'toothpaste', 'makeup'],
    10: ['soap', 'mixer', 'keyboard'],
    11: ['bag', 'wallet', 'shelf', 'note', 'clock'],
    12: ['guitar', 'shorts', 'piano', 'speaker']
}

# Remove the charger from Box 7.
boxes[7].remove('charger')

# Swap the bag in Box 11 with the horse in Box 0.
boxes[0].remove('horse')
boxes[11].remove('bag')
boxes[0].append('bag')
boxes[11].append('horse')

# Put the tie into Box 7.
boxes[7].append('tie')

# Swap the vase in Box 8 with the pot in Box 4.
boxes[8].remove('vase')
boxes[4].remove('pot')
boxes[8].append('pot')
boxes[4].append('vase')

# Put the piano into Box 0.
boxes[12].remove('piano')
boxes[0].append('piano')

# Replace the piano and the speaker and the guitar with the shelf and the fridge and the game in Box 12.
boxes[12].remove('piano')
boxes[12].remove('speaker')
boxes[12].remove('guitar')
boxes[12].append('shelf')
boxes[12].append('fridge')
boxes[12].append('game')

# Swap the submarine in Box 4 with the rock in Box 5.
boxes[4].remove('submarine')
boxes[5].remove('rock')
boxes[4].append('rock')
boxes[5].append('submarine')

# Remove the soap from Box 10.
boxes[10].remove('soap')

# Remove the mixer from Box 10.
boxes[10].remove('mixer')

# Put the skirt and the lock into Box 9.
boxes[9].append('skirt')
boxes[9].append('lock')

# Remove the note from Box 11.
boxes[11].remove('note')

# Remove the shelf and the fridge and the game from Box 12.
boxes[12].remove('shelf')
boxes[12].remove('fridge')
boxes[12].remove('game')

# Remove the tie from Box 7.
boxes[7].remove('tie')

# Replace the rock and the vase and the pan with the mountain and the plate and the tape in Box 4.
boxes[4].remove('rock')
boxes[4].remove('vase')
boxes[4].remove('pan')
boxes[4].append('mountain')
boxes[4].append('plate')
boxes[4].append('tape')

# Move the wallet and the clock from Box 11 to Box 3.
boxes[11].remove('wallet')
boxes[11].remove('clock')
boxes[3].append('wallet')
boxes[3].append('clock')

# Put the freezer into Box 5.
boxes[5].append('freezer')

# Replace the skirt and the toothpaste and the pillow with the mixer and the clock and the truck in Box 9.
boxes[9].remove('skirt')
boxes[9].remove('toothpaste')
boxes[9].remove('pillow')
boxes[9].append('mixer')
boxes[9].append('clock')
boxes[9].append('truck')

# Replace the coral and the lightning with the keyboard and the blender in Box 5.
boxes[5].remove('coral')
boxes[5].remove('lightning')
boxes[5].append('keyboard')
boxes[5].append('blender')

# Put the microscope and the toy into Box 12.
boxes[12].append('microscope')
boxes[12].append('toy')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")