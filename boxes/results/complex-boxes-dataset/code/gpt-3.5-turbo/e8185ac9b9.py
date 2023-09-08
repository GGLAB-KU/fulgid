# Initial state of boxes
boxes = {
    0: ['paint', 'shorts', 'sock', 'comet'],
    1: [],
    2: ['wire', 'freezer', 'toothbrush'],
    3: ['motorcycle', 'car', 'shark', 'horse'],
    4: ['octopus', 'cat', 'pan', 'toaster', 'cloud'],
    5: ['scarf', 'apple', 'tree', 'toothpaste', 'mixer'],
    6: [],
    7: ['dice', 'fork', 'rock', 'boat'],
    8: ['speaker'],
    9: ['book', 'leaf', 'island'],
    10: ['scissors'],
    11: ['plate', 'whistle', 'laptop', 'microwave'],
    12: [],
    13: ['umbrella', 'watch', 'bell', 'boot', 'mountain'],
    14: ['keyboard', 'puzzle', 'tape']
}

# Replace the sock and the paint with the camera and the car in Box 0.
boxes[0].remove('sock')
boxes[0].remove('paint')
boxes[0].append('camera')
boxes[0].append('car')

# Replace the scissors with the grass in Box 10.
boxes[10].remove('scissors')
boxes[10].append('grass')

# Move the speaker from Box 8 to Box 13.
boxes[8].remove('speaker')
boxes[13].append('speaker')

# Replace the whistle and the plate and the laptop with the usb and the wire and the book in Box 11.
boxes[11].remove('whistle')
boxes[11].remove('plate')
boxes[11].remove('laptop')
boxes[11].append('usb')
boxes[11].append('wire')
boxes[11].append('book')

# Replace the shark and the horse and the motorcycle with the snow and the oven and the blanket in Box 3.
boxes[3].remove('shark')
boxes[3].remove('horse')
boxes[3].remove('motorcycle')
boxes[3].append('snow')
boxes[3].append('oven')
boxes[3].append('blanket')

# Replace the oven with the cow in Box 3.
boxes[3].remove('oven')
boxes[3].append('cow')

# Put the beach and the truck and the island into Box 4.
boxes[4].append('beach')
boxes[4].append('truck')
boxes[4].append('island')

# Swap the mountain in Box 13 with the car in Box 3.
boxes[13].remove('mountain')
boxes[3].remove('car')
boxes[13].append('car')
boxes[3].append('mountain')

# Remove the toothbrush and the freezer and the wire from Box 2.
boxes[2].remove('toothbrush')
boxes[2].remove('freezer')
boxes[2].remove('wire')

# Move the dice from Box 7 to Box 0.
boxes[7].remove('dice')
boxes[0].append('dice')

# Move the boat and the rock and the fork from Box 7 to Box 4.
boxes[7].remove('boat')
boxes[7].remove('rock')
boxes[7].remove('fork')
boxes[4].append('boat')
boxes[4].append('rock')
boxes[4].append('fork')

# Move the wire and the usb from Box 11 to Box 8.
boxes[11].remove('wire')
boxes[11].remove('usb')
boxes[8].append('wire')
boxes[8].append('usb')

# Put the plane into Box 7.
boxes[7].append('plane')

# Move the speaker and the umbrella and the boot from Box 13 to Box 1.
boxes[13].remove('speaker')
boxes[13].remove('umbrella')
boxes[13].remove('boot')
boxes[1].append('speaker')
boxes[1].append('umbrella')
boxes[1].append('boot')

# Empty Box 0.
boxes[0] = []

# Replace the plane with the usb in Box 7.
boxes[7].remove('plane')
boxes[7].append('usb')

# Move the apple and the toothpaste and the scarf from Box 5 to Box 9.
boxes[5].remove('apple')
boxes[5].remove('toothpaste')
boxes[5].remove('scarf')
boxes[9].append('apple')
boxes[9].append('toothpaste')
boxes[9].append('scarf')

# Move the tree and the mixer from Box 5 to Box 4.
boxes[5].remove('tree')
boxes[5].remove('mixer')
boxes[4].append('tree')
boxes[4].append('mixer')

# Move the cow and the mountain and the snow from Box 3 to Box 2.
boxes[3].remove('cow')
boxes[3].remove('mountain')
boxes[3].remove('snow')
boxes[2].append('cow')
boxes[2].append('mountain')
boxes[2].append('snow')

# Put the sandals into Box 7.
boxes[7].append('sandals')

# Swap the keyboard in Box 14 with the bell in Box 13.
boxes[14].remove('keyboard')
boxes[13].remove('bell')
boxes[14].append('bell')
boxes[13].append('keyboard')

# Move the tree from Box 4 to Box 13.
boxes[4].remove('tree')
boxes[13].append('tree')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")