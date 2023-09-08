# Initial state of boxes
boxes = {
    0: ['cloud'],
    1: ['bracelet', 'oven', 'jungle', 'pillow'],
    2: ['tape', 'flower', 'basket'],
    3: ['zipper', 'storm', 'motorcycle'],
    4: ['island', 'beach', 'vase'],
    5: ['comet', 'polish', 'guitar'],
    6: [],
    7: ['earring', 'river', 'microwave'],
    8: ['violin'],
    9: ['blender', 'button'],
    10: ['pot', 'towel', 'comb', 'fish'],
    11: ['glove', 'magnet', 'shark'],
    12: ['shelf', 'dice', 'clock', 'soap'],
    13: ['harmonica', 'mirror'],
    14: ['coin', 'swimsuit']
}

# Remove the basket and the flower from Box 2.
boxes[2].remove('basket')
boxes[2].remove('flower')

# Remove the blender from Box 9.
boxes[9].remove('blender')

# Move the violin from Box 8 to Box 6.
boxes[8].remove('violin')
boxes[6].append('violin')

# Replace the harmonica and the mirror with the ship and the desert in Box 13.
boxes[13].remove('harmonica')
boxes[13].remove('mirror')
boxes[13].append('ship')
boxes[13].append('desert')

# Put the scarf and the lightning into Box 1.
boxes[1].append('scarf')
boxes[1].append('lightning')

# Move the cloud from Box 0 to Box 12.
boxes[0].remove('cloud')
boxes[12].append('cloud')

# Remove the button from Box 9.
boxes[9].remove('button')

# Remove the swimsuit and the coin from Box 14.
boxes[14].remove('swimsuit')
boxes[14].remove('coin')

# Replace the microwave and the river and the earring with the drum and the wig and the belt in Box 7.
boxes[7].remove('microwave')
boxes[7].remove('river')
boxes[7].remove('earring')
boxes[7].append('drum')
boxes[7].append('wig')
boxes[7].append('belt')

# Move the lightning and the scarf and the oven from Box 1 to Box 5.
items_to_move = ['lightning', 'scarf', 'oven']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[5].append(item)

# Put the leaf and the dress and the shampoo into Box 6.
boxes[6].append('leaf')
boxes[6].append('dress')
boxes[6].append('shampoo')

# Put the shelf and the headphone and the umbrella into Box 13.
boxes[13].append('shelf')
boxes[13].append('headphone')
boxes[13].append('umbrella')

# Replace the beach and the island and the vase with the bag and the violin and the basket in Box 4.
boxes[4].remove('beach')
boxes[4].remove('island')
boxes[4].remove('vase')
boxes[4].append('bag')
boxes[4].append('violin')
boxes[4].append('basket')

# Put the console and the shirt into Box 1.
boxes[1].append('console')
boxes[1].append('shirt')

# Move the dice and the soap and the clock from Box 12 to Box 7.
items_to_move = ['dice', 'soap', 'clock']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[7].append(item)

# Replace the dice with the speaker in Box 7.
boxes[7].remove('dice')
boxes[7].append('speaker')

# Remove the pillow and the shirt and the jungle from Box 1.
items_to_remove = ['pillow', 'shirt', 'jungle']
for item in items_to_remove:
    boxes[1].remove(item)

# Replace the wig and the belt and the clock with the scissors and the key and the glove in Box 7.
boxes[7].remove('wig')
boxes[7].remove('belt')
boxes[7].remove('clock')
boxes[7].append('scissors')
boxes[7].append('key')
boxes[7].append('glove')

# Empty Box 11.
boxes[11] = []

# Replace the ship and the shelf with the microwave and the drum in Box 13.
boxes[13].remove('ship')
boxes[13].remove('shelf')
boxes[13].append('microwave')
boxes[13].append('drum')

# Move the cloud and the shelf from Box 12 to Box 2.
items_to_move = ['cloud', 'shelf']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[2].append(item)

# Replace the shelf and the cloud and the tape with the crown and the plate and the usb in Box 2.
boxes[2].remove('shelf')
boxes[2].remove('cloud')
boxes[2].remove('tape')
boxes[2].append('crown')
boxes[2].append('plate')
boxes[2].append('usb')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")