# Initial state of boxes
boxes = {
    0: ['oven', 'usb', 'grinder'],
    1: [],
    2: ['train', 'comet', 'razor', 'harmonica', 'coat'],
    3: ['sun', 'ocean', 'chair', 'mask', 'note'],
    4: []
}

# Remove the train and the coat and the razor from Box 2.
items_to_remove = ['train', 'coat', 'razor']
for item in items_to_remove:
    boxes[2].remove(item)

# Swap the oven in Box 0 with the sun in Box 3.
boxes[0].remove('oven')
boxes[3].remove('sun')
boxes[0].append('sun')
boxes[3].append('oven')

# Replace the usb with the blender in Box 0.
boxes[0].remove('usb')
boxes[0].append('blender')

# Move the comet from Box 2 to Box 1.
boxes[2].remove('comet')
boxes[1].append('comet')

# Put the flute into Box 1.
boxes[1].append('flute')

# Put the dolphin into Box 3.
boxes[3].append('dolphin')

# Remove the harmonica from Box 2.
boxes[2].remove('harmonica')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")