# Initial state of boxes
boxes = {
    0: ['bowl', 'keyboard'],
    1: ['sandals'],
    2: ['microscope', 'shelf', 'sun', 'coat', 'dog'],
    3: ['rain'],
    4: ['drum', 'headphone', 'plane', 'camera'],
    5: []
}

# Put the toy into Box 2.
boxes[2].append('toy')

# Put the polish and the cloud and the sock into Box 2.
items_to_put = ['polish', 'cloud', 'sock']
for item in items_to_put:
    boxes[2].append(item)

# Put the plane and the thread into Box 3.
boxes[3].append('plane')
boxes[3].append('thread')

# Put the freezer and the bear and the umbrella into Box 0.
items_to_put = ['freezer', 'bear', 'umbrella']
for item in items_to_put:
    boxes[0].append(item)

# Swap the umbrella in Box 0 with the cloud in Box 2.
boxes[0].remove('umbrella')
boxes[2].remove('cloud')
boxes[0].append('cloud')
boxes[2].append('umbrella')

# Replace the sandals with the necklace in Box 1.
boxes[1].remove('sandals')
boxes[1].append('necklace')

# Swap the plane in Box 3 with the headphone in Box 4.
boxes[3].remove('plane')
boxes[4].remove('headphone')
boxes[3].append('headphone')
boxes[4].append('plane')

# Put the octopus and the coral and the plate into Box 4.
items_to_put = ['octopus', 'coral', 'plate']
for item in items_to_put:
    boxes[4].append(item)

# Swap the coral in Box 4 with the necklace in Box 1.
boxes[4].remove('coral')
boxes[1].remove('necklace')
boxes[4].append('necklace')
boxes[1].append('coral')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")