# Initial state of boxes
boxes = {
    0: ['thread', 'bicycle'],
    1: ['pillow'],
    2: ['seaweed', 'blanket', 'rain', 'meteor'],
    3: ['train', 'rock', 'boat'],
    4: ['swimsuit', 'perfume', 'charger'],
    5: ['key', 'camera'],
    6: [],
    7: ['toy', 'earring', 'gloves', 'tree'],
    8: ['scissors'],
    9: ['pen', 'butterfly', 'chair']
}

# Replace the thread with the comb in Box 0.
boxes[0].remove('thread')
boxes[0].append('comb')

# Replace the camera with the violin in Box 5.
boxes[5].remove('camera')
boxes[5].append('violin')

# Move the pen and the chair from Box 9 to Box 4.
items_to_move = ['pen', 'chair']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[4].append(item)

# Move the comb from Box 0 to Box 8.
boxes[0].remove('comb')
boxes[8].append('comb')

# Swap the swimsuit in Box 4 with the violin in Box 5.
boxes[4].remove('swimsuit')
boxes[5].remove('violin')
boxes[4].append('violin')
boxes[5].append('swimsuit')

# Replace the train and the rock and the boat with the bus and the harmonica and the tree in Box 3.
boxes[3].remove('train')
boxes[3].remove('rock')
boxes[3].remove('boat')
boxes[3].append('bus')
boxes[3].append('harmonica')
boxes[3].append('tree')

# Empty Box 7.
boxes[7] = []

# Put the truck and the pan into Box 6.
boxes[6].append('truck')
boxes[6].append('pan')

# Put the thunder into Box 9.
boxes[9].append('thunder')

# Move the pillow from Box 1 to Box 0.
boxes[1].remove('pillow')
boxes[0].append('pillow')

# Move the seaweed from Box 2 to Box 6.
boxes[2].remove('seaweed')
boxes[6].append('seaweed')

# Move the meteor and the blanket from Box 2 to Box 8.
boxes[2].remove('meteor')
boxes[2].remove('blanket')
boxes[8].append('meteor')
boxes[8].append('blanket')

# Put the wallet and the skirt and the storm into Box 9.
boxes[9].append('wallet')
boxes[9].append('skirt')
boxes[9].append('storm')

# Replace the bus and the tree with the jacket and the dice in Box 3.
boxes[3].remove('bus')
boxes[3].remove('tree')
boxes[3].append('jacket')
boxes[3].append('dice')

# Swap the thunder in Box 9 with the meteor in Box 8.
boxes[9].remove('thunder')
boxes[8].remove('meteor')
boxes[9].append('meteor')
boxes[8].append('thunder')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")