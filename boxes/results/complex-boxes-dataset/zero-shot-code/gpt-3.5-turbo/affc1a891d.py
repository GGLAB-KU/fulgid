box_0 = []
box_1 = ['chair', 'microscope', 'mountain']
box_2 = ['rocket', 'perfume', 'puzzle', 'lock']
box_3 = ['magnet', 'thunder', 'table']
box_4 = []
box_5 = []
box_6 = ['sandals', 'cat', 'car', 'island']
box_7 = ['forest', 'elephant', 'butterfly', 'bicycle']
box_8 = ['soap']
box_9 = []
box_10 = []

# Replace the jungle with the fork in Box 1
box_1.remove('mountain')
box_1.append('fork')

# Replace the cloud with the rock in Box 7
box_7.remove('butterfly')
box_7.append('rock')

# Empty Box 7
box_7 = []

# Put the pants into Box 2
box_2.append('pants')

# Move the thunder from Box 3 to Box 9
box_9.append(box_3.pop(box_3.index('thunder')))

# Move the controller from Box 8 to Box 7
box_7.append(box_8.pop(box_8.index('soap')))

# Replace the controller with the thread in Box 7
box_7.remove('soap')
box_7.append('thread')

# Remove the puzzle from Box 2
box_2.remove('puzzle')

# Put the shark and the controller and the drum into Box 2
box_2.extend(['shark', 'controller', 'drum'])

# Remove the fork from Box 1
box_1.remove('fork')

# Remove the thunder from Box 9
box_9.remove('thunder')

# Move the table from Box 3 to Box 2
box_2.append(box_3.pop(box_3.index('table')))

# Remove the magnet from Box 3
box_3.remove('magnet')

# Remove the thread from Box 7
box_7.remove('thread')

# Swap the mountain in Box 1 with the soap in Box 8
box_1.remove('mountain')
box_8.remove('soap')
box_1.append('soap')
box_8.append('mountain')

# Move the mountain from Box 8 to Box 4
box_4.append(box_8.pop(box_8.index('mountain')))

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