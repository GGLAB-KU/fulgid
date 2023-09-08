# Initial state of boxes
boxes = {
    0: ['wallet', 'snow', 'toothpaste', 'plane', 'pot'],
    1: ['forest', 'wig', 'earring'],
    2: ['freezer', 'oven'],
    3: [],
    4: ['shoes', 'meteor', 'game', 'zipper', 'moon'],
    5: ['boot', 'bird', 'desert', 'mask', 'candle'],
    6: ['key', 'needle', 'glasses'],
    7: ['jacket', 'speaker']
}

# Swap the bird in Box 5 with the game in Box 4.
boxes[5].remove('bird')
boxes[4].remove('game')
boxes[5].append('game')
boxes[4].append('bird')

# Replace the mask with the wire in Box 5.
boxes[5].remove('mask')
boxes[5].append('wire')

# Replace the oven and the freezer with the ocean and the thunder in Box 2.
boxes[2].remove('oven')
boxes[2].remove('freezer')
boxes[2].append('ocean')
boxes[2].append('thunder')

# Move the snow and the toothpaste and the pot from Box 0 to Box 5.
items_to_move = ['snow', 'toothpaste', 'pot']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Put the scissors and the plate and the table into Box 7.
items_to_put = ['scissors', 'plate', 'table']
for item in items_to_put:
    boxes[7].append(item)

# Replace the meteor and the shoes and the zipper with the charger and the pillow and the piano in Box 4.
boxes[4].remove('meteor')
boxes[4].remove('shoes')
boxes[4].remove('zipper')
boxes[4].append('charger')
boxes[4].append('pillow')
boxes[4].append('piano')

# Empty Box 1.
boxes[1] = []

# Put the octopus into Box 7.
boxes[7].append('octopus')

# Move the needle and the key and the glasses from Box 6 to Box 1.
items_to_move = ['needle', 'key', 'glasses']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[1].append(item)

# Swap the moon in Box 4 with the speaker in Box 7.
boxes[4].remove('moon')
boxes[7].remove('speaker')
boxes[4].append('speaker')
boxes[7].append('moon')

# Move the needle and the glasses and the key from Box 1 to Box 0.
items_to_move = ['needle', 'glasses', 'key']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[0].append(item)

# Remove the wire from Box 5.
boxes[5].remove('wire')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")