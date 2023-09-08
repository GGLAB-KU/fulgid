# Initial state of boxes
boxes = {
    0: [],
    1: ['vase', 'phone', 'grinder', 'shoe'],
    2: ['shark'],
    3: ['lightning', 'microscope', 'sock', 'polish', 'butterfly'],
    4: ['scissors', 'cup'],
    5: ['bus', 'mixer', 'keyboard'],
    6: ['shirt', 'shoes', 'paint'],
    7: ['earring', 'branch', 'rain'],
    8: [],
    9: ['spoon', 'boat']
}

# Put the keyboard into Box 2.
boxes[2].append('keyboard')

# Empty Box 5.
boxes[5] = []

# Swap the shark in Box 2 with the branch in Box 7.
boxes[2].remove('shark')
boxes[7].remove('branch')
boxes[2].append('branch')
boxes[7].append('shark')

# Swap the shark in Box 7 with the vase in Box 1.
boxes[7].remove('shark')
boxes[1].remove('vase')
boxes[7].append('vase')
boxes[1].append('shark')

# Put the butterfly and the snow into Box 9.
boxes[9].append('butterfly')
boxes[9].append('snow')

# Move the vase and the earring and the rain from Box 7 to Box 4.
items_to_move = ['vase', 'earring', 'rain']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[4].append(item)

# Put the puzzle and the leaf into Box 7.
boxes[7].append('puzzle')
boxes[7].append('leaf')

# Replace the paint and the shoes with the tiger and the truck in Box 6.
boxes[6].remove('paint')
boxes[6].remove('shoes')
boxes[6].append('tiger')
boxes[6].append('truck')

# Put the hat and the comb into Box 0.
boxes[0].append('hat')
boxes[0].append('comb')

# Move the polish and the microscope from Box 3 to Box 8.
items_to_move = ['polish', 'microscope']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[8].append(item)

# Move the puzzle from Box 7 to Box 6.
boxes[7].remove('puzzle')
boxes[6].append('puzzle')

# Remove the tiger from Box 6.
boxes[6].remove('tiger')

# Swap the sock in Box 3 with the shirt in Box 6.
boxes[3].remove('sock')
boxes[6].remove('shirt')
boxes[3].append('shirt')
boxes[6].append('sock')

# Swap the phone in Box 1 with the keyboard in Box 2.
boxes[1].remove('phone')
boxes[2].remove('keyboard')
boxes[1].append('keyboard')
boxes[2].append('phone')

# Replace the polish with the octopus in Box 8.
boxes[8].remove('polish')
boxes[8].append('octopus')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")