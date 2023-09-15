box_0 = []
box_1 = ['cat', 'plane', 'grinder', 'game', 'scarf']
box_2 = ['doll', 'moon']
box_3 = ['perfume', 'camera', 'controller', 'button', 'tie']
box_4 = []
box_5 = ['lamp', 'motorcycle', 'drum', 'gloves']
box_6 = ['glove', 'basket', 'sculpture', 'forest']
box_7 = []
box_8 = ['coral', 'telescope', 'toothpaste', 'tape']
box_9 = ['whistle']
box_10 = []
box_11 = ['cup', 'lightning', 'bowl']

def print_box(box_index, box_items):
    print(f"Box {box_index}: {box_items}")

# Move the basket and the forest from Box 6 to Box 4
box_4.extend([box_6.pop(box_6.index('basket')), box_6.pop(box_6.index('forest'))])
print_box(4, box_4)
print_box(6, box_6)

# Put the card and the cup and the glasses into Box 9
box_9.extend(['card', 'cup', 'glasses'])
print_box(9, box_9)

# Move the forest from Box 4 to Box 0
box_0.append(box_4.pop(box_4.index('forest')))
print_box(0, box_0)
print_box(4, box_4)

# Swap the doll in Box 2 with the plane in Box 1
box_2[box_2.index('doll')], box_1[box_1.index('plane')] = box_1[box_1.index('plane')], box_2[box_2.index('doll')]
print_box(1, box_1)
print_box(2, box_2)

# Put the shark into Box 0
box_0.append('shark')
print_box(0, box_0)

# Swap the shark in Box 0 with the motorcycle in Box 5
box_0[box_0.index('shark')], box_5[box_5.index('motorcycle')] = box_5[box_5.index('motorcycle')], box_0[box_0.index('shark')]
print_box(0, box_0)
print_box(5, box_5)

# Put the octopus and the skirt into Box 2
box_2.extend(['octopus', 'skirt'])
print_box(2, box_2)

# Replace the glove and the sculpture with the lipstick and the car in Box 6
box_6[box_6.index('glove')] = 'lipstick'
box_6[box_6.index('sculpture')] = 'car'
print_box(6, box_6)

# Move the scarf from Box 1 to Box 0
box_0.append(box_1.pop(box_1.index('scarf')))
print_box(0, box_0)
print_box(1, box_1)

# Remove the basket from Box 4
box_4.remove('basket')
print_box(4, box_4)

# Put the harmonica into Box 10
box_10.append('harmonica')
print_box(10, box_10)

# Swap the game in Box 1 with the whistle in Box 9
box_1[box_1.index('game')], box_9[box_9.index('whistle')] = box_9[box_9.index('whistle')], box_1[box_1.index('game')]
print_box(1, box_1)
print_box(9, box_9)

# Remove the car from Box 6
box_6.remove('car')
print_box(6, box_6)

# Replace the button and the tie and the camera with the starfish and the speaker and the pot in Box 3
box_3[box_3.index('button')] = 'starfish'
box_3[box_3.index('tie')] = 'speaker'
box_3[box_3.index('camera')] = 'pot'
print_box(3, box_3)

# Put the lion into Box 10
box_10.append('lion')
print_box(10, box_10)

# Remove the lion and the harmonica from Box 10
box_10.remove('lion')
box_10.remove('harmonica')
print_box(10, box_10)

# Replace the game and the cup and the card with the lamp and the beach and the sun in Box 9
box_9[box_9.index('game')] = 'lamp'
box_9[box_9.index('cup')] = 'beach'
box_9[box_9.index('card')] = 'sun'
print_box(9, box_9)

# Replace the moon with the cow in Box 2
box_2[box_2.index('moon')] = 'cow'
print_box(2, box_2)