# Initial state of boxes
boxes = {
    0: ['coin'],
    1: ['tape', 'octopus'],
    2: [],
    3: [],
    4: [],
    5: ['island', 'pen', 'bowl', 'star'],
    6: ['butterfly', 'branch', 'grass', 'soap'],
    7: ['umbrella', 'submarine', 'bear', 'bird'],
    8: ['scarf', 'doll'],
    9: ['cup', 'horn'],
    10: ['game', 'drum']
}

# Replace the cup with the apple in Box 9.
boxes[9].remove('cup')
boxes[9].append('apple')

# Swap the octopus in Box 1 with the submarine in Box 7.
boxes[1].remove('octopus')
boxes[7].remove('submarine')
boxes[1].append('submarine')
boxes[7].append('octopus')

# Remove the scarf and the doll from Box 8.
boxes[8].remove('scarf')
boxes[8].remove('doll')

# Put the guitar and the sun into Box 7.
boxes[7].append('guitar')
boxes[7].append('sun')

# Move the star and the bowl from Box 5 to Box 7.
boxes[5].remove('star')
boxes[5].remove('bowl')
boxes[7].append('star')
boxes[7].append('bowl')

# Swap the coin in Box 0 with the butterfly in Box 6.
boxes[0].remove('coin')
boxes[6].remove('butterfly')
boxes[0].append('butterfly')
boxes[6].append('coin')

# Replace the butterfly with the truck in Box 0.
boxes[0].remove('butterfly')
boxes[0].append('truck')

# Remove the truck from Box 0.
boxes[0].remove('truck')

# Put the starfish and the grinder into Box 0.
boxes[0].append('starfish')
boxes[0].append('grinder')

# Replace the branch and the soap and the coin with the shoe and the umbrella and the table in Box 6.
boxes[6].remove('branch')
boxes[6].remove('soap')
boxes[6].remove('coin')
boxes[6].append('shoe')
boxes[6].append('umbrella')
boxes[6].append('table')

# Remove the island from Box 5.
boxes[5].remove('island')

# Empty Box 5.
boxes[5] = []

# Put the earring into Box 4.
boxes[4].append('earring')

# Put the river and the tape and the desert into Box 3.
boxes[3].append('river')
boxes[3].append('tape')
boxes[3].append('desert')

# Put the mirror and the vase and the headphone into Box 5.
boxes[5].append('mirror')
boxes[5].append('vase')
boxes[5].append('headphone')

# Put the scissors into Box 4.
boxes[4].append('scissors')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")