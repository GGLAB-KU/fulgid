# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['shirt', 'phone', 'star', 'hat', 'mixer'],
    3: ['card']
}

# Put the coin and the pot into Box 1.
boxes[1].append('coin')
boxes[1].append('pot')

# Put the seaweed and the mirror and the usb into Box 0.
boxes[0].append('seaweed')
boxes[0].append('mirror')
boxes[0].append('usb')

# Swap the seaweed in Box 0 with the star in Box 2.
boxes[0].remove('seaweed')
boxes[2].remove('star')
boxes[0].append('star')
boxes[2].append('seaweed')

# Remove the card from Box 3.
boxes[3].remove('card')

# Swap the coin in Box 1 with the star in Box 0.
boxes[1].remove('coin')
boxes[0].remove('star')
boxes[1].append('star')
boxes[0].append('coin')

# Remove the phone from Box 2.
boxes[2].remove('phone')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")