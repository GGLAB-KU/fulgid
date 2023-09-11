# Initial state of boxes
boxes = {
    0: ['comet'],
    1: ['lamp', 'lock', 'flower', 'whistle', 'rain'],
    2: ['ship', 'leaf', 'game', 'blender'],
    3: ['plate', 'cup'],
    4: ['cow']
}

# Move the cow from Box 4 to Box 3.
boxes[4].remove('cow')
boxes[3].append('cow')

# Swap the cow in Box 3 with the lock in Box 1.
boxes[3].remove('cow')
boxes[1].remove('lock')
boxes[3].append('lock')
boxes[1].append('cow')

# Swap the rain in Box 1 with the leaf in Box 2.
boxes[1].remove('rain')
boxes[2].remove('leaf')
boxes[1].append('leaf')
boxes[2].append('rain')

# Move the leaf and the whistle and the flower from Box 1 to Box 3.
items_to_move = ['leaf', 'whistle', 'flower']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Move the comet from Box 0 to Box 4.
boxes[0].remove('comet')
boxes[4].append('comet')

# Swap the comet in Box 4 with the rain in Box 2.
boxes[4].remove('comet')
boxes[2].remove('rain')
boxes[4].append('rain')
boxes[2].append('comet')

# Move the lamp and the cow from Box 1 to Box 3.
items_to_move = ['lamp', 'cow']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Replace the rain with the truck in Box 4.
boxes[4].remove('rain')
boxes[4].append('truck')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")