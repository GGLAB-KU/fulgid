# Initial state of boxes
boxes = {
    0: ['microwave', 'bear', 'bag', 'river', 'tiger'],
    1: ['blender'],
    2: ['card', 'rock'],
    3: ['violin', 'shorts', 'shark', 'storm'],
    4: [],
    5: ['glove', 'dolphin', 'starfish'],
    6: [],
    7: ['usb', 'dress', 'flower', 'shampoo', 'sculpture'],
    8: ['polish', 'lion', 'coral', 'scarf'],
    9: ['scissors', 'chair', 'toothpaste'],
    10: ['branch', 'camera', 'lamp', 'candle', 'shirt']
}

# Replace the card with the shoes in Box 2.
boxes[2].remove('card')
boxes[2].append('shoes')

# Swap the scissors in Box 9 with the violin in Box 3.
boxes[9].remove('scissors')
boxes[3].remove('violin')
boxes[9].append('violin')
boxes[3].append('scissors')

# Swap the dress in Box 7 with the microwave in Box 0.
boxes[7].remove('dress')
boxes[0].remove('microwave')
boxes[7].append('microwave')
boxes[0].append('dress')

# Remove the blender from Box 1.
boxes[1].remove('blender')

# Replace the glove with the plane in Box 5.
boxes[5].remove('glove')
boxes[5].append('plane')

# Remove the shorts and the shark from Box 3.
boxes[3].remove('shorts')
boxes[3].remove('shark')

# Move the shirt from Box 10 to Box 4.
boxes[10].remove('shirt')
boxes[4].append('shirt')

# Move the shirt from Box 4 to Box 8.
boxes[4].remove('shirt')
boxes[8].append('shirt')

# Swap the starfish in Box 5 with the rock in Box 2.
boxes[5].remove('starfish')
boxes[2].remove('rock')
boxes[5].append('rock')
boxes[2].append('starfish')

# Move the toothpaste from Box 9 to Box 7.
boxes[9].remove('toothpaste')
boxes[7].append('toothpaste')

# Swap the flower in Box 7 with the tiger in Box 0.
boxes[7].remove('flower')
boxes[0].remove('tiger')
boxes[7].append('tiger')
boxes[0].append('flower')

# Put the mountain and the desert and the earring into Box 10.
items_to_put = ['mountain', 'desert', 'earring']
for item in items_to_put:
    boxes[10].append(item)

# Put the jacket and the frame and the horn into Box 2.
items_to_put = ['jacket', 'frame', 'horn']
for item in items_to_put:
    boxes[2].append(item)

# Replace the scissors with the ship in Box 3.
boxes[3].remove('scissors')
boxes[3].append('ship')

# Move the river from Box 0 to Box 10.
boxes[0].remove('river')
boxes[10].append('river')

# Move the ship from Box 3 to Box 6.
boxes[3].remove('ship')
boxes[6].append('ship')

# Swap the shampoo in Box 7 with the dolphin in Box 5.
boxes[7].remove('shampoo')
boxes[5].remove('dolphin')
boxes[7].append('dolphin')
boxes[5].append('shampoo')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")