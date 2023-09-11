# Initial state of boxes
boxes = {
    0: ['earring'],
    1: [],
    2: ['card', 'snow'],
    3: [],
    4: ['lightning', 'wire'],
    5: ['mixer'],
    6: ['fish', 'mountain', 'motorcycle', 'towel']
}

# Remove the mixer from Box 5.
boxes[5].remove('mixer')

# Move the card from Box 2 to Box 5.
boxes[2].remove('card')
boxes[5].append('card')

# Move the snow from Box 2 to Box 1.
boxes[2].remove('snow')
boxes[1].append('snow')

# Put the spoon into Box 5.
boxes[5].append('spoon')

# Remove the lightning and the wire from Box 4.
boxes[4].remove('lightning')
boxes[4].remove('wire')

# Move the card from Box 5 to Box 1.
boxes[5].remove('card')
boxes[1].append('card')

# Move the towel and the fish and the motorcycle from Box 6 to Box 0.
items_to_move = ['towel', 'fish', 'motorcycle']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[0].append(item)

# Swap the snow in Box 1 with the mountain in Box 6.
boxes[1].remove('snow')
boxes[6].remove('mountain')
boxes[1].append('mountain')
boxes[6].append('snow')

# Replace the spoon with the truck in Box 5.
boxes[5].remove('spoon')
boxes[5].append('truck')

# Swap the truck in Box 5 with the card in Box 1.
boxes[5].remove('truck')
boxes[1].remove('card')
boxes[5].append('card')
boxes[1].append('truck')

# Move the towel from Box 0 to Box 1.
boxes[0].remove('towel')
boxes[1].append('towel')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")