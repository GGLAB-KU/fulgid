# Initial state of boxes
boxes = {
    0: ['sock'],
    1: ['razor', 'seaweed'],
    2: ['shampoo', 'shorts', 'pan', 'crown'],
    3: ['rain', 'mirror', 'comet', 'shirt'],
    4: ['chair', 'piano'],
    5: ['motorcycle', 'toy'],
    6: ['shark']
}

# Move the shark from Box 6 to Box 4.
boxes[6].remove('shark')
boxes[4].append('shark')

# Move the sock from Box 0 to Box 2.
boxes[0].remove('sock')
boxes[2].append('sock')

# Move the razor from Box 1 to Box 4.
boxes[1].remove('razor')
boxes[4].append('razor')

# Put the coat into Box 3.
boxes[3].append('coat')

# Empty Box 1.
boxes[1] = []

# Empty Box 4.
boxes[4] = []

# Put the belt and the oven into Box 6.
boxes[6].extend(['belt', 'oven'])

# Put the bird and the comb and the toy into Box 4.
boxes[4].extend(['bird', 'comb', 'toy'])

# Remove the comb and the bird from Box 4.
boxes[4].remove('comb')
boxes[4].remove('bird')

# Move the belt and the oven from Box 6 to Box 2.
boxes[6].remove('belt')
boxes[6].remove('oven')
boxes[2].extend(['belt', 'oven'])

# Replace the coat and the shirt with the forest and the microscope in Box 3.
boxes[3].remove('coat')
boxes[3].remove('shirt')
boxes[3].extend(['forest', 'microscope'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")