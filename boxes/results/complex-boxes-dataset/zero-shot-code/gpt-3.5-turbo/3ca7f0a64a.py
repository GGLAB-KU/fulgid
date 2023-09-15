box_0 = ['camera', 'horn', 'tiger', 'controller', 'lamp']
box_1 = ['card', 'bell', 'hat', 'cup']
box_2 = ['harmonica', 'perfume', 'phone', 'sandals']
box_3 = ['sock', 'wig', 'pillow', 'polish']
box_4 = []
box_5 = ['microwave', 'basket', 'motorcycle', 'headphone']

# Put the ship into Box 4
box_4.append('ship')

# Move the hat from Box 1 to Box 2
box_2.append(box_1.pop(box_1.index('hat')))

# Replace the harmonica and the sandals and the hat with the leaf and the soap and the freezer in Box 2
box_2[box_2.index('harmonica')] = 'leaf'
box_2[box_2.index('sandals')] = 'soap'
box_2[box_2.index('hat')] = 'freezer'

# Swap the controller in Box 0 with the ship in Box 4
box_0[box_0.index('controller')], box_4[box_4.index('ship')] = box_4[box_4.index('ship')], box_0[box_0.index('controller')]

# Swap the controller in Box 4 with the horn in Box 0
box_4[box_4.index('controller')], box_0[box_0.index('horn')] = box_0[box_0.index('horn')], box_4[box_4.index('controller')]

# Replace the basket and the headphone with the frame and the umbrella in Box 5
box_5[box_5.index('basket')] = 'frame'
box_5[box_5.index('headphone')] = 'umbrella'

# Replace the motorcycle with the card in Box 5
box_5[box_5.index('motorcycle')] = 'card'

# Swap the microwave in Box 5 with the lamp in Box 0
box_5[box_5.index('microwave')], box_0[box_0.index('lamp')] = box_0[box_0.index('lamp')], box_5[box_5.index('microwave')]

# Remove the freezer and the leaf and the soap from Box 2
box_2.remove('freezer')
box_2.remove('leaf')
box_2.remove('soap')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)