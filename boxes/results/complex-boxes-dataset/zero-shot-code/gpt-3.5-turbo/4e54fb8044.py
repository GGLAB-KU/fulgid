box_0 = ['rocket', 'chair', 'key']
box_1 = ['bear', 'river', 'toothpaste', 'bowl', 'clock']
box_2 = ['sun', 'apple']
box_3 = []
box_4 = ['telescope', 'microwave', 'fridge', 'watch']

# Put the mask into Box 0
box_0.append('mask')

# Put the river into Box 2
box_2.append('river')

# Swap the clock in Box 1 with the river in Box 2
box_1.remove('clock')
box_1.append('river')

# Put the controller into Box 1
box_1.append('controller')

# Swap the sun in Box 2 with the fridge in Box 4
box_2.remove('sun')
box_4.remove('fridge')
box_2.append('fridge')
box_4.append('sun')

# Remove the telescope and the watch from Box 4
box_4.remove('telescope')
box_4.remove('watch')

# Put the forest and the tiger and the charger into Box 0
box_0.extend(['forest', 'tiger', 'charger'])

# Remove the sun and the microwave from Box 4
box_4.remove('sun')
box_4.remove('microwave')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)