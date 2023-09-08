# Initial state of boxes
boxes = {
    0: ['grass', 'leaf', 'thread'],
    1: [],
    2: ['dog', 'needle', 'zipper', 'river'],
    3: ['comet', 'note'],
    4: ['tiger', 'toothpaste', 'perfume'],
    5: ['blender'],
    6: ['toothbrush', 'candle', 'card', 'harmonica'],
    7: ['vase', 'ship', 'apple', 'submarine'],
    8: ['coat', 'key'],
    9: ['razor', 'scarf', 'hat'],
    10: ['boat', 'mask', 'rain', 'shorts', 'planet'],
    11: ['shoe', 'sculpture'],
    12: []
}

# Replace the sculpture with the shampoo in Box 11.
boxes[11].remove('sculpture')
boxes[11].append('shampoo')

# Replace the comet and the note with the jungle and the comb in Box 3.
boxes[3].remove('comet')
boxes[3].remove('note')
boxes[3].append('jungle')
boxes[3].append('comb')

# Remove the key and the coat from Box 8.
boxes[8].remove('key')
boxes[8].remove('coat')

# Move the shampoo from Box 11 to Box 3.
boxes[11].remove('shampoo')
boxes[3].append('shampoo')

# Remove the needle and the dog from Box 2.
boxes[2].remove('needle')
boxes[2].remove('dog')

# Replace the tiger with the glasses in Box 4.
boxes[4].remove('tiger')
boxes[4].append('glasses')

# Replace the scarf and the hat with the snow and the octopus in Box 9.
boxes[9].remove('scarf')
boxes[9].remove('hat')
boxes[9].append('snow')
boxes[9].append('octopus')

# Swap the shorts in Box 10 with the card in Box 6.
boxes[10].remove('shorts')
boxes[6].remove('card')
boxes[10].append('card')
boxes[6].append('shorts')

# Replace the leaf with the pan in Box 0.
boxes[0].remove('leaf')
boxes[0].append('pan')

# Empty Box 11.
boxes[11] = []

# Put the towel and the toy and the horse into Box 11.
boxes[11].extend(['towel', 'toy', 'horse'])

# Move the candle and the shorts and the toothbrush from Box 6 to Box 10.
items_to_move = ['candle', 'shorts', 'toothbrush']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[10].append(item)

# Replace the octopus and the razor and the snow with the beach and the tree and the moon in Box 9.
boxes[9].remove('octopus')
boxes[9].remove('razor')
boxes[9].remove('snow')
boxes[9].append('beach')
boxes[9].append('tree')
boxes[9].append('moon')

# Swap the towel in Box 11 with the vase in Box 7.
boxes[11].remove('towel')
boxes[7].remove('vase')
boxes[11].append('vase')
boxes[7].append('towel')

# Put the seaweed into Box 8.
boxes[8].append('seaweed')

# Replace the river and the zipper with the bicycle and the cup in Box 2.
boxes[2].remove('river')
boxes[2].remove('zipper')
boxes[2].append('bicycle')
boxes[2].append('cup')

# Move the harmonica from Box 6 to Box 7.
boxes[6].remove('harmonica')
boxes[7].append('harmonica')

# Put the dress and the pants and the moon into Box 12.
boxes[12].extend(['dress', 'pants', 'moon'])

# Swap the shampoo in Box 3 with the card in Box 10.
boxes[3].remove('shampoo')
boxes[10].remove('card')
boxes[3].append('card')
boxes[10].append('shampoo')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")