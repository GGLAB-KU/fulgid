# Initial state of boxes
boxes = {
    0: ['controller'],
    1: ['pillow', 'glove', 'river'],
    2: [],
    3: ['sock', 'tie', 'shelf'],
    4: [],
    5: [],
    6: [],
    7: ['note', 'tree', 'shoes', 'boat', 'toy'],
    8: ['coin', 'coral', 'skirt'],
    9: ['car', 'motorcycle'],
    10: [],
    11: ['lion', 'table', 'vase'],
    12: [],
    13: ['bag', 'battery', 'shorts', 'starfish'],
    14: ['scarf', 'jacket', 'guitar']
}

# Move the guitar from Box 14 to Box 11.
boxes[14].remove('guitar')
boxes[11].append('guitar')

# Remove the motorcycle and the car from Box 9.
boxes[9].remove('motorcycle')
boxes[9].remove('car')

# Replace the coin with the oven in Box 8.
boxes[8].remove('coin')
boxes[8].append('oven')

# Put the frame and the thunder into Box 1.
boxes[1].append('frame')
boxes[1].append('thunder')

# Remove the shelf from Box 3.
boxes[3].remove('shelf')

# Put the bicycle and the headphone into Box 3.
boxes[3].append('bicycle')
boxes[3].append('headphone')

# Remove the jacket and the scarf from Box 14.
boxes[14].remove('jacket')
boxes[14].remove('scarf')

# Swap the bicycle in Box 3 with the note in Box 7.
boxes[3].remove('bicycle')
boxes[7].remove('note')
boxes[3].append('note')
boxes[7].append('bicycle')

# Put the boat into Box 6.
boxes[6].append('boat')

# Move the note from Box 3 to Box 9.
boxes[3].remove('note')
boxes[9].append('note')

# Replace the bag and the starfish and the battery with the magnet and the wallet and the thunder in Box 13.
boxes[13].remove('bag')
boxes[13].remove('starfish')
boxes[13].remove('battery')
boxes[13].append('magnet')
boxes[13].append('wallet')
boxes[13].append('thunder')

# Swap the thunder in Box 1 with the coral in Box 8.
boxes[1].remove('thunder')
boxes[8].remove('coral')
boxes[1].append('coral')
boxes[8].append('thunder')

# Move the wallet and the thunder and the shorts from Box 13 to Box 5.
boxes[13].remove('wallet')
boxes[13].remove('thunder')
boxes[13].remove('shorts')
boxes[5].append('wallet')
boxes[5].append('thunder')
boxes[5].append('shorts')

# Remove the controller from Box 0.
boxes[0].remove('controller')

# Replace the glove with the rock in Box 1.
boxes[1].remove('glove')
boxes[1].append('rock')

# Move the frame and the rock and the coral from Box 1 to Box 13.
boxes[1].remove('frame')
boxes[1].remove('rock')
boxes[1].remove('coral')
boxes[13].append('frame')
boxes[13].append('rock')
boxes[13].append('coral')

# Replace the tree with the toy in Box 7.
boxes[7].remove('tree')
boxes[7].append('toy')

# Empty Box 3.
boxes[3] = []

# Put the flower and the fish and the clock into Box 2.
boxes[2].append('flower')
boxes[2].append('fish')
boxes[2].append('clock')

# Put the car and the plate into Box 9.
boxes[9].append('car')
boxes[9].append('plate')

# Put the toothpaste and the blender and the ring into Box 5.
boxes[5].append('toothpaste')
boxes[5].append('blender')
boxes[5].append('ring')

# Swap the thunder in Box 8 with the pillow in Box 1.
boxes[8].remove('thunder')
boxes[1].remove('pillow')
boxes[8].append('pillow')
boxes[1].append('thunder')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")