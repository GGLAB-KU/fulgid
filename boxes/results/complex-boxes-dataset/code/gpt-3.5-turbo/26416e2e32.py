# Initial state of boxes
boxes = {
    0: ['submarine', 'frame', 'helmet'],
    1: ['branch', 'grinder'],
    2: ['shark', 'plane', 'paint'],
    3: [],
    4: ['shoe', 'fish', 'dress', 'ship', 'puzzle'],
    5: ['doll', 'table', 'hat'],
    6: ['oven'],
    7: [],
    8: [],
    9: [],
    10: [],
    11: ['earring', 'sock'],
    12: ['truck', 'fork', 'planet', 'crown']
}

# Put the crown and the dress and the seaweed into Box 0.
boxes[0].append('crown')
boxes[0].append('dress')
boxes[0].append('seaweed')

# Put the beach and the pillow and the mixer into Box 0.
boxes[0].append('beach')
boxes[0].append('pillow')
boxes[0].append('mixer')

# Remove the table from Box 5.
boxes[5].remove('table')

# Put the shirt and the clock into Box 10.
boxes[10].append('shirt')
boxes[10].append('clock')

# Swap the earring in Box 11 with the shirt in Box 10.
boxes[11].remove('earring')
boxes[10].remove('shirt')
boxes[11].append('shirt')
boxes[10].append('earring')

# Put the wallet and the pen into Box 5.
boxes[5].append('wallet')
boxes[5].append('pen')

# Replace the oven with the skirt in Box 6.
boxes[6].remove('oven')
boxes[6].append('skirt')

# Put the boot and the basket and the plate into Box 4.
boxes[4].append('boot')
boxes[4].append('basket')
boxes[4].append('plate')

# Remove the grinder from Box 1.
boxes[1].remove('grinder')

# Swap the branch in Box 1 with the clock in Box 10.
boxes[1].remove('branch')
boxes[10].remove('clock')
boxes[1].append('clock')
boxes[10].append('branch')

# Replace the clock with the piano in Box 1.
boxes[1].remove('clock')
boxes[1].append('piano')

# Move the puzzle and the shoe and the fish from Box 4 to Box 5.
items_to_move = ['puzzle', 'shoe', 'fish']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[5].append(item)

# Move the pen and the hat from Box 5 to Box 2.
items_to_move = ['pen', 'hat']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[2].append(item)

# Swap the piano in Box 1 with the sock in Box 11.
boxes[1].remove('piano')
boxes[11].remove('sock')
boxes[1].append('sock')
boxes[11].append('piano')

# Swap the plane in Box 2 with the basket in Box 4.
boxes[2].remove('plane')
boxes[4].remove('basket')
boxes[2].append('basket')
boxes[4].append('plane')

# Put the toothpaste and the vase and the island into Box 7.
boxes[7].append('toothpaste')
boxes[7].append('vase')
boxes[7].append('island')

# Replace the branch and the earring with the polish and the dog in Box 10.
boxes[10].remove('branch')
boxes[11].remove('earring')
boxes[10].append('polish')
boxes[11].append('dog')

# Move the skirt from Box 6 to Box 0.
boxes[6].remove('skirt')
boxes[0].append('skirt')

# Replace the shark and the pen and the basket with the zipper and the needle and the card in Box 2.
boxes[2].remove('shark')
boxes[2].remove('pen')
boxes[4].remove('basket')
boxes[2].append('zipper')
boxes[2].append('needle')
boxes[2].append('card')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")