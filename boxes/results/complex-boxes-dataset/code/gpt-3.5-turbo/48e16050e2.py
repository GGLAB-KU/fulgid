# Initial state of boxes
boxes = {
    0: ['tie', 'rock'],
    1: ['elephant', 'beach', 'car', 'blender'],
    2: ['console'],
    3: ['submarine', 'shirt'],
    4: ['charger', 'needle', 'bicycle', 'table', 'shark'],
    5: ['seaweed', 'spoon'],
    6: ['boat', 'shorts', 'controller'],
    7: ['speaker', 'brush', 'toy'],
    8: ['lock', 'cat', 'note', 'usb'],
    9: ['soap', 'river', 'mirror', 'toaster'],
    10: [],
    11: ['jacket'],
    12: ['blanket', 'star', 'clock', 'wire'],
    13: ['meteor', 'sculpture', 'doll'],
    14: ['horse', 'game']
}

# Put the camera into Box 1.
boxes[1].append('camera')

# Replace the toy with the blender in Box 7.
boxes[7].remove('toy')
boxes[7].append('blender')

# Remove the charger and the table from Box 4.
boxes[4].remove('charger')
boxes[4].remove('table')

# Remove the meteor and the doll and the sculpture from Box 13.
boxes[13].remove('meteor')
boxes[13].remove('doll')
boxes[13].remove('sculpture')

# Replace the cat and the note with the controller and the skirt in Box 8.
boxes[8].remove('cat')
boxes[8].remove('note')
boxes[8].append('controller')
boxes[8].append('skirt')

# Empty Box 1.
boxes[1] = []

# Move the jacket from Box 11 to Box 14.
boxes[11].remove('jacket')
boxes[14].append('jacket')

# Replace the shark and the needle and the bicycle with the perfume and the sun and the motorcycle in Box 4.
boxes[4].remove('shark')
boxes[4].remove('needle')
boxes[4].remove('bicycle')
boxes[4].append('perfume')
boxes[4].append('sun')
boxes[4].append('motorcycle')

# Move the lock and the skirt from Box 8 to Box 7.
boxes[8].remove('lock')
boxes[8].remove('skirt')
boxes[7].append('lock')
boxes[7].append('skirt')

# Swap the usb in Box 8 with the tie in Box 0.
boxes[8].remove('usb')
boxes[0].remove('tie')
boxes[8].append('tie')
boxes[0].append('usb')

# Remove the mirror and the river and the soap from Box 9.
boxes[9].remove('mirror')
boxes[9].remove('river')
boxes[9].remove('soap')

# Put the shark into Box 10.
boxes[10].append('shark')

# Swap the console in Box 2 with the brush in Box 7.
boxes[2].remove('console')
boxes[7].remove('brush')
boxes[2].append('brush')
boxes[7].append('console')

# Move the usb and the rock from Box 0 to Box 7.
boxes[0].remove('usb')
boxes[0].remove('rock')
boxes[7].append('usb')
boxes[7].append('rock')

# Replace the brush with the grass in Box 2.
boxes[2].remove('brush')
boxes[2].append('grass')

# Move the rock from Box 7 to Box 3.
boxes[7].remove('rock')
boxes[3].append('rock')

# Replace the toaster with the grass in Box 9.
boxes[9].remove('toaster')
boxes[9].append('grass')

# Put the shirt into Box 14.
boxes[14].append('shirt')

# Put the meteor and the candle into Box 12.
boxes[12].append('meteor')
boxes[12].append('candle')

# Replace the shorts and the boat and the controller with the flute and the tie and the frame in Box 6.
boxes[6].remove('shorts')
boxes[6].remove('boat')
boxes[6].remove('controller')
boxes[6].append('flute')
boxes[6].append('tie')
boxes[6].append('frame')

# Remove the game and the horse from Box 14.
boxes[14].remove('game')
boxes[14].remove('horse')

# Move the speaker from Box 7 to Box 6.
boxes[7].remove('speaker')
boxes[6].append('speaker')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")