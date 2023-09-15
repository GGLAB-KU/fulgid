box_0 = []
box_1 = ['vase', 'microscope', 'shark', 'headphone', 'mountain']
box_2 = ['grass', 'fridge', 'toothbrush', 'scissors']
box_3 = []
box_4 = []
box_5 = []
box_6 = ['microwave', 'sock', 'dog']
box_7 = ['lipstick', 'belt', 'cow', 'perfume', 'pants']
box_8 = ['river']

# Remove the fridge from Box 2
box_2.remove('fridge')

# Remove the lipstick and the pants and the cow from Box 7
box_7.remove('lipstick')
box_7.remove('pants')
box_7.remove('cow')

# Put the sock into Box 4
box_4.append('sock')

# Remove the microscope and the shark and the headphone from Box 1
box_1.remove('microscope')
box_1.remove('shark')
box_1.remove('headphone')

# Remove the sock from Box 4
box_4.remove('sock')

# Remove the toothbrush from Box 2
box_2.remove('toothbrush')

# Put the microwave and the bicycle into Box 8
box_8.append('microwave')
box_8.append('bicycle')

# Move the microwave and the sock from Box 6 to Box 3
box_3.append('microwave')
box_3.append('sock')
box_6.remove('microwave')
box_6.remove('sock')

# Remove the bicycle and the microwave and the river from Box 8
box_8.remove('bicycle')
box_8.remove('microwave')
box_8.remove('river')

# Remove the microwave from Box 3
box_3.remove('microwave')

# Put the scissors and the jacket and the ship into Box 3
box_3.append('scissors')
box_3.append('jacket')
box_3.append('ship')

# Remove the perfume from Box 7
box_7.remove('perfume')

# Empty Box 3
box_3 = []

# Replace the scissors and the grass with the bicycle and the console in Box 2
box_2.remove('scissors')
box_2.remove('grass')
box_2.append('bicycle')
box_2.append('console')

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