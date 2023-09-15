box_0 = ['gloves', 'ring', 'rock']
box_1 = ['cup', 'tie', 'perfume', 'elephant', 'harmonica']
box_2 = []
box_3 = ['bird', 'glasses', 'pot', 'polish']
box_4 = ['crown', 'zipper', 'bell', 'controller', 'key']
box_5 = ['whistle', 'boat']
box_6 = ['game', 'headphone', 'toaster', 'magnet', 'ship']
box_7 = ['laptop', 'mask']
box_8 = ['piano', 'puzzle']
box_9 = ['storm', 'bicycle', 'rain', 'sun', 'star']
box_10 = ['helmet', 'tape', 'drum', 'boot', 'pillow']
box_11 = ['dolphin']
box_12 = ['desert']

# Move the key and the zipper from Box 4 to Box 0
box_0.extend([box_4.pop(box_4.index('key')), box_4.pop(box_4.index('zipper'))])

# Move the boat from Box 5 to Box 10
box_10.append(box_5.pop(box_5.index('boat')))

# Move the magnet and the toaster and the headphone from Box 6 to Box 1
box_1.extend([box_6.pop(box_6.index('magnet')), box_6.pop(box_6.index('toaster')), box_6.pop(box_6.index('headphone'))])

# Move the laptop from Box 7 to Box 10
box_10.append(box_7.pop(box_7.index('laptop')))

# Swap the key in Box 0 with the piano in Box 8
box_0[box_0.index('key')], box_8[box_8.index('piano')] = box_8[box_8.index('piano')], box_0[box_0.index('key')]

# Replace the zipper and the piano and the ring with the jacket and the swimsuit and the elephant in Box 0
box_0 = ['jacket', 'swimsuit', 'elephant']

# Move the toaster from Box 1 to Box 4
box_4.append(box_1.pop(box_1.index('toaster')))

# Remove the controller and the bell from Box 4
box_4.remove('controller')
box_4.remove('bell')

# Replace the boat and the boot and the helmet with the island and the mountain and the drum in Box 10
box_10 = ['island', 'mountain', 'drum']

# Swap the laptop in Box 10 with the whistle in Box 5
box_10, box_5 = box_5, box_10

# Move the rock and the jacket from Box 0 to Box 7
box_7.extend([box_0.pop(box_0.index('rock')), box_0.pop(box_0.index('jacket'))])

# Move the game and the ship from Box 6 to Box 1
box_1.extend([box_6.pop(box_6.index('game')), box_6.pop(box_6.index('ship'))])

# Move the key and the puzzle from Box 8 to Box 0
box_0.extend([box_8.pop(box_8.index('key')), box_8.pop(box_8.index('puzzle'))])

# Replace the dolphin with the truck in Box 11
box_11[box_11.index('dolphin')] = 'truck'

# Put the magnet and the coin and the lock into Box 3
box_3.extend(['magnet', 'coin', 'lock'])

# Put the cow into Box 6
box_6.append('cow')

# Move the mask and the jacket from Box 7 to Box 1
box_1.extend([box_7.pop(box_7.index('mask')), box_7.pop(box_7.index('jacket'))])

# Empty Box 5
box_5 = []

# Move the puzzle and the gloves from Box 0 to Box 8
box_8.extend([box_0.pop(box_0.index('puzzle')), box_0.pop(box_0.index('gloves'))])

# Put the mountain and the thread and the book into Box 12
box_12.extend(['mountain', 'thread', 'book'])

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]):
    print(f"Box {i}: {box}")