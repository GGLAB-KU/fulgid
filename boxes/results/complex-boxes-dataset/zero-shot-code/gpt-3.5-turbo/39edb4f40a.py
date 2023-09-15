box = {
    0: ['speaker', 'lipstick'],
    1: ['cloud', 'shoes'],
    2: ['cat', 'freezer', 'desert', 'bus', 'book'],
    3: ['horn', 'button', 'pen'],
    4: ['microwave'],
    5: ['shelf'],
    6: ['clock', 'apple', 'puzzle'],
    7: ['toy', 'river', 'guitar'],
    8: ['hat', 'keyboard', 'horse', 'ocean'],
    9: ['rocket'],
    10: ['headphone', 'candle', 'bicycle'],
    11: [],
    12: ['whistle', 'key', 'dolphin'],
    13: [],
    14: ['toaster', 'train', 'tree', 'flower', 'branch']
}

# Replace the whistle and the key and the dolphin with the microwave and the comb and the bag in Box 12
box[12] = ['microwave', 'comb', 'bag']

# Remove the hat from Box 8
box[8].remove('hat')

# Swap the tree in Box 14 with the clock in Box 6
box[14].remove('tree')
box[6].remove('clock')
box[14].append('clock')
box[6].append('tree')

# Move the shelf from Box 5 to Box 6
box[5].remove('shelf')
box[6].append('shelf')

# Remove the cloud from Box 1
box[1].remove('cloud')

# Remove the microwave from Box 4
box[4].remove('microwave')

# Remove the candle and the bicycle and the headphone from Box 10
box[10].remove('candle')
box[10].remove('bicycle')
box[10].remove('headphone')

# Move the ocean and the keyboard and the horse from Box 8 to Box 6
box[8].remove('ocean')
box[8].remove('keyboard')
box[8].remove('horse')
box[6].extend(['ocean', 'keyboard', 'horse'])

# Swap the shoes in Box 1 with the bus in Box 2
box[1].remove('shoes')
box[2].remove('bus')
box[1].append('bus')
box[2].append('shoes')

# Swap the ocean in Box 6 with the microwave in Box 12
box[6].remove('ocean')
box[12].remove('microwave')
box[6].append('microwave')
box[12].append('ocean')

# Move the rocket from Box 9 to Box 13
box[9].remove('rocket')
box[13].append('rocket')

# Put the pan into Box 10
box[10].append('pan')

# Remove the rocket from Box 13
box[13].remove('rocket')

# Swap the flower in Box 14 with the bus in Box 1
box[14].remove('flower')
box[1].remove('bus')
box[14].append('bus')
box[1].append('flower')

# Empty Box 3
box[3] = []

# Remove the pan from Box 10
box[10].remove('pan')

# Replace the lipstick and the speaker with the fridge and the bowl in Box 0
box[0] = ['fridge', 'bowl']

# Move the bowl and the fridge from Box 0 to Box 4
box[0].remove('bowl')
box[0].remove('fridge')
box[4].extend(['bowl', 'fridge'])

# Move the cat from Box 2 to Box 6
box[2].remove('cat')
box[6].append('cat')

# Move the flower from Box 1 to Box 7
box[1].remove('flower')
box[7].append('flower')

# Move the book from Box 2 to Box 6
box[2].remove('book')
box[6].append('book')

# Move the guitar from Box 7 to Box 11
box[7].remove('guitar')
box[11].append('guitar')

# Print the contents of each box
for i in range(15):
    print(f"Box {i}: {box[i]}")