# Initial state of boxes
boxes = {
    0: [],
    1: ['shirt', 'mixer'],
    2: ['needle', 'comb', 'toy', 'river', 'necklace'],
    3: ['storm', 'ocean', 'cat', 'glove', 'ship'],
    4: ['lion', 'dolphin', 'towel', 'snow'],
    5: ['piano'],
    6: ['ring', 'flute', 'microwave', 'dress'],
    7: ['makeup', 'button', 'charger'],
    8: [],
    9: ['microscope', 'console'],
    10: ['wire', 'island', 'dog', 'harmonica', 'seaweed'],
    11: ['skirt'],
    12: ['tape', 'sock', 'pen', 'key']
}

# Replace the ship and the glove and the cat with the sock and the pot and the ocean in Box 3.
boxes[3].remove('ship')
boxes[3].remove('glove')
boxes[3].remove('cat')
boxes[3].append('sock')
boxes[3].append('pot')
boxes[3].append('ocean')

# Replace the mixer and the shirt with the chair and the shampoo in Box 1.
boxes[1].remove('mixer')
boxes[1].remove('shirt')
boxes[1].append('chair')
boxes[1].append('shampoo')

# Remove the button and the makeup from Box 7.
boxes[7].remove('button')
boxes[7].remove('makeup')

# Put the whistle and the clock into Box 6.
boxes[6].append('whistle')
boxes[6].append('clock')

# Move the charger from Box 7 to Box 9.
boxes[7].remove('charger')
boxes[9].append('charger')

# Remove the microscope and the charger from Box 9.
boxes[9].remove('microscope')
boxes[9].remove('charger')

# Remove the dog and the wire and the seaweed from Box 10.
boxes[10].remove('dog')
boxes[10].remove('wire')
boxes[10].remove('seaweed')

# Put the crown and the tree and the tie into Box 7.
boxes[7].append('crown')
boxes[7].append('tree')
boxes[7].append('tie')

# Remove the key from Box 12.
boxes[12].remove('key')

# Swap the chair in Box 1 with the tree in Box 7.
boxes[1].remove('chair')
boxes[7].remove('tree')
boxes[1].append('tree')
boxes[7].append('chair')

# Remove the snow and the lion and the towel from Box 4.
boxes[4].remove('snow')
boxes[4].remove('lion')
boxes[4].remove('towel')

# Move the skirt from Box 11 to Box 1.
boxes[11].remove('skirt')
boxes[1].append('skirt')

# Put the shoe into Box 5.
boxes[5].append('shoe')

# Replace the pen and the tape with the branch and the sculpture in Box 12.
boxes[12].remove('pen')
boxes[12].remove('tape')
boxes[12].append('branch')
boxes[12].append('sculpture')

# Put the lock into Box 2.
boxes[2].append('lock')

# Remove the tie and the crown and the chair from Box 7.
boxes[7].remove('tie')
boxes[7].remove('crown')
boxes[7].remove('chair')

# Remove the piano and the shoe from Box 5.
boxes[5].remove('piano')
boxes[5].remove('shoe')

# Replace the console with the jacket in Box 9.
boxes[9].remove('console')
boxes[9].append('jacket')

# Move the island from Box 10 to Box 5.
boxes[10].remove('island')
boxes[5].append('island')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")