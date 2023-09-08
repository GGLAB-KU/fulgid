# Initial state of boxes
boxes = {
    0: ['shoe'],
    1: ['piano'],
    2: [],
    3: [],
    4: ['hat', 'belt', 'needle'],
    5: ['clock', 'bear', 'laptop']
}

# Move the laptop from Box 5 to Box 4.
boxes[5].remove('laptop')
boxes[4].append('laptop')

# Put the dress into Box 1.
boxes[1].append('dress')

# Remove the shoe from Box 0.
boxes[0].remove('shoe')

# Replace the piano and the dress with the game and the desert in Box 1.
boxes[1].remove('piano')
boxes[1].remove('dress')
boxes[1].append('game')
boxes[1].append('desert')

# Move the game from Box 1 to Box 3.
boxes[1].remove('game')
boxes[3].append('game')

# Replace the hat and the needle with the coral and the seaweed in Box 4.
boxes[4].remove('hat')
boxes[4].remove('needle')
boxes[4].append('coral')
boxes[4].append('seaweed')

# Swap the desert in Box 1 with the belt in Box 4.
boxes[1].remove('desert')
boxes[4].remove('belt')
boxes[1].append('belt')
boxes[4].append('desert')

# Put the bird and the butterfly and the branch into Box 4.
items_to_move = ['bird', 'butterfly', 'branch']
for item in items_to_move:
    boxes[4].append(item)

# Put the leaf and the scissors and the island into Box 1.
items_to_move = ['leaf', 'scissors', 'island']
for item in items_to_move:
    boxes[1].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")