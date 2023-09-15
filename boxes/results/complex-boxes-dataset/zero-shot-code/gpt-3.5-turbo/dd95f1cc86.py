box = {
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

def print_box_contents():
    for i in range(15):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

print_box_contents()

# Move the guitar from Box 14 to Box 11
box[11].append(box[14].pop())

# Remove the motorcycle and the car from Box 9
box[9].remove('motorcycle')
box[9].remove('car')

# Replace the coin with the oven in Box 8
box[8].remove('coin')
box[8].append('oven')

# Put the frame and the thunder into Box 1
box[1].extend(['frame', 'thunder'])

# Remove the shelf from Box 3
box[3].remove('shelf')

# Put the bicycle and the headphone into Box 3
box[3].extend(['bicycle', 'headphone'])

# Remove the jacket and the scarf from Box 14
box[14].remove('jacket')
box[14].remove('scarf')

# Swap the bicycle in Box 3 with the note in Box 7
box[3].remove('bicycle')
box[7].remove('note')
box[3].append('note')
box[7].append('bicycle')

# Put the boat into Box 6
box[6].append('boat')

# Move the note from Box 3 to Box 9
box[9].append(box[3].pop())

# Replace the bag and the starfish and the battery with the magnet and the wallet and the thunder in Box 13
box[13].remove('bag')
box[13].remove('starfish')
box[13].remove('battery')
box[13].extend(['magnet', 'wallet', 'thunder'])

# Swap the thunder in Box 1 with the coral in Box 8
box[1].remove('thunder')
box[8].remove('coral')
box[1].append('coral')
box[8].append('thunder')

# Move the wallet and the thunder and the shorts from Box 13 to Box 5
box[5].extend([box[13].pop(), box[13].pop(), box[13].pop()])

# Remove the controller from Box 0
box[0].remove('controller')

# Replace the glove with the rock in Box 1
box[1].remove('glove')
box[1].append('rock')

# Move the frame and the rock and the coral from Box 1 to Box 13
box[13].extend([box[1].pop(), box[1].pop(), box[1].pop()])

# Replace the tree with the toy in Box 7
box[7].remove('tree')
box[7].append('toy')

# Empty Box 3
box[3] = []

# Put the flower and the fish and the clock into Box 2
box[2].extend(['flower', 'fish', 'clock'])

# Put the car and the plate into Box 9
box[9].extend(['car', 'plate'])

# Put the toothpaste and the blender and the ring into Box 5
box[5].extend(['toothpaste', 'blender', 'ring'])

# Swap the thunder in Box 8 with the pillow in Box 1
box[8].remove('thunder')
box[1].remove('pillow')
box[8].append('pillow')
box[1].append('thunder')

print_box_contents()