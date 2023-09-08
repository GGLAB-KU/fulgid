# Initial state of boxes
boxes = {
    0: ['towel'],
    1: ['candle', 'fork'],
    2: ['makeup', 'whistle'],
    3: ['card', 'grinder'],
    4: ['comb'],
    5: ['mask', 'coat', 'bus'],
    6: [],
    7: ['magnet', 'mountain', 'mixer', 'zipper', 'tape'],
    8: ['razor']
}

# Replace the grinder with the sculpture in Box 3.
boxes[3].remove('grinder')
boxes[3].append('sculpture')

# Remove the towel from Box 0.
boxes[0].remove('towel')

# Empty Box 3.
boxes[3] = []

# Move the mountain and the magnet from Box 7 to Box 8.
items_to_move = ['mountain', 'magnet']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[8].append(item)

# Put the chair and the jungle and the fridge into Box 4.
items_to_move = ['chair', 'jungle', 'fridge']
for item in items_to_move:
    boxes[4].append(item)

# Swap the comb in Box 4 with the coat in Box 5.
boxes[4].remove('comb')
boxes[5].remove('coat')
boxes[4].append('coat')
boxes[5].append('comb')

# Remove the comb and the mask and the bus from Box 5.
items_to_remove = ['comb', 'mask', 'bus']
for item in items_to_remove:
    boxes[5].remove(item)

# Swap the candle in Box 1 with the whistle in Box 2.
boxes[1].remove('candle')
boxes[2].remove('whistle')
boxes[1].append('whistle')
boxes[2].append('candle')

# Empty Box 8.
boxes[8] = []

# Replace the mixer and the tape and the zipper with the dolphin and the towel and the island in Box 7.
boxes[7].remove('mixer')
boxes[7].remove('tape')
boxes[7].remove('zipper')
boxes[7].append('dolphin')
boxes[7].append('towel')
boxes[7].append('island')

# Replace the towel with the jacket in Box 7.
boxes[7].remove('towel')
boxes[7].append('jacket')

# Move the makeup from Box 2 to Box 8.
boxes[2].remove('makeup')
boxes[8].append('makeup')

# Remove the candle from Box 2.
boxes[2].remove('candle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")