# Initial state of boxes
boxes = {
    0: ['shirt', 'seaweed', 'thunder'],
    1: ['charger', 'pants', 'cat', 'bag', 'storm'],
    2: [],
    3: ['piano', 'ring', 'bird', 'guitar'],
    4: ['horse', 'controller', 'table'],
    5: ['toothbrush'],
    6: ['boot', 'towel']
}

# Replace the bird and the guitar with the glove and the puzzle in Box 3.
boxes[3] = ['piano', 'ring', 'glove', 'puzzle']

# Put the glasses into Box 2.
boxes[2].append('glasses')

# Remove the towel and the boot from Box 6.
boxes[6] = []

# Replace the seaweed and the thunder with the elephant and the freezer in Box 0.
boxes[0] = ['shirt', 'elephant', 'freezer']

# Swap the charger in Box 1 with the glasses in Box 2.
boxes[1].remove('charger')
boxes[2].remove('glasses')
boxes[1].append('glasses')
boxes[2].append('charger')

# Remove the charger from Box 2.
boxes[2].remove('charger')

# Move the shirt and the elephant and the freezer from Box 0 to Box 5.
items_to_move = ['shirt', 'elephant', 'freezer']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Remove the puzzle from Box 3.
boxes[3].remove('puzzle')

# Move the storm and the cat from Box 1 to Box 4.
items_to_move = ['storm', 'cat']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Move the toothbrush from Box 5 to Box 2.
boxes[5].remove('toothbrush')
boxes[2].append('toothbrush')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")