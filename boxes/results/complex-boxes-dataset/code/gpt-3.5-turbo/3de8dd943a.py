# Initial state of boxes
boxes = {
    0: ['apple', 'watch', 'frame', 'pan', 'key'],
    1: ['doll', 'tape', 'polish', 'cup'],
    2: ['pen', 'toy'],
    3: [],
    4: ['console'],
    5: ['rain'],
    6: ['oven', 'phone'],
    7: ['controller', 'bicycle', 'thread', 'pillow'],
    8: ['shoes', 'scissors', 'rocket', 'butterfly'],
    9: ['makeup', 'belt', 'charger'],
    10: ['laptop', 'ocean', 'ring'],
    11: [],
    12: ['comet', 'moon'],
    13: ['tiger', 'cloud', 'meteor', 'fridge', 'mountain']
}

# Remove the charger from Box 9.
boxes[9].remove('charger')

# Remove the pen and the toy from Box 2.
boxes[2].remove('pen')
boxes[2].remove('toy')

# Swap the ocean in Box 10 with the belt in Box 9.
boxes[10].remove('ocean')
boxes[9].remove('belt')
boxes[10].append('belt')
boxes[9].append('ocean')

# Put the paint and the pillow and the table into Box 9.
items_to_move = ['paint', 'pillow', 'table']
for item in items_to_move:
    boxes[9].append(item)

# Replace the belt and the laptop and the ring with the fridge and the dog and the comb in Box 10.
boxes[10].remove('belt')
boxes[10].remove('laptop')
boxes[10].remove('ring')
boxes[10].append('fridge')
boxes[10].append('dog')
boxes[10].append('comb')

# Move the polish from Box 1 to Box 4.
boxes[1].remove('polish')
boxes[4].append('polish')

# Move the fridge and the mountain from Box 13 to Box 0.
boxes[13].remove('fridge')
boxes[13].remove('mountain')
boxes[0].append('fridge')
boxes[0].append('mountain')

# Put the speaker and the umbrella into Box 7.
items_to_move = ['speaker', 'umbrella']
for item in items_to_move:
    boxes[7].append(item)

# Put the harmonica into Box 6.
boxes[6].append('harmonica')

# Put the boat into Box 8.
boxes[8].append('boat')

# Move the polish and the console from Box 4 to Box 3.
boxes[4].remove('polish')
boxes[4].remove('console')
boxes[3].append('polish')
boxes[3].append('console')

# Swap the console in Box 3 with the butterfly in Box 8.
boxes[3].remove('console')
boxes[8].remove('butterfly')
boxes[3].append('butterfly')
boxes[8].append('console')

# Replace the ocean and the paint with the shoes and the needle in Box 9.
boxes[9].remove('ocean')
boxes[9].remove('paint')
boxes[9].append('shoes')
boxes[9].append('needle')

# Move the tape and the cup and the doll from Box 1 to Box 4.
items_to_move = ['tape', 'cup', 'doll']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Swap the mountain in Box 0 with the boat in Box 8.
boxes[0].remove('mountain')
boxes[8].remove('boat')
boxes[0].append('boat')
boxes[8].append('mountain')

# Remove the apple from Box 0.
boxes[0].remove('apple')

# Move the cup and the tape and the doll from Box 4 to Box 5.
items_to_move = ['cup', 'tape', 'doll']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[5].append(item)

# Put the boat and the pan and the seaweed into Box 7.
items_to_move = ['boat', 'pan', 'seaweed']
for item in items_to_move:
    boxes[7].append(item)

# Replace the dog and the fridge with the chair and the car in Box 10.
boxes[10].remove('dog')
boxes[10].remove('fridge')
boxes[10].append('chair')
boxes[10].append('car')

# Put the camera and the makeup and the elephant into Box 1.
items_to_move = ['camera', 'makeup', 'elephant']
for item in items_to_move:
    boxes[1].append(item)

# Move the pan and the key from Box 0 to Box 11.
items_to_move = ['pan', 'key']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[11].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")