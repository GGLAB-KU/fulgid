# Initial state of boxes
boxes = {
    0: [],
    1: ['bag', 'scarf'],
    2: ['leaf', 'car', 'wallet'],
    3: [],
    4: ['battery'],
    5: ['frame'],
    6: ['guitar', 'jungle'],
    7: ['sock', 'tiger', 'polish', 'plane', 'rocket'],
    8: ['seaweed'],
    9: ['sun', 'comb', 'coat', 'forest', 'freezer'],
    10: ['wig', 'star', 'sculpture', 'desert'],
    11: [],
    12: ['chair', 'cat', 'whistle', 'glove', 'toy'],
    13: ['table', 'grass'],
    14: []
}

# Put the shampoo and the river and the pants into Box 2.
boxes[2].extend(['shampoo', 'river', 'pants'])

# Put the piano and the sculpture into Box 14.
boxes[14].extend(['piano', 'sculpture'])

# Swap the battery in Box 4 with the rocket in Box 7.
boxes[4], boxes[7] = boxes[7], boxes[4]

# Put the mirror and the star and the note into Box 1.
boxes[1].extend(['mirror', 'star', 'note'])

# Swap the jungle in Box 6 with the sculpture in Box 14.
boxes[6], boxes[14] = boxes[14], boxes[6]

# Replace the river with the shampoo in Box 2.
boxes[2].remove('river')
boxes[2].append('shampoo')

# Remove the star from Box 10.
boxes[10].remove('star')

# Replace the freezer and the forest with the horn and the table in Box 9.
boxes[9].remove('freezer')
boxes[9].remove('forest')
boxes[9].append('horn')
boxes[9].append('table')

# Put the fridge and the controller into Box 7.
boxes[7].extend(['fridge', 'controller'])

# Move the horn from Box 9 to Box 0.
boxes[9].remove('horn')
boxes[0].append('horn')

# Remove the jungle and the piano from Box 14.
boxes[14].remove('jungle')
boxes[14].remove('piano')

# Swap the frame in Box 5 with the cat in Box 12.
boxes[5], boxes[12] = boxes[12], boxes[5]

# Move the wig and the desert and the sculpture from Box 10 to Box 13.
items_to_move = ['wig', 'desert', 'sculpture']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[13].append(item)

# Swap the table in Box 9 with the grass in Box 13.
boxes[9], boxes[13] = boxes[13], boxes[9]

# Replace the sculpture with the toaster in Box 13.
boxes[13].remove('sculpture')
boxes[13].append('toaster')

# Remove the cat from Box 5.
boxes[5].remove('cat')

# Put the violin and the leaf into Box 10.
boxes[10].extend(['violin', 'leaf'])

# Move the star and the bag from Box 1 to Box 4.
items_to_move = ['star', 'bag']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Swap the guitar in Box 6 with the fridge in Box 7.
boxes[6], boxes[7] = boxes[7], boxes[6]

# Replace the wig and the desert and the toaster with the guitar and the violin and the bus in Box 13.
boxes[13].remove('wig')
boxes[13].remove('desert')
boxes[13].remove('toaster')
boxes[13].extend(['guitar', 'violin', 'bus'])

# Remove the sculpture and the fridge from Box 6.
boxes[6].remove('sculpture')
boxes[6].remove('fridge')

# Swap the leaf in Box 10 with the rocket in Box 4.
boxes[10], boxes[4] = boxes[4], boxes[10]

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")