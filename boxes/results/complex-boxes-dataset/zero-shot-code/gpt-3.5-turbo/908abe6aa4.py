box_0 = ['dolphin', 'beach', 'note', 'charger']
box_1 = ['controller', 'cat']
box_2 = ['rocket', 'table', 'piano']
box_3 = ['thunder', 'coin']

# Replace the beach with the shark in Box 0
box_0[1] = 'shark'

# Remove the bracelet from Box 0
box_0.remove('bracelet')

# Replace the table and the rocket with the shampoo and the earring in Box 2
box_2.remove('table')
box_2.remove('rocket')
box_2.extend(['shampoo', 'earring'])

# Put the flower into Box 1
box_1.append('flower')

# Remove the earring from Box 2
box_2.remove('earring')

# Remove the cat and the controller and the flower from Box 1
box_1.remove('controller')
box_1.remove('cat')
box_1.remove('flower')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)