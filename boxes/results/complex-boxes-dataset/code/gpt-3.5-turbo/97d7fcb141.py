# Initial state of boxes
boxes = {
    0: ['shoe', 'razor', 'frame', 'toy'],
    1: ['rock', 'telescope', 'button'],
    2: ['butterfly', 'snow', 'laptop'],
    3: ['polish', 'jungle', 'car', 'tape', 'usb'],
    4: ['lamp', 'bus', 'makeup'],
    5: ['lightning', 'oven', 'magnet'],
    6: ['fridge'],
    7: ['needle', 'coin'],
    8: ['freezer'],
    9: ['blanket', 'moon'],
    10: ['pen'],
    11: ['ocean', 'bear', 'scissors', 'grinder'],
    12: ['pan', 'mask', 'book', 'leaf'],
    13: [],
    14: ['keyboard', 'grass', 'mirror', 'dog']
}

# Move the butterfly from Box 2 to Box 11.
boxes[2].remove('butterfly')
boxes[11].append('butterfly')

# Replace the ocean and the butterfly with the tree and the scarf in Box 11.
boxes[11].remove('ocean')
boxes[11].remove('butterfly')
boxes[11].append('tree')
boxes[11].append('scarf')

# Move the pen from Box 10 to Box 6.
boxes[10].remove('pen')
boxes[6].append('pen')

# Remove the rock and the button and the telescope from Box 1.
items_to_remove = ['rock', 'button', 'telescope']
for item in items_to_remove:
    boxes[1].remove(item)

# Move the car and the usb and the jungle from Box 3 to Box 7.
items_to_move = ['car', 'usb', 'jungle']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[7].append(item)

# Replace the toy with the shoes in Box 0.
boxes[0].remove('toy')
boxes[0].append('shoes')

# Remove the car from Box 7.
boxes[7].remove('car')

# Replace the freezer with the makeup in Box 8.
boxes[8].remove('freezer')
boxes[8].append('makeup')

# Replace the laptop and the snow with the book and the harmonica in Box 2.
boxes[2].remove('laptop')
boxes[2].remove('snow')
boxes[2].append('book')
boxes[2].append('harmonica')

# Move the needle and the usb and the jungle from Box 7 to Box 8.
items_to_move = ['needle', 'usb', 'jungle']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[8].append(item)

# Remove the grinder and the scissors and the tree from Box 11.
items_to_remove = ['grinder', 'scissors', 'tree']
for item in items_to_remove:
    boxes[11].remove(item)

# Move the keyboard from Box 14 to Box 9.
boxes[14].remove('keyboard')
boxes[9].append('keyboard')

# Put the toy and the bear and the branch into Box 11.
items_to_put = ['toy', 'bear', 'branch']
for item in items_to_put:
    boxes[11].append(item)

# Put the rocket and the seaweed and the pot into Box 7.
items_to_put = ['rocket', 'seaweed', 'pot']
for item in items_to_put:
    boxes[7].append(item)

# Replace the needle with the island in Box 8.
boxes[8].remove('needle')
boxes[8].append('island')

# Empty Box 3.
boxes[3] = []

# Move the pan from Box 12 to Box 6.
boxes[12].remove('pan')
boxes[6].append('pan')

# Remove the pan from Box 6.
boxes[6].remove('pan')

# Swap the makeup in Box 4 with the blanket in Box 9.
boxes[4].remove('makeup')
boxes[9].remove('blanket')
boxes[4].append('blanket')
boxes[9].append('makeup')

# Move the moon from Box 9 to Box 8.
boxes[9].remove('moon')
boxes[8].append('moon')

# Replace the seaweed and the rocket with the microscope and the paint in Box 7.
boxes[7].remove('seaweed')
boxes[7].remove('rocket')
boxes[7].append('microscope')
boxes[7].append('paint')

# Remove the lamp from Box 4.
boxes[4].remove('lamp')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")