# Initial state of boxes
boxes = {
    0: ['spoon', 'shirt'],
    1: ['polish'],
    2: ['vase', 'shampoo', 'horse', 'battery', 'headphone'],
    3: ['game', 'lipstick'],
    4: ['rain', 'desert', 'microscope'],
    5: ['controller', 'wig', 'bell'],
    6: ['earring', 'shoes', 'fork', 'oven', 'camera'],
    7: ['chair', 'train', 'glove', 'mask', 'ring'],
    8: ['seaweed', 'pan', 'wallet', 'mountain', 'bag'],
    9: ['planet', 'plane', 'paint', 'violin', 'bus'],
    10: ['tape', 'harmonica', 'phone', 'swimsuit', 'plate'],
    11: ['dog']
}

# Move the swimsuit from Box 10 to Box 7.
boxes[10].remove('swimsuit')
boxes[7].append('swimsuit')

# Put the glasses and the necklace and the tie into Box 10.
items_to_put = ['glasses', 'necklace', 'tie']
for item in items_to_put:
    boxes[10].append(item)

# Swap the lipstick in Box 3 with the horse in Box 2.
boxes[3].remove('lipstick')
boxes[2].remove('horse')
boxes[3].append('horse')
boxes[2].append('lipstick')

# Move the vase and the battery from Box 2 to Box 5.
items_to_move = ['vase', 'battery']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[5].append(item)

# Remove the camera from Box 6.
boxes[6].remove('camera')

# Move the fork and the shoes and the earring from Box 6 to Box 7.
items_to_move = ['fork', 'shoes', 'earring']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[7].append(item)

# Move the microscope from Box 4 to Box 5.
boxes[4].remove('microscope')
boxes[5].append('microscope')

# Swap the paint in Box 9 with the lipstick in Box 2.
boxes[9].remove('paint')
boxes[2].remove('lipstick')
boxes[9].append('lipstick')
boxes[2].append('paint')

# Swap the horse in Box 3 with the phone in Box 10.
boxes[3].remove('horse')
boxes[10].remove('phone')
boxes[3].append('phone')
boxes[10].append('horse')

# Swap the bus in Box 9 with the shoes in Box 7.
boxes[9].remove('bus')
boxes[7].remove('shoes')
boxes[9].append('shoes')
boxes[7].append('bus')

# Move the mountain and the wallet from Box 8 to Box 3.
items_to_move = ['mountain', 'wallet']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[3].append(item)

# Move the shampoo and the paint from Box 2 to Box 3.
items_to_move = ['shampoo', 'paint']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Move the headphone from Box 2 to Box 11.
boxes[2].remove('headphone')
boxes[11].append('headphone')

# Put the fork into Box 0.
boxes[0].append('fork')

# Replace the polish with the coral in Box 1.
boxes[1].remove('polish')
boxes[1].append('coral')

# Replace the train and the glove with the lipstick and the horse in Box 7.
boxes[7].remove('train')
boxes[7].remove('glove')
boxes[7].append('lipstick')
boxes[7].append('horse')

# Replace the wallet and the shampoo with the fridge and the harmonica in Box 3.
boxes[3].remove('wallet')
boxes[3].remove('shampoo')
boxes[3].append('fridge')
boxes[3].append('harmonica')

# Move the dog from Box 11 to Box 6.
boxes[11].remove('dog')
boxes[6].append('dog')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")