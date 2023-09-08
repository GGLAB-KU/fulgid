# Initial state of boxes
boxes = {
    0: ['blanket', 'moon', 'drum'],
    1: [],
    2: ['motorcycle', 'star', 'pants', 'toothpaste', 'brush'],
    3: ['razor'],
    4: ['chair', 'lamp', 'laptop'],
    5: ['lock'],
    6: ['bird', 'grinder', 'skirt', 'forest', 'toothbrush'],
    7: [],
    8: ['bag', 'lightning'],
    9: ['river', 'pan', 'pen'],
    10: ['bell', 'storm', 'bowl']
}

# Swap the razor in Box 3 with the pan in Box 9.
boxes[3].remove('razor')
boxes[9].remove('pan')
boxes[3].append('pan')
boxes[9].append('razor')

# Put the elephant into Box 10.
boxes[10].append('elephant')

# Replace the motorcycle and the toothpaste and the brush with the cat and the usb and the shirt in Box 2.
boxes[2].remove('motorcycle')
boxes[2].remove('toothpaste')
boxes[2].remove('brush')
boxes[2].append('cat')
boxes[2].append('usb')
boxes[2].append('shirt')

# Swap the razor in Box 9 with the lamp in Box 4.
boxes[9].remove('razor')
boxes[4].remove('lamp')
boxes[9].append('lamp')
boxes[4].append('razor')

# Move the razor from Box 4 to Box 5.
boxes[4].remove('razor')
boxes[5].append('razor')

# Put the oven and the candle into Box 5.
boxes[5].append('oven')
boxes[5].append('candle')

# Replace the grinder with the skirt in Box 6.
boxes[6].remove('grinder')
boxes[6].append('skirt')

# Move the usb and the pants from Box 2 to Box 9.
boxes[2].remove('usb')
boxes[2].remove('pants')
boxes[9].append('usb')
boxes[9].append('pants')

# Swap the pan in Box 3 with the cat in Box 2.
boxes[3].remove('pan')
boxes[2].remove('cat')
boxes[3].append('cat')
boxes[2].append('pan')

# Empty Box 6.
boxes[6] = []

# Swap the star in Box 2 with the lightning in Box 8.
boxes[2].remove('star')
boxes[8].remove('lightning')
boxes[2].append('lightning')
boxes[8].append('star')

# Remove the bowl and the storm and the elephant from Box 10.
boxes[10].remove('bowl')
boxes[10].remove('storm')
boxes[10].remove('elephant')

# Put the charger and the frame and the lipstick into Box 3.
boxes[3].append('charger')
boxes[3].append('frame')
boxes[3].append('lipstick')

# Swap the chair in Box 4 with the bag in Box 8.
boxes[4].remove('chair')
boxes[8].remove('bag')
boxes[4].append('bag')
boxes[8].append('chair')

# Replace the river with the rock in Box 9.
boxes[9].remove('river')
boxes[9].append('rock')

# Replace the bell with the towel in Box 10.
boxes[10].remove('bell')
boxes[10].append('towel')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")