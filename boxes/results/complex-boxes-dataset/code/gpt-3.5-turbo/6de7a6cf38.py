# Initial state of boxes
boxes = {
    0: ['doll', 'comb', 'lipstick', 'shoe', 'rain'],
    1: ['flute', 'desert', 'wallet', 'bird', 'blanket'],
    2: ['truck', 'microscope', 'ocean', 'spoon'],
    3: ['table', 'tie', 'ring', 'zipper'],
    4: ['tree', 'storm', 'pen', 'plate', 'bowl'],
    5: ['pan', 'frame', 'boot'],
    6: [],
    7: ['cup', 'button', 'bear', 'branch', 'microwave'],
    8: ['freezer', 'headphone', 'key'],
    9: [],
    10: ['speaker', 'thread', 'battery', 'car', 'skirt'],
    11: ['keyboard', 'train', 'belt', 'violin'],
    12: []
}

# Put the starfish and the note and the train into Box 4.
boxes[4].extend(['starfish', 'note', 'train'])

# Swap the zipper in Box 3 with the button in Box 7.
boxes[3].remove('zipper')
boxes[7].remove('button')
boxes[3].append('button')
boxes[7].append('zipper')

# Replace the table and the tie with the horn and the microscope in Box 3.
boxes[3].remove('table')
boxes[3].remove('tie')
boxes[3].append('horn')
boxes[3].append('microscope')

# Replace the freezer with the dice in Box 8.
boxes[8].remove('freezer')
boxes[8].append('dice')

# Put the flute and the cup and the piano into Box 9.
boxes[9].extend(['flute', 'cup', 'piano'])

# Swap the cup in Box 9 with the train in Box 4.
boxes[9].remove('cup')
boxes[4].remove('train')
boxes[9].append('train')
boxes[4].append('cup')

# Put the cow and the leaf into Box 10.
boxes[10].extend(['cow', 'leaf'])

# Swap the note in Box 4 with the wallet in Box 1.
boxes[4].remove('note')
boxes[1].remove('wallet')
boxes[4].append('wallet')
boxes[1].append('note')

# Put the toaster and the fridge into Box 10.
boxes[10].extend(['toaster', 'fridge'])

# Swap the boot in Box 5 with the train in Box 11.
boxes[5].remove('boot')
boxes[11].remove('train')
boxes[5].append('train')
boxes[11].append('boot')

# Swap the belt in Box 11 with the horn in Box 3.
boxes[11].remove('belt')
boxes[3].remove('horn')
boxes[11].append('horn')
boxes[3].append('belt')

# Replace the cup and the branch with the helmet and the mirror in Box 7.
boxes[7].remove('cup')
boxes[7].remove('branch')
boxes[7].append('helmet')
boxes[7].append('mirror')

# Remove the bear from Box 7.
boxes[7].remove('bear')

# Swap the speaker in Box 10 with the key in Box 8.
boxes[10].remove('speaker')
boxes[8].remove('key')
boxes[10].append('key')
boxes[8].append('speaker')

# Put the cow and the pillow into Box 12.
boxes[12].extend(['cow', 'pillow'])

# Move the lipstick from Box 0 to Box 11.
boxes[0].remove('lipstick')
boxes[11].append('lipstick')

# Put the coral and the wallet and the jungle into Box 7.
boxes[7].extend(['coral', 'wallet', 'jungle'])

# Put the submarine into Box 2.
boxes[2].append('submarine')

# Move the flute from Box 1 to Box 2.
boxes[1].remove('flute')
boxes[2].append('flute')

# Swap the speaker in Box 8 with the cow in Box 12.
boxes[8].remove('speaker')
boxes[12].remove('cow')
boxes[8].append('cow')
boxes[12].append('speaker')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")