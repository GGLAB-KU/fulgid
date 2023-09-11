# Initial state of boxes
boxes = {
    0: ['apple', 'shark', 'coral'],
    1: [],
    2: ['telescope', 'pan', 'shorts', 'branch', 'moon'],
    3: ['coat', 'soap']
}

# Move the coat and the soap from Box 3 to Box 0.
boxes[0].extend(boxes[3])
boxes[3] = []

# Swap the apple in Box 0 with the shorts in Box 2.
boxes[0].remove('apple')
boxes[2].remove('shorts')
boxes[0].append('shorts')
boxes[2].append('apple')

# Swap the telescope in Box 2 with the coral in Box 0.
boxes[2].remove('telescope')
boxes[0].remove('coral')
boxes[2].append('coral')
boxes[0].append('telescope')

# Replace the apple and the moon with the lion and the butterfly in Box 2.
boxes[2].remove('apple')
boxes[2].remove('moon')
boxes[2].append('lion')
boxes[2].append('butterfly')

# Remove the soap and the telescope and the shark from Box 0.
items_to_remove = ['soap', 'telescope', 'shark']
for item in items_to_remove:
    boxes[0].remove(item)

# Move the coat from Box 0 to Box 3.
boxes[3].append('coat')
boxes[0].remove('coat')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")