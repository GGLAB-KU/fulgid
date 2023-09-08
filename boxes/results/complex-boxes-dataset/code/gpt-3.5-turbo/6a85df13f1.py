# Initial state of boxes
boxes = {
    0: ['clock', 'grass'],
    1: ['razor', 'ship', 'doll', 'lightning'],
    2: ['leaf', 'jacket'],
    3: [],
    4: ['shoe', 'glasses', 'belt'],
    5: ['shark'],
    6: ['scarf', 'rock', 'guitar', 'meteor', 'thread'],
    7: ['swimsuit', 'grinder', 'toy', 'cat'],
    8: ['train', 'forest', 'basket', 'rocket'],
    9: ['starfish', 'polish', 'beach', 'speaker', 'pan'],
    10: ['frame', 'earring', 'thunder']
}

# Move the leaf and the jacket from Box 2 to Box 3.
boxes[2].remove('leaf')
boxes[2].remove('jacket')
boxes[3].append('leaf')
boxes[3].append('jacket')

# Move the pan from Box 9 to Box 4.
boxes[9].remove('pan')
boxes[4].append('pan')

# Replace the forest with the truck in Box 8.
boxes[8].remove('forest')
boxes[8].append('truck')

# Remove the thread from Box 6.
boxes[6].remove('thread')

# Put the starfish and the cat into Box 2.
boxes[2].append('starfish')
boxes[2].append('cat')

# Move the meteor and the guitar from Box 6 to Box 3.
boxes[6].remove('meteor')
boxes[6].remove('guitar')
boxes[3].append('meteor')
boxes[3].append('guitar')

# Swap the shark in Box 5 with the leaf in Box 3.
boxes[5].remove('shark')
boxes[3].remove('leaf')
boxes[5].append('leaf')
boxes[3].append('shark')

# Swap the clock in Box 0 with the shark in Box 3.
boxes[0].remove('clock')
boxes[3].remove('shark')
boxes[0].append('shark')
boxes[3].append('clock')

# Put the lion and the paint and the harmonica into Box 9.
boxes[9].append('lion')
boxes[9].append('paint')
boxes[9].append('harmonica')

# Replace the polish and the beach with the bus and the controller in Box 9.
boxes[9].remove('polish')
boxes[9].remove('beach')
boxes[9].append('bus')
boxes[9].append('controller')

# Put the vase into Box 8.
boxes[8].append('vase')

# Empty Box 6.
boxes[6] = []

# Put the bear into Box 5.
boxes[5].append('bear')

# Put the swimsuit and the basket and the plate into Box 5.
boxes[7].remove('swimsuit')
boxes[8].remove('basket')
boxes[9].remove('plate')
boxes[5].append('swimsuit')
boxes[5].append('basket')
boxes[5].append('plate')

# Swap the earring in Box 10 with the shoe in Box 4.
boxes[10].remove('earring')
boxes[4].remove('shoe')
boxes[10].append('shoe')
boxes[4].append('earring')

# Move the clock from Box 3 to Box 4.
boxes[3].remove('clock')
boxes[4].append('clock')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")