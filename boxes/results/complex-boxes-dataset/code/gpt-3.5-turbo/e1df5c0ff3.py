# Initial state of boxes
boxes = {
    0: ['thunder', 'toothpaste', 'spoon'],
    1: ['motorcycle', 'note', 'pot', 'usb'],
    2: [],
    3: ['microwave', 'microscope'],
    4: ['toaster', 'ring', 'car', 'freezer', 'scissors'],
    5: ['console', 'plane'],
    6: ['boot', 'jungle'],
    7: ['plate', 'river', 'perfume'],
    8: ['controller', 'snow'],
    9: ['horse', 'sock', 'shoe', 'cow'],
    10: ['forest']
}

# Remove the toothpaste and the thunder and the spoon from Box 0.
items_to_remove = ['toothpaste', 'thunder', 'spoon']
for item in items_to_remove:
    boxes[0].remove(item)

# Move the river and the perfume and the plate from Box 7 to Box 10.
items_to_move = ['river', 'perfume', 'plate']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[10].append(item)

# Put the towel and the swimsuit into Box 8.
items_to_put = ['towel', 'swimsuit']
for item in items_to_put:
    boxes[8].append(item)

# Move the console from Box 5 to Box 7.
boxes[5].remove('console')
boxes[7].append('console')

# Swap the plate in Box 10 with the towel in Box 8.
boxes[10].remove('plate')
boxes[8].remove('towel')
boxes[10].append('towel')
boxes[8].append('plate')

# Put the phone and the bus and the horn into Box 2.
items_to_put = ['phone', 'bus', 'horn']
for item in items_to_put:
    boxes[2].append(item)

# Replace the forest and the perfume with the beach and the telescope in Box 10.
boxes[10].remove('forest')
boxes[10].remove('perfume')
boxes[10].append('beach')
boxes[10].append('telescope')

# Move the scissors and the car and the ring from Box 4 to Box 1.
items_to_move = ['scissors', 'car', 'ring']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[1].append(item)

# Empty Box 5.
boxes[5] = []

# Put the microwave into Box 4.
boxes[4].append('microwave')

# Move the ring from Box 1 to Box 2.
boxes[1].remove('ring')
boxes[2].append('ring')

# Remove the microscope from Box 3.
boxes[3].remove('microscope')

# Swap the jungle in Box 6 with the horn in Box 2.
boxes[6].remove('jungle')
boxes[2].remove('horn')
boxes[6].append('horn')
boxes[2].append('jungle')

# Move the horse and the cow and the sock from Box 9 to Box 7.
items_to_move = ['horse', 'cow', 'sock']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[7].append(item)

# Empty Box 2.
boxes[2] = []

# Remove the toaster from Box 4.
boxes[4].remove('toaster')

# Replace the snow with the wire in Box 8.
boxes[8].remove('snow')
boxes[8].append('wire')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")