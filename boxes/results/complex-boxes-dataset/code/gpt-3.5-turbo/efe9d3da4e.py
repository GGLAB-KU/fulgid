# Initial state of boxes
boxes = {
    0: ['tape', 'headphone', 'tie', 'lightning', 'comet'],
    1: ['mixer', 'swimsuit'],
    2: ['belt', 'desert', 'keyboard', 'cloud'],
    3: ['pan', 'towel', 'mask', 'dolphin', 'horn'],
    4: ['river', 'apple'],
    5: ['card', 'microscope', 'controller'],
    6: ['fridge'],
    7: [],
    8: ['sun', 'guitar', 'rock', 'whistle', 'cup'],
    9: ['leaf', 'laptop', 'sock', 'forest'],
    10: ['tiger', 'tree', 'shelf', 'usb', 'hat'],
    11: [],
    12: ['shorts']
}

# Swap the controller in Box 5 with the dolphin in Box 3.
boxes[5].remove('controller')
boxes[3].remove('dolphin')
boxes[5].append('dolphin')
boxes[3].append('controller')

# Move the towel and the pan and the controller from Box 3 to Box 8.
items_to_move = ['towel', 'pan', 'controller']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[8].append(item)

# Remove the keyboard and the cloud from Box 2.
boxes[2].remove('keyboard')
boxes[2].remove('cloud')

# Move the laptop and the leaf from Box 9 to Box 5.
items_to_move = ['laptop', 'leaf']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[5].append(item)

# Put the telescope and the razor and the pot into Box 0.
items_to_put = ['telescope', 'razor', 'pot']
for item in items_to_put:
    boxes[0].append(item)

# Put the phone and the bell and the necklace into Box 5.
items_to_put = ['phone', 'bell', 'necklace']
for item in items_to_put:
    boxes[5].append(item)

# Swap the horn in Box 3 with the swimsuit in Box 1.
boxes[3].remove('horn')
boxes[1].remove('swimsuit')
boxes[3].append('swimsuit')
boxes[1].append('horn')

# Replace the sock with the horn in Box 9.
boxes[9].remove('sock')
boxes[9].append('horn')

# Put the crown and the rocket and the horse into Box 8.
items_to_put = ['crown', 'rocket', 'horse']
for item in items_to_put:
    boxes[8].append(item)

# Move the horn and the forest from Box 9 to Box 5.
items_to_move = ['horn', 'forest']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[5].append(item)

# Replace the tiger and the hat with the scissors and the cup in Box 10.
boxes[10].remove('tiger')
boxes[10].remove('hat')
boxes[10].append('scissors')
boxes[10].append('cup')

# Put the shampoo and the flute and the train into Box 0.
items_to_put = ['shampoo', 'flute', 'train']
for item in items_to_put:
    boxes[0].append(item)

# Move the shorts from Box 12 to Box 11.
boxes[12].remove('shorts')
boxes[11].append('shorts')

# Remove the lightning and the train from Box 0.
boxes[0].remove('lightning')
boxes[0].remove('train')

# Put the truck and the grass into Box 7.
items_to_put = ['truck', 'grass']
for item in items_to_put:
    boxes[7].append(item)

# Move the horn and the mixer from Box 1 to Box 0.
items_to_move = ['horn', 'mixer']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[0].append(item)

# Swap the grass in Box 7 with the tree in Box 10.
boxes[7].remove('grass')
boxes[10].remove('tree')
boxes[7].append('tree')
boxes[10].append('grass')

# Swap the guitar in Box 8 with the headphone in Box 0.
boxes[8].remove('guitar')
boxes[0].remove('headphone')
boxes[8].append('headphone')
boxes[0].append('guitar')

# Swap the guitar in Box 0 with the desert in Box 2.
boxes[0].remove('guitar')
boxes[2].remove('desert')
boxes[0].append('desert')
boxes[2].append('guitar')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")