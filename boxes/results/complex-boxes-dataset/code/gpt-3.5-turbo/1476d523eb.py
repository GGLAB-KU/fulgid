# Initial state of boxes
boxes = {
    0: ['spoon', 'octopus', 'snow', 'fork'],
    1: ['boat', 'scissors'],
    2: ['umbrella', 'cow'],
    3: ['violin', 'button', 'hat'],
    4: ['seaweed']
}

# Move the boat from Box 1 to Box 3.
boxes[1].remove('boat')
boxes[3].append('boat')

# Put the necklace and the motorcycle and the puzzle into Box 0.
items_to_add = ['necklace', 'motorcycle', 'puzzle']
for item in items_to_add:
    boxes[0].append(item)

# Put the elephant into Box 4.
boxes[4].append('elephant')

# Replace the elephant with the horn in Box 4.
boxes[4].remove('elephant')
boxes[4].append('horn')

# Swap the seaweed in Box 4 with the cow in Box 2.
boxes[4].remove('seaweed')
boxes[2].remove('cow')
boxes[4].append('cow')
boxes[2].append('seaweed')

# Remove the horn and the cow from Box 4.
boxes[4].remove('horn')
boxes[4].remove('cow')

# Move the violin from Box 3 to Box 1.
boxes[3].remove('violin')
boxes[1].append('violin')

# Empty Box 3.
boxes[3] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")