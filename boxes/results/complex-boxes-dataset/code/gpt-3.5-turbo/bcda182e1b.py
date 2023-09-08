# Initial state of boxes
boxes = {
    0: [],
    1: ['rock', 'planet', 'shelf'],
    2: ['wire', 'cow', 'mixer', 'dice'],
    3: ['tape', 'tree', 'clock', 'headphone'],
    4: ['bear'],
    5: [],
    6: ['horn', 'violin', 'usb', 'freezer'],
    7: ['dress', 'pants', 'spoon', 'paint'],
    8: ['controller', 'book'],
    9: ['submarine', 'button'],
    10: ['telescope', 'leaf', 'shirt', 'helmet', 'moon'],
    11: ['thread', 'storm', 'snow', 'motorcycle'],
    12: [],
    13: ['brush', 'microscope', 'soap'],
    14: ['microwave', 'boot', 'seaweed']
}

# Put the controller and the jungle and the wig into Box 4.
boxes[4].append('controller')
boxes[4].append('jungle')
boxes[4].append('wig')

# Put the camera and the shampoo into Box 3.
boxes[3].append('camera')
boxes[3].append('shampoo')

# Remove the controller and the wig from Box 4.
boxes[4].remove('controller')
boxes[4].remove('wig')

# Swap the book in Box 8 with the wire in Box 2.
boxes[8].remove('book')
boxes[2].remove('wire')
boxes[8].append('wire')
boxes[2].append('book')

# Put the makeup and the necklace into Box 3.
boxes[3].append('makeup')
boxes[3].append('necklace')

# Put the tiger into Box 14.
boxes[14].append('tiger')

# Put the glove and the branch into Box 14.
boxes[14].append('glove')
boxes[14].append('branch')

# Empty Box 2.
boxes[2] = []

# Remove the tree and the camera and the necklace from Box 3.
boxes[3].remove('tree')
boxes[3].remove('camera')
boxes[3].remove('necklace')

# Move the makeup and the tape from Box 3 to Box 7.
boxes[3].remove('makeup')
boxes[3].remove('tape')
boxes[7].append('makeup')
boxes[7].append('tape')

# Swap the microwave in Box 14 with the jungle in Box 4.
boxes[14].remove('microwave')
boxes[4].remove('jungle')
boxes[14].append('jungle')
boxes[4].append('microwave')

# Move the microwave from Box 4 to Box 8.
boxes[4].remove('microwave')
boxes[8].append('microwave')

# Move the clock and the headphone from Box 3 to Box 2.
boxes[3].remove('clock')
boxes[3].remove('headphone')
boxes[2].append('clock')
boxes[2].append('headphone')

# Put the cat and the tie into Box 2.
boxes[2].append('cat')
boxes[2].append('tie')

# Remove the leaf and the shirt from Box 10.
boxes[10].remove('leaf')
boxes[10].remove('shirt')

# Move the usb and the violin from Box 6 to Box 5.
boxes[6].remove('usb')
boxes[6].remove('violin')
boxes[5].append('usb')
boxes[5].append('violin')

# Swap the horn in Box 6 with the clock in Box 2.
boxes[6].remove('horn')
boxes[2].remove('clock')
boxes[6].append('clock')
boxes[2].append('horn')

# Move the microwave and the controller and the wire from Box 8 to Box 14.
boxes[8].remove('microwave')
boxes[8].remove('controller')
boxes[8].remove('wire')
boxes[14].append('microwave')
boxes[14].append('controller')
boxes[14].append('wire')

# Put the lion and the comet and the boot into Box 2.
boxes[2].append('lion')
boxes[2].append('comet')
boxes[2].append('boot')

# Move the freezer from Box 6 to Box 1.
boxes[6].remove('freezer')
boxes[1].append('freezer')

# Replace the freezer and the rock with the piano and the cow in Box 1.
boxes[1].remove('freezer')
boxes[1].remove('rock')
boxes[1].append('piano')
boxes[1].append('cow')

# Remove the motorcycle and the snow and the thread from Box 11.
boxes[11].remove('motorcycle')
boxes[11].remove('snow')
boxes[11].remove('thread')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")