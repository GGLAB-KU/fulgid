# Initial state of boxes
boxes = {
    0: ['table', 'shirt', 'card'],
    1: ['river', 'phone'],
    2: ['pen', 'grass'],
    3: [],
    4: ['mountain', 'truck', 'whistle', 'charger', 'frame'],
    5: ['mixer', 'tiger', 'freezer'],
    6: ['submarine', 'violin', 'boat'],
    7: ['spoon', 'tree', 'sculpture'],
    8: ['ocean', 'star', 'scarf', 'fish']
}

# Remove the card and the shirt from Box 0.
boxes[0].remove('card')
boxes[0].remove('shirt')

# Remove the mixer from Box 5.
boxes[5].remove('mixer')

# Move the submarine and the boat and the violin from Box 6 to Box 8.
items_to_move = ['submarine', 'boat', 'violin']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[8].append(item)

# Replace the fish and the scarf with the freezer and the cup in Box 8.
boxes[8].remove('fish')
boxes[8].remove('scarf')
boxes[8].append('freezer')
boxes[8].append('cup')

# Put the shorts and the river into Box 3.
boxes[3].append('shorts')
boxes[3].append('river')

# Put the zipper and the fish and the seaweed into Box 2.
boxes[2].append('zipper')
boxes[2].append('fish')
boxes[2].append('seaweed')

# Put the sculpture into Box 6.
boxes[6].append('sculpture')

# Move the sculpture and the tree and the spoon from Box 7 to Box 4.
items_to_move = ['sculpture', 'tree', 'spoon']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[4].append(item)

# Move the phone from Box 1 to Box 3.
boxes[1].remove('phone')
boxes[3].append('phone')

# Put the car into Box 2.
boxes[2].append('car')

# Swap the river in Box 1 with the star in Box 8.
boxes[1].remove('river')
boxes[8].remove('star')
boxes[1].append('star')
boxes[8].append('river')

# Move the star from Box 1 to Box 0.
boxes[1].remove('star')
boxes[0].append('star')

# Move the sculpture from Box 6 to Box 8.
boxes[6].remove('sculpture')
boxes[8].append('sculpture')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")