# Initial state of boxes
boxes = {
    0: ['desert', 'belt'],
    1: ['phone', 'lamp'],
    2: ['chair', 'moon'],
    3: ['speaker', 'wallet'],
    4: ['whistle', 'oven', 'toothbrush'],
    5: ['island', 'butterfly', 'thread', 'fish', 'apple'],
    6: ['jacket', 'boot', 'bicycle'],
    7: ['controller'],
    8: ['scarf'],
    9: ['puzzle', 'coat'],
    10: ['bracelet', 'headphone', 'seaweed'],
    11: ['key', 'zipper']
}

# Move the key from Box 11 to Box 10.
boxes[11].remove('key')
boxes[10].append('key')

# Swap the moon in Box 2 with the scarf in Box 8.
boxes[2].remove('moon')
boxes[8].remove('scarf')
boxes[2].append('scarf')
boxes[8].append('moon')

# Replace the moon with the comb in Box 8.
boxes[8].remove('moon')
boxes[8].append('comb')

# Put the swimsuit and the shelf and the helmet into Box 7.
items_to_move = ['swimsuit', 'shelf', 'helmet']
for item in items_to_move:
    boxes[7].append(item)

# Swap the seaweed in Box 10 with the thread in Box 5.
boxes[10].remove('seaweed')
boxes[5].remove('thread')
boxes[10].append('thread')
boxes[5].append('seaweed')

# Remove the oven and the toothbrush and the whistle from Box 4.
items_to_remove = ['oven', 'toothbrush', 'whistle']
for item in items_to_remove:
    boxes[4].remove(item)

# Move the key and the headphone from Box 10 to Box 5.
boxes[10].remove('key')
boxes[10].remove('headphone')
boxes[5].append('key')
boxes[5].append('headphone')

# Move the chair from Box 2 to Box 4.
boxes[2].remove('chair')
boxes[4].append('chair')

# Remove the puzzle from Box 9.
boxes[9].remove('puzzle')

# Replace the island with the bracelet in Box 5.
boxes[5].remove('island')
boxes[5].append('bracelet')

# Swap the desert in Box 0 with the chair in Box 4.
boxes[0].remove('desert')
boxes[4].remove('chair')
boxes[0].append('chair')
boxes[4].append('desert')

# Empty Box 8.
boxes[8] = []

# Swap the controller in Box 7 with the scarf in Box 2.
boxes[7].remove('controller')
boxes[2].remove('scarf')
boxes[7].append('scarf')
boxes[2].append('controller')

# Remove the coat from Box 9.
boxes[9].remove('coat')

# Remove the wallet and the speaker from Box 3.
boxes[3].remove('wallet')
boxes[3].remove('speaker')

# Replace the zipper with the book in Box 11.
boxes[11].remove('zipper')
boxes[11].append('book')

# Swap the bracelet in Box 5 with the controller in Box 2.
boxes[5].remove('bracelet')
boxes[2].remove('controller')
boxes[5].append('controller')
boxes[2].append('bracelet')

# Put the camera and the perfume into Box 5.
items_to_move = ['camera', 'perfume']
for item in items_to_move:
    boxes[5].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")