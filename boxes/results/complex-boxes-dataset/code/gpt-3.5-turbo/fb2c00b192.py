# Initial state of boxes
boxes = {
    0: ['flower', 'shirt'],
    1: ['rain', 'scarf', 'needle', 'comet'],
    2: ['lamp', 'mirror', 'bicycle'],
    3: ['paint', 'shelf'],
    4: ['sun', 'necklace', 'guitar'],
    5: ['meteor'],
    6: ['blanket', 'wig', 'grass'],
    7: ['snow', 'butterfly', 'horse', 'puzzle'],
    8: ['wallet', 'lock', 'coin', 'makeup'],
    9: ['note', 'piano'],
    10: ['perfume', 'chair', 'console', 'sculpture'],
    11: [],
    12: ['horn', 'umbrella'],
    13: ['toaster']
}

# Swap the perfume in Box 10 with the shirt in Box 0.
boxes[0].remove('shirt')
boxes[10].remove('perfume')
boxes[0].append('perfume')
boxes[10].append('shirt')

# Remove the mirror from Box 2.
boxes[2].remove('mirror')

# Move the toaster from Box 13 to Box 12.
boxes[13].remove('toaster')
boxes[12].append('toaster')

# Move the flower and the perfume from Box 0 to Box 10.
items_to_move = ['flower', 'perfume']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[10].append(item)

# Swap the horn in Box 12 with the shelf in Box 3.
boxes[12].remove('horn')
boxes[3].remove('shelf')
boxes[12].append('shelf')
boxes[3].append('horn')

# Put the tree and the soap into Box 3.
items_to_move = ['tree', 'soap']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[3].append(item)

# Swap the meteor in Box 5 with the soap in Box 3.
boxes[5].remove('meteor')
boxes[3].remove('soap')
boxes[5].append('soap')
boxes[3].append('meteor')

# Replace the piano with the cat in Box 9.
boxes[9].remove('piano')
boxes[9].append('cat')

# Swap the sculpture in Box 10 with the note in Box 9.
boxes[10].remove('sculpture')
boxes[9].remove('note')
boxes[10].append('note')
boxes[9].append('sculpture')

# Move the sculpture from Box 9 to Box 3.
boxes[9].remove('sculpture')
boxes[3].append('sculpture')

# Move the rain and the scarf from Box 1 to Box 6.
items_to_move = ['rain', 'scarf']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[6].append(item)

# Replace the note with the belt in Box 10.
boxes[10].remove('note')
boxes[10].append('belt')

# Move the cat from Box 9 to Box 7.
boxes[9].remove('cat')
boxes[7].append('cat')

# Move the puzzle and the cat from Box 7 to Box 5.
items_to_move = ['puzzle', 'cat']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[5].append(item)

# Put the bicycle and the tree into Box 11.
items_to_move = ['bicycle', 'tree']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[11].append(item)

# Move the butterfly and the horse and the snow from Box 7 to Box 11.
items_to_move = ['butterfly', 'horse', 'snow']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[11].append(item)

# Put the lion and the blanket into Box 7.
items_to_move = ['lion', 'blanket']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[7].append(item)

# Move the needle and the comet from Box 1 to Box 8.
items_to_move = ['needle', 'comet']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[8].append(item)

# Move the horse from Box 11 to Box 13.
boxes[11].remove('horse')
boxes[13].append('horse')

# Replace the snow and the butterfly and the tree with the flute and the octopus and the controller in Box 11.
boxes[11].remove('snow')
boxes[11].remove('butterfly')
boxes[11].remove('tree')
boxes[11].append('flute')
boxes[11].append('octopus')
boxes[11].append('controller')

# Move the bicycle from Box 2 to Box 3.
boxes[2].remove('bicycle')
boxes[3].append('bicycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")