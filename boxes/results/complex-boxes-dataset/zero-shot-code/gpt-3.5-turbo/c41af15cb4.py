box_0 = ['spoon', 'shirt']
box_1 = ['polish']
box_2 = ['vase', 'shampoo', 'horse', 'battery', 'headphone']
box_3 = ['game', 'lipstick']
box_4 = ['rain', 'desert', 'microscope']
box_5 = ['controller', 'wig', 'bell']
box_6 = ['earring', 'shoes', 'fork', 'oven', 'camera']
box_7 = ['chair', 'train', 'glove', 'mask', 'ring']
box_8 = ['seaweed', 'pan', 'wallet', 'mountain', 'bag']
box_9 = ['planet', 'plane', 'paint', 'violin', 'bus']
box_10 = ['tape', 'harmonica', 'phone', 'plate']
box_11 = ['dog']

# Move the swimsuit from Box 10 to Box 7
box_7.append(box_10.pop(box_10.index('swimsuit')))

# Put the glasses and the necklace and the tie into Box 10
box_10.extend(['glasses', 'necklace', 'tie'])

# Swap the lipstick in Box 3 with the horse in Box 2
box_3[box_3.index('lipstick')], box_2[box_2.index('horse')] = box_2[box_2.index('horse')], box_3[box_3.index('lipstick')]

# Move the vase and the battery from Box 2 to Box 5
box_5.extend([box_2.pop(box_2.index('vase')), box_2.pop(box_2.index('battery'))])

# Remove the camera from Box 6
box_6.remove('camera')

# Move the fork and the shoes and the earring from Box 6 to Box 7
box_7.extend([box_6.pop(box_6.index('fork')), box_6.pop(box_6.index('shoes')), box_6.pop(box_6.index('earring'))])

# Move the microscope from Box 4 to Box 5
box_5.append(box_4.pop(box_4.index('microscope')))

# Swap the paint in Box 9 with the lipstick in Box 2
box_9[box_9.index('paint')], box_2[box_2.index('lipstick')] = box_2[box_2.index('lipstick')], box_9[box_9.index('paint')]

# Swap the horse in Box 3 with the phone in Box 10
box_3[box_3.index('horse')], box_10[box_10.index('phone')] = box_10[box_10.index('phone')], box_3[box_3.index('horse')]

# Swap the bus in Box 9 with the shoes in Box 7
box_9[box_9.index('bus')], box_7[box_7.index('shoes')] = box_7[box_7.index('shoes')], box_9[box_9.index('bus')]

# Move the mountain and the wallet from Box 8 to Box 3
box_3.extend([box_8.pop(box_8.index('mountain')), box_8.pop(box_8.index('wallet'))])

# Move the shampoo and the paint from Box 2 to Box 3
box_3.extend([box_2.pop(box_2.index('shampoo')), box_2.pop(box_2.index('paint'))])

# Move the headphone from Box 2 to Box 11
box_11.append(box_2.pop(box_2.index('headphone')))

# Put the fork into Box 0
box_0.append('fork')

# Replace the polish with the coral in Box 1
box_1[box_1.index('polish')] = 'coral'

# Replace the train and the glove with the lipstick and the horse in Box 7
box_7[box_7.index('train')], box_7[box_7.index('glove')] = box_3[box_3.index('lipstick')], box_2[box_2.index('horse')]

# Replace the wallet and the shampoo with the fridge and the harmonica in Box 3
box_3[box_3.index('wallet')], box_3[box_3.index('shampoo')] = 'fridge', 'harmonica'

# Move the dog from Box 11 to Box 6
box_6.append(box_11.pop(box_11.index('dog')))

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11]):
    print(f"Box {i}: {box}")