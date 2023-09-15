box_0 = ['dolphin', 'butterfly']
box_1 = ['microscope', 'bicycle', 'tree', 'microwave', 'spoon']
box_2 = ['earring', 'cloud', 'scarf', 'crown', 'cup']
box_3 = ['branch', 'laptop', 'doll', 'drum', 'bell']
box_4 = ['button', 'polish', 'coat', 'bowl']
box_5 = ['lightning', 'oven']
box_6 = ['lamp', 'fridge', 'camera', 'moon', 'sculpture']
box_7 = ['whistle']
box_8 = ['ship', 'dress']
box_9 = ['glasses', 'charger', 'bag', 'book', 'umbrella']
box_10 = ['mixer']

# Remove the lamp and the sculpture from Box 6
box_6.remove('lamp')
box_6.remove('sculpture')

# Remove the umbrella from Box 9
box_9.remove('umbrella')

# Move the fridge from Box 6 to Box 5
box_5.append('fridge')
box_6.remove('fridge')

# Move the moon from Box 6 to Box 7
box_7.append('moon')
box_6.remove('moon')

# Replace the fridge with the ocean in Box 5
box_5.remove('fridge')
box_5.append('ocean')

# Remove the microwave and the bicycle and the microscope from Box 1
box_1.remove('microscope')
box_1.remove('bicycle')
box_1.remove('microwave')

# Move the cloud and the earring and the scarf from Box 2 to Box 10
box_10.extend(['cloud', 'earring', 'scarf'])
box_2.remove('cloud')
box_2.remove('earring')
box_2.remove('scarf')

# Remove the butterfly from Box 0
box_0.remove('butterfly')

# Replace the scarf and the mixer with the sandals and the clock in Box 10
box_10.remove('scarf')
box_10.remove('mixer')
box_10.extend(['sandals', 'clock'])

# Move the bag and the charger from Box 9 to Box 6
box_6.extend(['bag', 'charger'])
box_9.remove('bag')
box_9.remove('charger')

# Move the doll and the bell from Box 3 to Box 1
box_1.extend(['doll', 'bell'])
box_3.remove('doll')
box_3.remove('bell')

# Empty Box 9
box_9 = []

# Empty Box 3
box_3 = []

# Remove the oven from Box 5
box_5.remove('oven')

# Put the apple into Box 8
box_8.append('apple')

# Put the guitar and the speaker and the bracelet into Box 7
box_7.extend(['guitar', 'speaker', 'bracelet'])

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