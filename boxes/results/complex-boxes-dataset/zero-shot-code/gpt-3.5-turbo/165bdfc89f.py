box_0 = ['cow', 'beach']
box_1 = ['pants']
box_2 = ['clock', 'coat', 'shark', 'note']
box_3 = ['ocean', 'coin', 'toy']
box_4 = ['sun', 'makeup', 'magnet']

# Remove items from Box 3
box_3.remove('ocean')
box_3.remove('coin')
box_3.remove('toy')

# Move pants from Box 1 to Box 3
box_3.append(box_1.pop())

# Replace items in Box 2
box_2.remove('clock')
box_2.remove('note')
box_2.remove('shark')
box_2.extend(['dolphin', 'soap', 'battery'])

# Replace items in Box 2 again
box_2.remove('coat')
box_2.remove('dolphin')
box_2.remove('battery')
box_2.extend(['needle', 'game', 'oven'])

# Move pants from Box 3 to Box 4
box_4.append(box_3.pop())

# Swap magnet in Box 4 with beach in Box 0
box_0.remove('beach')
box_4.remove('magnet')
box_0.append('magnet')
box_4.append('beach')

# Remove items from Box 4
box_4.remove('beach')
box_4.remove('makeup')
box_4.remove('pants')

# Remove sun from Box 4
box_4.remove('sun')

# Print the final contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)