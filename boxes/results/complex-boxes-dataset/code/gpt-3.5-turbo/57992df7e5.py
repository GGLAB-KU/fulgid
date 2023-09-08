# Initial state of boxes
boxes = {
    0: ['fish', 'toothbrush'],
    1: ['cloud', 'razor', 'soap'],
    2: ['scarf', 'lamp'],
    3: ['grinder', 'tie', 'cow'],
    4: ['whistle', 'card', 'elephant'],
    5: ['battery'],
    6: ['pot', 'blanket', 'shark', 'charger', 'lightning'],
    7: ['horse', 'candle'],
    8: ['towel', 'needle', 'jungle', 'blender'],
    9: [],
    10: ['toothpaste', 'belt', 'speaker', 'key', 'table'],
    11: [],
    12: ['swimsuit'],
    13: []
}

# Move the towel and the needle and the blender from Box 8 to Box 7.
items_to_move = ['towel', 'needle', 'blender']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[7].append(item)

# Swap the lightning in Box 6 with the whistle in Box 4.
boxes[6].remove('lightning')
boxes[4].remove('whistle')
boxes[6].append('whistle')
boxes[4].append('lightning')

# Put the charger into Box 3.
boxes[3].append('charger')

# Swap the jungle in Box 8 with the battery in Box 5.
boxes[8].remove('jungle')
boxes[5].remove('battery')
boxes[8].append('battery')
boxes[5].append('jungle')

# Move the key and the toothpaste and the speaker from Box 10 to Box 8.
items_to_move = ['key', 'toothpaste', 'speaker']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[8].append(item)

# Remove the cow from Box 3.
boxes[3].remove('cow')

# Put the cup and the vase and the umbrella into Box 0.
items_to_put = ['cup', 'vase', 'umbrella']
for item in items_to_put:
    boxes[0].append(item)

# Move the razor and the soap and the cloud from Box 1 to Box 9.
items_to_move = ['razor', 'soap', 'cloud']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[9].append(item)

# Put the truck into Box 9.
boxes[9].append('truck')

# Replace the fish and the toothbrush with the battery and the car in Box 0.
boxes[0].remove('fish')
boxes[0].remove('toothbrush')
boxes[0].append('battery')
boxes[0].append('car')

# Move the charger and the shark and the blanket from Box 6 to Box 8.
items_to_move = ['charger', 'shark', 'blanket']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[8].append(item)

# Swap the table in Box 10 with the grinder in Box 3.
boxes[10].remove('table')
boxes[3].remove('grinder')
boxes[10].append('grinder')
boxes[3].append('table')

# Empty Box 6.
boxes[6] = []

# Replace the scarf with the flute in Box 2.
boxes[2].remove('scarf')
boxes[2].append('flute')

# Remove the towel and the needle from Box 7.
boxes[7].remove('towel')
boxes[7].remove('needle')

# Replace the blanket with the game in Box 8.
boxes[8].remove('blanket')
boxes[8].append('game')

# Replace the belt and the grinder with the grass and the wig in Box 10.
boxes[10].remove('belt')
boxes[10].remove('grinder')
boxes[10].append('grass')
boxes[10].append('wig')

# Move the horse and the blender and the candle from Box 7 to Box 3.
items_to_move = ['horse', 'blender', 'candle']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[3].append(item)

# Move the card and the lightning and the elephant from Box 4 to Box 13.
items_to_move = ['card', 'lightning', 'elephant']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[13].append(item)

# Put the horn into Box 2.
boxes[2].append('horn')

# Replace the lamp and the horn and the flute with the comet and the perfume and the guitar in Box 2.
boxes[2].remove('lamp')
boxes[2].remove('horn')
boxes[2].remove('flute')
boxes[2].append('comet')
boxes[2].append('perfume')
boxes[2].append('guitar')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")