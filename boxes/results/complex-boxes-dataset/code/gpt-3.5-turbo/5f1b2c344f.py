# Initial state of boxes
boxes = {
    0: ['beach', 'coin', 'thunder', 'bowl', 'makeup'],
    1: ['coral', 'basket', 'guitar', 'cup'],
    2: ['earring'],
    3: [],
    4: ['blanket', 'phone'],
    5: ['pillow'],
    6: ['puzzle', 'key', 'toothbrush', 'table'],
    7: [],
    8: ['desert', 'ring', 'boot', 'bracelet', 'microscope']
}

# Remove the coral from Box 1.
boxes[1].remove('coral')

# Swap the earring in Box 2 with the blanket in Box 4.
boxes[2].remove('earring')
boxes[4].remove('blanket')
boxes[2].append('blanket')
boxes[4].append('earring')

# Move the cup and the guitar and the basket from Box 1 to Box 6.
items_to_move = ['cup', 'guitar', 'basket']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[6].append(item)

# Empty Box 6.
boxes[6] = []

# Remove the coin from Box 0.
boxes[0].remove('coin')

# Move the phone from Box 4 to Box 5.
boxes[4].remove('phone')
boxes[5].append('phone')

# Move the blanket from Box 2 to Box 8.
boxes[2].remove('blanket')
boxes[8].append('blanket')

# Move the bowl from Box 0 to Box 6.
boxes[0].remove('bowl')
boxes[6].append('bowl')

# Remove the bracelet from Box 8.
boxes[8].remove('bracelet')

# Put the mirror and the coral and the dice into Box 5.
items_to_put = ['mirror', 'coral', 'dice']
for item in items_to_put:
    boxes[5].append(item)

# Put the usb into Box 6.
boxes[6].append('usb')

# Swap the earring in Box 4 with the blanket in Box 8.
boxes[4].remove('earring')
boxes[8].remove('blanket')
boxes[4].append('blanket')
boxes[8].append('earring')

# Swap the microscope in Box 8 with the blanket in Box 4.
boxes[8].remove('microscope')
boxes[4].remove('blanket')
boxes[8].append('blanket')
boxes[4].append('microscope')

# Put the paint and the beach into Box 6.
items_to_put = ['paint', 'beach']
for item in items_to_put:
    boxes[6].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")