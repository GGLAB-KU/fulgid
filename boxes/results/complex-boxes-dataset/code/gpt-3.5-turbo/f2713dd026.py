# Initial state of boxes
boxes = {
    0: [],
    1: ['towel', 'candle', 'lock', 'jacket', 'lightning'],
    2: ['doll', 'brush'],
    3: ['blanket', 'violin', 'ring'],
    4: [],
    5: ['console', 'pen', 'button', 'train', 'shark'],
    6: ['skirt', 'perfume', 'boat', 'pants', 'flute'],
    7: ['rock', 'spoon', 'tape', 'shoes'],
    8: ['whistle', 'elephant', 'puzzle', 'coin'],
    9: ['dog', 'speaker', 'tiger'],
    10: [],
    11: ['bag', 'sculpture'],
    12: [],
    13: ['shelf', 'apple', 'motorcycle'],
    14: ['submarine', 'makeup', 'grass', 'harmonica', 'wallet']
}

# Move the ring from Box 3 to Box 14.
boxes[3].remove('ring')
boxes[14].append('ring')

# Remove the brush from Box 2.
boxes[2].remove('brush')

# Move the pen and the shark from Box 5 to Box 14.
items_to_move = ['pen', 'shark']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[14].append(item)

# Put the vase into Box 4.
boxes[4].append('vase')

# Empty Box 11.
boxes[11] = []

# Put the pillow and the lock into Box 0.
boxes[0].append('pillow')
boxes[0].append('lock')

# Move the rock and the spoon and the tape from Box 7 to Box 11.
items_to_move = ['rock', 'spoon', 'tape']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[11].append(item)

# Swap the train in Box 5 with the flute in Box 6.
boxes[5].remove('train')
boxes[6].remove('flute')
boxes[5].append('flute')
boxes[6].append('train')

# Replace the vase with the bell in Box 4.
boxes[4].remove('vase')
boxes[4].append('bell')

# Move the coin from Box 8 to Box 3.
boxes[8].remove('coin')
boxes[3].append('coin')

# Move the bell from Box 4 to Box 9.
boxes[4].remove('bell')
boxes[9].append('bell')

# Remove the candle from Box 1.
boxes[1].remove('candle')

# Move the shelf and the apple and the motorcycle from Box 13 to Box 14.
items_to_move = ['shelf', 'apple', 'motorcycle']
for item in items_to_move:
    boxes[13].remove(item)
    boxes[14].append(item)

# Replace the shoes with the lipstick in Box 7.
boxes[7].remove('shoes')
boxes[7].append('lipstick')

# Move the doll from Box 2 to Box 10.
boxes[2].remove('doll')
boxes[10].append('doll')

# Empty Box 14.
boxes[14] = []

# Remove the console and the flute from Box 5.
boxes[5].remove('console')
boxes[5].remove('flute')

# Put the frame and the sock into Box 11.
boxes[11].append('frame')
boxes[11].append('sock')

# Move the elephant from Box 8 to Box 5.
boxes[8].remove('elephant')
boxes[5].append('elephant')

# Replace the button and the elephant with the necklace and the keyboard in Box 5.
boxes[5].remove('button')
boxes[5].remove('elephant')
boxes[5].append('necklace')
boxes[5].append('keyboard')

# Swap the puzzle in Box 8 with the tiger in Box 9.
boxes[8].remove('puzzle')
boxes[9].remove('tiger')
boxes[8].append('tiger')
boxes[9].append('puzzle')

# Replace the doll with the sculpture in Box 10.
boxes[10].remove('doll')
boxes[10].append('sculpture')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")