# Initial state of boxes
boxes = {
    0: ['battery', 'controller'],
    1: ['bracelet'],
    2: ['toothpaste'],
    3: ['helmet', 'microscope', 'note', 'paint', 'shoes'],
    4: ['hat', 'bird', 'ship'],
    5: [],
    6: ['fish', 'freezer', 'soap', 'storm'],
    7: ['headphone'],
    8: ['sculpture'],
    9: ['microwave', 'drum', 'table', 'flute', 'submarine'],
    10: ['dice'],
    11: ['shelf', 'river'],
    12: ['crown', 'tree', 'butterfly']
}

# Replace the dice with the bowl in Box 10.
boxes[10].remove('dice')
boxes[10].append('bowl')

# Swap the fish in Box 6 with the battery in Box 0.
boxes[0].remove('battery')
boxes[6].remove('fish')
boxes[0].append('fish')
boxes[6].append('battery')

# Remove the note and the helmet and the shoes from Box 3.
items_to_remove = ['note', 'helmet', 'shoes']
for item in items_to_remove:
    boxes[3].remove(item)

# Swap the storm in Box 6 with the fish in Box 0.
boxes[0].remove('fish')
boxes[6].remove('storm')
boxes[0].append('storm')
boxes[6].append('fish')

# Move the bracelet from Box 1 to Box 4.
boxes[1].remove('bracelet')
boxes[4].append('bracelet')

# Swap the controller in Box 0 with the headphone in Box 7.
boxes[0].remove('controller')
boxes[7].remove('headphone')
boxes[0].append('headphone')
boxes[7].append('controller')

# Move the crown from Box 12 to Box 0.
boxes[12].remove('crown')
boxes[0].append('crown')

# Swap the butterfly in Box 12 with the hat in Box 4.
boxes[4].remove('hat')
boxes[12].remove('butterfly')
boxes[4].append('butterfly')
boxes[12].append('hat')

# Empty Box 6.
boxes[6] = []

# Put the swimsuit and the crown and the toaster into Box 3.
items_to_move = ['swimsuit', 'crown', 'toaster']
for item in items_to_move:
    boxes[3].append(item)

# Remove the toothpaste from Box 2.
boxes[2].remove('toothpaste')

# Replace the river and the shelf with the branch and the plane in Box 11.
boxes[11].remove('river')
boxes[11].remove('shelf')
boxes[11].append('branch')
boxes[11].append('plane')

# Empty Box 10.
boxes[10] = []

# Remove the paint from Box 3.
boxes[3].remove('paint')

# Replace the sculpture with the wallet in Box 8.
boxes[8].remove('sculpture')
boxes[8].append('wallet')

# Replace the flute and the drum and the submarine with the whistle and the car and the camera in Box 9.
boxes[9].remove('flute')
boxes[9].remove('drum')
boxes[9].remove('submarine')
boxes[9].append('whistle')
boxes[9].append('car')
boxes[9].append('camera')

# Remove the plane and the branch from Box 11.
boxes[11].remove('plane')
boxes[11].remove('branch')

# Put the speaker and the bowl and the glasses into Box 8.
items_to_move = ['speaker', 'bowl', 'glasses']
for item in items_to_move:
    boxes[8].append(item)

# Move the wallet and the glasses from Box 8 to Box 0.
boxes[8].remove('wallet')
boxes[8].remove('glasses')
boxes[0].append('wallet')
boxes[0].append('glasses')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")