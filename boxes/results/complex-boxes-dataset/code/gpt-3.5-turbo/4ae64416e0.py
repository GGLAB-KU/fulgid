# Initial state of boxes
boxes = {
    0: ['boat', 'hat'],
    1: [],
    2: ['paint', 'earring'],
    3: ['scarf', 'pen'],
    4: ['horse'],
    5: ['battery', 'motorcycle', 'oven', 'star', 'piano'],
    6: ['shampoo'],
    7: [],
    8: ['scissors', 'river', 'wallet', 'bicycle'],
    9: ['grinder', 'rain', 'mountain', 'guitar', 'toothbrush'],
    10: ['planet'],
    11: ['chair', 'jungle', 'thunder', 'zipper', 'snow'],
    12: ['meteor', 'comb', 'candle'],
    13: []
}

# Move the earring and the paint from Box 2 to Box 1.
boxes[2].remove('earring')
boxes[2].remove('paint')
boxes[1].append('earring')
boxes[1].append('paint')

# Replace the guitar and the mountain with the microwave and the sock in Box 9.
boxes[9].remove('guitar')
boxes[9].remove('mountain')
boxes[9].append('microwave')
boxes[9].append('sock')

# Remove the earring from Box 1.
boxes[1].remove('earring')

# Swap the hat in Box 0 with the planet in Box 10.
boxes[0].remove('hat')
boxes[10].remove('planet')
boxes[0].append('planet')
boxes[10].append('hat')

# Remove the paint from Box 1.
boxes[1].remove('paint')

# Remove the scarf from Box 3.
boxes[3].remove('scarf')

# Replace the meteor and the comb with the pen and the oven in Box 12.
boxes[12].remove('meteor')
boxes[12].remove('comb')
boxes[12].append('pen')
boxes[12].append('oven')

# Replace the rain and the toothbrush and the grinder with the spoon and the makeup and the earring in Box 9.
boxes[9].remove('rain')
boxes[9].remove('toothbrush')
boxes[9].remove('grinder')
boxes[9].append('spoon')
boxes[9].append('makeup')
boxes[9].append('earring')

# Put the gloves and the polish and the spoon into Box 4.
items_to_move = ['gloves', 'polish', 'spoon']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Put the beach and the pants into Box 8.
items_to_move = ['beach', 'pants']
for item in items_to_move:
    boxes[8].append(item)

# Swap the jungle in Box 11 with the scissors in Box 8.
boxes[11].remove('jungle')
boxes[8].remove('scissors')
boxes[11].append('scissors')
boxes[8].append('jungle')

# Replace the earring and the spoon and the makeup with the train and the flute and the seaweed in Box 9.
boxes[9].remove('earring')
boxes[9].remove('spoon')
boxes[9].remove('makeup')
boxes[9].append('train')
boxes[9].append('flute')
boxes[9].append('seaweed')

# Remove the hat from Box 10.
boxes[10].remove('hat')

# Swap the planet in Box 0 with the zipper in Box 11.
boxes[0].remove('planet')
boxes[11].remove('zipper')
boxes[0].append('zipper')
boxes[11].append('planet')

# Replace the snow with the guitar in Box 11.
boxes[11].remove('snow')
boxes[11].append('guitar')

# Move the boat from Box 0 to Box 5.
boxes[0].remove('boat')
boxes[5].append('boat')

# Swap the shampoo in Box 6 with the zipper in Box 0.
boxes[6].remove('shampoo')
boxes[0].remove('zipper')
boxes[6].append('zipper')
boxes[0].append('shampoo')

# Replace the thunder and the planet with the river and the scarf in Box 11.
boxes[11].remove('thunder')
boxes[11].remove('planet')
boxes[11].append('river')
boxes[11].append('scarf')

# Replace the shampoo with the toy in Box 0.
boxes[0].remove('shampoo')
boxes[0].append('toy')

# Replace the pen with the ocean in Box 3.
boxes[3].remove('pen')
boxes[3].append('ocean')

# Replace the toy with the gloves in Box 0.
boxes[0].remove('toy')
boxes[0].append('gloves')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")