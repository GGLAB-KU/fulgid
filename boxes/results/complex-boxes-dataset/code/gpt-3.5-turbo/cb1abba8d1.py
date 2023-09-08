# Initial state of boxes
boxes = {
    0: ['fish', 'drum'],
    1: ['tie'],
    2: ['battery', 'shampoo', 'book', 'soap'],
    3: ['blanket', 'umbrella', 'submarine', 'wig', 'whistle'],
    4: []
}

# Move the soap and the battery from Box 2 to Box 1.
boxes[2].remove('soap')
boxes[2].remove('battery')
boxes[1].append('soap')
boxes[1].append('battery')

# Move the wig from Box 3 to Box 2.
boxes[3].remove('wig')
boxes[2].append('wig')

# Remove the shampoo and the book from Box 2.
boxes[2].remove('shampoo')
boxes[2].remove('book')

# Remove the wig from Box 2.
boxes[2].remove('wig')

# Empty Box 1.
boxes[1] = []

# Put the comet into Box 0.
boxes[0].append('comet')

# Put the button and the rock and the glasses into Box 0.
boxes[0].append('button')
boxes[0].append('rock')
boxes[0].append('glasses')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")