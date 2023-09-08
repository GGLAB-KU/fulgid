# Initial state of boxes
boxes = {
    0: ['helmet', 'sandals'],
    1: [],
    2: ['tiger', 'key', 'train', 'spoon'],
    3: [],
    4: ['soap', 'forest', 'bus', 'submarine'],
    5: [],
    6: ['pan', 'oven', 'butterfly'],
    7: ['scissors', 'dice', 'toy', 'motorcycle'],
    8: ['brush', 'drum', 'pillow', 'mountain', 'tape'],
    9: ['meteor', 'button', 'keyboard', 'jacket', 'phone'],
    10: ['mirror', 'coat']
}

# Remove the forest and the soap and the bus from Box 4.
boxes[4].remove('forest')
boxes[4].remove('soap')
boxes[4].remove('bus')

# Swap the submarine in Box 4 with the brush in Box 8.
boxes[4].remove('submarine')
boxes[8].remove('brush')
boxes[4].append('brush')
boxes[8].append('submarine')

# Replace the scissors and the motorcycle and the toy with the sculpture and the bear and the rocket in Box 7.
boxes[7].remove('scissors')
boxes[7].remove('motorcycle')
boxes[7].remove('toy')
boxes[7].append('sculpture')
boxes[7].append('bear')
boxes[7].append('rocket')

# Move the submarine from Box 8 to Box 0.
boxes[8].remove('submarine')
boxes[0].append('submarine')

# Move the sculpture and the dice from Box 7 to Box 4.
boxes[7].remove('sculpture')
boxes[7].remove('dice')
boxes[4].append('sculpture')
boxes[4].append('dice')

# Swap the oven in Box 6 with the jacket in Box 9.
boxes[6].remove('oven')
boxes[9].remove('jacket')
boxes[6].append('jacket')
boxes[9].append('oven')

# Replace the jacket and the pan and the butterfly with the shoe and the comet and the coin in Box 6.
boxes[6].remove('jacket')
boxes[6].remove('pan')
boxes[6].remove('butterfly')
boxes[6].append('shoe')
boxes[6].append('comet')
boxes[6].append('coin')

# Remove the spoon and the key and the train from Box 2.
boxes[2].remove('spoon')
boxes[2].remove('key')
boxes[2].remove('train')

# Move the mirror from Box 10 to Box 2.
boxes[10].remove('mirror')
boxes[2].append('mirror')

# Swap the mirror in Box 2 with the coat in Box 10.
boxes[2].remove('mirror')
boxes[10].remove('coat')
boxes[2].append('coat')
boxes[10].append('mirror')

# Replace the phone with the ocean in Box 9.
boxes[9].remove('phone')
boxes[9].append('ocean')

# Put the comet and the vase into Box 1.
boxes[1].append('comet')
boxes[1].append('vase')

# Replace the comet and the vase with the rock and the tree in Box 1.
boxes[1].remove('comet')
boxes[1].remove('vase')
boxes[1].append('rock')
boxes[1].append('tree')

# Move the button and the keyboard from Box 9 to Box 1.
boxes[9].remove('button')
boxes[9].remove('keyboard')
boxes[1].append('button')
boxes[1].append('keyboard')

# Move the meteor from Box 9 to Box 0.
boxes[9].remove('meteor')
boxes[0].append('meteor')

# Remove the tiger and the coat from Box 2.
boxes[2].remove('tiger')
boxes[2].remove('coat')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")