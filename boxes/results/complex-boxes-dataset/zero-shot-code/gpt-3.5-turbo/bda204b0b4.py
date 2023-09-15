box_0 = ['needle', 'scissors', 'glasses', 'laptop', 'train']
box_1 = ['shirt', 'dolphin', 'scarf', 'toy', 'cat']
box_2 = []
box_3 = ['umbrella', 'bag', 'cow', 'mirror']
box_4 = ['lightning', 'towel']
box_5 = ['horse']
box_6 = ['sock', 'controller', 'skirt', 'lipstick', 'mask']
box_7 = ['blender', 'keyboard', 'rock', 'boot']
box_8 = ['razor']
box_9 = ['beach', 'fish']

# Replace the beach with the whistle in Box 9
box_9.remove('beach')
box_9.append('whistle')

# Move the controller and the mask from Box 6 to Box 7
box_7.extend([box_6.pop(box_6.index('controller')), box_6.pop(box_6.index('mask'))])

# Move the glasses and the train from Box 0 to Box 8
box_8.extend([box_0.pop(box_0.index('glasses')), box_0.pop(box_0.index('train'))])

# Swap the horse in Box 5 with the skirt in Box 6
box_5[0], box_6[box_6.index('skirt')] = box_6[box_6.index('skirt')], box_5[0]

# Remove the lightning from Box 4
box_4.remove('lightning')

# Put the shirt and the necklace and the clock into Box 8
box_8.extend(['shirt', 'necklace', 'clock'])

# Put the cow and the toy into Box 0
box_0.extend(['cow', 'toy'])

# Move the towel from Box 4 to Box 1
box_1.append(box_4.pop(box_4.index('towel')))

# Swap the shirt in Box 8 with the skirt in Box 5
box_8[box_8.index('shirt')], box_5[0] = box_5[0], box_8[box_8.index('shirt')]

# Swap the toy in Box 1 with the fish in Box 9
box_1[box_1.index('toy')], box_9[box_9.index('fish')] = box_9[box_9.index('fish')], box_1[box_1.index('toy')]

# Remove the laptop from Box 0
box_0.remove('laptop')

# Swap the toy in Box 9 with the lipstick in Box 6
box_9[box_9.index('toy')], box_6[box_6.index('lipstick')] = box_6[box_6.index('lipstick')], box_9[box_9.index('toy')]

# Remove the sock and the toy from Box 6
box_6.remove('sock')
box_6.remove('toy')

# Put the microscope and the grass into Box 6
box_6.extend(['microscope', 'grass'])

# Put the soap and the microwave into Box 5
box_5.extend(['soap', 'microwave'])

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