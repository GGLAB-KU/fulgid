# Initial state of boxes
boxes = {
    0: ['watch', 'dolphin', 'shoes', 'bus', 'scissors'],
    1: ['key'],
    2: ['bicycle', 'bag', 'button', 'guitar', 'belt'],
    3: ['game', 'sun', 'pants', 'freezer', 'mountain'],
    4: ['lipstick', 'horn', 'table'],
    5: ['spoon', 'crown', 'comb', 'pillow'],
    6: ['violin'],
    7: [],
    8: ['blender'],
    9: ['apple', 'helmet', 'shorts', 'car'],
    10: ['shampoo'],
    11: ['planet'],
    12: [],
    13: ['towel'],
    14: ['octopus', 'ocean', 'puzzle', 'wig']
}

# Move the towel from Box 13 to Box 10.
boxes[13].remove('towel')
boxes[10].append('towel')

# Put the beach and the bell and the toy into Box 13.
items_to_put = ['beach', 'bell', 'toy']
for item in items_to_put:
    boxes[13].append(item)

# Put the guitar and the key into Box 5.
items_to_put = ['guitar', 'key']
for item in items_to_put:
    boxes[5].append(item)

# Replace the mountain and the sun with the scissors and the headphone in Box 3.
boxes[3].remove('mountain')
boxes[3].remove('sun')
boxes[3].append('scissors')
boxes[3].append('headphone')

# Remove the puzzle from Box 14.
boxes[14].remove('puzzle')

# Replace the helmet and the shorts with the shampoo and the necklace in Box 9.
boxes[9].remove('helmet')
boxes[9].remove('shorts')
boxes[9].append('shampoo')
boxes[9].append('necklace')

# Put the makeup and the bicycle and the submarine into Box 11.
items_to_put = ['makeup', 'bicycle', 'submarine']
for item in items_to_put:
    boxes[11].append(item)

# Remove the necklace and the apple and the car from Box 9.
items_to_remove = ['necklace', 'apple', 'car']
for item in items_to_remove:
    boxes[9].remove(item)

# Remove the towel from Box 10.
boxes[10].remove('towel')

# Swap the blender in Box 8 with the shampoo in Box 9.
boxes[8], boxes[9] = boxes[9], boxes[8]

# Replace the shampoo with the necklace in Box 10.
boxes[10].remove('shampoo')
boxes[10].append('necklace')

# Put the glove into Box 0.
boxes[0].append('glove')

# Put the phone into Box 12.
boxes[12].append('phone')

# Remove the submarine from Box 11.
boxes[11].remove('submarine')

# Move the shoes and the scissors from Box 0 to Box 9.
items_to_move = ['shoes', 'scissors']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[9].append(item)

# Remove the violin from Box 6.
boxes[6].remove('violin')

# Swap the horn in Box 4 with the scissors in Box 3.
boxes[4], boxes[3] = boxes[3], boxes[4]

# Replace the horn and the game and the pants with the shirt and the train and the glasses in Box 3.
boxes[3].remove('horn')
boxes[3].remove('game')
boxes[3].remove('pants')
boxes[3].append('shirt')
boxes[3].append('train')
boxes[3].append('glasses')

# Remove the phone from Box 12.
boxes[12].remove('phone')

# Put the cow and the usb into Box 10.
items_to_put = ['cow', 'usb']
for item in items_to_put:
    boxes[10].append(item)

# Replace the guitar and the spoon and the pillow with the bird and the towel and the oven in Box 5.
boxes[5].remove('guitar')
boxes[5].remove('spoon')
boxes[5].remove('pillow')
boxes[5].append('bird')
boxes[5].append('towel')
boxes[5].append('oven')

# Swap the scissors in Box 9 with the bicycle in Box 11.
boxes[9], boxes[11] = boxes[11], boxes[9]

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")