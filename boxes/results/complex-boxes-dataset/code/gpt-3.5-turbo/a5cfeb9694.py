# Initial state of boxes
boxes = {
    0: ['harmonica', 'soap', 'coat', 'clock'],
    1: [],
    2: ['drum'],
    3: ['toothbrush', 'shoes', 'mountain', 'bowl'],
    4: ['tiger', 'microwave'],
    5: ['plane', 'umbrella', 'crown', 'jacket'],
    6: [],
    7: ['cloud', 'polish', 'controller', 'violin', 'cat'],
    8: ['thunder', 'flower', 'earring', 'desert', 'candle'],
    9: ['table']
}

# Move the shoes from Box 3 to Box 4.
boxes[3].remove('shoes')
boxes[4].append('shoes')

# Put the meteor and the mixer and the thread into Box 5.
items_to_move = ['meteor', 'mixer', 'thread']
for item in items_to_move:
    boxes[5].append(item)

# Remove the earring from Box 8.
boxes[8].remove('earring')

# Replace the drum with the freezer in Box 2.
boxes[2].remove('drum')
boxes[2].append('freezer')

# Remove the clock and the coat from Box 0.
boxes[0].remove('clock')
boxes[0].remove('coat')

# Swap the cat in Box 7 with the flower in Box 8.
boxes[7].remove('cat')
boxes[8].remove('flower')
boxes[7].append('flower')
boxes[8].append('cat')

# Replace the freezer with the ship in Box 2.
boxes[2].remove('freezer')
boxes[2].append('ship')

# Put the guitar and the oven and the flower into Box 2.
items_to_move = ['guitar', 'oven', 'flower']
for item in items_to_move:
    boxes[2].append(item)

# Move the umbrella and the meteor from Box 5 to Box 2.
items_to_move = ['umbrella', 'meteor']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[2].append(item)

# Swap the thunder in Box 8 with the controller in Box 7.
boxes[8].remove('thunder')
boxes[7].remove('controller')
boxes[8].append('controller')
boxes[7].append('thunder')

# Remove the violin and the polish from Box 7.
boxes[7].remove('violin')
boxes[7].remove('polish')

# Remove the cat from Box 8.
boxes[8].remove('cat')

# Put the needle into Box 5.
boxes[5].append('needle')

# Put the glove and the jacket into Box 4.
items_to_move = ['glove', 'jacket']
for item in items_to_move:
    boxes[4].append(item)

# Swap the jacket in Box 5 with the toothbrush in Box 3.
boxes[5].remove('jacket')
boxes[3].remove('toothbrush')
boxes[5].append('toothbrush')
boxes[3].append('jacket')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")