box = {
    0: ['puzzle'],
    1: [],
    2: ['submarine'],
    3: ['elephant', 'boot', 'bag', 'zipper'],
    4: [],
    5: [],
    6: ['grinder', 'perfume', 'button', 'river', 'coat'],
    7: ['rock', 'lion'],
    8: ['speaker', 'car', 'glove', 'train']
}

# Replace the elephant and the bag with the desert and the shampoo in Box 3
box[3] = ['desert', 'shampoo']

# Move the car from Box 8 to Box 1
box[1].append(box[8].pop(box[8].index('car')))

# Remove the submarine from Box 2
box[2] = []

# Swap the perfume in Box 6 with the puzzle in Box 0
box[0], box[6] = box[6], box[0]

# Swap the shampoo in Box 3 with the lion in Box 7
box[3][box[3].index('shampoo')], box[7][box[7].index('lion')] = box[7][box[7].index('lion')], box[3][box[3].index('shampoo')]

# Move the puzzle and the grinder from Box 6 to Box 5
box[5].extend([box[6].pop(box[6].index('puzzle')), box[6].pop(box[6].index('grinder'))])

# Put the river into Box 3
box[3].append('river')

# Replace the puzzle with the piano in Box 5
box[5][box[5].index('puzzle')] = 'piano'

# Empty Box 7
box[7] = []

# Move the glove and the train and the speaker from Box 8 to Box 5
box[5].extend([box[8].pop(box[8].index('glove')), box[8].pop(box[8].index('train')), box[8].pop(box[8].index('speaker'))])

# Put the coral into Box 8
box[8].append('coral')

# Remove the desert and the zipper and the boot from Box 3
box[3].remove('desert')
box[3].remove('zipper')
box[3].remove('boot')

# Swap the river in Box 6 with the car in Box 1
box[1][box[1].index('car')], box[6][box[6].index('river')] = box[6][box[6].index('river')], box[1][box[1].index('car')]

# Print the contents of each box
for i in range(9):
    print(f"Box {i}: {box[i]}")