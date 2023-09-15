box = {
    0: ['swimsuit', 'harmonica'],
    1: ['earring', 'bird'],
    2: ['lipstick'],
    3: ['game', 'vase', 'violin', 'phone', 'zipper'],
    4: ['clock', 'coin'],
    5: ['plate'],
    6: ['note', 'chair'],
    7: [],
    8: ['shark', 'polish', 'console', 'oven'],
    9: [],
    10: ['train'],
    11: ['thread'],
    12: ['shoes'],
    13: ['rain', 'cow', 'guitar', 'snow', 'needle']
}

# Remove the console from Box 8
box[8].remove('console')

# Replace the bird with the rocket in Box 1
box[1].remove('bird')
box[1].append('rocket')

# Move the violin and the vase from Box 3 to Box 8
box[8].extend(box[3].pop(box[3].index('violin')))
box[8].extend(box[3].pop(box[3].index('vase')))

# Move the train from Box 10 to Box 8
box[8].extend(box[10].pop(box[10].index('train')))

# Remove the chair from Box 6
box[6].remove('chair')

# Replace the lipstick with the earring in Box 2
box[2].remove('lipstick')
box[2].append('earring')

# Move the needle from Box 13 to Box 7
box[7].extend(box[13].pop(box[13].index('needle')))

# Remove the plate from Box 5
box[5].remove('plate')

# Swap the phone in Box 3 with the earring in Box 2
box[3].remove('phone')
box[3].append('earring')
box[2].remove('earring')
box[2].append('phone')

# Swap the harmonica in Box 0 with the violin in Box 8
box[0].remove('harmonica')
box[0].append('violin')
box[8].remove('violin')
box[8].append('harmonica')

# Remove the rocket and the earring from Box 1
box[1].remove('rocket')
box[1].remove('earring')

# Swap the clock in Box 4 with the rain in Box 13
box[4].remove('clock')
box[4].append('rain')
box[13].remove('rain')
box[13].append('clock')

# Replace the shoes with the fish in Box 12
box[12].remove('shoes')
box[12].append('fish')

# Put the train into Box 12
box[12].append('train')

# Replace the guitar and the cow with the coat and the glove in Box 13
box[13].remove('guitar')
box[13].remove('cow')
box[13].append('coat')
box[13].append('glove')

# Move the violin from Box 0 to Box 10
box[10].append(box[0].pop(box[0].index('violin')))

# Replace the needle with the toaster in Box 7
box[7].remove('needle')
box[7].append('toaster')

# Swap the thread in Box 11 with the polish in Box 8
box[11].remove('thread')
box[11].append('polish')
box[8].remove('polish')
box[8].append('thread')

# Put the dress and the earring into Box 6
box[6].append('dress')
box[6].append('earring')

# Replace the violin with the wallet in Box 10
box[10].remove('violin')
box[10].append('wallet')

# Put the whistle and the drum into Box 5
box[5].append('whistle')
box[5].append('drum')

# Print the contents of each box
for i in range(14):
    print(f"Box {i}: {box[i]}")