# Initial state of boxes
boxes = {
    0: ['coral', 'scarf', 'apple'],
    1: ['skirt', 'ring', 'note', 'keyboard', 'wig'],
    2: [],
    3: ['jacket', 'paint', 'swimsuit', 'horse'],
    4: ['comb', 'glasses'],
    5: ['puzzle'],
    6: ['dress'],
    7: ['pants', 'pot', 'shark'],
    8: ['desert', 'button', 'polish', 'river'],
    9: ['coin', 'sculpture', 'rock'],
    10: ['table', 'toaster', 'elephant', 'snow'],
    11: ['watch'],
    12: ['storm', 'brush', 'bicycle', 'cat', 'bird']
}

# Remove the apple and the coral from Box 0.
boxes[0].remove('apple')
boxes[0].remove('coral')

# Put the telescope and the bowl and the ship into Box 7.
boxes[7].append('telescope')
boxes[7].append('bowl')
boxes[7].append('ship')

# Put the bicycle into Box 9.
boxes[9].append('bicycle')

# Remove the pot from Box 7.
boxes[7].remove('pot')

# Replace the note and the keyboard and the ring with the motorcycle and the mirror and the thunder in Box 1.
boxes[1].remove('note')
boxes[1].remove('keyboard')
boxes[1].remove('ring')
boxes[1].append('motorcycle')
boxes[1].append('mirror')
boxes[1].append('thunder')

# Replace the scarf with the mask in Box 0.
boxes[0].remove('scarf')
boxes[0].append('mask')

# Move the brush and the storm and the bird from Box 12 to Box 2.
items_to_move = ['brush', 'storm', 'bird']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[2].append(item)

# Empty Box 6.
boxes[6] = []

# Move the paint and the jacket and the horse from Box 3 to Box 12.
items_to_move = ['paint', 'jacket', 'horse']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[12].append(item)

# Move the bicycle and the sculpture from Box 9 to Box 10.
items_to_move = ['bicycle', 'sculpture']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[10].append(item)

# Remove the pants from Box 7.
boxes[7].remove('pants')

# Move the thunder and the motorcycle and the wig from Box 1 to Box 12.
items_to_move = ['thunder', 'motorcycle', 'wig']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[12].append(item)

# Remove the puzzle from Box 5.
boxes[5].remove('puzzle')

# Put the makeup into Box 2.
boxes[2].append('makeup')

# Move the rock and the coin from Box 9 to Box 0.
items_to_move = ['rock', 'coin']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[0].append(item)

# Replace the button with the toy in Box 8.
boxes[8].remove('button')
boxes[8].append('toy')

# Put the beach into Box 1.
boxes[1].append('beach')

# Remove the rock and the mask and the coin from Box 0.
items_to_remove = ['rock', 'mask', 'coin']
for item in items_to_remove:
    boxes[0].remove(item)

# Put the harmonica and the wallet into Box 12.
boxes[12].append('harmonica')
boxes[12].append('wallet')

# Move the mirror from Box 1 to Box 8.
boxes[1].remove('mirror')
boxes[8].append('mirror')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")