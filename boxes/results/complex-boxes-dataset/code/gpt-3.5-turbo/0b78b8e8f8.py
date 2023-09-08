# Initial state of boxes
boxes = {
    0: ['lock', 'telescope'],
    1: ['note', 'shampoo', 'violin', 'dog', 'fridge'],
    2: ['bus', 'table'],
    3: ['scissors', 'grass', 'boot', 'toy', 'polish'],
    4: [],
    5: [],
    6: ['wire', 'elephant', 'toaster'],
    7: [],
    8: ['submarine', 'bowl', 'mask', 'jungle', 'shelf'],
    9: ['paint', 'crown', 'game', 'pan'],
    10: []
}

# Move the toy and the boot from Box 3 to Box 6.
items_to_move = ['toy', 'boot']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[6].append(item)

# Swap the toy in Box 6 with the fridge in Box 1.
boxes[6].remove('toy')
boxes[1].remove('fridge')
boxes[6].append('fridge')
boxes[1].append('toy')

# Put the dice into Box 9.
boxes[9].append('dice')

# Remove the bowl and the mask from Box 8.
boxes[8].remove('bowl')
boxes[8].remove('mask')

# Put the scissors and the piano and the submarine into Box 8.
items_to_move = ['scissors', 'piano', 'submarine']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[8].append(item)

# Put the skirt and the coat and the boat into Box 8.
items_to_move = ['skirt', 'coat', 'boat']
for item in items_to_move:
    boxes[8].append(item)

# Replace the polish and the scissors with the comb and the truck in Box 3.
boxes[3].remove('polish')
boxes[3].remove('scissors')
boxes[3].append('comb')
boxes[3].append('truck')

# Put the wallet and the razor into Box 10.
boxes[10].append('wallet')
boxes[10].append('razor')

# Move the shampoo and the dog from Box 1 to Box 4.
items_to_move = ['shampoo', 'dog']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Move the violin from Box 1 to Box 2.
boxes[1].remove('violin')
boxes[2].append('violin')

# Move the wallet from Box 10 to Box 4.
boxes[10].remove('wallet')
boxes[4].append('wallet')

# Remove the elephant from Box 6.
boxes[6].remove('elephant')

# Move the skirt and the shelf from Box 8 to Box 7.
items_to_move = ['skirt', 'shelf']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[7].append(item)

# Move the table and the violin and the bus from Box 2 to Box 10.
items_to_move = ['table', 'violin', 'bus']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[10].append(item)

# Replace the note and the toy with the rocket and the pot in Box 1.
boxes[1].remove('note')
boxes[1].remove('toy')
boxes[1].append('rocket')
boxes[1].append('pot')

# Move the shelf from Box 7 to Box 8.
boxes[7].remove('shelf')
boxes[8].append('shelf')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")