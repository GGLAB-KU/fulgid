# Initial state of boxes
boxes = {
    0: [],
    1: ['dog', 'spoon', 'train', 'plane', 'bus'],
    2: ['mountain', 'mixer', 'boot'],
    3: [],
    4: ['jungle', 'soap', 'pot'],
    5: ['shark', 'hat', 'wig', 'towel'],
    6: ['brush', 'mirror', 'bird'],
    7: ['phone'],
    8: [],
    9: [],
    10: ['grinder', 'elephant', 'branch']
}

# Move the mirror from Box 6 to Box 4.
boxes[6].remove('mirror')
boxes[4].append('mirror')

# Swap the spoon in Box 1 with the boot in Box 2.
boxes[1].remove('spoon')
boxes[2].remove('boot')
boxes[1].append('boot')
boxes[2].append('spoon')

# Remove the mixer and the spoon from Box 2.
boxes[2].remove('mixer')
boxes[2].remove('spoon')

# Remove the towel and the shark from Box 5.
boxes[5].remove('towel')
boxes[5].remove('shark')

# Replace the mirror and the pot with the towel and the hat in Box 4.
boxes[4].remove('mirror')
boxes[4].remove('pot')
boxes[4].append('towel')
boxes[4].append('hat')

# Empty Box 1.
boxes[1] = []

# Put the jacket and the speaker and the horse into Box 5.
items_to_move = ['jacket', 'speaker', 'horse']
for item in items_to_move:
    boxes[5].append(item)

# Empty Box 6.
boxes[6] = []

# Replace the elephant with the basket in Box 10.
boxes[10].remove('elephant')
boxes[10].append('basket')

# Move the basket and the branch and the grinder from Box 10 to Box 7.
items_to_move = ['basket', 'branch', 'grinder']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[7].append(item)

# Move the basket from Box 7 to Box 10.
boxes[7].remove('basket')
boxes[10].append('basket')

# Put the sculpture into Box 9.
boxes[9].append('sculpture')

# Remove the sculpture from Box 9.
boxes[9].remove('sculpture')

# Empty Box 10.
boxes[10] = []

# Swap the jungle in Box 4 with the grinder in Box 7.
boxes[4].remove('jungle')
boxes[7].remove('grinder')
boxes[4].append('grinder')
boxes[7].append('jungle')

# Replace the horse and the wig and the speaker with the controller and the starfish and the tiger in Box 5.
boxes[5].remove('horse')
boxes[5].remove('wig')
boxes[5].remove('speaker')
boxes[5].append('controller')
boxes[5].append('starfish')
boxes[5].append('tiger')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")