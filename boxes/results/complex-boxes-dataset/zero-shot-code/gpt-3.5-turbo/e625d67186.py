box_0 = ['book', 'mask', 'tree', 'submarine']
box_1 = ['beach', 'needle', 'coral']
box_2 = ['bird', 'branch']
box_3 = ['soap', 'controller', 'tiger']

# Remove items from Box 3
box_3.remove('controller')
box_3.remove('tiger')
box_3.remove('soap')

# Replace items in Box 1
box_1.remove('beach')
box_1.remove('needle')
box_1.remove('coral')
box_1.extend(['horn', 'frame', 'pillow'])

# Remove items from Box 1
box_1.remove('horn')
box_1.remove('frame')
box_1.remove('pillow')

# Put guitar into Box 3
box_3.append('guitar')

# Move items from Box 2 to Box 3
box_3.extend(box_2)
box_2.clear()

# Put sculpture, jacket, and fork into Box 0
box_0.extend(['sculpture', 'jacket', 'fork'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)