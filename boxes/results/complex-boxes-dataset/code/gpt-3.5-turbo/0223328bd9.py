# Initial state of boxes
boxes = {
    0: ['plane', 'dress'],
    1: ['frame', 'fork'],
    2: ['shark', 'wig', 'toy', 'truck', 'storm'],
    3: ['umbrella', 'train', 'cow', 'brush', 'starfish'],
    4: ['belt'],
    5: ['boat', 'perfume', 'cat', 'button'],
    6: ['horn', 'shirt', 'shelf'],
    7: ['shoe', 'whistle', 'grass'],
    8: ['apple'],
    9: ['headphone'],
    10: ['flute', 'thunder'],
    11: [],
    12: ['island', 'branch', 'polish'],
    13: ['lamp', 'tiger', 'thread', 'lightning', 'motorcycle'],
    14: ['comb']
}

# Swap the headphone in Box 9 with the flute in Box 10.
boxes[9].remove('headphone')
boxes[10].remove('flute')
boxes[9].append('flute')
boxes[10].append('headphone')

# Swap the apple in Box 8 with the wig in Box 2.
boxes[8].remove('apple')
boxes[2].remove('wig')
boxes[8].append('wig')
boxes[2].append('apple')

# Remove the storm and the truck from Box 2.
boxes[2].remove('storm')
boxes[2].remove('truck')

# Swap the umbrella in Box 3 with the tiger in Box 13.
boxes[3].remove('umbrella')
boxes[13].remove('tiger')
boxes[3].append('tiger')
boxes[13].append('umbrella')

# Put the leaf into Box 11.
boxes[11].append('leaf')

# Remove the button and the perfume and the cat from Box 5.
boxes[5].remove('button')
boxes[5].remove('perfume')
boxes[5].remove('cat')

# Replace the leaf with the ocean in Box 11.
boxes[11].remove('leaf')
boxes[11].append('ocean')

# Replace the wig with the frame in Box 8.
boxes[8].remove('wig')
boxes[8].append('frame')

# Move the belt from Box 4 to Box 14.
boxes[4].remove('belt')
boxes[14].append('belt')

# Replace the train with the shampoo in Box 3.
boxes[3].remove('train')
boxes[3].append('shampoo')

# Put the keyboard into Box 9.
boxes[9].append('keyboard')

# Move the shark and the apple from Box 2 to Box 7.
boxes[2].remove('shark')
boxes[2].remove('apple')
boxes[7].append('shark')
boxes[7].append('apple')

# Swap the polish in Box 12 with the ocean in Box 11.
boxes[12].remove('polish')
boxes[11].remove('ocean')
boxes[12].append('ocean')
boxes[11].append('polish')

# Empty Box 10.
boxes[10] = []

# Replace the boat with the scissors in Box 5.
boxes[5].remove('boat')
boxes[5].append('scissors')

# Replace the scissors with the rocket in Box 5.
boxes[5].remove('scissors')
boxes[5].append('rocket')

# Swap the horn in Box 6 with the flute in Box 9.
boxes[6].remove('horn')
boxes[9].remove('flute')
boxes[6].append('flute')
boxes[9].append('horn')

# Replace the rocket with the glasses in Box 5.
boxes[5].remove('rocket')
boxes[5].append('glasses')

# Move the frame and the fork from Box 1 to Box 3.
boxes[1].remove('frame')
boxes[1].remove('fork')
boxes[3].append('frame')
boxes[3].append('fork')

# Empty Box 8.
boxes[8] = []

# Replace the keyboard with the paint in Box 9.
boxes[9].remove('keyboard')
boxes[9].append('paint')

# Swap the lightning in Box 13 with the glasses in Box 5.
boxes[13].remove('lightning')
boxes[5].remove('glasses')
boxes[13].append('glasses')
boxes[5].append('lightning')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")