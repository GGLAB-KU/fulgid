# Initial state of boxes
boxes = {
    0: ['battery'],
    1: ['ring', 'boat', 'shirt'],
    2: ['makeup', 'pan'],
    3: ['rocket', 'cat', 'chair', 'toaster'],
    4: ['towel', 'coat', 'magnet', 'freezer', 'sun'],
    5: [],
    6: [],
    7: ['truck', 'pillow', 'vase', 'belt']
}

# Put the dolphin and the forest into Box 1.
boxes[1].append('dolphin')
boxes[1].append('forest')

# Swap the magnet in Box 4 with the rocket in Box 3.
boxes[4].remove('magnet')
boxes[3].remove('rocket')
boxes[4].append('rocket')
boxes[3].append('magnet')

# Swap the pillow in Box 7 with the pan in Box 2.
boxes[7].remove('pillow')
boxes[2].remove('pan')
boxes[7].append('pan')
boxes[2].append('pillow')

# Put the planet into Box 6.
boxes[6].append('planet')

# Remove the coat and the rocket and the sun from Box 4.
items_to_remove = ['coat', 'rocket', 'sun']
for item in items_to_remove:
    boxes[4].remove(item)

# Put the toothpaste and the horn into Box 4.
boxes[4].append('toothpaste')
boxes[4].append('horn')

# Replace the makeup and the pillow with the bag and the tiger in Box 2.
boxes[2].remove('makeup')
boxes[2].remove('pillow')
boxes[2].append('bag')
boxes[2].append('tiger')

# Move the planet from Box 6 to Box 2.
boxes[6].remove('planet')
boxes[2].append('planet')

# Remove the shirt from Box 1.
boxes[1].remove('shirt')

# Put the chair and the scissors into Box 3.
boxes[3].append('chair')
boxes[3].append('scissors')

# Move the boat and the dolphin from Box 1 to Box 2.
boxes[1].remove('boat')
boxes[1].remove('dolphin')
boxes[2].append('boat')
boxes[2].append('dolphin')

# Move the pan and the truck from Box 7 to Box 6.
boxes[7].remove('pan')
boxes[7].remove('truck')
boxes[6].append('pan')
boxes[6].append('truck')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")