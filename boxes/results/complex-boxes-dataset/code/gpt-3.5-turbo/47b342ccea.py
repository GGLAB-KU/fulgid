# Initial state of boxes
boxes = {
    0: ['shelf', 'dress', 'starfish', 'boot', 'lipstick'],
    1: ['desert', 'scissors', 'doll', 'wig'],
    2: ['perfume', 'pot', 'leaf', 'thread'],
    3: ['basket', 'crown', 'makeup', 'table', 'blender'],
    4: ['lightning', 'sun', 'wallet'],
    5: ['meteor', 'ship', 'sandals', 'flower'],
    6: ['magnet', 'harmonica', 'zipper']
}

# Move the pot and the thread and the perfume from Box 2 to Box 0.
items_to_move = ['pot', 'thread', 'perfume']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Swap the meteor in Box 5 with the sun in Box 4.
boxes[5].remove('meteor')
boxes[4].remove('sun')
boxes[5].append('sun')
boxes[4].append('meteor')

# Swap the makeup in Box 3 with the meteor in Box 4.
boxes[3].remove('makeup')
boxes[4].remove('meteor')
boxes[3].append('meteor')
boxes[4].append('makeup')

# Put the wig and the river into Box 4.
boxes[4].append('wig')
boxes[4].append('river')

# Put the clock and the sculpture and the bowl into Box 2.
boxes[2].append('clock')
boxes[2].append('sculpture')
boxes[2].append('bowl')

# Put the ocean and the candle into Box 3.
boxes[3].append('ocean')
boxes[3].append('candle')

# Remove the harmonica and the zipper and the magnet from Box 6.
boxes[6].remove('harmonica')
boxes[6].remove('zipper')
boxes[6].remove('magnet')

# Put the swimsuit into Box 3.
boxes[3].append('swimsuit')

# Put the comet and the vase and the tie into Box 5.
boxes[5].append('comet')
boxes[5].append('vase')
boxes[5].append('tie')

# Move the wallet and the makeup from Box 4 to Box 1.
boxes[4].remove('wallet')
boxes[4].remove('makeup')
boxes[1].append('wallet')
boxes[1].append('makeup')

# Swap the meteor in Box 3 with the lipstick in Box 0.
boxes[3].remove('meteor')
boxes[0].remove('lipstick')
boxes[3].append('lipstick')
boxes[0].append('meteor')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")