box = {
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

# Put the moon into Box 0
box[0].append('moon')

# Remove the pen and the horse and the console from Box 8
box[8].remove('pen')
box[8].remove('horse')
box[8].remove('console')

# Move the brush and the moon from Box 0 to Box 3
box[3].extend(box[0])
box[0] = []

# Swap the bicycle in Box 2 with the moon in Box 9
box[2], box[9] = box[9], box[2]

# Replace the moon and the brush and the game with the shoe and the flute and the apple in Box 3
box[3].remove('moon')
box[3].remove('brush')
box[3].remove('game')
box[3].extend(['shoe', 'flute', 'apple'])

# Remove the magnet from Box 6
box[6] = []

# Put the shampoo and the mirror and the toy into Box 9
box[9].extend(['shampoo', 'mirror', 'toy'])

# Replace the moon and the grass with the comb and the bell in Box 2
box[2].remove('moon')
box[2].remove('grass')
box[2].extend(['comb', 'bell'])

# Swap the dog in Box 5 with the fridge in Box 9
box[5], box[9] = box[9], box[5]

# Remove the lipstick and the shampoo and the toy from Box 9
box[9].remove('lipstick')
box[9].remove('shampoo')
box[9].remove('toy')

# Replace the fridge with the jungle in Box 5
box[5] = ['jungle']

# Remove the bicycle and the dog from Box 9
box[9] = []

# Put the shark into Box 8
box[8].append('shark')

# Remove the thunder from Box 10
box[10].remove('thunder')

# Empty Box 8
box[8] = []

# Swap the bell in Box 2 with the jungle in Box 5
box[2], box[5] = box[5], box[2]

# Put the sandals and the sculpture into Box 9
box[9].extend(['sandals', 'sculpture'])

# Put the train and the glasses into Box 2
box[2].extend(['train', 'glasses'])

# Print the contents of each box
for i in range(12):
    print(f"Box {i}: {box[i]}")