# Initial state of boxes
boxes = {
    0: ['pot', 'controller'],
    1: ['sculpture', 'sandals', 'magnet'],
    2: ['fork'],
    3: ['apple', 'helmet', 'dog', 'flower', 'beach'],
    4: ['bell', 'note', 'watch', 'toaster'],
    5: ['game', 'bicycle', 'desert'],
    6: ['tiger', 'gloves', 'polish'],
    7: ['headphone', 'doll', 'battery', 'branch'],
    8: ['belt', 'comb', 'shelf', 'dice']
}

# Put the starfish into Box 4.
boxes[4].append('starfish')

# Replace the game and the desert with the thunder and the gloves in Box 5.
boxes[5].remove('game')
boxes[5].remove('desert')
boxes[5].append('thunder')
boxes[5].append('gloves')

# Move the sandals and the sculpture and the magnet from Box 1 to Box 3.
items_to_move = ['sandals', 'sculpture', 'magnet']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Put the jacket and the thread and the card into Box 1.
items_to_put = ['jacket', 'thread', 'card']
for item in items_to_put:
    boxes[1].append(item)

# Replace the thread and the card with the flower and the coin in Box 1.
boxes[1].remove('thread')
boxes[1].remove('card')
boxes[1].append('flower')
boxes[1].append('coin')

# Put the lion and the mountain into Box 3.
items_to_put = ['lion', 'mountain']
for item in items_to_put:
    boxes[3].append(item)

# Remove the controller from Box 0.
boxes[0].remove('controller')

# Replace the fork with the towel in Box 2.
boxes[2].remove('fork')
boxes[2].append('towel')

# Remove the lion and the sandals from Box 3.
boxes[3].remove('lion')
boxes[3].remove('sandals')

# Move the bell and the watch and the note from Box 4 to Box 3.
items_to_move = ['bell', 'watch', 'note']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Put the necklace and the wallet and the battery into Box 5.
items_to_put = ['necklace', 'wallet', 'battery']
for item in items_to_put:
    boxes[5].append(item)

# Remove the starfish and the toaster from Box 4.
boxes[4].remove('starfish')
boxes[4].remove('toaster')

# Replace the belt and the shelf with the note and the fork in Box 8.
boxes[8].remove('belt')
boxes[8].remove('shelf')
boxes[8].append('note')
boxes[8].append('fork')

# Move the comb and the note from Box 8 to Box 5.
boxes[8].remove('comb')
boxes[8].remove('note')
boxes[5].append('comb')
boxes[5].append('note')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")