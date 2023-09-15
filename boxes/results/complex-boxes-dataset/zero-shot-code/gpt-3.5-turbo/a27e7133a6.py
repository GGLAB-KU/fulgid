box_0 = ['dice', 'coat', 'bird', 'controller', 'helmet']
box_1 = ['book', 'crown', 'coral', 'keyboard']
box_2 = ['vase', 'skirt']
box_3 = ['soap']
box_4 = ['frame']
box_5 = ['table', 'leaf']
box_6 = []

# Remove the leaf from Box 5
box_5.remove('leaf')

# Remove the keyboard and the coral from Box 1
box_1.remove('keyboard')
box_1.remove('coral')

# Replace the skirt and the vase with the blanket and the dice in Box 2
box_2.remove('skirt')
box_2.remove('vase')
box_2.extend(['blanket', 'dice'])

# Replace the frame with the scissors in Box 4
box_4.remove('frame')
box_4.append('scissors')

# Remove the scissors from Box 4
box_4.remove('scissors')

# Move the soap from Box 3 to Box 6
box_6.append(box_3.pop())

# Replace the bird and the coat and the controller with the oven and the camera and the cloud in Box 0
box_0.remove('bird')
box_0.remove('coat')
box_0.remove('controller')
box_0.extend(['oven', 'camera', 'cloud'])

# Replace the soap with the note in Box 6
box_6.remove('soap')
box_6.append('note')

# Empty Box 5
box_5.clear()

# Move the crown from Box 1 to Box 5
box_5.append(box_1.pop(box_1.index('crown')))

# Swap the book in Box 1 with the note in Box 6
box_1[box_1.index('book')], box_6[box_6.index('note')] = box_6[box_6.index('note')], box_1[box_1.index('book')]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)