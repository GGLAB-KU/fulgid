# Initial state of boxes
boxes = {
    0: ['wire', 'freezer', 'belt', 'piano'],
    1: [],
    2: ['plate', 'mask', 'lock', 'dress'],
    3: [],
    4: ['thread', 'sculpture', 'wallet', 'needle'],
    5: ['sock', 'pants', 'rain', 'lamp'],
    6: ['bag', 'tiger', 'chair'],
    7: ['necklace', 'ocean', 'rocket', 'lion', 'charger'],
    8: ['toy', 'leaf', 'rock'],
    9: []
}

# Swap the rock in Box 8 with the sock in Box 5.
boxes[8].remove('rock')
boxes[5].remove('sock')
boxes[8].append('sock')
boxes[5].append('rock')

# Swap the thread in Box 4 with the wire in Box 0.
boxes[4].remove('thread')
boxes[0].remove('wire')
boxes[4].append('wire')
boxes[0].append('thread')

# Move the belt from Box 0 to Box 5.
boxes[0].remove('belt')
boxes[5].append('belt')

# Remove the chair and the tiger from Box 6.
boxes[6].remove('chair')
boxes[6].remove('tiger')

# Remove the plate and the dress from Box 2.
boxes[2].remove('plate')
boxes[2].remove('dress')

# Replace the thread and the piano with the bird and the glove in Box 0.
boxes[0].remove('thread')
boxes[0].remove('piano')
boxes[0].append('bird')
boxes[0].append('glove')

# Put the apple and the dog and the watch into Box 6.
items_to_put = ['apple', 'dog', 'watch']
for item in items_to_put:
    boxes[6].append(item)

# Swap the watch in Box 6 with the glove in Box 0.
boxes[6].remove('watch')
boxes[0].remove('glove')
boxes[6].append('glove')
boxes[0].append('watch')

# Put the elephant and the book and the razor into Box 0.
items_to_put = ['elephant', 'book', 'razor']
for item in items_to_put:
    boxes[0].append(item)

# Move the leaf from Box 8 to Box 2.
boxes[8].remove('leaf')
boxes[2].append('leaf')

# Remove the lamp and the rock from Box 5.
boxes[5].remove('lamp')
boxes[5].remove('rock')

# Replace the wire and the sculpture with the horn and the comb in Box 4.
boxes[4].remove('wire')
boxes[4].remove('sculpture')
boxes[4].append('horn')
boxes[4].append('comb')

# Remove the sock from Box 8.
boxes[8].remove('sock')

# Remove the belt and the pants and the rain from Box 5.
boxes[5].remove('belt')
boxes[5].remove('pants')
boxes[5].remove('rain')

# Put the hat and the flower and the tie into Box 9.
items_to_put = ['hat', 'flower', 'tie']
for item in items_to_put:
    boxes[9].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")