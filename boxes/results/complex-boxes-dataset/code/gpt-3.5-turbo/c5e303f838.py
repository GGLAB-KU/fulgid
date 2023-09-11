# Initial state of boxes
boxes = {
    0: ['dog', 'blender', 'mountain'],
    1: [],
    2: ['pen', 'ship', 'shoes', 'pants'],
    3: ['lamp', 'book', 'brush', 'microscope'],
    4: [],
    5: ['submarine', 'snow'],
    6: ['phone', 'lipstick']
}

# Put the clock and the pen into Box 2.
boxes[2].append('clock')
boxes[2].append('pen')

# Replace the blender and the mountain with the mirror and the storm in Box 0.
boxes[0].remove('blender')
boxes[0].remove('mountain')
boxes[0].append('mirror')
boxes[0].append('storm')

# Swap the mirror in Box 0 with the ship in Box 2.
boxes[0].remove('mirror')
boxes[2].remove('ship')
boxes[0].append('ship')
boxes[2].append('mirror')

# Replace the dog and the ship and the storm with the razor and the plate and the horse in Box 0.
boxes[0].remove('dog')
boxes[0].remove('ship')
boxes[0].remove('storm')
boxes[0].append('razor')
boxes[0].append('plate')
boxes[0].append('horse')

# Put the phone into Box 3.
boxes[3].append('phone')

# Swap the pants in Box 2 with the lamp in Box 3.
boxes[2].remove('pants')
boxes[3].remove('lamp')
boxes[2].append('lamp')
boxes[3].append('pants')

# Swap the snow in Box 5 with the mirror in Box 2.
boxes[5].remove('snow')
boxes[2].remove('mirror')
boxes[5].append('mirror')
boxes[2].append('snow')

# Remove the lipstick from Box 6.
boxes[6].remove('lipstick')

# Remove the phone from Box 6.
boxes[6].remove('phone')

# Empty Box 0.
boxes[0] = []

# Move the mirror and the submarine from Box 5 to Box 3.
boxes[5].remove('mirror')
boxes[3].append('mirror')
boxes[5].remove('submarine')
boxes[3].append('submarine')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")