# Initial state of boxes
boxes = {
    0: [],
    1: ['ocean', 'pan'],
    2: ['wallet', 'microscope', 'scissors', 'sandals', 'octopus'],
    3: [],
    4: ['shorts', 'skirt', 'rain', 'note', 'game'],
    5: ['needle', 'candle']
}

# Put the candle into Box 4.
boxes[4].append('candle')

# Put the apple and the piano and the dog into Box 4.
items_to_move = ['apple', 'piano', 'dog']
for item in items_to_move:
    boxes[4].append(item)

# Replace the octopus and the scissors with the shirt and the usb in Box 2.
boxes[2].remove('octopus')
boxes[2].remove('scissors')
boxes[2].append('shirt')
boxes[2].append('usb')

# Put the microwave into Box 5.
boxes[5].append('microwave')

# Put the jacket and the forest into Box 2.
items_to_move = ['jacket', 'forest']
for item in items_to_move:
    boxes[2].append(item)

# Move the needle and the candle from Box 5 to Box 3.
items_to_move = ['needle', 'candle']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[3].append(item)

# Empty Box 3.
boxes[3] = []

# Swap the microwave in Box 5 with the forest in Box 2.
boxes[5].remove('microwave')
boxes[2].remove('forest')
boxes[5].append('forest')
boxes[2].append('microwave')

# Remove the jacket from Box 2.
boxes[2].remove('jacket')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")