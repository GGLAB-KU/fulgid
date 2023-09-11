# Initial state of boxes
boxes = {
    0: ['gloves', 'ring', 'rock'],
    1: ['cup', 'tie', 'perfume', 'elephant', 'harmonica'],
    2: [],
    3: ['bird', 'glasses', 'pot', 'polish'],
    4: ['crown', 'zipper', 'bell', 'controller', 'key'],
    5: ['whistle', 'boat'],
    6: ['game', 'headphone', 'toaster', 'magnet', 'ship'],
    7: ['laptop', 'mask'],
    8: ['piano', 'puzzle'],
    9: ['storm', 'bicycle', 'rain', 'sun', 'star'],
    10: ['helmet', 'tape', 'drum', 'boot', 'pillow'],
    11: ['dolphin'],
    12: ['desert']
}

# Move the key and the zipper from Box 4 to Box 0.
boxes[4].remove('key')
boxes[4].remove('zipper')
boxes[0].append('key')
boxes[0].append('zipper')

# Move the boat from Box 5 to Box 10.
boxes[5].remove('boat')
boxes[10].append('boat')

# Move the magnet and the toaster and the headphone from Box 6 to Box 1.
boxes[6].remove('magnet')
boxes[6].remove('toaster')
boxes[6].remove('headphone')
boxes[1].append('magnet')
boxes[1].append('toaster')
boxes[1].append('headphone')

# Move the laptop from Box 7 to Box 10.
boxes[7].remove('laptop')
boxes[10].append('laptop')

# Swap the key in Box 0 with the piano in Box 8.
boxes[0].remove('key')
boxes[8].remove('piano')
boxes[0].append('piano')
boxes[8].append('key')

# Replace the zipper and the piano and the ring with the jacket and the swimsuit and the elephant in Box 0.
boxes[0].remove('zipper')
boxes[0].remove('piano')
boxes[0].remove('ring')
boxes[0].append('jacket')
boxes[0].append('swimsuit')
boxes[0].append('elephant')

# Move the toaster from Box 1 to Box 4.
boxes[1].remove('toaster')
boxes[4].append('toaster')

# Remove the controller and the bell from Box 4.
boxes[4].remove('controller')
boxes[4].remove('bell')

# Replace the boat and the boot and the helmet with the island and the mountain and the drum in Box 10.
boxes[10].remove('boat')
boxes[10].remove('boot')
boxes[10].remove('helmet')
boxes[10].append('island')
boxes[10].append('mountain')
boxes[10].append('drum')

# Swap the laptop in Box 10 with the whistle in Box 5.
boxes[10].remove('laptop')
boxes[5].remove('whistle')
boxes[10].append('whistle')
boxes[5].append('laptop')

# Move the rock and the jacket from Box 0 to Box 7.
boxes[0].remove('rock')
boxes[0].remove('jacket')
boxes[7].append('rock')
boxes[7].append('jacket')

# Move the game and the ship from Box 6 to Box 1.
boxes[6].remove('game')
boxes[6].remove('ship')
boxes[1].append('game')
boxes[1].append('ship')

# Move the key and the puzzle from Box 8 to Box 0.
boxes[8].remove('key')
boxes[8].remove('puzzle')
boxes[0].append('key')
boxes[0].append('puzzle')

# Replace the dolphin with the truck in Box 11.
boxes[11].remove('dolphin')
boxes[11].append('truck')

# Put the magnet and the coin and the lock into Box 3.
boxes[3].append('magnet')
boxes[3].append('coin')
boxes[3].append('lock')

# Put the cow into Box 6.
boxes[6].append('cow')

# Move the mask and the jacket from Box 7 to Box 1.
boxes[7].remove('mask')
boxes[7].remove('jacket')
boxes[1].append('mask')
boxes[1].append('jacket')

# Empty Box 5.
boxes[5] = []

# Move the puzzle and the gloves from Box 0 to Box 8.
boxes[0].remove('puzzle')
boxes[0].remove('gloves')
boxes[8].append('puzzle')
boxes[8].append('gloves')

# Put the mountain and the thread and the book into Box 12.
boxes[12].append('mountain')
boxes[12].append('thread')
boxes[12].append('book')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")