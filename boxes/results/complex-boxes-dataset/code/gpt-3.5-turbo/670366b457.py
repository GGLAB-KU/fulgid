# Initial state of boxes
boxes = {
    0: ['boat', 'wire'],
    1: [],
    2: ['table', 'violin'],
    3: ['scissors', 'bus', 'key', 'moon', 'drum'],
    4: ['necklace'],
    5: ['plate'],
    6: ['bracelet', 'charger', 'shelf', 'speaker'],
    7: ['book', 'dolphin'],
    8: ['lipstick', 'cup', 'comet'],
    9: ['harmonica', 'wallet', 'controller', 'note'],
    10: ['laptop', 'rocket', 'pan'],
    11: ['shoes', 'polish', 'scarf', 'glasses'],
    12: ['truck', 'pants', 'motorcycle', 'flower'],
    13: ['cow', 'mirror', 'elephant'],
    14: ['plane', 'makeup', 'bicycle', 'boot']
}

# Replace the key with the car in Box 3.
boxes[3].remove('key')
boxes[3].append('car')

# Put the doll and the dice and the planet into Box 5.
items_to_put = ['doll', 'dice', 'planet']
for item in items_to_put:
    boxes[5].append(item)

# Put the mirror and the snow into Box 13.
items_to_put = ['mirror', 'snow']
for item in items_to_put:
    boxes[13].append(item)

# Replace the plate and the doll with the earring and the book in Box 5.
boxes[5].remove('plate')
boxes[5].remove('doll')
boxes[5].append('earring')
boxes[5].append('book')

# Swap the drum in Box 3 with the pan in Box 10.
boxes[3].remove('drum')
boxes[10].remove('pan')
boxes[3].append('pan')
boxes[10].append('drum')

# Move the bowl and the snow from Box 13 to Box 1.
items_to_move = ['bowl', 'snow']
for item in items_to_move:
    boxes[13].remove(item)
    boxes[1].append(item)

# Replace the wallet and the note with the toothbrush and the watch in Box 9.
boxes[9].remove('wallet')
boxes[9].remove('note')
boxes[9].append('toothbrush')
boxes[9].append('watch')

# Swap the harmonica in Box 9 with the plane in Box 14.
boxes[9].remove('harmonica')
boxes[14].remove('plane')
boxes[9].append('plane')
boxes[14].append('harmonica')

# Replace the cup with the snow in Box 8.
boxes[8].remove('cup')
boxes[8].append('snow')

# Remove the snow and the comet from Box 8.
boxes[8].remove('snow')
boxes[8].remove('comet')

# Put the lock and the tiger and the moon into Box 1.
items_to_put = ['lock', 'tiger', 'moon']
for item in items_to_put:
    boxes[1].append(item)

# Remove the rocket and the drum and the laptop from Box 10.
items_to_remove = ['rocket', 'drum', 'laptop']
for item in items_to_remove:
    boxes[10].remove(item)

# Move the bowl from Box 1 to Box 3.
boxes[1].remove('bowl')
boxes[3].append('bowl')

# Move the pants from Box 12 to Box 5.
boxes[12].remove('pants')
boxes[5].append('pants')

# Replace the polish with the console in Box 11.
boxes[11].remove('polish')
boxes[11].append('console')

# Move the plane from Box 9 to Box 0.
boxes[9].remove('plane')
boxes[0].append('plane')

# Swap the elephant in Box 13 with the tiger in Box 1.
boxes[13].remove('elephant')
boxes[1].remove('tiger')
boxes[13].append('tiger')
boxes[1].append('elephant')

# Put the makeup into Box 10.
boxes[10].append('makeup')

# Move the makeup from Box 14 to Box 9.
boxes[14].remove('makeup')
boxes[9].append('makeup')

# Move the toothbrush and the watch and the controller from Box 9 to Box 5.
items_to_move = ['toothbrush', 'watch', 'controller']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[5].append(item)

# Replace the lipstick with the belt in Box 8.
boxes[8].remove('lipstick')
boxes[8].append('belt')

# Remove the flower from Box 12.
boxes[12].remove('flower')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")