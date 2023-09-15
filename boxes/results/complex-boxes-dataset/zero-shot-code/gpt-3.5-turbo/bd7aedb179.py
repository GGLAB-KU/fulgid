box_0 = ['apple', 'umbrella', 'shoe', 'wig']
box_1 = ['polish']
box_2 = ['wire', 'dice', 'ship']
box_3 = ['puzzle', 'coat', 'necklace', 'whistle']
box_4 = []
box_5 = ['beach', 'plate', 'meteor', 'thunder', 'blanket']
box_6 = ['sandals']
box_7 = ['grinder', 'branch', 'storm']
box_8 = ['octopus', 'motorcycle']
box_9 = ['gloves', 'fish', 'pot', 'tiger']
box_10 = []
box_11 = ['sun', 'chair']
box_12 = ['plane', 'keyboard', 'paint', 'shoes']

# Swap storm in Box 7 with necklace in Box 3
box_7.remove('storm')
box_3.remove('necklace')
box_7.append('necklace')
box_3.append('storm')

# Remove dice from Box 2
box_2.remove('dice')

# Replace sandals with microwave in Box 6
box_6.remove('sandals')
box_6.append('microwave')

# Remove branch from Box 7
box_7.remove('branch')

# Remove fish, gloves, and pot from Box 9
box_9.remove('fish')
box_9.remove('gloves')
box_9.remove('pot')

# Put usb and wire into Box 11
box_11.append('usb')
box_11.append('wire')

# Move microwave from Box 6 to Box 7
box_6.remove('microwave')
box_7.append('microwave')

# Move necklace from Box 7 to Box 8
box_7.remove('necklace')
box_8.append('necklace')

# Put apple, scissors, and shoe into Box 3
box_0.remove('apple')
box_0.remove('shoe')
box_3.append('apple')
box_3.append('shoe')

# Remove microwave from Box 7
box_7.remove('microwave')

# Remove grinder from Box 7
box_7.remove('grinder')

# Move motorcycle from Box 8 to Box 6
box_8.remove('motorcycle')
box_6.append('motorcycle')

# Move tiger from Box 9 to Box 6
box_9.remove('tiger')
box_6.append('tiger')

# Remove polish from Box 1
box_1.remove('polish')

# Swap octopus in Box 8 with whistle in Box 3
box_8.remove('octopus')
box_3.remove('whistle')
box_8.append('whistle')
box_3.append('octopus')

# Remove plane from Box 12
box_12.remove('plane')

# Move usb and wire from Box 11 to Box 3
box_11.remove('usb')
box_11.remove('wire')
box_3.append('usb')
box_3.append('wire')

# Move wig, apple, and shoe from Box 0 to Box 3
box_0.remove('wig')
box_0.remove('apple')
box_0.remove('shoe')
box_3.append('wig')
box_3.append('apple')
box_3.append('shoe')

# Put cloud and bear into Box 5
box_5.append('cloud')
box_5.append('bear')

# Move storm, wire, and apple from Box 3 to Box 11
box_3.remove('storm')
box_3.remove('wire')
box_3.remove('apple')
box_11.append('storm')
box_11.append('wire')
box_11.append('apple')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]):
    print(f"Box {i}: {box}")