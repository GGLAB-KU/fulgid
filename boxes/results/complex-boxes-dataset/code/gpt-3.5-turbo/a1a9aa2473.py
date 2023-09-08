# Initial state of boxes
boxes = {
    0: ['table', 'necklace'],
    1: ['polish', 'camera', 'plate', 'starfish', 'coin'],
    2: ['console', 'branch', 'jacket', 'doll', 'glove'],
    3: ['lock', 'headphone', 'coral'],
    4: ['toy', 'freezer', 'zipper'],
    5: ['leaf', 'grinder', 'puzzle', 'whistle', 'keyboard'],
    6: ['bell', 'candle', 'belt', 'fridge', 'ship'],
    7: ['tie', 'perfume', 'shampoo', 'oven']
}

# Replace the necklace and the table with the vase and the flute in Box 0.
boxes[0].remove('table')
boxes[0].remove('necklace')
boxes[0].append('vase')
boxes[0].append('flute')

# Swap the flute in Box 0 with the puzzle in Box 5.
boxes[0].remove('flute')
boxes[5].remove('puzzle')
boxes[0].append('puzzle')
boxes[5].append('flute')

# Remove the leaf from Box 5.
boxes[5].remove('leaf')

# Remove the zipper and the toy from Box 4.
boxes[4].remove('zipper')
boxes[4].remove('toy')

# Replace the shampoo with the lamp in Box 7.
boxes[7].remove('shampoo')
boxes[7].append('lamp')

# Swap the coin in Box 1 with the belt in Box 6.
boxes[1].remove('coin')
boxes[6].remove('belt')
boxes[1].append('belt')
boxes[6].append('coin')

# Put the book into Box 4.
boxes[4].append('book')

# Replace the grinder and the flute with the seaweed and the magnet in Box 5.
boxes[5].remove('grinder')
boxes[5].remove('flute')
boxes[5].append('seaweed')
boxes[5].append('magnet')

# Move the headphone and the coral from Box 3 to Box 0.
boxes[3].remove('headphone')
boxes[3].remove('coral')
boxes[0].append('headphone')
boxes[0].append('coral')

# Put the belt into Box 5.
boxes[6].remove('belt')
boxes[5].append('belt')

# Move the starfish and the plate and the camera from Box 1 to Box 3.
items_to_move = ['starfish', 'plate', 'camera']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Put the microwave into Box 5.
boxes[5].append('microwave')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")