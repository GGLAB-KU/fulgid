# Initial state of boxes
boxes = {
    0: ['butterfly', 'tiger'],
    1: ['necklace'],
    2: ['bowl'],
    3: ['needle'],
    4: ['pillow', 'shampoo', 'phone']
}

# Put the piano and the needle into Box 3.
boxes[3].append('piano')
boxes[3].append('needle')

# Move the bowl from Box 2 to Box 4.
boxes[2].remove('bowl')
boxes[4].append('bowl')

# Replace the butterfly and the tiger with the bag and the keyboard in Box 0.
boxes[0].remove('butterfly')
boxes[0].remove('tiger')
boxes[0].append('bag')
boxes[0].append('keyboard')

# Remove the keyboard from Box 0.
boxes[0].remove('keyboard')

# Move the bag from Box 0 to Box 2.
boxes[0].remove('bag')
boxes[2].append('bag')

# Remove the phone and the shampoo from Box 4.
boxes[4].remove('phone')
boxes[4].remove('shampoo')

# Move the bag from Box 2 to Box 0.
boxes[2].remove('bag')
boxes[0].append('bag')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")