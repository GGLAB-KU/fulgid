# Initial state of boxes
boxes = {
    0: ['thread', 'coin', 'ocean', 'bracelet', 'razor'],
    1: ['belt', 'tree'],
    2: ['shark'],
    3: ['console'],
    4: ['plate'],
    5: ['key', 'note', 'storm', 'shelf', 'whistle'],
    6: ['cow', 'perfume'],
    7: ['train', 'needle', 'island'],
    8: [],
    9: ['vase', 'lipstick']
}

# Replace the console with the charger in Box 3.
boxes[3].remove('console')
boxes[3].append('charger')

# Move the cow from Box 6 to Box 2.
boxes[6].remove('cow')
boxes[2].append('cow')

# Remove the plate from Box 4.
boxes[4].remove('plate')

# Remove the needle and the island and the train from Box 7.
items_to_remove = ['needle', 'island', 'train']
for item in items_to_remove:
    boxes[7].remove(item)

# Swap the charger in Box 3 with the shark in Box 2.
boxes[3].remove('charger')
boxes[2].remove('shark')
boxes[3].append('shark')
boxes[2].append('charger')

# Replace the belt with the crown in Box 1.
boxes[1].remove('belt')
boxes[1].append('crown')

# Replace the charger with the plane in Box 2.
boxes[2].remove('charger')
boxes[2].append('plane')

# Move the shark from Box 3 to Box 0.
boxes[3].remove('shark')
boxes[0].append('shark')

# Put the mountain into Box 1.
boxes[1].append('mountain')

# Put the bowl into Box 1.
boxes[1].append('bowl')

# Put the whistle and the planet into Box 3.
boxes[3].append('whistle')
boxes[3].append('planet')

# Replace the vase with the game in Box 9.
boxes[9].remove('vase')
boxes[9].append('game')

# Remove the key and the shelf from Box 5.
items_to_remove = ['key', 'shelf']
for item in items_to_remove:
    boxes[5].remove(item)

# Move the perfume from Box 6 to Box 8.
boxes[6].remove('perfume')
boxes[8].append('perfume')

# Replace the note with the horn in Box 5.
boxes[5].remove('note')
boxes[5].append('horn')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")