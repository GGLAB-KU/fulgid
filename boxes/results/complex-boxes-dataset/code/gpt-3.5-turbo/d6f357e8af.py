# Initial state of boxes
boxes = {
    0: ['desert', 'shelf', 'fish', 'glasses', 'grass'],
    1: ['mixer'],
    2: ['polish', 'shark', 'mountain', 'necklace', 'flute'],
    3: ['seaweed', 'controller', 'dice', 'button'],
    4: ['bracelet', 'needle', 'harmonica', 'sandals', 'meteor'],
    5: ['elephant', 'moon', 'ring', 'console', 'shampoo'],
    6: ['leaf'],
    7: ['shoes', 'piano', 'paint', 'microscope'],
    8: []
}

# Put the toaster and the usb into Box 6.
boxes[6].append('toaster')
boxes[6].append('usb')

# Swap the shoes in Box 7 with the grass in Box 0.
boxes[7].remove('shoes')
boxes[0].remove('grass')
boxes[7].append('grass')
boxes[0].append('shoes')

# Put the crown and the controller into Box 2.
boxes[2].append('crown')
boxes[2].append('controller')

# Move the moon and the ring and the console from Box 5 to Box 2.
items_to_move = ['moon', 'ring', 'console']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[2].append(item)

# Replace the dice and the controller and the button with the chair and the blender and the pan in Box 3.
boxes[3].remove('dice')
boxes[3].remove('controller')
boxes[3].remove('button')
boxes[3].append('chair')
boxes[3].append('blender')
boxes[3].append('pan')

# Swap the mixer in Box 1 with the harmonica in Box 4.
boxes[1].remove('mixer')
boxes[4].remove('harmonica')
boxes[1].append('harmonica')
boxes[4].append('mixer')

# Put the octopus into Box 4.
boxes[4].append('octopus')

# Put the flute into Box 2.
boxes[2].append('flute')

# Replace the ring with the pen in Box 2.
boxes[2].remove('ring')
boxes[2].append('pen')

# Swap the meteor in Box 4 with the shark in Box 2.
boxes[4].remove('meteor')
boxes[2].remove('shark')
boxes[4].append('shark')
boxes[2].append('meteor')

# Remove the shampoo and the elephant from Box 5.
boxes[5].remove('shampoo')
boxes[5].remove('elephant')

# Move the microscope and the paint and the piano from Box 7 to Box 1.
items_to_move = ['microscope', 'paint', 'piano']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[1].append(item)

# Remove the shoes and the shelf from Box 0.
boxes[0].remove('shoes')
boxes[0].remove('shelf')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")