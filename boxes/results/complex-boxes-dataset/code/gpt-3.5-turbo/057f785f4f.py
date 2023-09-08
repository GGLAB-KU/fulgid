# Initial state of boxes
boxes = {
    0: ['toaster', 'glove', 'train'],
    1: ['thunder', 'cow', 'keyboard', 'boat', 'bus'],
    2: ['pan', 'jungle', 'cup', 'console', 'car'],
    3: ['key', 'plane', 'necklace', 'swimsuit', 'cat'],
    4: ['coat', 'scarf', 'perfume', 'moon', 'basket'],
    5: [],
    6: []
}

# Put the lion and the boat into Box 5.
boxes[5].append('lion')
boxes[5].append('boat')

# Swap the glove in Box 0 with the coat in Box 4.
boxes[0].remove('glove')
boxes[4].remove('coat')
boxes[0].append('coat')
boxes[4].append('glove')

# Replace the lion with the polish in Box 5.
boxes[5].remove('lion')
boxes[5].append('polish')

# Move the necklace from Box 3 to Box 0.
boxes[3].remove('necklace')
boxes[0].append('necklace')

# Remove the necklace and the toaster from Box 0.
boxes[0].remove('necklace')
boxes[0].remove('toaster')

# Move the boat from Box 5 to Box 1.
boxes[5].remove('boat')
boxes[1].append('boat')

# Swap the polish in Box 5 with the coat in Box 0.
boxes[5].remove('polish')
boxes[0].remove('coat')
boxes[5].append('coat')
boxes[0].append('polish')

# Swap the coat in Box 5 with the cat in Box 3.
boxes[5].remove('coat')
boxes[3].remove('cat')
boxes[5].append('cat')
boxes[3].append('coat')

# Replace the pan and the car and the console with the grinder and the microwave and the cup in Box 2.
boxes[2].remove('pan')
boxes[2].remove('car')
boxes[2].remove('console')
boxes[2].append('grinder')
boxes[2].append('microwave')
boxes[2].append('cup')

# Move the perfume and the scarf and the glove from Box 4 to Box 5.
items_to_move = ['perfume', 'scarf', 'glove']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[5].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")