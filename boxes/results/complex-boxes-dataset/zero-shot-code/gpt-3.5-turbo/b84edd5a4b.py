box_0 = ['game', 'battery', 'island', 'gloves', 'violin']
box_1 = []
box_2 = ['shampoo', 'snow']
box_3 = ['toaster', 'sandals', 'boot', 'pillow', 'mixer']
box_4 = ['truck', 'paint', 'clock', 'wire', 'sculpture']
box_5 = []
box_6 = ['candle', 'skirt', 'harmonica']
box_7 = ['rock', 'dolphin', 'ocean', 'seaweed', 'flower']
box_8 = ['glove']
box_9 = ['storm', 'submarine', 'thunder', 'controller', 'lightning']
box_10 = ['toothbrush']
box_11 = ['apple', 'shirt', 'console', 'motorcycle', 'guitar']
box_12 = ['ship', 'perfume', 'dice']

# Swap the truck in Box 4 with the console in Box 11
box_4.remove('truck')
box_11.remove('console')
box_4.append('console')
box_11.append('truck')

# Move the clock and the wire and the paint from Box 4 to Box 9
box_4.remove('clock')
box_4.remove('wire')
box_4.remove('paint')
box_9.extend(['clock', 'wire', 'paint'])

# Swap the flower in Box 7 with the violin in Box 0
box_7.remove('flower')
box_0.remove('violin')
box_7.append('violin')
box_0.append('flower')

# Put the tree into Box 8
box_8.append('tree')

# Swap the shampoo in Box 2 with the skirt in Box 6
box_2.remove('shampoo')
box_6.remove('skirt')
box_2.append('skirt')
box_6.append('shampoo')

# Put the doll and the hat and the card into Box 2
box_2.extend(['doll', 'hat', 'card'])

# Empty Box 7
box_7.clear()

# Put the truck and the fridge into Box 12
box_12.extend(['truck', 'fridge'])

# Move the pillow from Box 3 to Box 1
box_3.remove('pillow')
box_1.append('pillow')

# Swap the card in Box 2 with the toaster in Box 3
box_2.remove('card')
box_3.remove('toaster')
box_2.append('toaster')
box_3.append('card')

# Put the rocket into Box 3
box_3.append('rocket')

# Put the lipstick and the toothbrush into Box 7
box_7.extend(['lipstick', 'toothbrush'])

# Empty Box 11
box_11.clear()

# Move the pillow from Box 1 to Box 7
box_1.remove('pillow')
box_7.append('pillow')

# Put the octopus and the needle into Box 10
box_10.extend(['octopus', 'needle'])

# Put the storm and the boat into Box 4
box_4.extend(['storm', 'boat'])

# Swap the tree in Box 8 with the needle in Box 10
box_8.remove('tree')
box_10.remove('needle')
box_8.append('needle')
box_10.append('tree')

# Move the storm and the controller and the submarine from Box 9 to Box 8
box_9.remove('storm')
box_9.remove('controller')
box_9.remove('submarine')
box_8.extend(['storm', 'controller', 'submarine'])

# Replace the rocket and the card with the shoes and the shoe in Box 3
box_3.remove('rocket')
box_3.remove('card')
box_3.extend(['shoes', 'shoe'])

# Move the controller and the glove and the needle from Box 8 to Box 4
box_8.remove('controller')
box_8.remove('glove')
box_8.remove('needle')
box_4.extend(['controller', 'glove', 'needle'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)
print("Box 10:", box_10)
print("Box 11:", box_11)
print("Box 12:", box_12)