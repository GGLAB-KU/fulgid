# Initial state of boxes
boxes = {
    0: ['table', 'earring', 'chair', 'lock', 'shirt'],
    1: ['comb', 'magnet', 'bag', 'river'],
    2: ['pot', 'coral', 'tie', 'forest', 'controller'],
    3: ['shoe'],
    4: ['basket', 'toaster', 'star', 'toothpaste'],
    5: ['bear', 'candle', 'whistle', 'polish', 'elephant'],
    6: ['blanket', 'speaker'],
    7: ['grass', 'razor', 'wig', 'ring', 'laptop'],
    8: ['necklace', 'brush', 'octopus', 'keyboard', 'makeup']
}

# Move the wig from Box 7 to Box 0.
boxes[7].remove('wig')
boxes[0].append('wig')

# Swap the magnet in Box 1 with the blanket in Box 6.
boxes[1].remove('magnet')
boxes[6].remove('blanket')
boxes[1].append('blanket')
boxes[6].append('magnet')

# Put the toothpaste and the elephant into Box 4.
boxes[4].append('toothpaste')
boxes[5].remove('elephant')
boxes[4].append('elephant')

# Put the chair and the rain into Box 0.
boxes[0].append('chair')
boxes[0].append('rain')

# Remove the elephant and the swimsuit from Box 4.
boxes[4].remove('elephant')
boxes[4].remove('swimsuit')

# Put the shampoo and the coral and the dice into Box 8.
boxes[8].append('shampoo')
boxes[2].remove('coral')
boxes[8].append('coral')
boxes[8].append('dice')

# Swap the laptop in Box 7 with the brush in Box 8.
boxes[7].remove('laptop')
boxes[8].remove('brush')
boxes[7].append('brush')
boxes[8].append('laptop')

# Put the piano and the swimsuit and the lion into Box 5.
boxes[5].append('piano')
boxes[4].remove('swimsuit')
boxes[5].append('swimsuit')
boxes[5].append('lion')

# Remove the blanket and the river and the bag from Box 1.
boxes[1].remove('blanket')
boxes[1].remove('river')
boxes[1].remove('bag')

# Replace the swimsuit with the shark in Box 5.
boxes[5].remove('swimsuit')
boxes[5].append('shark')

# Move the basket from Box 4 to Box 1.
boxes[4].remove('basket')
boxes[1].append('basket')

# Swap the lock in Box 0 with the grass in Box 7.
boxes[0].remove('lock')
boxes[7].remove('grass')
boxes[0].append('grass')
boxes[7].append('lock')

# Move the controller and the pot and the tie from Box 2 to Box 3.
boxes[2].remove('controller')
boxes[2].remove('pot')
boxes[2].remove('tie')
boxes[3].append('controller')
boxes[3].append('pot')
boxes[3].append('tie')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")