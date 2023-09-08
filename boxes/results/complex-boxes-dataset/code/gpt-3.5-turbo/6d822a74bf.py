# Initial state of boxes
boxes = {
    0: ['key', 'cloud', 'beach', 'glasses'],
    1: ['horse', 'card', 'blanket', 'truck', 'boot'],
    2: ['needle', 'comb', 'soap', 'helmet'],
    3: ['skirt', 'piano', 'shorts', 'bracelet'],
    4: ['watch', 'note', 'game', 'plane'],
    5: ['starfish', 'bowl', 'umbrella'],
    6: ['dolphin', 'dice', 'console'],
    7: ['telescope', 'puzzle', 'fish', 'thread', 'bird'],
    8: ['lion', 'scissors', 'glove', 'microscope'],
    9: ['ring', 'pot', 'speaker', 'paint', 'train'],
    10: ['frame', 'boat', 'rocket'],
    11: ['perfume', 'shoe', 'horn', 'shampoo'],
    12: ['moon', 'sculpture', 'lightning'],
    13: ['fork', 'freezer', 'cat', 'toothbrush', 'seaweed'],
    14: []
}

# Replace the console with the train in Box 6.
boxes[6].remove('console')
boxes[6].append('train')

# Swap the horn in Box 11 with the glove in Box 8.
boxes[11].remove('horn')
boxes[8].remove('glove')
boxes[11].append('glove')
boxes[8].append('horn')

# Move the ring and the speaker and the pot from Box 9 to Box 11.
items_to_move = ['ring', 'speaker', 'pot']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[11].append(item)

# Swap the shoe in Box 11 with the bowl in Box 5.
boxes[11].remove('shoe')
boxes[5].remove('bowl')
boxes[11].append('bowl')
boxes[5].append('shoe')

# Replace the bracelet and the skirt with the blender and the seaweed in Box 3.
boxes[3].remove('bracelet')
boxes[3].remove('skirt')
boxes[3].append('blender')
boxes[3].append('seaweed')

# Swap the sculpture in Box 12 with the horn in Box 8.
boxes[12].remove('sculpture')
boxes[8].remove('horn')
boxes[12].append('horn')
boxes[8].append('sculpture')

# Swap the plane in Box 4 with the moon in Box 12.
boxes[4].remove('plane')
boxes[12].remove('moon')
boxes[4].append('moon')
boxes[12].append('plane')

# Move the shorts and the blender from Box 3 to Box 9.
boxes[3].remove('shorts')
boxes[3].remove('blender')
boxes[9].append('shorts')
boxes[9].append('blender')

# Swap the pot in Box 11 with the beach in Box 0.
boxes[11].remove('pot')
boxes[0].remove('beach')
boxes[11].append('beach')
boxes[0].append('pot')

# Replace the piano and the seaweed with the battery and the towel in Box 3.
boxes[3].remove('piano')
boxes[3].remove('seaweed')
boxes[3].append('battery')
boxes[3].append('towel')

# Move the train and the blender from Box 9 to Box 8.
boxes[9].remove('train')
boxes[9].remove('blender')
boxes[8].append('train')
boxes[8].append('blender')

# Replace the battery and the towel with the lion and the bag in Box 3.
boxes[3].remove('battery')
boxes[3].remove('towel')
boxes[3].append('lion')
boxes[3].append('bag')

# Replace the paint with the sandals in Box 9.
boxes[9].remove('paint')
boxes[9].append('sandals')

# Move the cloud and the glasses from Box 0 to Box 12.
boxes[0].remove('cloud')
boxes[0].remove('glasses')
boxes[12].append('cloud')
boxes[12].append('glasses')

# Remove the starfish from Box 5.
boxes[5].remove('starfish')

# Put the laptop into Box 6.
boxes[6].append('laptop')

# Move the freezer and the cat from Box 13 to Box 2.
boxes[13].remove('freezer')
boxes[13].remove('cat')
boxes[2].append('freezer')
boxes[2].append('cat')

# Replace the soap with the vase in Box 2.
boxes[2].remove('soap')
boxes[2].append('vase')

# Replace the pot with the shampoo in Box 0.
boxes[0].remove('pot')
boxes[0].append('shampoo')

# Remove the horse and the card from Box 1.
boxes[1].remove('horse')
boxes[1].remove('card')

# Swap the bowl in Box 11 with the train in Box 8.
boxes[11].remove('bowl')
boxes[8].remove('train')
boxes[11].append('train')
boxes[8].append('bowl')

# Replace the boot and the truck with the clock and the leaf in Box 1.
boxes[1].remove('boot')
boxes[1].remove('truck')
boxes[1].append('clock')
boxes[1].append('leaf')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")