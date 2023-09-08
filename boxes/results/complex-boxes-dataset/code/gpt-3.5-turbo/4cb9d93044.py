# Initial state of boxes
boxes = {
    0: ['elephant', 'blender', 'umbrella', 'flower'],
    1: [],
    2: ['tape', 'thread'],
    3: ['horse', 'shorts', 'gloves', 'magnet'],
    4: ['vase', 'frame', 'doll', 'toothpaste', 'scarf'],
    5: ['earring', 'meteor'],
    6: ['pillow', 'bell'],
    7: ['plate'],
    8: ['bowl', 'horn', 'harmonica'],
    9: [],
    10: [],
    11: [],
    12: ['rain'],
    13: ['paint', 'sun']
}

# Move the umbrella and the flower from Box 0 to Box 3.
boxes[0].remove('umbrella')
boxes[0].remove('flower')
boxes[3].append('umbrella')
boxes[3].append('flower')

# Put the sculpture into Box 6.
boxes[6].append('sculpture')

# Move the sun from Box 13 to Box 2.
boxes[13].remove('sun')
boxes[2].append('sun')

# Put the scissors and the cup and the telescope into Box 3.
items_to_move = ['scissors', 'cup', 'telescope']
for item in items_to_move:
    boxes[3].append(item)

# Put the dolphin into Box 9.
boxes[9].append('dolphin')

# Swap the vase in Box 4 with the tape in Box 2.
boxes[4].remove('vase')
boxes[2].remove('tape')
boxes[4].append('tape')
boxes[2].append('vase')

# Replace the paint with the star in Box 13.
boxes[13].remove('paint')
boxes[13].append('star')

# Remove the plate from Box 7.
boxes[7].remove('plate')

# Swap the rain in Box 12 with the sun in Box 2.
boxes[12].remove('rain')
boxes[2].remove('sun')
boxes[12].append('sun')
boxes[2].append('rain')

# Move the star from Box 13 to Box 11.
boxes[13].remove('star')
boxes[11].append('star')

# Move the horse and the magnet from Box 3 to Box 10.
items_to_move = ['horse', 'magnet']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[10].append(item)

# Swap the magnet in Box 10 with the scarf in Box 4.
boxes[10].remove('magnet')
boxes[4].remove('scarf')
boxes[10].append('scarf')
boxes[4].append('magnet')

# Replace the bowl with the vase in Box 8.
boxes[8].remove('bowl')
boxes[4].remove('vase')
boxes[8].append('vase')
boxes[4].append('bowl')

# Remove the horse and the scarf from Box 10.
items_to_remove = ['horse', 'scarf']
for item in items_to_remove:
    boxes[10].remove(item)

# Remove the sun from Box 12.
boxes[12].remove('sun')

# Move the earring and the meteor from Box 5 to Box 4.
items_to_move = ['earring', 'meteor']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Swap the dolphin in Box 9 with the sculpture in Box 6.
boxes[9].remove('dolphin')
boxes[6].remove('sculpture')
boxes[9].append('sculpture')
boxes[6].append('dolphin')

# Empty Box 0.
boxes[0] = []

# Replace the vase and the rain with the coat and the freezer in Box 2.
boxes[2].remove('vase')
boxes[2].remove('rain')
boxes[2].append('coat')
boxes[2].append('freezer')

# Put the cow and the beach and the lipstick into Box 0.
items_to_move = ['cow', 'beach', 'lipstick']
for item in items_to_move:
    boxes[0].append(item)

# Remove the tape and the doll and the frame from Box 4.
items_to_remove = ['tape', 'doll', 'frame']
for item in items_to_remove:
    boxes[4].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")