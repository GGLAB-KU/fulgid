box = {
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

# Swap the shelf in Box 10 with the key in Box 0
box[10], box[0] = box[0], box[10]

# Remove the towel from Box 3
box[3].remove('towel')

# Swap the bird in Box 2 with the shelf in Box 0
box[2], box[0] = box[0], box[2]

# Replace the cat with the train in Box 10
box[10] = ['train']

# Move the mountain from Box 5 to Box 0
box[0].append(box[5].pop())

# Put the pen and the moon into Box 12
box[12].extend(['pen', 'moon'])

# Move the key from Box 10 to Box 6
box[6].append(box[10].pop())

# Remove the bell and the camera from Box 9
box[9].remove('bell')
box[9].remove('camera')

# Remove the lion from Box 12
box[12].remove('lion')

# Empty Box 4
box[4] = []

# Replace the plane with the lamp in Box 8
box[8] = ['lamp']

# Swap the lamp in Box 8 with the key in Box 6
box[8], box[6] = box[6], box[8]

# Remove the train and the mixer from Box 12
box[12].remove('train')
box[12].remove('mixer')

# Replace the bird with the lock in Box 0
box[0] = ['lock']

# Put the shark into Box 0
box[0].append('shark')

# Swap the coat in Box 9 with the frame in Box 12
box[9], box[12] = box[12], box[9]

# Swap the shelf in Box 2 with the key in Box 8
box[2], box[8] = box[8], box[2]

# Remove the key from Box 2
box[2].remove('key')

# Put the tiger and the jungle into Box 0
box[0].extend(['tiger', 'jungle'])

# Swap the shelf in Box 8 with the mountain in Box 0
box[8], box[0] = box[0], box[8]

# Print the contents of each box
for i in range(13):
    print(f"Box {i}: {box[i]}")