box_0 = ['comb']
box_1 = ['mountain', 'oven', 'charger', 'drum', 'chair']
box_2 = ['basket', 'blender', 'bracelet']
box_3 = ['island']
box_4 = []
box_5 = ['fish']
box_6 = ['seaweed', 'blanket']
box_7 = ['clock']
box_8 = []

# Swap the fish in Box 5 with the clock in Box 7
box_5.remove('fish')
box_7.remove('clock')
box_5.append('clock')
box_7.append('fish')

# Swap the basket in Box 2 with the fish in Box 7
box_2.remove('basket')
box_7.remove('fish')
box_2.append('fish')
box_7.append('basket')

# Swap the island in Box 3 with the clock in Box 5
box_3.remove('island')
box_5.remove('clock')
box_3.append('clock')
box_5.append('island')

# Swap the basket in Box 7 with the clock in Box 3
box_7.remove('basket')
box_3.remove('clock')
box_7.append('clock')
box_3.append('basket')

# Replace the comb with the helmet in Box 0
box_0.remove('comb')
box_0.append('helmet')

# Put the coral and the freezer and the console into Box 0
box_0.extend(['coral', 'freezer', 'console'])

# Remove the mountain and the drum and the chair from Box 1
box_1.remove('mountain')
box_1.remove('drum')
box_1.remove('chair')

# Empty Box 3
box_3 = []

# Remove the oven and the charger from Box 1
box_1.remove('oven')
box_1.remove('charger')

# Swap the helmet in Box 0 with the island in Box 5
box_0.remove('helmet')
box_5.remove('island')
box_0.append('island')
box_5.append('helmet')

# Move the helmet from Box 5 to Box 8
box_5.remove('helmet')
box_8.append('helmet')

# Remove the freezer and the console from Box 0
box_0.remove('freezer')
box_0.remove('console')

# Swap the fish in Box 2 with the clock in Box 7
box_2.remove('fish')
box_7.remove('clock')
box_2.append('clock')
box_7.append('fish')

# Remove the helmet from Box 8
box_8.remove('helmet')

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