# Initial state of boxes
boxes = {
    0: ['laptop', 'soap', 'boat', 'book'],
    1: ['usb', 'bell'],
    2: ['perfume'],
    3: ['shoes', 'lamp', 'shoe', 'ring', 'cup'],
    4: ['gloves'],
    5: ['ship', 'microwave', 'battery', 'phone', 'whistle'],
    6: ['glasses', 'oven', 'beach', 'train', 'razor']
}

# Swap the gloves in Box 4 with the perfume in Box 2.
boxes[4].remove('gloves')
boxes[2].remove('perfume')
boxes[4].append('perfume')
boxes[2].append('gloves')

# Put the scarf and the violin and the card into Box 4.
items_to_put = ['scarf', 'violin', 'card']
for item in items_to_put:
    boxes[4].append(item)

# Put the car into Box 0.
boxes[0].append('car')

# Remove the gloves from Box 2.
boxes[2].remove('gloves')

# Put the river and the moon into Box 1.
items_to_put = ['river', 'moon']
for item in items_to_put:
    boxes[1].append(item)

# Swap the violin in Box 4 with the usb in Box 1.
boxes[4].remove('violin')
boxes[1].remove('usb')
boxes[4].append('usb')
boxes[1].append('violin')

# Replace the microwave with the shark in Box 5.
boxes[5].remove('microwave')
boxes[5].append('shark')

# Remove the ring and the shoes from Box 3.
items_to_remove = ['ring', 'shoes']
for item in items_to_remove:
    boxes[3].remove(item)

# Swap the cup in Box 3 with the boat in Box 0.
boxes[3].remove('cup')
boxes[0].remove('boat')
boxes[3].append('boat')
boxes[0].append('cup')

# Replace the moon and the bell and the violin with the perfume and the zipper and the forest in Box 1.
boxes[1].remove('moon')
boxes[1].remove('bell')
boxes[1].remove('violin')
boxes[1].append('perfume')
boxes[1].append('zipper')
boxes[1].append('forest')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")