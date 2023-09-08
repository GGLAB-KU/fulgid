# Initial state of boxes
boxes = {
    0: [],
    1: ['plate'],
    2: ['comb', 'shorts', 'toothpaste'],
    3: [],
    4: [],
    5: ['sculpture', 'cat', 'truck', 'horse']
}

# Replace the plate with the phone in Box 1.
boxes[1].remove('plate')
boxes[1].append('phone')

# Swap the toothpaste in Box 2 with the cat in Box 5.
boxes[2].remove('toothpaste')
boxes[5].remove('cat')
boxes[2].append('cat')
boxes[5].append('toothpaste')

# Remove the toothpaste and the truck and the sculpture from Box 5.
items_to_remove = ['toothpaste', 'truck', 'sculpture']
for item in items_to_remove:
    boxes[5].remove(item)

# Move the phone from Box 1 to Box 4.
boxes[1].remove('phone')
boxes[4].append('phone')

# Remove the comb from Box 2.
boxes[2].remove('comb')

# Move the phone from Box 4 to Box 1.
boxes[4].remove('phone')
boxes[1].append('phone')

# Put the grass and the horse into Box 5.
boxes[5].append('grass')
boxes[5].append('horse')

# Move the cat and the shorts from Box 2 to Box 4.
boxes[2].remove('cat')
boxes[2].remove('shorts')
boxes[4].append('cat')
boxes[4].append('shorts')

# Swap the ship in Box 5 with the shorts in Box 4.
boxes[5].remove('ship')
boxes[4].remove('shorts')
boxes[5].append('shorts')
boxes[4].append('ship')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")