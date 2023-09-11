# Initial state of boxes
boxes = {
    0: [],
    1: ['vase', 'microscope', 'shark', 'headphone', 'mountain'],
    2: ['grass', 'fridge', 'toothbrush', 'scissors'],
    3: [],
    4: [],
    5: [],
    6: ['microwave', 'sock', 'dog'],
    7: ['lipstick', 'belt', 'cow', 'perfume', 'pants'],
    8: ['river']
}

# Remove the fridge from Box 2.
boxes[2].remove('fridge')

# Remove the lipstick and the pants and the cow from Box 7.
items_to_remove = ['lipstick', 'pants', 'cow']
for item in items_to_remove:
    boxes[7].remove(item)

# Put the sock into Box 4.
boxes[4].append('sock')

# Remove the microscope and the shark and the headphone from Box 1.
items_to_remove = ['microscope', 'shark', 'headphone']
for item in items_to_remove:
    boxes[1].remove(item)

# Remove the sock from Box 4.
boxes[4].remove('sock')

# Remove the toothbrush from Box 2.
boxes[2].remove('toothbrush')

# Put the microwave and the bicycle into Box 8.
boxes[8].append('microwave')
boxes[8].append('bicycle')

# Move the microwave and the sock from Box 6 to Box 3.
items_to_move = ['microwave', 'sock']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[3].append(item)

# Remove the bicycle and the microwave and the river from Box 8.
items_to_remove = ['bicycle', 'microwave', 'river']
for item in items_to_remove:
    boxes[8].remove(item)

# Remove the microwave from Box 3.
boxes[3].remove('microwave')

# Put the scissors and the jacket and the ship into Box 3.
items_to_add = ['scissors', 'jacket', 'ship']
for item in items_to_add:
    boxes[3].append(item)

# Remove the perfume from Box 7.
boxes[7].remove('perfume')

# Empty Box 3.
boxes[3] = []

# Replace the scissors and the grass with the bicycle and the console in Box 2.
boxes[2].remove('scissors')
boxes[2].remove('grass')
boxes[2].append('bicycle')
boxes[2].append('console')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")