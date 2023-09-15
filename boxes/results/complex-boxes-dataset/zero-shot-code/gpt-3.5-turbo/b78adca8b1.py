box_0 = ['guitar', 'keyboard']
box_1 = ['meteor', 'key', 'toothbrush', 'needle', 'moon']
box_2 = ['lipstick', 'motorcycle', 'island', 'phone', 'razor']
box_3 = ['earring', 'magnet']
box_4 = ['coat', 'drum', 'button']
box_5 = []
box_6 = ['mountain', 'pillow', 'bowl']
box_7 = ['cat', 'table']
box_8 = []

# Remove magnet from Box 3
box_3.remove('magnet')

# Swap guitar in Box 0 with pillow in Box 6
box_0.remove('guitar')
box_6.remove('pillow')
box_0.append('pillow')
box_6.append('guitar')

# Move earring from Box 3 to Box 1
box_3.remove('earring')
box_1.append('earring')

# Remove button from Box 4
box_4.remove('button')

# Replace mountain and bowl with tree and violin in Box 6
box_6.remove('mountain')
box_6.remove('bowl')
box_6.append('tree')
box_6.append('violin')

# Remove keyboard and pillow from Box 0
box_0.remove('keyboard')
box_0.remove('pillow')

# Replace drum with coin in Box 4
box_4.remove('drum')
box_4.append('coin')

# Put sandals and train into Box 7
box_7.append('sandals')
box_7.append('train')

# Put horse into Box 1
box_1.append('horse')

# Remove guitar from Box 6
box_6.remove('guitar')

# Replace razor and lipstick with headphone and cat in Box 2
box_2.remove('razor')
box_2.remove('lipstick')
box_2.append('headphone')
box_2.append('cat')

# Move table from Box 7 to Box 1
box_7.remove('table')
box_1.append('table')

# Move coat and coin from Box 4 to Box 1
box_4.remove('coat')
box_4.remove('coin')
box_1.append('coat')
box_1.append('coin')

# Remove tree from Box 6
box_6.remove('tree')

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