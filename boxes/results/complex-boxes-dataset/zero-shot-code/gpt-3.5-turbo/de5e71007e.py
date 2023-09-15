box_0 = []
box_1 = []
box_2 = ['button', 'magnet']
box_3 = ['puzzle', 'tie']
box_4 = []
box_5 = ['plate']
box_6 = []

# Put the elephant and the dice and the thread into Box 5
box_5.extend(['elephant', 'dice', 'thread'])

# Swap the button in Box 2 with the puzzle in Box 3
box_2.remove('button')
box_3.remove('puzzle')
box_2.append('puzzle')
box_3.append('button')

# Empty Box 5
box_5 = []

# Move the button and the tie from Box 3 to Box 0
box_0.extend(['button', 'tie'])
box_3.remove('button')
box_3.remove('tie')

# Swap the puzzle in Box 2 with the tie in Box 0
box_2.remove('puzzle')
box_0.remove('tie')
box_2.append('tie')
box_0.append('puzzle')

# Swap the magnet in Box 2 with the puzzle in Box 0
box_2.remove('magnet')
box_0.remove('puzzle')
box_2.append('puzzle')
box_0.append('magnet')

# Move the button and the magnet from Box 0 to Box 3
box_3.extend(['button', 'magnet'])
box_0.remove('button')
box_0.remove('magnet')

# Swap the tie in Box 2 with the magnet in Box 3
box_2.remove('tie')
box_3.remove('magnet')
box_2.append('magnet')
box_3.append('tie')

# Put the scarf and the elephant into Box 1
box_1.extend(['scarf', 'elephant'])

# Remove the button from Box 3
box_3.remove('button')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)