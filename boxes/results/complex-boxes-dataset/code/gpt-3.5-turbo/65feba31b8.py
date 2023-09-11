# Initial state of boxes
boxes = {
    0: ['forest'],
    1: ['apple', 'toothpaste', 'horse'],
    2: ['shelf', 'ring', 'rain', 'boat', 'lion'],
    3: ['blanket', 'game', 'train', 'tie', 'hat'],
    4: ['bag', 'shampoo', 'elephant', 'flute', 'mask']
}

# Replace the rain and the boat and the ring with the fork and the wig and the perfume in Box 2.
boxes[2].remove('rain')
boxes[2].remove('boat')
boxes[2].remove('ring')
boxes[2].append('fork')
boxes[2].append('wig')
boxes[2].append('perfume')

# Swap the wig in Box 2 with the tie in Box 3.
boxes[2].remove('wig')
boxes[3].remove('tie')
boxes[2].append('tie')
boxes[3].append('wig')

# Put the perfume into Box 2.
boxes[2].append('perfume')

# Remove the forest from Box 0.
boxes[0].remove('forest')

# Move the flute from Box 4 to Box 2.
boxes[4].remove('flute')
boxes[2].append('flute')

# Remove the shampoo and the elephant and the mask from Box 4.
items_to_remove = ['shampoo', 'elephant', 'mask']
for item in items_to_remove:
    boxes[4].remove(item)

# Swap the tie in Box 2 with the horse in Box 1.
boxes[2].remove('tie')
boxes[1].remove('horse')
boxes[2].append('horse')
boxes[1].append('tie')

# Move the bag from Box 4 to Box 3.
boxes[4].remove('bag')
boxes[3].append('bag')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")