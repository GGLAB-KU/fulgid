# Initial state of boxes
boxes = {
    0: ['hat', 'charger', 'moon', 'rain', 'toothbrush'],
    1: ['belt', 'shampoo', 'motorcycle', 'oven'],
    2: ['submarine', 'paint', 'microscope', 'phone'],
    3: ['branch', 'skirt', 'cat', 'star'],
    4: ['key', 'meteor', 'island', 'earring', 'pillow'],
    5: ['necklace'],
    6: ['spoon', 'grinder', 'cow', 'note', 'shelf'],
    7: ['train', 'violin', 'shoes', 'mountain', 'octopus'],
    8: ['soap', 'battery', 'card', 'plane'],
    9: ['cloud', 'forest', 'thread', 'brush', 'puzzle'],
    10: [],
    11: ['tiger'],
    12: ['mask', 'boot', 'horse', 'flower', 'coat']
}

# Put the needle and the coin into Box 5.
boxes[5].append('needle')
boxes[5].append('coin')

# Remove the star and the skirt from Box 3.
boxes[3].remove('star')
boxes[3].remove('skirt')

# Move the earring and the pillow from Box 4 to Box 2.
boxes[4].remove('earring')
boxes[4].remove('pillow')
boxes[2].append('earring')
boxes[2].append('pillow')

# Put the toothpaste and the candle into Box 12.
boxes[12].append('toothpaste')
boxes[12].append('candle')

# Put the cup into Box 7.
boxes[7].append('cup')

# Remove the soap from Box 8.
boxes[8].remove('soap')

# Remove the brush from Box 9.
boxes[9].remove('brush')

# Move the shampoo and the motorcycle and the belt from Box 1 to Box 2.
items_to_move = ['shampoo', 'motorcycle', 'belt']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Swap the tiger in Box 11 with the cat in Box 3.
boxes[11], boxes[3] = boxes[3], boxes[11]

# Replace the coin and the necklace and the needle with the fish and the grass and the freezer in Box 5.
boxes[5].remove('coin')
boxes[5].remove('necklace')
boxes[5].remove('needle')
boxes[5].append('fish')
boxes[5].append('grass')
boxes[5].append('freezer')

# Remove the tiger and the branch from Box 3.
boxes[3].remove('tiger')
boxes[3].remove('branch')

# Move the toothbrush and the charger and the hat from Box 0 to Box 9.
items_to_move = ['toothbrush', 'charger', 'hat']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[9].append(item)

# Remove the candle and the horse from Box 12.
boxes[12].remove('candle')
boxes[12].remove('horse')

# Move the card and the plane from Box 8 to Box 3.
boxes[8].remove('card')
boxes[8].remove('plane')
boxes[3].append('card')
boxes[3].append('plane')

# Swap the moon in Box 0 with the fish in Box 5.
boxes[0], boxes[5] = boxes[5], boxes[0]

# Put the octopus and the wire and the telescope into Box 6.
boxes[6].append('octopus')
boxes[6].append('wire')
boxes[6].append('telescope')

# Remove the cat from Box 11.
boxes[11].remove('cat')

# Remove the card and the plane from Box 3.
boxes[3].remove('card')
boxes[3].remove('plane')

# Swap the key in Box 4 with the grass in Box 5.
boxes[4], boxes[5] = boxes[5], boxes[4]

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")