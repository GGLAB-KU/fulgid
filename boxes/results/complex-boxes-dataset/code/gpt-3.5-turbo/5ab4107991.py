# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['shoe'],
    3: [],
    4: ['book'],
    5: [],
    6: ['pen', 'snow'],
    7: ['rock'],
    8: ['truck', 'helmet', 'needle'],
    9: ['freezer'],
    10: ['basket', 'wire'],
    11: [],
    12: ['jungle', 'ring', 'note', 'glasses', 'key'],
    13: ['zipper', 'comet', 'thread']
}

# Move the book from Box 4 to Box 9.
boxes[4].remove('book')
boxes[9].append('book')

# Replace the needle with the gloves in Box 8.
boxes[8].remove('needle')
boxes[8].append('gloves')

# Replace the gloves with the razor in Box 8.
boxes[8].remove('gloves')
boxes[8].append('razor')

# Put the grinder into Box 2.
boxes[2].append('grinder')

# Put the wig into Box 3.
boxes[3].append('wig')

# Move the wire and the basket from Box 10 to Box 11.
items_to_move = ['wire', 'basket']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[11].append(item)

# Remove the rock from Box 7.
boxes[7].remove('rock')

# Move the freezer from Box 9 to Box 11.
boxes[9].remove('freezer')
boxes[11].append('freezer')

# Swap the razor in Box 8 with the grinder in Box 2.
boxes[8].remove('razor')
boxes[2].remove('grinder')
boxes[8].append('grinder')
boxes[2].append('razor')

# Remove the wig from Box 3.
boxes[3].remove('wig')

# Put the river and the branch into Box 12.
boxes[12].append('river')
boxes[12].append('branch')

# Replace the shoe and the razor with the motorcycle and the shelf in Box 2.
boxes[2].remove('shoe')
boxes[2].remove('razor')
boxes[2].append('motorcycle')
boxes[2].append('shelf')

# Move the wire from Box 11 to Box 12.
boxes[11].remove('wire')
boxes[12].append('wire')

# Put the telescope and the spoon and the pants into Box 10.
boxes[10].append('telescope')
boxes[10].append('spoon')
boxes[10].append('pants')

# Swap the helmet in Box 8 with the shelf in Box 2.
boxes[8].remove('helmet')
boxes[2].remove('shelf')
boxes[8].append('shelf')
boxes[2].append('helmet')

# Empty Box 2.
boxes[2] = []

# Replace the grinder and the truck with the comb and the gloves in Box 8.
boxes[8].remove('grinder')
boxes[8].remove('truck')
boxes[8].append('comb')
boxes[8].append('gloves')

# Replace the comb with the frame in Box 8.
boxes[8].remove('comb')
boxes[8].append('frame')

# Move the snow from Box 6 to Box 0.
boxes[6].remove('snow')
boxes[0].append('snow')

# Put the cup into Box 2.
boxes[2].append('cup')

# Move the pen from Box 6 to Box 2.
boxes[6].remove('pen')
boxes[2].append('pen')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")