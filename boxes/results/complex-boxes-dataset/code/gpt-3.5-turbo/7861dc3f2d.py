# Initial state of boxes
boxes = {
    0: ['violin', 'watch', 'bird', 'magnet', 'drum'],
    1: [],
    2: ['horn', 'shark', 'dolphin', 'brush'],
    3: ['hat', 'mixer', 'snow', 'fish', 'beach'],
    4: ['lamp', 'whistle', 'blanket'],
    5: ['boat', 'piano', 'helmet', 'bicycle'],
    6: [],
    7: ['shelf', 'vase', 'swimsuit', 'pillow'],
    8: ['river', 'shoes', 'branch', 'submarine'],
    9: ['pan', 'plate'],
    10: ['motorcycle']
}

# Swap the shark in Box 2 with the mixer in Box 3.
boxes[2].remove('shark')
boxes[3].remove('mixer')
boxes[2].append('mixer')
boxes[3].append('shark')

# Swap the pillow in Box 7 with the river in Box 8.
boxes[7].remove('pillow')
boxes[8].remove('river')
boxes[7].append('river')
boxes[8].append('pillow')

# Move the hat and the snow from Box 3 to Box 0.
items_to_move = ['hat', 'snow']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Move the bicycle and the piano and the helmet from Box 5 to Box 8.
items_to_move = ['bicycle', 'piano', 'helmet']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[8].append(item)

# Swap the bird in Box 0 with the beach in Box 3.
boxes[0].remove('bird')
boxes[3].remove('beach')
boxes[0].append('beach')
boxes[3].append('bird')

# Remove the pillow and the branch from Box 8.
boxes[8].remove('pillow')
boxes[8].remove('branch')

# Move the vase and the river from Box 7 to Box 10.
boxes[7].remove('vase')
boxes[8].remove('river')
boxes[10].append('vase')
boxes[10].append('river')

# Move the fish and the shark and the bird from Box 3 to Box 0.
items_to_move = ['fish', 'shark', 'bird']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Put the dice and the coat and the fridge into Box 2.
items_to_put = ['dice', 'coat', 'fridge']
for item in items_to_put:
    boxes[2].append(item)

# Swap the shelf in Box 7 with the dolphin in Box 2.
boxes[7].remove('shelf')
boxes[2].remove('dolphin')
boxes[7].append('dolphin')
boxes[2].append('shelf')

# Remove the pan and the plate from Box 9.
boxes[9].remove('pan')
boxes[9].remove('plate')

# Remove the dolphin from Box 7.
boxes[7].remove('dolphin')

# Swap the brush in Box 2 with the lamp in Box 4.
boxes[2].remove('brush')
boxes[4].remove('lamp')
boxes[2].append('lamp')
boxes[4].append('brush')

# Move the motorcycle from Box 10 to Box 8.
boxes[10].remove('motorcycle')
boxes[8].append('motorcycle')

# Remove the mixer and the coat and the horn from Box 2.
boxes[2].remove('mixer')
boxes[2].remove('coat')
boxes[2].remove('horn')

# Remove the whistle from Box 4.
boxes[4].remove('whistle')

# Move the boat from Box 5 to Box 4.
boxes[5].remove('boat')
boxes[4].append('boat')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")