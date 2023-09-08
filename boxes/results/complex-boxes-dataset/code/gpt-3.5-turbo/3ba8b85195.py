# Initial state of boxes
boxes = {
    0: ['flute', 'card', 'snow', 'razor', 'toothpaste'],
    1: ['moon', 'shark', 'toaster', 'towel', 'helmet'],
    2: ['island', 'toothbrush', 'scissors', 'vase'],
    3: ['pen', 'sculpture', 'doll', 'bear'],
    4: ['candle', 'lion'],
    5: ['note', 'boot', 'forest', 'jungle', 'grinder'],
    6: ['fridge'],
    7: []
}

# Swap the fridge in Box 6 with the island in Box 2.
boxes[6], boxes[2] = boxes[2], boxes[6]

# Replace the candle with the shirt in Box 4.
boxes[4].remove('candle')
boxes[4].append('shirt')

# Replace the shirt and the lion with the fork and the needle in Box 4.
boxes[4].remove('shirt')
boxes[4].remove('lion')
boxes[4].append('fork')
boxes[4].append('needle')

# Move the note and the jungle from Box 5 to Box 7.
items_to_move = ['note', 'jungle']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[7].append(item)

# Put the wallet and the usb into Box 3.
boxes[3].append('wallet')
boxes[3].append('usb')

# Remove the vase from Box 2.
boxes[2].remove('vase')

# Put the octopus and the book and the grass into Box 5.
boxes[5].append('octopus')
boxes[5].append('book')
boxes[5].append('grass')

# Put the mask into Box 4.
boxes[4].append('mask')

# Remove the razor from Box 0.
boxes[0].remove('razor')

# Put the swimsuit and the phone and the zipper into Box 5.
boxes[5].append('swimsuit')
boxes[5].append('phone')
boxes[5].append('zipper')

# Remove the note and the jungle from Box 7.
boxes[7].remove('note')
boxes[7].remove('jungle')

# Swap the card in Box 0 with the towel in Box 1.
boxes[0], boxes[1] = boxes[1], boxes[0]

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")