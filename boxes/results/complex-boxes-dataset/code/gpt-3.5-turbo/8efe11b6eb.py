# Initial state of boxes
boxes = {
    0: ['horn', 'lamp'],
    1: ['usb', 'pillow'],
    2: ['rocket', 'starfish', 'shelf', 'skirt'],
    3: ['book', 'bag', 'bus'],
    4: ['chair', 'planet'],
    5: ['forest', 'glasses'],
    6: ['cat']
}

# Remove the forest from Box 5.
boxes[5].remove('forest')

# Replace the usb with the shorts in Box 1.
boxes[1].remove('usb')
boxes[1].append('shorts')

# Put the wig and the laptop and the snow into Box 5.
items_to_add = ['wig', 'laptop', 'snow']
for item in items_to_add:
    boxes[5].append(item)

# Swap the skirt in Box 2 with the pillow in Box 1.
boxes[2].remove('skirt')
boxes[1].remove('pillow')
boxes[2].append('pillow')
boxes[1].append('skirt')

# Put the butterfly into Box 3.
boxes[3].append('butterfly')

# Move the laptop from Box 5 to Box 3.
boxes[5].remove('laptop')
boxes[3].append('laptop')

# Swap the lamp in Box 0 with the laptop in Box 3.
boxes[0].remove('lamp')
boxes[3].remove('laptop')
boxes[0].append('laptop')
boxes[3].append('lamp')

# Put the flower into Box 2.
boxes[2].append('flower')

# Replace the shorts and the skirt with the gloves and the microwave in Box 1.
boxes[1].remove('shorts')
boxes[1].remove('skirt')
boxes[1].append('gloves')
boxes[1].append('microwave')

# Move the cat from Box 6 to Box 5.
boxes[6].remove('cat')
boxes[5].append('cat')

# Swap the bus in Box 3 with the planet in Box 4.
boxes[3].remove('bus')
boxes[4].remove('planet')
boxes[3].append('planet')
boxes[4].append('bus')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")