# Initial state of boxes
boxes = {
    0: ['mixer', 'microwave', 'bracelet', 'key', 'book'],
    1: ['truck', 'microscope'],
    2: ['bag', 'horse', 'shorts', 'laptop', 'storm'],
    3: ['note', 'river', 'bear'],
    4: ['shampoo', 'razor', 'pants', 'mountain', 'helmet'],
    5: ['mirror'],
    6: ['bowl', 'sock', 'tape', 'console', 'soap'],
    7: ['lion', 'candle', 'charger']
}

# Move the book and the bracelet and the microwave from Box 0 to Box 1.
items_to_move = ['book', 'bracelet', 'microwave']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Remove the soap and the tape from Box 6.
boxes[6].remove('soap')
boxes[6].remove('tape')

# Empty Box 5.
boxes[5] = []

# Put the piano and the horse and the button into Box 1.
items_to_move = ['piano', 'horse', 'button']
for item in items_to_move:
    boxes[1].append(item)

# Replace the mixer and the key with the crown and the star in Box 0.
boxes[0].remove('mixer')
boxes[0].remove('key')
boxes[0].append('crown')
boxes[0].append('star')

# Remove the helmet and the razor from Box 4.
boxes[4].remove('helmet')
boxes[4].remove('razor')

# Remove the shampoo and the mountain from Box 4.
boxes[4].remove('shampoo')
boxes[4].remove('mountain')

# Move the star from Box 0 to Box 1.
boxes[0].remove('star')
boxes[1].append('star')

# Put the rain and the sock into Box 0.
boxes[0].append('rain')
boxes[0].append('sock')

# Move the rain and the sock from Box 0 to Box 5.
boxes[0].remove('rain')
boxes[0].remove('sock')
boxes[5].append('rain')
boxes[5].append('sock')

# Replace the bag and the storm with the glove and the grass in Box 2.
boxes[2].remove('bag')
boxes[2].remove('storm')
boxes[2].append('glove')
boxes[2].append('grass')

# Put the bear into Box 5.
boxes[5].append('bear')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")