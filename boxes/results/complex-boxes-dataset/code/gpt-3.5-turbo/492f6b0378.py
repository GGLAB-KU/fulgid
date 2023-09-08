# Initial state of boxes
boxes = {
    0: ['bell'],
    1: ['tape', 'sandals', 'branch', 'pan', 'puzzle'],
    2: ['watch', 'snow', 'lipstick', 'shark'],
    3: ['coat', 'hat', 'whistle', 'horse'],
    4: ['perfume', 'table', 'submarine', 'dolphin'],
    5: ['shoes', 'blender', 'meteor', 'fish', 'grass'],
    6: ['lamp', 'seaweed', 'glasses', 'console'],
    7: ['rocket', 'rain'],
    8: ['skirt', 'moon', 'dog'],
    9: ['crown'],
    10: [],
    11: ['coin', 'magnet', 'game', 'dress', 'shirt'],
    12: ['swimsuit', 'tiger'],
    13: ['spoon', 'violin', 'scissors', 'horn']
}

# Move the moon and the dog from Box 8 to Box 6.
boxes[8].remove('moon')
boxes[8].remove('dog')
boxes[6].append('moon')
boxes[6].append('dog')

# Move the swimsuit and the tiger from Box 12 to Box 9.
boxes[12].remove('swimsuit')
boxes[12].remove('tiger')
boxes[9].append('swimsuit')
boxes[9].append('tiger')

# Swap the skirt in Box 8 with the shark in Box 2.
boxes[8].remove('skirt')
boxes[2].remove('shark')
boxes[8].append('shark')
boxes[2].append('skirt')

# Remove the rocket from Box 7.
boxes[7].remove('rocket')

# Move the tiger and the crown from Box 9 to Box 4.
boxes[9].remove('tiger')
boxes[9].remove('crown')
boxes[4].append('tiger')
boxes[4].append('crown')

# Swap the rain in Box 7 with the bell in Box 0.
boxes[7].remove('rain')
boxes[0].remove('bell')
boxes[7].append('bell')
boxes[0].append('rain')

# Move the rain from Box 0 to Box 8.
boxes[0].remove('rain')
boxes[8].append('rain')

# Replace the dolphin and the table and the perfume with the thunder and the sun and the jacket in Box 4.
boxes[4].remove('dolphin')
boxes[4].remove('table')
boxes[4].remove('perfume')
boxes[4].append('thunder')
boxes[4].append('sun')
boxes[4].append('jacket')

# Swap the sandals in Box 1 with the hat in Box 3.
boxes[1].remove('sandals')
boxes[3].remove('hat')
boxes[1].append('hat')
boxes[3].append('sandals')

# Remove the spoon and the scissors and the violin from Box 13.
boxes[13].remove('spoon')
boxes[13].remove('scissors')
boxes[13].remove('violin')

# Move the fish and the blender and the shoes from Box 5 to Box 12.
boxes[5].remove('fish')
boxes[5].remove('blender')
boxes[5].remove('shoes')
boxes[12].append('fish')
boxes[12].append('blender')
boxes[12].append('shoes')

# Put the skirt and the fish into Box 4.
boxes[8].remove('skirt')
boxes[12].remove('fish')
boxes[4].append('skirt')
boxes[4].append('fish')

# Replace the grass with the branch in Box 5.
boxes[5].remove('grass')
boxes[5].append('branch')

# Remove the dog from Box 6.
boxes[6].remove('dog')

# Replace the horn with the storm in Box 13.
boxes[13].remove('horn')
boxes[13].append('storm')

# Put the hat and the toothpaste into Box 10.
boxes[3].remove('hat')
boxes[10].append('hat')
boxes[10].append('toothpaste')

# Put the leaf and the game into Box 6.
boxes[6].append('leaf')
boxes[11].remove('game')
boxes[6].append('game')

# Empty Box 6.
boxes[6] = []

# Remove the fish and the crown from Box 4.
boxes[4].remove('fish')
boxes[4].remove('crown')

# Replace the whistle and the coat with the watch and the sun in Box 3.
boxes[3].remove('whistle')
boxes[3].remove('coat')
boxes[3].append('watch')
boxes[3].append('sun')

# Put the doll and the book into Box 4.
boxes[11].remove('doll')
boxes[11].remove('book')
boxes[4].append('doll')
boxes[4].append('book')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")