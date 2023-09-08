# Initial state of boxes
boxes = {
    0: ['snow', 'rain'],
    1: ['flower', 'horse', 'fridge', 'telescope'],
    2: [],
    3: [],
    4: [],
    5: ['skirt', 'sun', 'sculpture'],
    6: ['doll', 'violin', 'microwave', 'lipstick', 'plane'],
    7: ['shark', 'microscope', 'headphone'],
    8: ['blender', 'note', 'branch', 'button'],
    9: []
}

# Remove the skirt from Box 5.
boxes[5].remove('skirt')

# Replace the rain with the cloud in Box 0.
boxes[0].remove('rain')
boxes[0].append('cloud')

# Put the cow and the book and the apple into Box 6.
items_to_put = ['cow', 'book', 'apple']
for item in items_to_put:
    boxes[6].append(item)

# Swap the doll in Box 6 with the horse in Box 1.
boxes[6].remove('doll')
boxes[1].remove('horse')
boxes[6].append('horse')
boxes[1].append('doll')

# Swap the sun in Box 5 with the flower in Box 1.
boxes[5].remove('sun')
boxes[1].remove('flower')
boxes[5].append('flower')
boxes[1].append('sun')

# Remove the snow from Box 0.
boxes[0].remove('snow')

# Swap the sculpture in Box 5 with the shark in Box 7.
boxes[5].remove('sculpture')
boxes[7].remove('shark')
boxes[5].append('shark')
boxes[7].append('sculpture')

# Swap the microscope in Box 7 with the telescope in Box 1.
boxes[7].remove('microscope')
boxes[1].remove('telescope')
boxes[7].append('telescope')
boxes[1].append('microscope')

# Put the doll and the razor and the soap into Box 6.
items_to_put = ['doll', 'razor', 'soap']
for item in items_to_put:
    boxes[6].append(item)

# Move the cloud from Box 0 to Box 8.
boxes[0].remove('cloud')
boxes[8].append('cloud')

# Put the jungle and the river and the tree into Box 0.
items_to_put = ['jungle', 'river', 'tree']
for item in items_to_put:
    boxes[0].append(item)

# Move the microwave from Box 6 to Box 4.
boxes[6].remove('microwave')
boxes[4].append('microwave')

# Replace the flower with the needle in Box 5.
boxes[5].remove('flower')
boxes[5].append('needle')

# Swap the microwave in Box 4 with the needle in Box 5.
boxes[4].remove('microwave')
boxes[5].remove('needle')
boxes[4].append('needle')
boxes[5].append('microwave')

# Move the needle from Box 4 to Box 7.
boxes[4].remove('needle')
boxes[7].append('needle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")