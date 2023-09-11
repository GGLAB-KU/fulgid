# Initial state of boxes
boxes = {
    0: ['key'],
    1: [],
    2: ['bird'],
    3: ['console', 'game', 'towel'],
    4: ['blender', 'thread', 'toothbrush', 'freezer', 'piano'],
    5: ['mountain'],
    6: [],
    7: [],
    8: ['plane'],
    9: ['camera', 'coat', 'island', 'bell', 'magnet'],
    10: ['cat', 'shelf'],
    11: [],
    12: ['mixer', 'keyboard', 'lion', 'train', 'frame']
}

# Swap the shelf in Box 10 with the key in Box 0.
boxes[0].remove('key')
boxes[10].remove('shelf')
boxes[0].append('shelf')
boxes[10].append('key')

# Remove the towel from Box 3.
boxes[3].remove('towel')

# Swap the bird in Box 2 with the shelf in Box 0.
boxes[0].remove('shelf')
boxes[2].remove('bird')
boxes[0].append('bird')
boxes[2].append('shelf')

# Replace the cat with the train in Box 10.
boxes[10].remove('cat')
boxes[10].append('train')

# Move the mountain from Box 5 to Box 0.
boxes[5].remove('mountain')
boxes[0].append('mountain')

# Put the pen and the moon into Box 12.
boxes[12].append('pen')
boxes[12].append('moon')

# Move the key from Box 10 to Box 6.
boxes[10].remove('key')
boxes[6].append('key')

# Remove the bell and the camera from Box 9.
boxes[9].remove('bell')
boxes[9].remove('camera')

# Remove the lion from Box 12.
boxes[12].remove('lion')

# Empty Box 4.
boxes[4] = []

# Replace the plane with the lamp in Box 8.
boxes[8].remove('plane')
boxes[8].append('lamp')

# Swap the lamp in Box 8 with the key in Box 6.
boxes[6].remove('key')
boxes[8].remove('lamp')
boxes[6].append('lamp')
boxes[8].append('key')

# Remove the train and the mixer from Box 12.
boxes[12].remove('train')
boxes[12].remove('mixer')

# Replace the bird with the lock in Box 0.
boxes[0].remove('bird')
boxes[0].append('lock')

# Put the shark into Box 0.
boxes[0].append('shark')

# Swap the coat in Box 9 with the frame in Box 12.
boxes[9].remove('coat')
boxes[12].remove('frame')
boxes[9].append('frame')
boxes[12].append('coat')

# Swap the shelf in Box 2 with the key in Box 8.
boxes[2].remove('shelf')
boxes[8].remove('key')
boxes[2].append('key')
boxes[8].append('shelf')

# Remove the key from Box 2.
boxes[2].remove('key')

# Put the tiger and the jungle into Box 0.
boxes[0].append('tiger')
boxes[0].append('jungle')

# Swap the shelf in Box 8 with the mountain in Box 0.
boxes[0].remove('shelf')
boxes[8].remove('mountain')
boxes[0].append('mountain')
boxes[8].append('shelf')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")