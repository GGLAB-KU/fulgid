# Initial state of boxes
boxes = {
    0: ['earring', 'puzzle', 'bowl'],
    1: ['charger', 'card', 'towel', 'blender'],
    2: ['wallet', 'elephant', 'comet'],
    3: ['violin'],
    4: ['rocket', 'note', 'toothbrush'],
    5: ['cloud'],
    6: [],
    7: [],
    8: ['shirt', 'cat', 'cow'],
    9: ['sandals'],
    10: ['island', 'branch', 'flute', 'piano'],
    11: [],
    12: ['dog']
}

# Put the lamp and the spoon into Box 0.
boxes[0].append('lamp')
boxes[0].append('spoon')

# Empty Box 5.
boxes[5] = []

# Replace the charger and the blender with the train and the drum in Box 1.
boxes[1].remove('charger')
boxes[1].remove('blender')
boxes[1].append('train')
boxes[1].append('drum')

# Put the microwave and the bicycle into Box 9.
boxes[9].append('microwave')
boxes[9].append('bicycle')

# Move the elephant and the comet from Box 2 to Box 3.
boxes[2].remove('elephant')
boxes[2].remove('comet')
boxes[3].append('elephant')
boxes[3].append('comet')

# Put the brush and the cat into Box 0.
boxes[0].append('brush')
boxes[0].append('cat')

# Move the card from Box 1 to Box 6.
boxes[1].remove('card')
boxes[6].append('card')

# Empty Box 6.
boxes[6] = []

# Swap the cow in Box 8 with the wallet in Box 2.
boxes[8].remove('cow')
boxes[2].remove('wallet')
boxes[8].append('wallet')
boxes[2].append('cow')

# Replace the violin and the elephant with the motorcycle and the controller in Box 3.
boxes[3].remove('violin')
boxes[3].remove('elephant')
boxes[3].append('motorcycle')
boxes[3].append('controller')

# Replace the cat and the shirt and the wallet with the wig and the lipstick and the jungle in Box 8.
boxes[8].remove('cat')
boxes[8].remove('shirt')
boxes[8].remove('wallet')
boxes[8].append('wig')
boxes[8].append('lipstick')
boxes[8].append('jungle')

# Put the grinder into Box 4.
boxes[4].append('grinder')

# Swap the cow in Box 2 with the dog in Box 12.
boxes[2].remove('cow')
boxes[12].remove('dog')
boxes[2].append('dog')
boxes[12].append('cow')

# Remove the branch from Box 10.
boxes[10].remove('branch')

# Move the note and the grinder and the toothbrush from Box 4 to Box 7.
boxes[4].remove('note')
boxes[4].remove('grinder')
boxes[4].remove('toothbrush')
boxes[7].append('note')
boxes[7].append('grinder')
boxes[7].append('toothbrush')

# Put the scissors into Box 5.
boxes[5].append('scissors')

# Replace the rocket with the tie in Box 4.
boxes[4].remove('rocket')
boxes[4].append('tie')

# Remove the dog from Box 2.
boxes[2].remove('dog')

# Swap the comet in Box 3 with the scissors in Box 5.
boxes[3].remove('comet')
boxes[5].remove('scissors')
boxes[3].append('scissors')
boxes[5].append('comet')

# Empty Box 10.
boxes[10] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")