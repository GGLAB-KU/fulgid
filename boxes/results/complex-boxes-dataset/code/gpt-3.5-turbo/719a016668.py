# Initial state of boxes
boxes = {
    0: ['lamp', 'shelf', 'motorcycle'],
    1: ['soap'],
    2: ['game', 'toy', 'wig'],
    3: [],
    4: ['moon', 'glasses', 'earring'],
    5: ['needle', 'dog', 'paint', 'blender', 'freezer'],
    6: ['keyboard', 'horse'],
    7: ['magnet', 'coral', 'whistle', 'wire', 'guitar'],
    8: ['seaweed', 'flower'],
    9: [],
    10: ['hat', 'cup', 'shoe', 'mask']
}

# Swap the soap in Box 1 with the keyboard in Box 6.
boxes[1].remove('soap')
boxes[6].remove('keyboard')
boxes[1].append('keyboard')
boxes[6].append('soap')

# Remove the blender and the paint and the freezer from Box 5.
items_to_remove = ['blender', 'paint', 'freezer']
for item in items_to_remove:
    boxes[5].remove(item)

# Move the flower and the seaweed from Box 8 to Box 5.
items_to_move = ['flower', 'seaweed']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[5].append(item)

# Swap the soap in Box 6 with the cup in Box 10.
boxes[6].remove('soap')
boxes[10].remove('cup')
boxes[6].append('cup')
boxes[10].append('soap')

# Put the ring into Box 8.
boxes[8].append('ring')

# Swap the game in Box 2 with the keyboard in Box 1.
boxes[2].remove('game')
boxes[1].remove('keyboard')
boxes[2].append('keyboard')
boxes[1].append('game')

# Swap the soap in Box 10 with the dog in Box 5.
boxes[10].remove('soap')
boxes[5].remove('dog')
boxes[10].append('dog')
boxes[5].append('soap')

# Swap the ring in Box 8 with the toy in Box 2.
boxes[8].remove('ring')
boxes[2].remove('toy')
boxes[8].append('toy')
boxes[2].append('ring')

# Swap the ring in Box 2 with the hat in Box 10.
boxes[2].remove('ring')
boxes[10].remove('hat')
boxes[2].append('hat')
boxes[10].append('ring')

# Replace the soap and the flower and the needle with the mirror and the earring and the doll in Box 5.
boxes[5].remove('soap')
boxes[5].remove('flower')
boxes[5].remove('needle')
boxes[5].append('mirror')
boxes[5].append('earring')
boxes[5].append('doll')

# Swap the toy in Box 8 with the cup in Box 6.
boxes[8].remove('toy')
boxes[6].remove('cup')
boxes[8].append('cup')
boxes[6].append('toy')

# Swap the dog in Box 10 with the seaweed in Box 5.
boxes[10].remove('dog')
boxes[5].remove('seaweed')
boxes[10].append('seaweed')
boxes[5].append('dog')

# Put the fridge into Box 10.
boxes[10].append('fridge')

# Replace the whistle and the guitar with the jungle and the piano in Box 7.
boxes[7].remove('whistle')
boxes[7].remove('guitar')
boxes[7].append('jungle')
boxes[7].append('piano')

# Replace the fridge and the mask and the ring with the scarf and the drum and the tree in Box 10.
boxes[10].remove('fridge')
boxes[10].remove('mask')
boxes[10].remove('ring')
boxes[10].append('scarf')
boxes[10].append('drum')
boxes[10].append('tree')

# Move the lamp and the motorcycle from Box 0 to Box 2.
items_to_move = ['lamp', 'motorcycle']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")