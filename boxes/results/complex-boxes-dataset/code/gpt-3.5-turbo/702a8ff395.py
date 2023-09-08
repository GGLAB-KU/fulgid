# Initial state of boxes
boxes = {
    0: ['bear', 'boat'],
    1: [],
    2: ['truck', 'sculpture', 'umbrella', 'laptop', 'violin'],
    3: [],
    4: ['shark', 'magnet', 'train'],
    5: ['fork', 'guitar', 'scarf', 'doll', 'bicycle'],
    6: ['island', 'makeup'],
    7: []
}

# Move the fork from Box 5 to Box 2.
boxes[5].remove('fork')
boxes[2].append('fork')

# Move the island and the makeup from Box 6 to Box 5.
boxes[6].remove('island')
boxes[6].remove('makeup')
boxes[5].append('island')
boxes[5].append('makeup')

# Replace the magnet with the grass in Box 4.
boxes[4].remove('magnet')
boxes[4].append('grass')

# Remove the grass and the shark from Box 4.
boxes[4].remove('grass')
boxes[4].remove('shark')

# Replace the bear and the boat with the truck and the makeup in Box 0.
boxes[0].remove('bear')
boxes[0].remove('boat')
boxes[0].append('truck')
boxes[0].append('makeup')

# Move the fork and the umbrella from Box 2 to Box 5.
boxes[2].remove('fork')
boxes[2].remove('umbrella')
boxes[5].append('fork')
boxes[5].append('umbrella')

# Remove the train from Box 4.
boxes[4].remove('train')

# Move the truck and the makeup from Box 0 to Box 7.
boxes[0].remove('truck')
boxes[0].remove('makeup')
boxes[7].append('truck')
boxes[7].append('makeup')

# Empty Box 2.
boxes[2] = []

# Move the makeup from Box 5 to Box 1.
boxes[5].remove('makeup')
boxes[1].append('makeup')

# Swap the truck in Box 7 with the makeup in Box 1.
boxes[7].remove('truck')
boxes[1].remove('makeup')
boxes[7].append('makeup')
boxes[1].append('truck')

# Replace the makeup and the makeup with the starfish and the battery in Box 7.
boxes[7].remove('makeup')
boxes[7].remove('makeup')
boxes[7].append('starfish')
boxes[7].append('battery')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")