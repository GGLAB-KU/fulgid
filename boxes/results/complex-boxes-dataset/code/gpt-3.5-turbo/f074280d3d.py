# Initial state of boxes
boxes = {
    0: ['beach', 'plane'],
    1: ['meteor', 'wire', 'forest', 'sculpture', 'sandals'],
    2: [],
    3: [],
    4: ['pants', 'frame', 'sun'],
    5: ['scarf', 'thunder', 'dice'],
    6: ['microscope', 'blanket', 'harmonica'],
    7: ['swimsuit', 'seaweed'],
    8: ['makeup'],
    9: ['boot', 'moon', 'cup', 'train', 'gloves'],
    10: ['belt'],
    11: ['toothpaste', 'keyboard'],
    12: ['earring', 'butterfly', 'headphone', 'candle', 'bag']
}

# Swap the makeup in Box 8 with the moon in Box 9.
boxes[8], boxes[9] = boxes[9], boxes[8]

# Remove the harmonica from Box 6.
boxes[6].remove('harmonica')

# Put the fish into Box 10.
boxes[10].append('fish')

# Replace the blanket with the lightning in Box 6.
boxes[6].remove('blanket')
boxes[6].append('lightning')

# Replace the seaweed with the swimsuit in Box 7.
boxes[7].remove('seaweed')
boxes[7].append('swimsuit')

# Put the ocean and the glasses and the thread into Box 6.
items_to_put = ['ocean', 'glasses', 'thread']
for item in items_to_put:
    boxes[6].append(item)

# Move the pants from Box 4 to Box 6.
boxes[4].remove('pants')
boxes[6].append('pants')

# Move the keyboard from Box 11 to Box 3.
boxes[11].remove('keyboard')
boxes[3].append('keyboard')

# Put the shorts and the game and the comb into Box 0.
items_to_put = ['shorts', 'game', 'comb']
for item in items_to_put:
    boxes[0].append(item)

# Swap the keyboard in Box 3 with the swimsuit in Box 7.
boxes[3], boxes[7] = boxes[7], boxes[3]

# Swap the comb in Box 0 with the frame in Box 4.
boxes[0], boxes[4] = boxes[4], boxes[0]

# Put the fish and the jungle and the umbrella into Box 12.
items_to_put = ['fish', 'jungle', 'umbrella']
for item in items_to_put:
    boxes[12].append(item)

# Put the shorts and the drum into Box 9.
items_to_put = ['shorts', 'drum']
for item in items_to_put:
    boxes[9].append(item)

# Swap the candle in Box 12 with the swimsuit in Box 3.
boxes[12], boxes[3] = boxes[3], boxes[12]

# Remove the game and the shorts and the beach from Box 0.
items_to_remove = ['game', 'shorts', 'beach']
for item in items_to_remove:
    boxes[0].remove(item)

# Move the dice and the scarf and the thunder from Box 5 to Box 11.
items_to_move = ['dice', 'scarf', 'thunder']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[11].append(item)

# Remove the shorts and the cup and the boot from Box 9.
items_to_remove = ['shorts', 'cup', 'boot']
for item in items_to_remove:
    boxes[9].remove(item)

# Swap the keyboard in Box 7 with the makeup in Box 9.
boxes[7], boxes[9] = boxes[9], boxes[7]

# Replace the sculpture with the microwave in Box 1.
boxes[1].remove('sculpture')
boxes[1].append('microwave')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")