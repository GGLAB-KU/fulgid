# Initial state of boxes
boxes = {
    0: [],
    1: ['crown'],
    2: ['lamp'],
    3: ['grinder', 'toothpaste', 'bear'],
    4: ['toaster', 'tape', 'blender', 'wallet'],
    5: ['pot', 'jungle', 'island', 'flute'],
    6: ['shorts', 'toy'],
    7: ['controller', 'dog', 'river'],
    8: ['comet'],
    9: ['butterfly', 'plane', 'note', 'fork'],
    10: ['key', 'shoe', 'bell'],
    11: ['drum', 'shirt'],
    12: ['brush', 'table', 'coral', 'storm'],
    13: ['frame', 'zipper', 'makeup', 'spoon']
}

# Swap the lamp in Box 2 with the grinder in Box 3.
boxes[2], boxes[3] = boxes[3], boxes[2]

# Move the grinder from Box 2 to Box 1.
boxes[2].remove('grinder')
boxes[1].append('grinder')

# Put the keyboard and the dress into Box 11.
boxes[11].append('keyboard')
boxes[11].append('dress')

# Move the toothpaste from Box 3 to Box 2.
boxes[3].remove('toothpaste')
boxes[2].append('toothpaste')

# Move the wallet and the toaster from Box 4 to Box 10.
boxes[4].remove('wallet')
boxes[4].remove('toaster')
boxes[10].append('wallet')
boxes[10].append('toaster')

# Put the toothbrush and the snow into Box 4.
boxes[4].append('toothbrush')
boxes[4].append('snow')

# Move the toothpaste from Box 2 to Box 7.
boxes[2].remove('toothpaste')
boxes[7].append('toothpaste')

# Move the blender from Box 4 to Box 13.
boxes[4].remove('blender')
boxes[13].append('blender')

# Move the island and the flute from Box 5 to Box 10.
boxes[5].remove('island')
boxes[5].remove('flute')
boxes[10].append('island')
boxes[10].append('flute')

# Put the scarf and the grass into Box 13.
boxes[13].append('scarf')
boxes[13].append('grass')

# Empty Box 7.
boxes[7] = []

# Remove the snow from Box 4.
boxes[4].remove('snow')

# Move the island and the wallet from Box 10 to Box 11.
boxes[10].remove('island')
boxes[10].remove('wallet')
boxes[11].append('island')
boxes[11].append('wallet')

# Put the blender and the blanket and the bracelet into Box 5.
boxes[5].append('blender')
boxes[5].append('blanket')
boxes[5].append('bracelet')

# Remove the brush and the coral from Box 12.
boxes[12].remove('brush')
boxes[12].remove('coral')

# Replace the toy and the shorts with the apple and the laptop in Box 6.
boxes[6].remove('toy')
boxes[6].remove('shorts')
boxes[6].append('apple')
boxes[6].append('laptop')

# Move the blanket and the bracelet from Box 5 to Box 11.
boxes[5].remove('blanket')
boxes[5].remove('bracelet')
boxes[11].append('blanket')
boxes[11].append('bracelet')

# Put the motorcycle and the tie into Box 2.
boxes[2].append('motorcycle')
boxes[2].append('tie')

# Put the telescope and the dolphin and the seaweed into Box 13.
boxes[13].append('telescope')
boxes[13].append('dolphin')
boxes[13].append('seaweed')

# Swap the apple in Box 6 with the comet in Box 8.
boxes[6], boxes[8] = boxes[8], boxes[6]

# Replace the fork and the butterfly and the plane with the planet and the charger and the sun in Box 9.
boxes[9].remove('fork')
boxes[9].remove('butterfly')
boxes[9].remove('plane')
boxes[9].append('planet')
boxes[9].append('charger')
boxes[9].append('sun')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")