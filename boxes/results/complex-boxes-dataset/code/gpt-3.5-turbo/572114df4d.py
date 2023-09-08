# Initial state of boxes
boxes = {
    0: [],
    1: ['star', 'coral'],
    2: ['scissors'],
    3: ['laptop', 'hat', 'polish', 'mirror', 'ship'],
    4: ['ring'],
    5: [],
    6: ['game', 'spoon', 'wig', 'bicycle'],
    7: ['toaster', 'lamp', 'microwave'],
    8: ['seaweed', 'console']
}

# Remove the spoon and the bicycle and the game from Box 6.
items_to_remove = ['spoon', 'bicycle', 'game']
for item in items_to_remove:
    boxes[6].remove(item)

# Move the star and the coral from Box 1 to Box 3.
items_to_move = ['star', 'coral']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Replace the console and the seaweed with the branch and the swimsuit in Box 8.
boxes[8].remove('console')
boxes[8].remove('seaweed')
boxes[8].append('branch')
boxes[8].append('swimsuit')

# Move the scissors from Box 2 to Box 5.
boxes[2].remove('scissors')
boxes[5].append('scissors')

# Swap the wig in Box 6 with the ring in Box 4.
boxes[6].remove('wig')
boxes[4].remove('ring')
boxes[6].append('ring')
boxes[4].append('wig')

# Replace the wig with the train in Box 4.
boxes[4].remove('wig')
boxes[4].append('train')

# Put the starfish and the flute and the wig into Box 7.
items_to_move = ['starfish', 'flute', 'wig']
for item in items_to_move:
    boxes[7].append(item)

# Swap the scissors in Box 5 with the train in Box 4.
boxes[5].remove('scissors')
boxes[4].remove('train')
boxes[5].append('train')
boxes[4].append('scissors')

# Empty Box 3.
boxes[3] = []

# Swap the swimsuit in Box 8 with the scissors in Box 4.
boxes[8].remove('swimsuit')
boxes[4].remove('scissors')
boxes[8].append('scissors')
boxes[4].append('swimsuit')

# Empty Box 6.
boxes[6] = []

# Swap the train in Box 5 with the starfish in Box 7.
boxes[5].remove('train')
boxes[7].remove('starfish')
boxes[5].append('starfish')
boxes[7].append('train')

# Put the jungle and the glasses into Box 7.
items_to_move = ['jungle', 'glasses']
for item in items_to_move:
    boxes[7].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")