box_0 = ['sun', 'dice', 'cloud', 'thunder']
box_1 = []
box_2 = ['wig', 'hat', 'key', 'controller']
box_3 = ['whistle', 'horse']
box_4 = ['blanket', 'fish']
box_5 = ['mask', 'cow', 'soap', 'plate', 'dog']
box_6 = ['note']
box_7 = ['toaster']

# Replace thunder and cloud with needle and boat in Box 0
box_0.remove('thunder')
box_0.remove('cloud')
box_0.extend(['needle', 'boat'])

# Put sun and spoon into Box 2
box_2.append('sun')
box_2.append('spoon')

# Remove horse from Box 3
box_3.remove('horse')

# Put grinder and bell into Box 5
box_5.append('grinder')
box_5.append('bell')

# Move whistle from Box 3 to Box 7
box_3.remove('whistle')
box_7.append('whistle')

# Swap toaster in Box 7 with blanket in Box 4
box_7.remove('toaster')
box_4.remove('blanket')
box_7.append('blanket')
box_4.append('toaster')

# Replace whistle and blanket with dice and ship in Box 7
box_7.remove('whistle')
box_7.remove('blanket')
box_7.extend(['dice', 'ship'])

# Replace fish and toaster with rock and keyboard in Box 4
box_4.remove('fish')
box_4.remove('toaster')
box_4.extend(['rock', 'keyboard'])

# Remove ship and dice from Box 7
box_7.remove('ship')
box_7.remove('dice')

# Remove note from Box 6
box_6.remove('note')

# Put coin into Box 1
box_1.append('coin')

# Swap sun in Box 0 with keyboard in Box 4
box_0.remove('sun')
box_4.remove('keyboard')
box_0.append('keyboard')
box_4.append('sun')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)