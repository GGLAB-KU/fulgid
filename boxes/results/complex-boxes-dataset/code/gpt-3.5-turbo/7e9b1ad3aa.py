# Initial state of boxes
boxes = {
    0: ['jacket', 'pillow', 'bird', 'sun'],
    1: ['tiger', 'shirt', 'note', 'train'],
    2: ['horse'],
    3: ['shoe', 'octopus'],
    4: ['headphone', 'car'],
    5: ['wire', 'charger'],
    6: ['piano', 'tape', 'cup'],
    7: ['flower'],
    8: ['helmet'],
    9: ['bowl', 'elephant'],
    10: ['microwave', 'drum', 'oven', 'mask', 'desert'],
    11: ['microscope', 'lightning', 'magnet'],
    12: []
}

# Put the wire and the shorts and the pants into Box 0.
items_to_put = ['wire', 'shorts', 'pants']
for item in items_to_put:
    boxes[0].append(item)

# Put the grinder and the thunder into Box 8.
items_to_put = ['grinder', 'thunder']
for item in items_to_put:
    boxes[8].append(item)

# Swap the octopus in Box 3 with the flower in Box 7.
boxes[3].remove('octopus')
boxes[7].remove('flower')
boxes[3].append('flower')
boxes[7].append('octopus')

# Put the toaster into Box 2.
boxes[2].append('toaster')

# Swap the bowl in Box 9 with the headphone in Box 4.
boxes[9].remove('bowl')
boxes[4].remove('headphone')
boxes[9].append('headphone')
boxes[4].append('bowl')

# Swap the toaster in Box 2 with the drum in Box 10.
boxes[2].remove('toaster')
boxes[10].remove('drum')
boxes[2].append('drum')
boxes[10].append('toaster')

# Remove the wire from Box 5.
boxes[5].remove('wire')

# Put the glove and the toaster and the fork into Box 8.
items_to_put = ['glove', 'toaster', 'fork']
for item in items_to_put:
    boxes[8].append(item)

# Remove the charger from Box 5.
boxes[5].remove('charger')

# Put the pillow into Box 7.
boxes[7].append('pillow')

# Move the pillow and the octopus from Box 7 to Box 12.
items_to_move = ['pillow', 'octopus']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[12].append(item)

# Remove the elephant and the headphone from Box 9.
boxes[9].remove('elephant')
boxes[9].remove('headphone')

# Put the battery and the toothpaste and the lipstick into Box 5.
items_to_put = ['battery', 'toothpaste', 'lipstick']
for item in items_to_put:
    boxes[5].append(item)

# Replace the bowl with the mountain in Box 4.
boxes[4].remove('bowl')
boxes[4].append('mountain')

# Replace the horse and the drum with the tree and the harmonica in Box 2.
boxes[2].remove('horse')
boxes[2].remove('drum')
boxes[2].append('tree')
boxes[2].append('harmonica')

# Swap the battery in Box 5 with the car in Box 4.
boxes[5].remove('battery')
boxes[4].remove('car')
boxes[5].append('car')
boxes[4].append('battery')

# Swap the mask in Box 10 with the tape in Box 6.
boxes[10].remove('mask')
boxes[6].remove('tape')
boxes[10].append('tape')
boxes[6].append('mask')

# Remove the tree and the harmonica from Box 2.
boxes[2].remove('tree')
boxes[2].remove('harmonica')

# Replace the train with the star in Box 1.
boxes[1].remove('train')
boxes[1].append('star')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")