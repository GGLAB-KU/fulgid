# Initial state of boxes
boxes = {
    0: ['earring', 'frame', 'thunder', 'hat'],
    1: ['sandals', 'phone', 'cloud', 'doll', 'fridge'],
    2: ['keyboard'],
    3: ['swimsuit', 'controller', 'lipstick', 'mirror', 'ring'],
    4: ['wallet'],
    5: ['shark'],
    6: ['clock', 'star', 'magnet'],
    7: ['rocket', 'island', 'coat']
}

# Swap the earring in Box 0 with the keyboard in Box 2.
boxes[0].remove('earring')
boxes[2].remove('keyboard')
boxes[0].append('keyboard')
boxes[2].append('earring')

# Swap the hat in Box 0 with the clock in Box 6.
boxes[0].remove('hat')
boxes[6].remove('clock')
boxes[0].append('clock')
boxes[6].append('hat')

# Put the oven and the helmet into Box 6.
boxes[6].append('oven')
boxes[6].append('helmet')

# Remove the frame and the clock from Box 0.
boxes[0].remove('frame')
boxes[0].remove('clock')

# Put the sock and the pants into Box 3.
boxes[3].append('sock')
boxes[3].append('pants')

# Swap the wallet in Box 4 with the swimsuit in Box 3.
boxes[4].remove('wallet')
boxes[3].remove('swimsuit')
boxes[4].append('swimsuit')
boxes[3].append('wallet')

# Move the shark from Box 5 to Box 0.
boxes[5].remove('shark')
boxes[0].append('shark')

# Remove the oven and the magnet from Box 6.
boxes[6].remove('oven')
boxes[6].remove('magnet')

# Swap the swimsuit in Box 4 with the star in Box 6.
boxes[4].remove('swimsuit')
boxes[6].remove('star')
boxes[4].append('star')
boxes[6].append('swimsuit')

# Move the thunder from Box 0 to Box 5.
boxes[0].remove('thunder')
boxes[5].append('thunder')

# Move the doll from Box 1 to Box 0.
boxes[1].remove('doll')
boxes[0].append('doll')

# Remove the keyboard and the doll from Box 0.
boxes[0].remove('keyboard')
boxes[0].remove('doll')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")