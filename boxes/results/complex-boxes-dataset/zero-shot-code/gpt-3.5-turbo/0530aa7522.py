box_0 = ['sculpture', 'key']
box_1 = ['motorcycle', 'card', 'toy', 'phone', 'seaweed']
box_2 = []
box_3 = ['headphone', 'bell', 'tie', 'zipper', 'snow']
box_4 = ['lightning', 'crown', 'sandals']
box_5 = ['soap', 'brush']
box_6 = ['harmonica', 'glove', 'microscope']
box_7 = ['pan', 'controller', 'lamp']
box_8 = ['octopus', 'sun', 'perfume']
box_9 = ['bicycle', 'gloves', 'fish', 'pillow']
box_10 = ['scissors', 'wallet']

# Move fish from Box 9 to Box 3
box_3.append(box_9.pop(box_9.index('fish')))

# Put polish and battery into Box 10
box_10.extend(['polish', 'battery'])

# Replace bicycle with truck in Box 9
box_9[box_9.index('bicycle')] = 'truck'

# Move truck and gloves from Box 9 to Box 5
box_5.extend([box_9.pop(box_9.index('truck')), box_9.pop(box_9.index('gloves'))])

# Swap sculpture in Box 0 with truck in Box 5
box_0[box_0.index('sculpture')], box_5[box_5.index('truck')] = box_5[box_5.index('truck')], box_0[box_0.index('sculpture')]

# Replace pillow with train in Box 9
box_9[box_9.index('pillow')] = 'train'

# Replace snow, tie, zipper with rain, swimsuit, chair in Box 3
box_3[box_3.index('snow')] = 'rain'
box_3[box_3.index('tie')] = 'swimsuit'
box_3[box_3.index('zipper')] = 'chair'

# Replace soap, gloves, sculpture with helmet, towel, comet in Box 5
box_5[box_5.index('soap')] = 'helmet'
box_5[box_5.index('gloves')] = 'towel'
box_5[box_5.index('sculpture')] = 'comet'

# Replace crown with mirror in Box 4
box_4[box_4.index('crown')] = 'mirror'

# Put ship into Box 6
box_6.append('ship')

# Put shirt, scarf, usb into Box 6
box_6.extend(['shirt', 'scarf', 'usb'])

# Swap lightning in Box 4 with motorcycle in Box 1
box_4[box_4.index('lightning')], box_1[box_1.index('motorcycle')] = box_1[box_1.index('motorcycle')], box_4[box_4.index('lightning')]

# Remove sun, perfume, octopus from Box 8
box_8.remove('sun')
box_8.remove('perfume')
box_8.remove('octopus')

# Put soap, key, sandals into Box 6
box_6.extend(['soap', 'key', 'sandals'])

# Swap train in Box 9 with comet in Box 5
box_9[box_9.index('train')], box_5[box_5.index('comet')] = box_5[box_5.index('comet')], box_9[box_9.index('train')]

# Swap motorcycle in Box 4 with truck in Box 0
box_4[box_4.index('motorcycle')], box_0[box_0.index('truck')] = box_0[box_0.index('truck')], box_4[box_4.index('motorcycle')]

# Swap key in Box 0 with wallet in Box 10
box_0[box_0.index('key')], box_10[box_10.index('wallet')] = box_10[box_10.index('wallet')], box_0[box_0.index('key')]

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