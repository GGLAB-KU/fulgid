# Initial state of boxes
boxes = {
    0: ['horse', 'candle', 'cup'],
    1: ['perfume'],
    2: ['shirt', 'skirt', 'desert', 'rain', 'rocket'],
    3: ['necklace', 'ship', 'whistle'],
    4: [],
    5: ['butterfly', 'microwave', 'bear', 'toothpaste', 'bowl'],
    6: [],
    7: ['key']
}

# Swap the skirt in Box 2 with the key in Box 7.
boxes[2].remove('skirt')
boxes[7].remove('key')
boxes[2].append('key')
boxes[7].append('skirt')

# Put the ship into Box 7.
boxes[3].remove('ship')
boxes[7].append('ship')

# Move the candle from Box 0 to Box 3.
boxes[0].remove('candle')
boxes[3].append('candle')

# Swap the horse in Box 0 with the ship in Box 7.
boxes[0].remove('horse')
boxes[7].remove('ship')
boxes[0].append('ship')
boxes[7].append('horse')

# Move the perfume from Box 1 to Box 5.
boxes[1].remove('perfume')
boxes[5].append('perfume')

# Replace the cup with the belt in Box 0.
boxes[0].remove('cup')
boxes[0].append('belt')

# Swap the ship in Box 0 with the bear in Box 5.
boxes[0].remove('ship')
boxes[5].remove('bear')
boxes[0].append('bear')
boxes[5].append('ship')

# Swap the horse in Box 7 with the toothpaste in Box 5.
boxes[7].remove('horse')
boxes[5].remove('toothpaste')
boxes[7].append('toothpaste')
boxes[5].append('horse')

# Swap the rocket in Box 2 with the necklace in Box 3.
boxes[2].remove('rocket')
boxes[3].remove('necklace')
boxes[2].append('necklace')
boxes[3].append('rocket')

# Move the whistle and the rocket from Box 3 to Box 6.
boxes[3].remove('whistle')
boxes[3].remove('rocket')
boxes[6].append('whistle')
boxes[6].append('rocket')

# Move the belt and the bear from Box 0 to Box 1.
boxes[0].remove('belt')
boxes[0].remove('bear')
boxes[1].append('belt')
boxes[1].append('bear')

# Move the whistle from Box 6 to Box 3.
boxes[6].remove('whistle')
boxes[3].append('whistle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")