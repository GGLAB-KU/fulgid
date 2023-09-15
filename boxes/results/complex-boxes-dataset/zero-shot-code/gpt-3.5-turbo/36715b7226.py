box_0 = ['laptop', 'soap', 'boat', 'book']
box_1 = ['usb', 'bell']
box_2 = ['perfume']
box_3 = ['shoes', 'lamp', 'shoe', 'ring', 'cup']
box_4 = ['gloves']
box_5 = ['ship', 'microwave', 'battery', 'phone', 'whistle']
box_6 = ['glasses', 'oven', 'beach', 'train', 'razor']

# Swap gloves in Box 4 with perfume in Box 2
box_4, box_2 = box_2, box_4

# Put scarf, violin, and card into Box 4
box_4.extend(['scarf', 'violin', 'card'])

# Put car into Box 0
box_0.append('car')

# Remove gloves from Box 2
box_2.remove('gloves')

# Put river and moon into Box 1
box_1.extend(['river', 'moon'])

# Swap violin in Box 4 with usb in Box 1
box_4[box_4.index('violin')], box_1[box_1.index('usb')] = box_1[box_1.index('usb')], box_4[box_4.index('violin')]

# Replace microwave with shark in Box 5
box_5[box_5.index('microwave')] = 'shark'

# Remove ring and shoes from Box 3
box_3.remove('ring')
box_3.remove('shoes')

# Swap cup in Box 3 with boat in Box 0
box_3[box_3.index('cup')], box_0[box_0.index('boat')] = box_0[box_0.index('boat')], box_3[box_3.index('cup')]

# Replace moon, bell, and violin with perfume, zipper, and forest in Box 1
box_1[box_1.index('moon')] = 'perfume'
box_1[box_1.index('bell')] = 'zipper'
box_1[box_1.index('violin')] = 'forest'

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)