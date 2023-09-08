# Initial state of boxes
boxes = {
    0: ['watch', 'comb', 'river'],
    1: ['cloud', 'soap'],
    2: ['train', 'toaster', 'glove', 'microwave', 'desert'],
    3: ['cup', 'shark', 'butterfly', 'microscope', 'grinder'],
    4: [],
    5: ['whistle', 'shelf', 'submarine', 'pan', 'grass']
}

# Put the earring and the harmonica and the tie into Box 4.
items_to_move = ['earring', 'harmonica', 'tie']
for item in items_to_move:
    boxes[4].append(item)

# Replace the cup and the shark and the grinder with the bird and the keyboard and the octopus in Box 3.
boxes[3].remove('cup')
boxes[3].remove('shark')
boxes[3].remove('grinder')
boxes[3].append('bird')
boxes[3].append('keyboard')
boxes[3].append('octopus')

# Swap the microwave in Box 2 with the butterfly in Box 3.
boxes[2].remove('microwave')
boxes[3].remove('butterfly')
boxes[2].append('butterfly')
boxes[3].append('microwave')

# Move the soap and the cloud from Box 1 to Box 4.
items_to_move = ['soap', 'cloud']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Swap the river in Box 0 with the grass in Box 5.
boxes[0].remove('river')
boxes[5].remove('grass')
boxes[0].append('grass')
boxes[5].append('river')

# Remove the octopus from Box 3.
boxes[3].remove('octopus')

# Remove the watch and the comb from Box 0.
items_to_remove = ['watch', 'comb']
for item in items_to_remove:
    boxes[0].remove(item)

# Swap the river in Box 5 with the glove in Box 2.
boxes[5].remove('river')
boxes[2].remove('glove')
boxes[5].append('glove')
boxes[2].append('river')

# Remove the grass from Box 0.
boxes[0].remove('grass')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")