# Initial state of boxes
boxes = {
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

# Replace the whistle and the key and the dolphin with the microwave and the comb and the bag in Box 12.
boxes[12].remove('whistle')
boxes[12].remove('key')
boxes[12].remove('dolphin')
boxes[12].append('microwave')
boxes[12].append('comb')
boxes[12].append('bag')

# Remove the hat from Box 8.
boxes[8].remove('hat')

# Swap the tree in Box 14 with the clock in Box 6.
boxes[14].remove('tree')
boxes[6].remove('clock')
boxes[14].append('clock')
boxes[6].append('tree')

# Move the shelf from Box 5 to Box 6.
boxes[5].remove('shelf')
boxes[6].append('shelf')

# Remove the cloud from Box 1.
boxes[1].remove('cloud')

# Remove the microwave from Box 4.
boxes[4].remove('microwave')

# Remove the candle and the bicycle and the headphone from Box 10.
items_to_remove = ['candle', 'bicycle', 'headphone']
for item in items_to_remove:
    boxes[10].remove(item)

# Move the ocean and the keyboard and the horse from Box 8 to Box 6.
items_to_move = ['ocean', 'keyboard', 'horse']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[6].append(item)

# Swap the shoes in Box 1 with the bus in Box 2.
boxes[1].remove('shoes')
boxes[2].remove('bus')
boxes[1].append('bus')
boxes[2].append('shoes')

# Swap the ocean in Box 6 with the microwave in Box 12.
boxes[6].remove('ocean')
boxes[12].remove('microwave')
boxes[6].append('microwave')
boxes[12].append('ocean')

# Move the rocket from Box 9 to Box 13.
boxes[9].remove('rocket')
boxes[13].append('rocket')

# Put the pan into Box 10.
boxes[10].append('pan')

# Remove the rocket from Box 13.
boxes[13].remove('rocket')

# Swap the flower in Box 14 with the bus in Box 1.
boxes[14].remove('flower')
boxes[1].remove('bus')
boxes[14].append('bus')
boxes[1].append('flower')

# Empty Box 3.
boxes[3] = []

# Remove the pan from Box 10.
boxes[10].remove('pan')

# Replace the lipstick and the speaker with the fridge and the bowl in Box 0.
boxes[0].remove('lipstick')
boxes[0].remove('speaker')
boxes[0].append('fridge')
boxes[0].append('bowl')

# Move the bowl and the fridge from Box 0 to Box 4.
boxes[0].remove('bowl')
boxes[0].remove('fridge')
boxes[4].append('bowl')
boxes[4].append('fridge')

# Move the cat from Box 2 to Box 6.
boxes[2].remove('cat')
boxes[6].append('cat')

# Move the flower from Box 1 to Box 7.
boxes[1].remove('flower')
boxes[7].append('flower')

# Move the book from Box 2 to Box 6.
boxes[2].remove('book')
boxes[6].append('book')

# Move the guitar from Box 7 to Box 11.
boxes[7].remove('guitar')
boxes[11].append('guitar')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")