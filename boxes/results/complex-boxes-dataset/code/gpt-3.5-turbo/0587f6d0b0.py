# Initial state of boxes
boxes = {
    0: ['lion', 'toy'],
    1: ['cup'],
    2: ['console'],
    3: ['controller', 'coin', 'horse', 'freezer'],
    4: ['wig', 'flower'],
    5: ['coral', 'shark', 'train', 'puzzle'],
    6: ['whistle', 'submarine', 'star'],
    7: ['battery'],
    8: [],
    9: ['branch', 'dolphin', 'mixer', 'sculpture', 'moon']
}

# Put the butterfly into Box 4.
boxes[4].append('butterfly')

# Put the fish and the shelf and the soap into Box 3.
items_to_put = ['fish', 'shelf', 'soap']
for item in items_to_put:
    boxes[3].append(item)

# Put the octopus and the cow and the fork into Box 9.
items_to_put = ['octopus', 'cow', 'fork']
for item in items_to_put:
    boxes[9].append(item)

# Replace the coin with the horse in Box 3.
boxes[3].remove('coin')
boxes[3].append('horse')

# Put the tiger into Box 0.
boxes[0].append('tiger')

# Swap the submarine in Box 6 with the cup in Box 1.
boxes[6].remove('submarine')
boxes[1].remove('cup')
boxes[6].append('cup')
boxes[1].append('submarine')

# Replace the lion and the toy and the tiger with the octopus and the horse and the umbrella in Box 0.
items_to_remove = ['lion', 'toy', 'tiger']
items_to_put = ['octopus', 'horse', 'umbrella']
for item in items_to_remove:
    boxes[0].remove(item)
for item in items_to_put:
    boxes[0].append(item)

# Empty Box 4.
boxes[4] = []

# Put the dress and the glasses into Box 8.
items_to_put = ['dress', 'glasses']
for item in items_to_put:
    boxes[8].append(item)

# Move the whistle and the star from Box 6 to Box 1.
items_to_move = ['whistle', 'star']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[1].append(item)

# Swap the cup in Box 6 with the shelf in Box 3.
boxes[6].remove('cup')
boxes[3].remove('shelf')
boxes[6].append('shelf')
boxes[3].append('cup')

# Put the coat into Box 4.
boxes[4].append('coat')

# Move the dress and the glasses from Box 8 to Box 5.
items_to_move = ['dress', 'glasses']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[5].append(item)

# Remove the umbrella and the octopus and the horse from Box 0.
items_to_remove = ['umbrella', 'octopus', 'horse']
for item in items_to_remove:
    boxes[0].remove(item)

# Replace the console with the helmet in Box 2.
boxes[2] = ['helmet']

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")