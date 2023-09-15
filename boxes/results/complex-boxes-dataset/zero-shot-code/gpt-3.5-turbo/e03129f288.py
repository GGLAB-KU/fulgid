box_0 = ['clock', 'telescope', 'cloud', 'coat', 'tie']
box_1 = ['dice']
box_2 = ['pot', 'fish', 'soap', 'camera', 'octopus']
box_3 = []
box_4 = []
box_5 = ['plane']

# Remove fish, pot, and camera from Box 2
box_2.remove('fish')
box_2.remove('pot')
box_2.remove('camera')

# Remove clock and tie from Box 0
box_0.remove('clock')
box_0.remove('tie')

# Remove coat from Box 0
box_0.remove('coat')

# Swap soap in Box 2 with plane in Box 5
box_2.remove('soap')
box_5.remove('plane')
box_2.append('plane')
box_5.append('soap')

# Swap telescope in Box 0 with dice in Box 1
box_0.remove('telescope')
box_1.remove('dice')
box_0.append('dice')
box_1.append('telescope')

# Move telescope from Box 1 to Box 5
box_1.remove('telescope')
box_5.append('telescope')

# Move dice and cloud from Box 0 to Box 4
box_0.remove('dice')
box_0.remove('cloud')
box_4.append('dice')
box_4.append('cloud')

# Move plane from Box 5 to Box 2
box_5.remove('plane')
box_2.append('plane')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)