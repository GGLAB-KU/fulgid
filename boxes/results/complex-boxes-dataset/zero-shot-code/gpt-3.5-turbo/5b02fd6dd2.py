box_0 = []
box_1 = ['branch', 'telescope', 'lion', 'lightning']
box_2 = ['harmonica', 'tie', 'note', 'shampoo']
box_3 = ['puzzle', 'mask', 'lamp']
box_4 = ['cup']

# Remove cup from Box 4
box_4.remove('cup')

# Remove branch from Box 1
box_1.remove('branch')

# Replace lion, lightning, and telescope with scissors, shelf, and scarf in Box 1
box_1.remove('lion')
box_1.remove('lightning')
box_1.remove('telescope')
box_1.extend(['scissors', 'shelf', 'scarf'])

# Replace harmonica and tie with earring and octopus in Box 2
box_2.remove('harmonica')
box_2.remove('tie')
box_2.extend(['earring', 'octopus'])

# Move shampoo, earring, and octopus from Box 2 to Box 3
box_2.remove('shampoo')
box_2.remove('earring')
box_2.remove('octopus')
box_3.extend(['shampoo', 'earring', 'octopus'])

# Move lamp and earring from Box 3 to Box 1
box_3.remove('lamp')
box_3.remove('earring')
box_1.extend(['lamp', 'earring'])

# Remove octopus from Box 3
box_3.remove('octopus')

# Replace shampoo with violin in Box 3
box_3.remove('shampoo')
box_3.append('violin')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)