# Initial state of boxes
boxes = {
    0: ['cat', 'pen'],
    1: ['coral', 'brush', 'mixer'],
    2: ['bus', 'toy', 'swimsuit', 'sun', 'fork'],
    3: [],
    4: [],
    5: [],
    6: ['drum', 'microscope', 'wire', 'rocket'],
    7: ['doll', 'dog', 'button', 'boot'],
    8: ['chair', 'harmonica', 'sculpture', 'wallet'],
    9: [],
    10: ['speaker', 'rock', 'apple', 'fish', 'perfume'],
    11: ['lion', 'bell', 'shelf', 'jacket', 'microwave'],
    12: []
}

# Move the toy and the swimsuit and the bus from Box 2 to Box 1.
items_to_move = ['toy', 'swimsuit', 'bus']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Replace the speaker and the perfume and the apple with the cat and the belt and the branch in Box 10.
boxes[10].remove('speaker')
boxes[10].remove('perfume')
boxes[10].remove('apple')
boxes[10].append('cat')
boxes[10].append('belt')
boxes[10].append('branch')

# Remove the sun and the fork from Box 2.
boxes[2].remove('sun')
boxes[2].remove('fork')

# Put the shampoo and the bag into Box 5.
boxes[5].append('shampoo')
boxes[5].append('bag')

# Move the dog and the doll from Box 7 to Box 12.
items_to_move = ['dog', 'doll']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[12].append(item)

# Replace the wire and the microscope and the rocket with the battery and the pot and the moon in Box 6.
boxes[6].remove('wire')
boxes[6].remove('microscope')
boxes[6].remove('rocket')
boxes[6].append('battery')
boxes[6].append('pot')
boxes[6].append('moon')

# Move the harmonica and the sculpture from Box 8 to Box 6.
items_to_move = ['harmonica', 'sculpture']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[6].append(item)

# Replace the rock and the cat with the helmet and the hat in Box 10.
boxes[10].remove('rock')
boxes[10].remove('cat')
boxes[10].append('helmet')
boxes[10].append('hat')

# Remove the harmonica from Box 6.
boxes[6].remove('harmonica')

# Empty Box 5.
boxes[5] = []

# Move the doll from Box 12 to Box 11.
boxes[12].remove('doll')
boxes[11].append('doll')

# Swap the dog in Box 12 with the boot in Box 7.
boxes[12].remove('dog')
boxes[7].remove('boot')
boxes[12].append('boot')
boxes[7].append('dog')

# Move the bus and the coral from Box 1 to Box 11.
items_to_move = ['bus', 'coral']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[11].append(item)

# Swap the swimsuit in Box 1 with the microwave in Box 11.
boxes[1].remove('swimsuit')
boxes[11].remove('microwave')
boxes[1].append('microwave')
boxes[11].append('swimsuit')

# Remove the pen and the cat from Box 0.
boxes[0].remove('pen')
boxes[0].remove('cat')

# Replace the brush and the microwave and the toy with the scissors and the belt and the forest in Box 1.
boxes[1].remove('brush')
boxes[1].remove('microwave')
boxes[1].remove('toy')
boxes[1].append('scissors')
boxes[1].append('belt')
boxes[1].append('forest')

# Remove the chair and the wallet from Box 8.
boxes[8].remove('chair')
boxes[8].remove('wallet')

# Move the forest and the scissors and the belt from Box 1 to Box 4.
items_to_move = ['forest', 'scissors', 'belt']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Put the horn and the star and the river into Box 3.
boxes[3].append('horn')
boxes[3].append('star')
boxes[3].append('river')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")