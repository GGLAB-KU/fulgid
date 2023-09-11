# Initial state of boxes
boxes = {
    0: ['pen', 'whistle', 'scarf', 'speaker'],
    1: [],
    2: ['boot', 'crown', 'shark'],
    3: ['table', 'magnet'],
    4: ['coin'],
    5: ['jungle', 'soap'],
    6: []
}

# Replace the soap with the charger in Box 5.
boxes[5].remove('soap')
boxes[5].append('charger')

# Put the boot and the coin and the snow into Box 1.
items_to_put = ['boot', 'coin', 'snow']
for item in items_to_put:
    boxes[1].append(item)

# Move the boot and the coin from Box 1 to Box 0.
items_to_move = ['boot', 'coin']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[0].append(item)

# Put the phone and the jungle into Box 3.
items_to_put = ['phone', 'jungle']
for item in items_to_put:
    boxes[3].append(item)

# Empty Box 4.
boxes[4] = []

# Replace the table and the phone with the coat and the needle in Box 3.
boxes[3].remove('table')
boxes[3].remove('phone')
boxes[3].append('coat')
boxes[3].append('needle')

# Swap the speaker in Box 0 with the needle in Box 3.
boxes[0].remove('speaker')
boxes[3].remove('needle')
boxes[0].append('needle')
boxes[3].append('speaker')

# Move the snow from Box 1 to Box 3.
boxes[1].remove('snow')
boxes[3].append('snow')

# Swap the crown in Box 2 with the coat in Box 3.
boxes[2].remove('crown')
boxes[3].remove('coat')
boxes[2].append('coat')
boxes[3].append('crown')

# Put the train into Box 4.
boxes[4].append('train')

# Put the river into Box 1.
boxes[1].append('river')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")