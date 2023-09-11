# Initial state of boxes
boxes = {
    0: ['cow', 'beach'],
    1: ['pants'],
    2: ['clock', 'coat', 'shark', 'note'],
    3: ['ocean', 'coin', 'toy'],
    4: ['sun', 'makeup', 'magnet']
}

# Remove the coin and the ocean and the toy from Box 3.
boxes[3].remove('coin')
boxes[3].remove('ocean')
boxes[3].remove('toy')

# Move the pants from Box 1 to Box 3.
boxes[1].remove('pants')
boxes[3].append('pants')

# Replace the clock and the note and the shark with the dolphin and the soap and the battery in Box 2.
boxes[2].remove('clock')
boxes[2].remove('note')
boxes[2].remove('shark')
boxes[2].append('dolphin')
boxes[2].append('soap')
boxes[2].append('battery')

# Replace the coat and the dolphin and the battery with the needle and the game and the oven in Box 2.
boxes[2].remove('coat')
boxes[2].remove('dolphin')
boxes[2].remove('battery')
boxes[2].append('needle')
boxes[2].append('game')
boxes[2].append('oven')

# Move the pants from Box 3 to Box 4.
boxes[3].remove('pants')
boxes[4].append('pants')

# Swap the magnet in Box 4 with the beach in Box 0.
boxes[4].remove('magnet')
boxes[0].remove('beach')
boxes[4].append('beach')
boxes[0].append('magnet')

# Remove the beach and the makeup and the pants from Box 4.
boxes[4].remove('beach')
boxes[4].remove('makeup')
boxes[4].remove('pants')

# Remove the sun from Box 4.
boxes[4].remove('sun')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")