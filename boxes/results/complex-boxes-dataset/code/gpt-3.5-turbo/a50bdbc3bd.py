# Initial state of boxes
boxes = {
    0: ['tiger', 'button', 'octopus', 'mountain', 'fridge'],
    1: ['towel', 'card', 'console', 'lion', 'bear'],
    2: ['train', 'horn', 'wire'],
    3: ['bag'],
    4: ['spoon', 'basket', 'drum', 'helmet'],
    5: ['ring', 'fish', 'forest', 'butterfly', 'bicycle'],
    6: ['mask'],
    7: ['island']
}

# Move the horn and the wire and the train from Box 2 to Box 6.
items_to_move = ['horn', 'wire', 'train']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[6].append(item)

# Remove the horn from Box 6.
boxes[6].remove('horn')

# Replace the spoon and the helmet and the drum with the soap and the jacket and the bird in Box 4.
boxes[4].remove('spoon')
boxes[4].remove('helmet')
boxes[4].remove('drum')
boxes[4].append('soap')
boxes[4].append('jacket')
boxes[4].append('bird')

# Replace the wire with the shampoo in Box 6.
boxes[6].remove('wire')
boxes[6].append('shampoo')

# Swap the bear in Box 1 with the bag in Box 3.
boxes[1].remove('bear')
boxes[3].remove('bag')
boxes[1].append('bag')
boxes[3].append('bear')

# Swap the forest in Box 5 with the mask in Box 6.
boxes[5].remove('forest')
boxes[6].remove('mask')
boxes[5].append('mask')
boxes[6].append('forest')

# Remove the island from Box 7.
boxes[7].remove('island')

# Replace the bear with the cow in Box 3.
boxes[3].remove('bear')
boxes[3].append('cow')

# Move the button and the octopus from Box 0 to Box 1.
items_to_move = ['button', 'octopus']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Move the mountain from Box 0 to Box 1.
boxes[0].remove('mountain')
boxes[1].append('mountain')

# Empty Box 0.
boxes[0] = []

# Replace the button and the mountain with the sock and the camera in Box 1.
boxes[1].remove('button')
boxes[1].remove('mountain')
boxes[1].append('sock')
boxes[1].append('camera')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")