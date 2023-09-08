# Initial state of boxes
boxes = {
    0: ['sun', 'pillow', 'planet', 'thunder', 'microwave'],
    1: [],
    2: ['magnet', 'helmet', 'whistle', 'wig'],
    3: ['leaf', 'cow', 'shirt', 'dolphin', 'dress'],
    4: ['watch', 'grass', 'pan', 'cat', 'dog'],
    5: ['bag'],
    6: ['freezer', 'bracelet'],
    7: ['game'],
    8: ['thread', 'phone'],
    9: ['truck', 'lion', 'horn'],
    10: ['snow', 'lightning'],
    11: ['sock', 'oven', 'charger'],
    12: [],
    13: ['hat', 'headphone', 'glasses', 'bell', 'rock'],
    14: ['shelf', 'fish', 'branch']
}

# Replace the phone and the thread with the horn and the earring in Box 8.
boxes[8].remove('phone')
boxes[8].remove('thread')
boxes[8].append('horn')
boxes[8].append('earring')

# Swap the glasses in Box 13 with the charger in Box 11.
boxes[13].remove('glasses')
boxes[11].remove('charger')
boxes[13].append('charger')
boxes[11].append('glasses')

# Swap the pan in Box 4 with the snow in Box 10.
boxes[4].remove('pan')
boxes[10].remove('snow')
boxes[4].append('snow')
boxes[10].append('pan')

# Swap the bag in Box 5 with the fish in Box 14.
boxes[5].remove('bag')
boxes[14].remove('fish')
boxes[5].append('fish')
boxes[14].append('bag')

# Replace the game with the glove in Box 7.
boxes[7].remove('game')
boxes[7].append('glove')

# Move the oven and the sock and the glasses from Box 11 to Box 4.
items_to_move = ['oven', 'sock', 'glasses']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[4].append(item)

# Put the camera and the gloves and the coral into Box 8.
items_to_put = ['camera', 'gloves', 'coral']
for item in items_to_put:
    boxes[8].append(item)

# Replace the glasses with the speaker in Box 4.
boxes[4].remove('glasses')
boxes[4].append('speaker')

# Remove the glove from Box 7.
boxes[7].remove('glove')

# Move the microwave and the thunder from Box 0 to Box 7.
items_to_move = ['microwave', 'thunder']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[7].append(item)

# Replace the magnet and the wig and the whistle with the apple and the snow and the shoe in Box 2.
boxes[2].remove('magnet')
boxes[2].remove('wig')
boxes[2].remove('whistle')
boxes[2].append('apple')
boxes[2].append('snow')
boxes[2].append('shoe')

# Replace the snow and the apple and the helmet with the lamp and the telescope and the sandals in Box 2.
boxes[2].remove('snow')
boxes[2].remove('apple')
boxes[2].remove('helmet')
boxes[2].append('lamp')
boxes[2].append('telescope')
boxes[2].append('sandals')

# Remove the bracelet from Box 6.
boxes[6].remove('bracelet')

# Put the book into Box 4.
boxes[4].append('book')

# Replace the telescope with the jacket in Box 2.
boxes[2].remove('telescope')
boxes[2].append('jacket')

# Put the elephant and the toaster and the boat into Box 14.
items_to_put = ['elephant', 'toaster', 'boat']
for item in items_to_put:
    boxes[14].append(item)

# Empty Box 4.
boxes[4] = []

# Remove the pan from Box 10.
boxes[10].remove('pan')

# Move the freezer from Box 6 to Box 12.
boxes[6].remove('freezer')
boxes[12].append('freezer')

# Put the belt and the thunder into Box 14.
items_to_put = ['belt', 'thunder']
for item in items_to_put:
    boxes[14].append(item)

# Remove the lamp and the sandals from Box 2.
boxes[2].remove('lamp')
boxes[2].remove('sandals')

# Empty Box 13.
boxes[13] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")