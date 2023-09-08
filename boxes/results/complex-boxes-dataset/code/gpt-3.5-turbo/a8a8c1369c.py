# Initial state of boxes
boxes = {
    0: ['coral', 'toy', 'pants', 'guitar'],
    1: ['vase', 'blender', 'pillow', 'mountain'],
    2: ['makeup', 'microscope', 'apple'],
    3: ['ocean', 'drum'],
    4: [],
    5: ['lightning'],
    6: ['shorts', 'sculpture', 'dice'],
    7: [],
    8: ['harmonica', 'shirt'],
    9: ['elephant', 'plane'],
    10: ['wire'],
    11: [],
    12: ['crown', 'piano', 'thunder']
}

# Move the plane from Box 9 to Box 10.
boxes[9].remove('plane')
boxes[10].append('plane')

# Move the shirt and the harmonica from Box 8 to Box 4.
boxes[8].remove('shirt')
boxes[8].remove('harmonica')
boxes[4].append('shirt')
boxes[4].append('harmonica')

# Replace the ocean and the drum with the boot and the shoe in Box 3.
boxes[3].remove('ocean')
boxes[3].remove('drum')
boxes[3].append('boot')
boxes[3].append('shoe')

# Move the elephant from Box 9 to Box 0.
boxes[9].remove('elephant')
boxes[0].append('elephant')

# Move the pants and the elephant and the coral from Box 0 to Box 12.
items_to_move = ['pants', 'elephant', 'coral']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[12].append(item)

# Move the boot from Box 3 to Box 5.
boxes[3].remove('boot')
boxes[5].append('boot')

# Swap the plane in Box 10 with the coral in Box 12.
boxes[10].remove('plane')
boxes[12].remove('coral')
boxes[10].append('coral')
boxes[12].append('plane')

# Remove the vase and the mountain from Box 1.
boxes[1].remove('vase')
boxes[1].remove('mountain')

# Move the harmonica from Box 4 to Box 10.
boxes[4].remove('harmonica')
boxes[10].append('harmonica')

# Remove the dice from Box 6.
boxes[6].remove('dice')

# Move the blender from Box 1 to Box 0.
boxes[1].remove('blender')
boxes[0].append('blender')

# Swap the shirt in Box 4 with the sculpture in Box 6.
boxes[4].remove('shirt')
boxes[6].remove('sculpture')
boxes[4].append('sculpture')
boxes[6].append('shirt')

# Replace the microscope and the apple and the makeup with the snow and the freezer and the bag in Box 2.
boxes[2].remove('microscope')
boxes[2].remove('apple')
boxes[2].remove('makeup')
boxes[2].append('snow')
boxes[2].append('freezer')
boxes[2].append('bag')

# Put the pillow and the storm into Box 10.
boxes[1].remove('pillow')
boxes[5].remove('storm')
boxes[10].append('pillow')
boxes[10].append('storm')

# Swap the elephant in Box 12 with the pillow in Box 1.
boxes[12].remove('elephant')
boxes[1].remove('pillow')
boxes[12].append('pillow')
boxes[1].append('elephant')

# Remove the plane and the pillow and the piano from Box 12.
boxes[12].remove('plane')
boxes[12].remove('pillow')
boxes[12].remove('piano')

# Swap the storm in Box 10 with the sculpture in Box 4.
boxes[10].remove('storm')
boxes[4].remove('sculpture')
boxes[10].append('sculpture')
boxes[4].append('storm')

# Move the shirt and the shorts from Box 6 to Box 2.
boxes[6].remove('shirt')
boxes[6].remove('shorts')
boxes[2].append('shirt')
boxes[2].append('shorts')

# Swap the thunder in Box 12 with the sculpture in Box 10.
boxes[12].remove('thunder')
boxes[10].remove('sculpture')
boxes[12].append('sculpture')
boxes[10].append('thunder')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")