# Initial state of boxes
boxes = {
    0: ['motorcycle', 'sun', 'shark', 'wire'],
    1: ['needle', 'toy'],
    2: ['console', 'fish', 'soap', 'lamp', 'drum'],
    3: [],
    4: [],
    5: ['coin', 'sculpture', 'shelf', 'zipper', 'perfume'],
    6: ['skirt'],
    7: ['shirt', 'razor', 'makeup'],
    8: ['tie', 'dress', 'boot', 'hat'],
    9: ['dog', 'leaf', 'toothbrush'],
    10: ['seaweed', 'bird', 'charger', 'card']
}

# Empty Box 5.
boxes[5] = []

# Replace the dog with the blanket in Box 9.
boxes[9].remove('dog')
boxes[9].append('blanket')

# Move the shirt and the razor from Box 7 to Box 8.
boxes[7].remove('shirt')
boxes[7].remove('razor')
boxes[8].append('shirt')
boxes[8].append('razor')

# Replace the card with the shirt in Box 10.
boxes[10].remove('card')
boxes[10].append('shirt')

# Put the harmonica into Box 4.
boxes[4].append('harmonica')

# Replace the skirt with the headphone in Box 6.
boxes[6].remove('skirt')
boxes[6].append('headphone')

# Remove the harmonica from Box 4.
boxes[4].remove('harmonica')

# Swap the fish in Box 2 with the boot in Box 8.
boxes[2].remove('fish')
boxes[8].remove('boot')
boxes[2].append('boot')
boxes[8].append('fish')

# Replace the shirt with the comb in Box 10.
boxes[10].remove('shirt')
boxes[10].append('comb')

# Put the car into Box 2.
boxes[2].append('car')

# Move the toothbrush and the blanket from Box 9 to Box 10.
boxes[9].remove('toothbrush')
boxes[9].remove('blanket')
boxes[10].append('toothbrush')
boxes[10].append('blanket')

# Remove the makeup from Box 7.
boxes[7].remove('makeup')

# Remove the headphone from Box 6.
boxes[6].remove('headphone')

# Put the shorts and the shirt and the tree into Box 1.
items_to_move = ['shorts', 'shirt', 'tree']
for item in items_to_move:
    boxes[1].append(item)

# Swap the shark in Box 0 with the tree in Box 1.
boxes[0].remove('shark')
boxes[1].remove('tree')
boxes[0].append('tree')
boxes[1].append('shark')

# Put the battery into Box 4.
boxes[4].append('battery')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")