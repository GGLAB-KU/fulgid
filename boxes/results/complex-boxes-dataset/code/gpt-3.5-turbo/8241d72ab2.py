# Initial state of boxes
boxes = {
    0: ['toothpaste', 'charger', 'toothbrush', 'coin', 'scarf'],
    1: ['umbrella', 'ship', 'zipper'],
    2: ['belt'],
    3: ['train', 'pants', 'mask', 'bus'],
    4: [],
    5: ['storm', 'butterfly'],
    6: ['mixer', 'rock', 'car'],
    7: ['scissors'],
    8: ['sandals', 'watch'],
    9: ['pen', 'freezer', 'shelf'],
    10: [],
    11: ['console'],
    12: ['controller', 'phone'],
    13: ['shoes']
}

# Replace the console with the rocket in Box 11.
boxes[11].remove('console')
boxes[11].append('rocket')

# Swap the toothbrush in Box 0 with the controller in Box 12.
boxes[0].remove('toothbrush')
boxes[12].remove('controller')
boxes[0].append('controller')
boxes[12].append('toothbrush')

# Put the scarf and the comet and the mask into Box 3.
items_to_move = ['scarf', 'comet', 'mask']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Replace the freezer with the lion in Box 9.
boxes[9].remove('freezer')
boxes[9].append('lion')

# Swap the butterfly in Box 5 with the umbrella in Box 1.
boxes[5].remove('butterfly')
boxes[1].remove('umbrella')
boxes[5].append('umbrella')
boxes[1].append('butterfly')

# Put the freezer and the ring into Box 0.
boxes[9].remove('freezer')
boxes[0].append('freezer')
boxes[0].append('ring')

# Remove the scissors from Box 7.
boxes[7].remove('scissors')

# Replace the shoes with the shampoo in Box 13.
boxes[13].remove('shoes')
boxes[13].append('shampoo')

# Replace the butterfly and the zipper and the ship with the phone and the sandals and the cup in Box 1.
items_to_remove = ['butterfly', 'zipper', 'ship']
items_to_add = ['phone', 'sandals', 'cup']
for item in items_to_remove:
    boxes[1].remove(item)
for item in items_to_add:
    boxes[1].append(item)

# Put the candle and the thunder into Box 6.
items_to_move = ['candle', 'thunder']
for item in items_to_move:
    boxes[6].append(item)

# Move the controller and the scarf from Box 0 to Box 7.
items_to_move = ['controller', 'scarf']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[7].append(item)

# Put the mask into Box 6.
boxes[3].remove('mask')
boxes[6].append('mask')

# Empty Box 8.
boxes[8] = []

# Move the rocket from Box 11 to Box 0.
boxes[11].remove('rocket')
boxes[0].append('rocket')

# Move the scarf and the controller from Box 7 to Box 5.
items_to_move = ['scarf', 'controller']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[5].append(item)

# Replace the candle and the thunder and the rock with the chair and the lock and the jacket in Box 6.
items_to_remove = ['candle', 'thunder', 'rock']
items_to_add = ['chair', 'lock', 'jacket']
for item in items_to_remove:
    boxes[6].remove(item)
for item in items_to_add:
    boxes[6].append(item)

# Remove the shampoo from Box 13.
boxes[13].remove('shampoo')

# Move the umbrella from Box 5 to Box 10.
boxes[5].remove('umbrella')
boxes[10].append('umbrella')

# Empty Box 3.
boxes[3] = []

# Replace the toothbrush and the phone with the glove and the thunder in Box 12.
boxes[12].remove('toothbrush')
boxes[12].remove('phone')
boxes[12].append('glove')
boxes[12].append('thunder')

# Remove the sandals and the phone and the cup from Box 1.
items_to_remove = ['sandals', 'phone', 'cup']
for item in items_to_remove:
    boxes[1].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")