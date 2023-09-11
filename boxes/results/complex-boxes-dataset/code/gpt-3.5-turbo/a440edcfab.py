# Initial state of boxes
boxes = {
    0: ['helmet'],
    1: ['umbrella', 'fridge'],
    2: ['cup', 'skirt', 'keyboard', 'usb', 'cow'],
    3: ['motorcycle'],
    4: ['pan']
}

# Remove the umbrella and the fridge from Box 1.
boxes[1].remove('umbrella')
boxes[1].remove('fridge')

# Remove the helmet from Box 0.
boxes[0].remove('helmet')

# Empty Box 4.
boxes[4] = []

# Replace the keyboard with the skirt in Box 2.
boxes[2].remove('keyboard')
boxes[2].append('skirt')

# Put the shirt into Box 3.
boxes[3].append('shirt')

# Remove the skirt from Box 2.
boxes[2].remove('skirt')

# Swap the usb in Box 2 with the motorcycle in Box 3.
boxes[2].remove('usb')
boxes[3].remove('motorcycle')
boxes[2].append('motorcycle')
boxes[3].append('usb')

# Replace the cup and the skirt and the cow with the forest and the necklace and the lipstick in Box 2.
boxes[2].remove('cup')
boxes[2].remove('skirt')
boxes[2].remove('cow')
boxes[2].append('forest')
boxes[2].append('necklace')
boxes[2].append('lipstick')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")