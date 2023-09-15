box = {
    0: [],
    1: [],
    2: ['shoe'],
    3: [],
    4: [],
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

def print_boxes():
    for index, items in box.items():
        print(f"Box {index}: {items}")

# Move the book from Box 4 to Box 9
box[9].append(box[4].pop())

# Replace the needle with the gloves in Box 8
box[8].remove('needle')
box[8].append('gloves')

# Replace the gloves with the razor in Box 8
box[8].remove('gloves')
box[8].append('razor')

# Put the grinder into Box 2
box[2].append('grinder')

# Put the wig into Box 3
box[3].append('wig')

# Move the wire and the basket from Box 10 to Box 11
box[11].extend(box[10])
box[10].clear()

# Remove the rock from Box 7
box[7].clear()

# Move the freezer from Box 9 to Box 11
box[11].append(box[9].pop())

# Swap the razor in Box 8 with the grinder in Box 2
box[8].remove('razor')
box[2].remove('grinder')
box[8].append('grinder')
box[2].append('razor')

# Remove the wig from Box 3
box[3].clear()

# Put the river and the branch into Box 12
box[12].extend(['river', 'branch'])

# Replace the shoe and the razor with the motorcycle and the shelf in Box 2
box[2].remove('shoe')
box[2].remove('razor')
box[2].extend(['motorcycle', 'shelf'])

# Move the wire from Box 11 to Box 12
box[12].append(box[11].pop(box[11].index('wire')))

# Put the telescope and the spoon and the pants into Box 10
box[10].extend(['telescope', 'spoon', 'pants'])

# Swap the helmet in Box 8 with the shelf in Box 2
box[8].remove('helmet')
box[2].remove('shelf')
box[8].append('shelf')
box[2].append('helmet')

# Empty Box 2
box[2].clear()

# Replace the grinder and the truck with the comb and the gloves in Box 8
box[8].remove('grinder')
box[8].remove('truck')
box[8].extend(['comb', 'gloves'])

# Replace the comb with the frame in Box 8
box[8].remove('comb')
box[8].append('frame')

# Move the snow from Box 6 to Box 0
box[0].append(box[6].pop(box[6].index('snow')))

# Put the cup into Box 2
box[2].append('cup')

# Move the pen from Box 6 to Box 2
box[2].append(box[6].pop(box[6].index('pen')))

# Print the final state of the boxes
print_boxes()