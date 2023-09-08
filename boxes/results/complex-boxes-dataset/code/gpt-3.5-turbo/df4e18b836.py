# Initial state of boxes
boxes = {
    0: ['thread', 'forest', 'zipper', 'toaster', 'soap'],
    1: ['pants', 'bracelet', 'keyboard', 'table'],
    2: ['bear', 'submarine', 'coat'],
    3: ['beach', 'sock', 'sun'],
    4: ['ring', 'mixer', 'key', 'brush', 'glasses'],
    5: ['mask', 'car', 'dog', 'scissors', 'fish'],
    6: [],
    7: ['sculpture', 'elephant', 'helmet'],
    8: ['oven', 'belt', 'seaweed', 'harmonica', 'pan'],
    9: ['clock', 'cow', 'hat', 'phone', 'wallet'],
    10: ['pot', 'charger', 'book', 'perfume'],
    11: ['vase', 'usb', 'polish', 'blender', 'button'],
    12: ['doll', 'planet', 'tree', 'cat']
}

# Put the swimsuit and the sun and the lamp into Box 2.
boxes[2].append('swimsuit')
boxes[2].append('sun')
boxes[2].append('lamp')

# Remove the sculpture and the helmet from Box 7.
boxes[7].remove('sculpture')
boxes[7].remove('helmet')

# Replace the table with the cup in Box 1.
boxes[1].remove('table')
boxes[1].append('cup')

# Move the elephant from Box 7 to Box 9.
boxes[7].remove('elephant')
boxes[9].append('elephant')

# Replace the usb and the polish with the spoon and the shoe in Box 11.
boxes[11].remove('usb')
boxes[11].remove('polish')
boxes[11].append('spoon')
boxes[11].append('shoe')

# Move the elephant and the wallet and the phone from Box 9 to Box 1.
items_to_move = ['elephant', 'wallet', 'phone']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[1].append(item)

# Swap the cup in Box 1 with the coat in Box 2.
boxes[1].remove('cup')
boxes[2].remove('coat')
boxes[1].append('coat')
boxes[2].append('cup')

# Put the flower and the rain and the whistle into Box 6.
boxes[6].append('flower')
boxes[6].append('rain')
boxes[6].append('whistle')

# Put the scissors and the freezer into Box 7.
boxes[7].append('scissors')
boxes[7].append('freezer')

# Move the scissors and the freezer from Box 7 to Box 5.
items_to_move = ['scissors', 'freezer']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[5].append(item)

# Remove the key and the ring from Box 4.
boxes[4].remove('key')
boxes[4].remove('ring')

# Swap the book in Box 10 with the glasses in Box 4.
boxes[10].remove('book')
boxes[4].remove('glasses')
boxes[10].append('glasses')
boxes[4].append('book')

# Swap the bear in Box 2 with the toaster in Box 0.
boxes[2].remove('bear')
boxes[0].remove('toaster')
boxes[2].append('toaster')
boxes[0].append('bear')

# Move the soap and the forest and the bear from Box 0 to Box 1.
items_to_move = ['soap', 'forest', 'bear']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Move the pan and the belt from Box 8 to Box 6.
items_to_move = ['pan', 'belt']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[6].append(item)

# Swap the pants in Box 1 with the doll in Box 12.
boxes[1].remove('pants')
boxes[12].remove('doll')
boxes[1].append('doll')
boxes[12].append('pants')

# Replace the wallet with the whistle in Box 1.
boxes[1].remove('wallet')
boxes[1].append('whistle')

# Move the sock and the beach from Box 3 to Box 0.
boxes[3].remove('sock')
boxes[3].remove('beach')
boxes[0].append('sock')
boxes[0].append('beach')

# Move the book and the mixer and the brush from Box 4 to Box 9.
items_to_move = ['book', 'mixer', 'brush']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[9].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")