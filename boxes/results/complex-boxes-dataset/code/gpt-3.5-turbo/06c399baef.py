# Initial state of boxes
boxes = {
    0: ['brush'],
    1: [],
    2: ['bicycle', 'shark', 'grass'],
    3: ['harmonica', 'fork', 'game', 'sock', 'lamp'],
    4: ['flower', 'key', 'leaf'],
    5: ['dog'],
    6: ['magnet'],
    7: [],
    8: ['pen', 'horse', 'console'],
    9: ['fridge', 'lipstick', 'moon'],
    10: ['thunder', 'battery'],
    11: []
}

# Put the moon into Box 0.
boxes[0].append('moon')

# Remove the pen and the horse and the console from Box 8.
boxes[8].remove('pen')
boxes[8].remove('horse')
boxes[8].remove('console')

# Move the brush and the moon from Box 0 to Box 3.
boxes[0].remove('brush')
boxes[0].remove('moon')
boxes[3].append('brush')
boxes[3].append('moon')

# Swap the bicycle in Box 2 with the moon in Box 9.
boxes[2].remove('bicycle')
boxes[9].remove('moon')
boxes[2].append('moon')
boxes[9].append('bicycle')

# Replace the moon and the brush and the game with the shoe and the flute and the apple in Box 3.
boxes[3].remove('moon')
boxes[3].remove('brush')
boxes[3].remove('game')
boxes[3].append('shoe')
boxes[3].append('flute')
boxes[3].append('apple')

# Remove the magnet from Box 6.
boxes[6].remove('magnet')

# Put the shampoo and the mirror and the toy into Box 9.
boxes[9].append('shampoo')
boxes[9].append('mirror')
boxes[9].append('toy')

# Replace the moon and the grass with the comb and the bell in Box 2.
boxes[2].remove('moon')
boxes[2].remove('grass')
boxes[2].append('comb')
boxes[2].append('bell')

# Swap the dog in Box 5 with the fridge in Box 9.
boxes[5].remove('dog')
boxes[9].remove('fridge')
boxes[5].append('fridge')
boxes[9].append('dog')

# Remove the lipstick and the shampoo and the toy from Box 9.
boxes[9].remove('lipstick')
boxes[9].remove('shampoo')
boxes[9].remove('toy')

# Replace the fridge with the jungle in Box 5.
boxes[5].remove('fridge')
boxes[5].append('jungle')

# Remove the bicycle and the dog from Box 9.
boxes[9].remove('bicycle')
boxes[9].remove('dog')

# Put the shark into Box 8.
boxes[8].append('shark')

# Remove the thunder from Box 10.
boxes[10].remove('thunder')

# Empty Box 8.
boxes[8] = []

# Swap the bell in Box 2 with the jungle in Box 5.
boxes[2].remove('bell')
boxes[5].remove('jungle')
boxes[2].append('jungle')
boxes[5].append('bell')

# Put the sandals and the sculpture into Box 9.
boxes[9].append('sandals')
boxes[9].append('sculpture')

# Put the train and the glasses into Box 2.
boxes[2].append('train')
boxes[2].append('glasses')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")