# Initial state of boxes
boxes = {
    0: ['razor', 'zipper', 'whistle'],
    1: [],
    2: ['coin', 'coat', 'branch', 'note', 'spoon'],
    3: [],
    4: ['keyboard', 'game', 'blender', 'grinder'],
    5: ['hat', 'toy', 'dice', 'thunder', 'makeup'],
    6: ['sculpture', 'gloves', 'beach', 'jacket', 'bus'],
    7: ['necklace', 'mirror', 'polish', 'sock'],
    8: ['crown', 'controller'],
    9: ['pan', 'book'],
    10: ['candle', 'truck', 'island', 'lion', 'telescope']
}

# Put the thread and the headphone into Box 5.
boxes[5].append('thread')
boxes[5].append('headphone')

# Replace the mirror with the branch in Box 7.
boxes[7].remove('mirror')
boxes[7].append('branch')

# Swap the controller in Box 8 with the thunder in Box 5.
boxes[8].remove('controller')
boxes[5].remove('thunder')
boxes[8].append('thunder')
boxes[5].append('controller')

# Swap the coat in Box 2 with the sculpture in Box 6.
boxes[2].remove('coat')
boxes[6].remove('sculpture')
boxes[2].append('sculpture')
boxes[6].append('coat')

# Move the thread and the dice and the headphone from Box 5 to Box 9.
items_to_move = ['thread', 'dice', 'headphone']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[9].append(item)

# Remove the telescope and the lion and the island from Box 10.
items_to_remove = ['telescope', 'lion', 'island']
for item in items_to_remove:
    boxes[10].remove(item)

# Put the towel into Box 7.
boxes[7].append('towel')

# Put the dress into Box 7.
boxes[7].append('dress')

# Replace the pan and the book and the thread with the rocket and the whistle and the headphone in Box 9.
boxes[9].remove('pan')
boxes[9].remove('book')
boxes[9].remove('thread')
boxes[9].append('rocket')
boxes[9].append('whistle')
boxes[9].append('headphone')

# Remove the coat and the beach from Box 6.
boxes[6].remove('coat')
boxes[6].remove('beach')

# Replace the crown with the gloves in Box 8.
boxes[8].remove('crown')
boxes[8].append('gloves')

# Put the comet into Box 8.
boxes[8].append('comet')

# Empty Box 8.
boxes[8] = []

# Move the headphone from Box 9 to Box 5.
boxes[9].remove('headphone')
boxes[5].append('headphone')

# Put the shirt and the bowl and the bell into Box 10.
boxes[10].append('shirt')
boxes[10].append('bowl')
boxes[10].append('bell')

# Empty Box 0.
boxes[0] = []

# Put the thunder into Box 2.
boxes[2].append('thunder')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")