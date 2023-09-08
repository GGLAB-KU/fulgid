# Initial state of boxes
boxes = {
    0: ['charger', 'coat', 'shoes', 'tape'],
    1: ['spoon', 'keyboard', 'belt'],
    2: ['helmet', 'ocean'],
    3: ['magnet'],
    4: ['needle', 'grass', 'hat', 'submarine', 'scissors'],
    5: [],
    6: ['card'],
    7: ['key', 'guitar'],
    8: [],
    9: ['planet'],
    10: ['cup', 'polish', 'storm'],
    11: ['mixer', 'whistle']
}

# Remove the hat and the needle from Box 4.
boxes[4].remove('hat')
boxes[4].remove('needle')

# Swap the cup in Box 10 with the card in Box 6.
boxes[10].remove('cup')
boxes[6].remove('card')
boxes[10].append('card')
boxes[6].append('cup')

# Move the belt and the keyboard from Box 1 to Box 2.
items_to_move = ['belt', 'keyboard']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Put the lipstick and the earring into Box 10.
boxes[10].append('lipstick')
boxes[10].append('earring')

# Remove the whistle from Box 11.
boxes[11].remove('whistle')

# Swap the mixer in Box 11 with the coat in Box 0.
boxes[11].remove('mixer')
boxes[0].remove('coat')
boxes[11].append('coat')
boxes[0].append('mixer')

# Put the fridge and the swimsuit into Box 0.
boxes[0].append('fridge')
boxes[0].append('swimsuit')

# Remove the planet from Box 9.
boxes[9].remove('planet')

# Swap the magnet in Box 3 with the coat in Box 11.
boxes[3].remove('magnet')
boxes[11].remove('coat')
boxes[3].append('coat')
boxes[11].append('magnet')

# Put the cup and the dolphin and the shirt into Box 5.
boxes[5].append('cup')
boxes[5].append('dolphin')
boxes[5].append('shirt')

# Remove the lipstick from Box 10.
boxes[10].remove('lipstick')

# Remove the coat from Box 3.
boxes[3].remove('coat')

# Remove the guitar from Box 7.
boxes[7].remove('guitar')

# Replace the scissors with the shark in Box 4.
boxes[4].remove('scissors')
boxes[4].append('shark')

# Remove the storm from Box 10.
boxes[10].remove('storm')

# Swap the card in Box 10 with the key in Box 7.
boxes[10].remove('card')
boxes[7].remove('key')
boxes[10].append('key')
boxes[7].append('card')

# Put the makeup into Box 9.
boxes[9].append('makeup')

# Move the polish and the key from Box 10 to Box 2.
items_to_move = ['polish', 'key']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")