# Initial state of boxes
boxes = {
    0: ['dog', 'scarf', 'sandals'],
    1: ['toothbrush', 'submarine', 'earring', 'dolphin', 'lipstick'],
    2: ['wig', 'frame', 'lightning', 'fridge'],
    3: ['coral', 'ocean', 'tiger'],
    4: [],
    5: [],
    6: ['cow', 'pot', 'horn', 'apple'],
    7: ['grass', 'toaster', 'beach', 'table'],
    8: ['fish', 'zipper', 'crown', 'basket', 'puzzle'],
    9: ['thunder', 'dice', 'shelf', 'mirror'],
    10: ['bag', 'microwave', 'dress']
}

# Remove the wig from Box 2.
boxes[2].remove('wig')

# Move the microwave and the bag from Box 10 to Box 7.
items_to_move = ['microwave', 'bag']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[7].append(item)

# Swap the table in Box 7 with the sandals in Box 0.
boxes[7].remove('table')
boxes[0].remove('sandals')
boxes[7].append('sandals')
boxes[0].append('table')

# Move the pot and the apple and the horn from Box 6 to Box 10.
items_to_move = ['pot', 'apple', 'horn']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[10].append(item)

# Put the leaf and the phone and the sun into Box 2.
items_to_add = ['leaf', 'phone', 'sun']
for item in items_to_add:
    boxes[2].append(item)

# Move the frame from Box 2 to Box 3.
boxes[2].remove('frame')
boxes[3].append('frame')

# Remove the dog and the table and the scarf from Box 0.
items_to_remove = ['dog', 'table', 'scarf']
for item in items_to_remove:
    boxes[0].remove(item)

# Replace the lightning with the table in Box 2.
boxes[2].remove('lightning')
boxes[2].append('table')

# Move the cow from Box 6 to Box 10.
boxes[6].remove('cow')
boxes[10].append('cow')

# Move the puzzle and the fish from Box 8 to Box 4.
items_to_move = ['puzzle', 'fish']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[4].append(item)

# Put the shirt and the usb into Box 6.
items_to_add = ['shirt', 'usb']
for item in items_to_add:
    boxes[6].append(item)

# Empty Box 7.
boxes[7] = []

# Remove the coral and the frame and the tiger from Box 3.
items_to_remove = ['coral', 'frame', 'tiger']
for item in items_to_remove:
    boxes[3].remove(item)

# Swap the apple in Box 10 with the usb in Box 6.
boxes[10].remove('apple')
boxes[6].remove('usb')
boxes[10].append('usb')
boxes[6].append('apple')

# Move the dice and the thunder and the mirror from Box 9 to Box 10.
items_to_move = ['dice', 'thunder', 'mirror']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[10].append(item)

# Remove the fish and the puzzle from Box 4.
items_to_remove = ['fish', 'puzzle']
for item in items_to_remove:
    boxes[4].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")