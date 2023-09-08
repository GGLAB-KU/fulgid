# Initial state of boxes
boxes = {
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

# Remove the console from Box 8.
boxes[8].remove('console')

# Replace the bird with the rocket in Box 1.
boxes[1].remove('bird')
boxes[1].append('rocket')

# Move the violin and the vase from Box 3 to Box 8.
items_to_move = ['violin', 'vase']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[8].append(item)

# Move the train from Box 10 to Box 8.
boxes[10].remove('train')
boxes[8].append('train')

# Remove the chair from Box 6.
boxes[6].remove('chair')

# Replace the lipstick with the earring in Box 2.
boxes[2].remove('lipstick')
boxes[2].append('earring')

# Move the needle from Box 13 to Box 7.
boxes[13].remove('needle')
boxes[7].append('needle')

# Remove the plate from Box 5.
boxes[5].remove('plate')

# Swap the phone in Box 3 with the earring in Box 2.
boxes[3].remove('phone')
boxes[2].remove('earring')
boxes[3].append('earring')
boxes[2].append('phone')

# Swap the harmonica in Box 0 with the violin in Box 8.
boxes[0].remove('harmonica')
boxes[8].remove('violin')
boxes[0].append('violin')
boxes[8].append('harmonica')

# Remove the rocket and the earring from Box 1.
boxes[1].remove('rocket')
boxes[1].remove('earring')

# Swap the clock in Box 4 with the rain in Box 13.
boxes[4].remove('clock')
boxes[13].remove('rain')
boxes[4].append('rain')
boxes[13].append('clock')

# Replace the shoes with the fish in Box 12.
boxes[12].remove('shoes')
boxes[12].append('fish')

# Put the train into Box 12.
boxes[12].append('train')

# Replace the guitar and the cow with the coat and the glove in Box 13.
boxes[13].remove('guitar')
boxes[13].remove('cow')
boxes[13].append('coat')
boxes[13].append('glove')

# Move the violin from Box 0 to Box 10.
boxes[0].remove('violin')
boxes[10].append('violin')

# Replace the needle with the toaster in Box 7.
boxes[7].remove('needle')
boxes[7].append('toaster')

# Swap the thread in Box 11 with the polish in Box 8.
boxes[11].remove('thread')
boxes[8].remove('polish')
boxes[11].append('polish')
boxes[8].append('thread')

# Put the dress and the earring into Box 6.
boxes[6].append('dress')
boxes[6].append('earring')

# Replace the violin with the wallet in Box 10.
boxes[10].remove('violin')
boxes[10].append('wallet')

# Put the whistle and the drum into Box 5.
boxes[5].append('whistle')
boxes[5].append('drum')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")