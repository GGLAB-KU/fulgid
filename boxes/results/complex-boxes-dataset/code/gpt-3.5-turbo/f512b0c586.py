# Initial state of boxes
boxes = {
    0: ['sandals', 'lightning', 'guitar', 'ring', 'basket'],
    1: [],
    2: ['submarine', 'thunder', 'mountain'],
    3: [],
    4: ['bell'],
    5: ['toy', 'shorts', 'controller', 'forest', 'charger'],
    6: ['toothbrush', 'earring'],
    7: ['fridge', 'laptop', 'needle', 'motorcycle', 'brush'],
    8: [],
    9: ['leaf', 'zipper', 'headphone', 'glove'],
    10: ['boot', 'magnet', 'card', 'tie', 'watch'],
    11: ['scarf'],
    12: ['table'],
    13: ['shark', 'hat', 'shelf'],
    14: ['speaker']
}

# Replace the table with the dog in Box 12.
boxes[12].remove('table')
boxes[12].append('dog')

# Replace the shelf and the hat with the perfume and the frame in Box 13.
boxes[13].remove('shelf')
boxes[13].remove('hat')
boxes[13].append('perfume')
boxes[13].append('frame')

# Move the headphone and the leaf and the zipper from Box 9 to Box 6.
items_to_move = ['headphone', 'leaf', 'zipper']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[6].append(item)

# Remove the thunder from Box 2.
boxes[2].remove('thunder')

# Replace the scarf with the ocean in Box 11.
boxes[11].remove('scarf')
boxes[11].append('ocean')

# Swap the perfume in Box 13 with the mountain in Box 2.
boxes[13].remove('perfume')
boxes[2].remove('mountain')
boxes[13].append('mountain')
boxes[2].append('perfume')

# Replace the earring and the zipper with the grass and the freezer in Box 6.
boxes[6].remove('earring')
boxes[9].remove('zipper')
boxes[6].append('grass')
boxes[6].append('freezer')

# Empty Box 0.
boxes[0] = []

# Move the charger and the forest and the shorts from Box 5 to Box 13.
items_to_move = ['charger', 'forest', 'shorts']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[13].append(item)

# Empty Box 10.
boxes[10] = []

# Move the fridge and the brush and the laptop from Box 7 to Box 10.
items_to_move = ['fridge', 'brush', 'laptop']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[10].append(item)

# Put the lion and the cat and the watch into Box 4.
items_to_put = ['lion', 'cat', 'watch']
for item in items_to_put:
    boxes[4].append(item)

# Put the shoes into Box 12.
boxes[12].append('shoes')

# Put the apple and the mask into Box 4.
items_to_put = ['apple', 'mask']
for item in items_to_put:
    boxes[4].append(item)

# Swap the shorts in Box 13 with the toy in Box 5.
boxes[13].remove('shorts')
boxes[5].remove('toy')
boxes[13].append('toy')
boxes[5].append('shorts')

# Move the apple and the cat and the bell from Box 4 to Box 10.
items_to_move = ['apple', 'cat', 'bell']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[10].append(item)

# Replace the submarine with the toothpaste in Box 2.
boxes[2].remove('submarine')
boxes[2].append('toothpaste')

# Replace the glove with the charger in Box 9.
boxes[9].remove('glove')
boxes[9].append('charger')

# Replace the motorcycle with the sock in Box 7.
boxes[7].remove('motorcycle')
boxes[7].append('sock')

# Put the dress into Box 3.
boxes[3].append('dress')

# Replace the controller and the shorts with the cow and the thunder in Box 5.
boxes[5].remove('controller')
boxes[5].remove('shorts')
boxes[5].append('cow')
boxes[5].append('thunder')

# Move the dress from Box 3 to Box 10.
boxes[3].remove('dress')
boxes[10].append('dress')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")