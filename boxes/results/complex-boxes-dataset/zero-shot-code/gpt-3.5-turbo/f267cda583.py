box_0 = ['pants', 'sock', 'bowl', 'card']
box_1 = ['freezer', 'towel', 'coat', 'scissors']
box_2 = ['key']
box_3 = ['ring', 'pillow', 'mirror']
box_4 = ['laptop']
box_5 = []
box_6 = ['makeup', 'console', 'tiger', 'oven']
box_7 = ['rock']
box_8 = ['lion', 'vase', 'whistle', 'ship']
box_9 = ['tie', 'comet', 'blender', 'horse', 'train']
box_10 = ['grass', 'controller', 'shampoo']

# Replace the makeup and the oven with the fridge and the microwave in Box 6
box_6 = ['fridge', 'microwave']

# Put the usb and the jungle into Box 9
box_9.extend(['usb', 'jungle'])

# Remove the sock and the pants from Box 0
box_0.remove('sock')
box_0.remove('pants')

# Put the shoes and the thread into Box 5
box_5.extend(['shoes', 'thread'])

# Put the lipstick and the scissors into Box 1
box_1.extend(['lipstick', 'scissors'])

# Put the dolphin and the bicycle into Box 7
box_7.extend(['dolphin', 'bicycle'])

# Remove the fridge from Box 6
box_6.remove('fridge')

# Move the laptop from Box 4 to Box 1
box_1.append('laptop')
box_4.remove('laptop')

# Replace the pillow and the mirror with the oven and the brush in Box 3
box_3.remove('pillow')
box_3.remove('mirror')
box_3.extend(['oven', 'brush'])

# Replace the lion with the bus in Box 8
box_8.remove('lion')
box_8.append('bus')

# Put the shoes and the starfish into Box 0
box_0.extend(['shoes', 'starfish'])

# Move the shoes from Box 5 to Box 9
box_9.append('shoes')
box_5.remove('shoes')

# Remove the shampoo and the grass and the controller from Box 10
box_10.remove('shampoo')
box_10.remove('grass')
box_10.remove('controller')

# Move the brush and the ring and the oven from Box 3 to Box 1
box_1.extend(['brush', 'ring', 'oven'])
box_3.remove('brush')
box_3.remove('ring')
box_3.remove('oven')

# Move the whistle from Box 8 to Box 1
box_1.append('whistle')
box_8.remove('whistle')

# Swap the key in Box 2 with the bicycle in Box 7
box_2.remove('key')
box_7.remove('bicycle')
box_2.append('bicycle')
box_7.append('key')

# Replace the towel with the freezer in Box 1
box_1.remove('towel')
box_1.append('freezer')

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