# Initial state of boxes
boxes = {
    0: ['pants', 'sock', 'bowl', 'card'],
    1: ['freezer', 'towel', 'coat', 'scissors'],
    2: ['key'],
    3: ['ring', 'pillow', 'mirror'],
    4: ['laptop'],
    5: [],
    6: ['makeup', 'console', 'tiger', 'oven'],
    7: ['rock'],
    8: ['lion', 'vase', 'whistle', 'ship'],
    9: ['tie', 'comet', 'blender', 'horse', 'train'],
    10: ['grass', 'controller', 'shampoo']
}

# Replace the makeup and the oven with the fridge and the microwave in Box 6.
boxes[6].remove('makeup')
boxes[6].remove('oven')
boxes[6].append('fridge')
boxes[6].append('microwave')

# Put the usb and the jungle into Box 9.
boxes[9].append('usb')
boxes[9].append('jungle')

# Remove the sock and the pants from Box 0.
boxes[0].remove('sock')
boxes[0].remove('pants')

# Put the shoes and the thread into Box 5.
boxes[5].append('shoes')
boxes[5].append('thread')

# Put the lipstick and the scissors into Box 1.
boxes[1].append('lipstick')
boxes[1].append('scissors')

# Put the dolphin and the bicycle into Box 7.
boxes[7].append('dolphin')
boxes[7].append('bicycle')

# Remove the fridge from Box 6.
boxes[6].remove('fridge')

# Move the laptop from Box 4 to Box 1.
boxes[4].remove('laptop')
boxes[1].append('laptop')

# Replace the pillow and the mirror with the oven and the brush in Box 3.
boxes[3].remove('pillow')
boxes[3].remove('mirror')
boxes[3].append('oven')
boxes[3].append('brush')

# Replace the lion with the bus in Box 8.
boxes[8].remove('lion')
boxes[8].append('bus')

# Put the shoes and the starfish into Box 0.
boxes[0].append('shoes')
boxes[0].append('starfish')

# Move the shoes from Box 5 to Box 9.
boxes[5].remove('shoes')
boxes[9].append('shoes')

# Remove the shampoo and the grass and the controller from Box 10.
boxes[10].remove('shampoo')
boxes[10].remove('grass')
boxes[10].remove('controller')

# Move the brush and the ring and the oven from Box 3 to Box 1.
items_to_move = ['brush', 'ring', 'oven']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[1].append(item)

# Move the whistle from Box 8 to Box 1.
boxes[8].remove('whistle')
boxes[1].append('whistle')

# Swap the key in Box 2 with the bicycle in Box 7.
boxes[2], boxes[7] = boxes[7], boxes[2]

# Replace the towel with the freezer in Box 1.
boxes[1].remove('towel')
boxes[1].append('freezer')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")