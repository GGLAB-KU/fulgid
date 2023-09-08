# Initial state of boxes
boxes = {
    0: ['magnet', 'mirror'],
    1: ['wig', 'seaweed', 'umbrella'],
    2: ['rain', 'crown', 'jungle', 'shorts'],
    3: ['toothpaste', 'soap', 'helmet'],
    4: ['leaf', 'cow', 'game']
}

# Remove the wig and the umbrella from Box 1.
boxes[1].remove('wig')
boxes[1].remove('umbrella')

# Empty Box 3.
boxes[3] = []

# Replace the mirror and the magnet with the swimsuit and the submarine in Box 0.
boxes[0].remove('mirror')
boxes[0].remove('magnet')
boxes[0].append('swimsuit')
boxes[0].append('submarine')

# Put the island into Box 4.
boxes[4].append('island')

# Move the swimsuit from Box 0 to Box 3.
boxes[0].remove('swimsuit')
boxes[3].append('swimsuit')

# Move the game and the island from Box 4 to Box 2.
boxes[4].remove('game')
boxes[4].remove('island')
boxes[2].append('game')
boxes[2].append('island')

# Move the cow from Box 4 to Box 3.
boxes[4].remove('cow')
boxes[3].append('cow')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")