# Initial state of boxes
boxes = {
    0: [],
    1: ['glove'],
    2: ['harmonica', 'magnet', 'lipstick', 'game'],
    3: ['ocean', 'motorcycle', 'sculpture', 'jacket', 'butterfly'],
    4: ['dolphin', 'microwave', 'doll', 'shoes'],
    5: [],
    6: ['moon', 'thunder', 'gloves'],
    7: ['sun', 'key', 'paint'],
    8: ['battery', 'rock', 'dog', 'charger', 'mask']
}

# Remove the rock and the dog from Box 8.
boxes[8].remove('rock')
boxes[8].remove('dog')

# Replace the harmonica and the game with the bird and the truck in Box 2.
boxes[2].remove('harmonica')
boxes[2].remove('game')
boxes[2].append('bird')
boxes[2].append('truck')

# Replace the shoes and the microwave and the doll with the shampoo and the cloud and the bicycle in Box 4.
boxes[4].remove('shoes')
boxes[4].remove('microwave')
boxes[4].remove('doll')
boxes[4].append('shampoo')
boxes[4].append('cloud')
boxes[4].append('bicycle')

# Move the butterfly and the jacket and the ocean from Box 3 to Box 5.
items_to_move = ['butterfly', 'jacket', 'ocean']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[5].append(item)

# Swap the bird in Box 2 with the thunder in Box 6.
boxes[2].remove('bird')
boxes[6].remove('thunder')
boxes[2].append('thunder')
boxes[6].append('bird')

# Move the mask and the charger from Box 8 to Box 5.
items_to_move = ['mask', 'charger']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[5].append(item)

# Put the swimsuit and the battery into Box 2.
boxes[2].append('swimsuit')
boxes[2].append('battery')

# Replace the cloud and the bicycle and the shampoo with the tie and the speaker and the watch in Box 4.
boxes[4].remove('cloud')
boxes[4].remove('bicycle')
boxes[4].remove('shampoo')
boxes[4].append('tie')
boxes[4].append('speaker')
boxes[4].append('watch')

# Remove the truck and the swimsuit from Box 2.
boxes[2].remove('truck')
boxes[2].remove('swimsuit')

# Put the shirt and the submarine into Box 7.
boxes[7].append('shirt')
boxes[7].append('submarine')

# Move the key and the sun and the paint from Box 7 to Box 8.
items_to_move = ['key', 'sun', 'paint']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[8].append(item)

# Swap the battery in Box 2 with the battery in Box 8.
boxes[2].remove('battery')
boxes[8].remove('battery')
boxes[2].append('battery')
boxes[8].append('battery')

# Swap the thunder in Box 2 with the glove in Box 1.
boxes[2].remove('thunder')
boxes[1].remove('glove')
boxes[2].append('glove')
boxes[1].append('thunder')

# Put the magnet and the tie into Box 1.
boxes[1].append('magnet')
boxes[1].append('tie')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")