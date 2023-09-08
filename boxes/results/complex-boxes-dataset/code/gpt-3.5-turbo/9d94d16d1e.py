# Initial state of boxes
boxes = {
    0: ['sculpture', 'doll'],
    1: ['charger', 'toaster', 'wig', 'shirt', 'elephant'],
    2: ['frame', 'sock', 'octopus', 'clock', 'fork'],
    3: ['microwave', 'seaweed', 'puzzle', 'storm', 'apple'],
    4: ['umbrella', 'rain', 'gloves', 'game'],
    5: [],
    6: ['beach', 'crown', 'dog', 'leaf', 'wallet'],
    7: ['usb', 'dice', 'ocean', 'chair', 'razor'],
    8: ['dolphin', 'soap', 'perfume', 'bear', 'starfish'],
    9: ['coral', 'harmonica', 'mask', 'pillow', 'whistle'],
    10: ['microscope', 'note', 'towel']
}

# Put the tree into Box 2.
boxes[2].append('tree')

# Replace the puzzle and the apple with the car and the doll in Box 3.
boxes[3].remove('puzzle')
boxes[3].remove('apple')
boxes[3].append('car')
boxes[3].append('doll')

# Move the toaster and the wig from Box 1 to Box 6.
items_to_move = ['toaster', 'wig']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[6].append(item)

# Remove the crown and the toaster from Box 6.
boxes[6].remove('crown')
boxes[6].remove('toaster')

# Swap the microwave in Box 3 with the note in Box 10.
boxes[3].remove('microwave')
boxes[10].remove('note')
boxes[3].append('note')
boxes[10].append('microwave')

# Put the flute and the glasses into Box 7.
boxes[7].append('flute')
boxes[7].append('glasses')

# Replace the doll with the ship in Box 0.
boxes[0].remove('doll')
boxes[0].append('ship')

# Replace the seaweed with the bear in Box 3.
boxes[3].remove('seaweed')
boxes[3].append('bear')

# Put the pot into Box 3.
boxes[3].append('pot')

# Move the whistle and the mask from Box 9 to Box 1.
items_to_move = ['whistle', 'mask']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[1].append(item)

# Remove the starfish and the perfume and the dolphin from Box 8.
items_to_remove = ['starfish', 'perfume', 'dolphin']
for item in items_to_remove:
    boxes[8].remove(item)

# Move the usb from Box 7 to Box 8.
boxes[7].remove('usb')
boxes[8].append('usb')

# Put the car into Box 2.
boxes[2].append('car')

# Remove the game from Box 4.
boxes[4].remove('game')

# Replace the rain and the umbrella with the phone and the tree in Box 4.
boxes[4].remove('rain')
boxes[4].remove('umbrella')
boxes[4].append('phone')
boxes[4].append('tree')

# Replace the coral and the pillow and the harmonica with the clock and the battery and the branch in Box 9.
boxes[9].remove('coral')
boxes[9].remove('pillow')
boxes[9].remove('harmonica')
boxes[9].append('clock')
boxes[9].append('battery')
boxes[9].append('branch')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")