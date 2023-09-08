# Initial state of boxes
boxes = {
    0: ['chair'],
    1: ['starfish'],
    2: ['usb', 'submarine', 'razor', 'wire', 'desert'],
    3: ['toaster', 'glasses', 'lamp'],
    4: [],
    5: ['dice', 'plate', 'meteor'],
    6: ['magnet', 'snow', 'towel', 'sock'],
    7: ['tree', 'shoes', 'bracelet', 'wallet'],
    8: ['shoe', 'grass', 'book', 'doll', 'sun'],
    9: [],
    10: []
}

# Remove the starfish from Box 1.
boxes[1].remove('starfish')

# Put the jungle into Box 0.
boxes[0].append('jungle')

# Swap the plate in Box 5 with the snow in Box 6.
boxes[5].remove('plate')
boxes[6].remove('snow')
boxes[5].append('snow')
boxes[6].append('plate')

# Swap the plate in Box 6 with the glasses in Box 3.
boxes[6].remove('plate')
boxes[3].remove('glasses')
boxes[6].append('glasses')
boxes[3].append('plate')

# Put the ocean and the headphone and the wig into Box 4.
items_to_move = ['ocean', 'headphone', 'wig']
for item in items_to_move:
    boxes[4].append(item)

# Swap the towel in Box 6 with the wire in Box 2.
boxes[6].remove('towel')
boxes[2].remove('wire')
boxes[6].append('wire')
boxes[2].append('towel')

# Remove the tree and the shoes and the wallet from Box 7.
items_to_remove = ['tree', 'shoes', 'wallet']
for item in items_to_remove:
    boxes[7].remove(item)

# Swap the chair in Box 0 with the glasses in Box 6.
boxes[0].remove('chair')
boxes[6].remove('glasses')
boxes[0].append('glasses')
boxes[6].append('chair')

# Move the jungle and the glasses from Box 0 to Box 9.
items_to_move = ['jungle', 'glasses']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[9].append(item)

# Put the soap and the snow into Box 4.
items_to_move = ['soap', 'snow']
for item in items_to_move:
    boxes[4].append(item)

# Replace the lamp with the speaker in Box 3.
boxes[3].remove('lamp')
boxes[3].append('speaker')

# Swap the soap in Box 4 with the bracelet in Box 7.
boxes[4].remove('soap')
boxes[7].remove('bracelet')
boxes[4].append('bracelet')
boxes[7].append('soap')

# Empty Box 3.
boxes[3] = []

# Move the soap from Box 7 to Box 3.
boxes[7].remove('soap')
boxes[3].append('soap')

# Put the horn and the key into Box 0.
items_to_move = ['horn', 'key']
for item in items_to_move:
    boxes[0].append(item)

# Remove the meteor and the dice from Box 5.
items_to_remove = ['meteor', 'dice']
for item in items_to_remove:
    boxes[5].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")