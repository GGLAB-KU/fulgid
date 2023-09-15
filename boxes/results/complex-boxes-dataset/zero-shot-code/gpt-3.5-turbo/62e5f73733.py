box = {
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

# Replace the dice with the bowl in Box 10
box[10] = ['bowl']

# Swap the fish in Box 6 with the battery in Box 0
box[0], box[6] = box[6], box[0]

# Remove the note and the helmet and the shoes from Box 3
box[3] = []

# Swap the storm in Box 6 with the fish in Box 0
box[0], box[6] = box[6], box[0]

# Move the bracelet from Box 1 to Box 4
box[4].append(box[1][0])
box[1] = []

# Swap the controller in Box 0 with the headphone in Box 7
box[0], box[7] = box[7], box[0]

# Move the crown from Box 12 to Box 0
box[0].append(box[12][0])
box[12] = []

# Swap the butterfly in Box 12 with the hat in Box 4
box[4].append(box[12][0])
box[12] = []

# Empty Box 6
box[6] = []

# Put the swimsuit and the crown and the toaster into Box 3
box[3].extend(['swimsuit', 'crown', 'toaster'])

# Remove the toothpaste from Box 2
box[2] = []

# Replace the river and the shelf with the branch and the plane in Box 11
box[11] = ['branch', 'plane']

# Empty Box 10
box[10] = []

# Remove the paint from Box 3
box[3].remove('paint')

# Replace the sculpture with the wallet in Box 8
box[8] = ['wallet']

# Replace the flute and the drum and the submarine with the whistle and the car and the camera in Box 9
box[9] = ['whistle', 'car', 'camera']

# Remove the plane and the branch from Box 11
box[11] = []

# Put the speaker and the bowl and the glasses into Box 8
box[8].extend(['speaker', 'bowl', 'glasses'])

# Move the wallet and the glasses from Box 8 to Box 0
box[0].extend([box[8][0], box[8][2]])
box[8] = []

# Print the contents of each box
for i in range(13):
    print(f"Box {i}: {box[i]}")