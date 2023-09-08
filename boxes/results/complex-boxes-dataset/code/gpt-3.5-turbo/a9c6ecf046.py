# Initial state of boxes
boxes = {
    0: ['rock', 'candle'],
    1: ['lipstick', 'fork'],
    2: ['tie', 'hat', 'shoe', 'sandals', 'spoon'],
    3: ['polish'],
    4: [],
    5: ['cup', 'submarine', 'bicycle'],
    6: ['dice'],
    7: ['shorts', 'apple', 'usb'],
    8: ['fridge', 'river'],
    9: ['tree', 'speaker', 'keyboard', 'shirt', 'sun'],
    10: ['star', 'dolphin', 'storm'],
    11: [],
    12: ['sculpture'],
    13: ['lock', 'island'],
    14: ['wire', 'thunder', 'flower']
}

# Replace the rock with the whistle in Box 0.
boxes[0].remove('rock')
boxes[0].append('whistle')

# Put the lightning and the tiger into Box 7.
boxes[7].append('lightning')
boxes[7].append('tiger')

# Remove the sun and the speaker from Box 9.
boxes[9].remove('sun')
boxes[9].remove('speaker')

# Replace the polish with the thunder in Box 3.
boxes[3].remove('polish')
boxes[3].append('thunder')

# Put the train and the dice into Box 9.
boxes[9].append('train')
boxes[9].append('dice')

# Move the tiger from Box 7 to Box 2.
boxes[7].remove('tiger')
boxes[2].append('tiger')

# Swap the lightning in Box 7 with the thunder in Box 3.
boxes[7].remove('lightning')
boxes[3].remove('thunder')
boxes[7].append('thunder')
boxes[3].append('lightning')

# Move the dolphin and the star and the storm from Box 10 to Box 3.
items_to_move = ['dolphin', 'star', 'storm']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[3].append(item)

# Remove the tree and the shirt from Box 9.
boxes[9].remove('tree')
boxes[9].remove('shirt')

# Replace the keyboard and the train and the dice with the grass and the grinder and the swimsuit in Box 9.
boxes[9].remove('keyboard')
boxes[9].remove('train')
boxes[9].remove('dice')
boxes[9].append('grass')
boxes[9].append('grinder')
boxes[9].append('swimsuit')

# Put the violin and the headphone into Box 5.
boxes[5].append('violin')
boxes[5].append('headphone')

# Put the toothpaste into Box 12.
boxes[12].append('toothpaste')

# Swap the dice in Box 6 with the whistle in Box 0.
boxes[6].remove('dice')
boxes[0].remove('whistle')
boxes[6].append('whistle')
boxes[0].append('dice')

# Move the lipstick from Box 1 to Box 10.
boxes[1].remove('lipstick')
boxes[10].append('lipstick')

# Replace the lock with the note in Box 13.
boxes[13].remove('lock')
boxes[13].append('note')

# Move the candle from Box 0 to Box 1.
boxes[0].remove('candle')
boxes[1].append('candle')

# Put the towel and the razor and the game into Box 13.
boxes[13].append('towel')
boxes[13].append('razor')
boxes[13].append('game')

# Remove the submarine and the headphone from Box 5.
boxes[5].remove('submarine')
boxes[5].remove('headphone')

# Move the thunder and the apple from Box 7 to Box 12.
boxes[7].remove('thunder')
boxes[7].remove('apple')
boxes[12].append('thunder')
boxes[12].append('apple')

# Replace the lipstick with the thunder in Box 10.
boxes[10].remove('lipstick')
boxes[10].append('thunder')

# Empty Box 13.
boxes[13] = []

# Put the ocean and the towel into Box 4.
boxes[4].append('ocean')
boxes[4].append('towel')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")