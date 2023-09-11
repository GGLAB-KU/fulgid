# Initial state of boxes
boxes = {
    0: [],
    1: ['snow', 'cat', 'star'],
    2: ['flute', 'thread'],
    3: ['whistle', 'horse', 'sandals'],
    4: [],
    5: ['lightning', 'magnet', 'shoes', 'seaweed', 'island'],
    6: ['table'],
    7: ['toothpaste', 'lion'],
    8: ['headphone'],
    9: ['shoe', 'leaf'],
    10: ['cup', 'key', 'doll', 'lock'],
    11: ['battery', 'charger', 'candle', 'necklace'],
    12: ['bag', 'butterfly', 'horn']
}

# Swap the thread in Box 2 with the cup in Box 10.
boxes[2].remove('thread')
boxes[10].remove('cup')
boxes[2].append('cup')
boxes[10].append('thread')

# Put the ring into Box 11.
boxes[11].append('ring')

# Put the basket and the train and the river into Box 12.
boxes[12].extend(['basket', 'train', 'river'])

# Put the paint into Box 11.
boxes[11].append('paint')

# Swap the leaf in Box 9 with the key in Box 10.
boxes[9].remove('leaf')
boxes[10].remove('key')
boxes[9].append('key')
boxes[10].append('leaf')

# Remove the lightning and the island and the shoes from Box 5.
items_to_remove = ['lightning', 'island', 'shoes']
for item in items_to_remove:
    boxes[5].remove(item)

# Move the horse and the sandals and the whistle from Box 3 to Box 1.
items_to_move = ['horse', 'sandals', 'whistle']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[1].append(item)

# Swap the charger in Box 11 with the river in Box 12.
boxes[11].remove('charger')
boxes[12].remove('river')
boxes[11].append('river')
boxes[12].append('charger')

# Remove the lock from Box 10.
boxes[10].remove('lock')

# Move the cup from Box 2 to Box 11.
boxes[2].remove('cup')
boxes[11].append('cup')

# Swap the flute in Box 2 with the headphone in Box 8.
boxes[2].remove('flute')
boxes[8].remove('headphone')
boxes[2].append('headphone')
boxes[8].append('flute')

# Remove the basket and the butterfly from Box 12.
boxes[12].remove('basket')
boxes[12].remove('butterfly')

# Swap the whistle in Box 1 with the seaweed in Box 5.
boxes[1].remove('whistle')
boxes[5].remove('seaweed')
boxes[1].append('seaweed')
boxes[5].append('whistle')

# Remove the table from Box 6.
boxes[6].remove('table')

# Move the whistle and the magnet from Box 5 to Box 0.
boxes[5].remove('whistle')
boxes[5].remove('magnet')
boxes[0].extend(['whistle', 'magnet'])

# Put the skirt and the polish and the snow into Box 11.
boxes[11].extend(['skirt', 'polish', 'snow'])

# Move the leaf and the thread and the doll from Box 10 to Box 12.
items_to_move = ['leaf', 'thread', 'doll']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[12].append(item)

# Remove the toothpaste and the lion from Box 7.
boxes[7].remove('toothpaste')
boxes[7].remove('lion')

# Swap the flute in Box 8 with the shoe in Box 9.
boxes[8].remove('flute')
boxes[9].remove('shoe')
boxes[8].append('shoe')
boxes[9].append('flute')

# Put the hat and the star into Box 0.
boxes[0].extend(['hat', 'star'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")