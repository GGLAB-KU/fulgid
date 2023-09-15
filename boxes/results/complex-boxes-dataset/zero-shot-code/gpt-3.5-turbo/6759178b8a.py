box_0 = ['doll', 'candle']
box_1 = ['scarf', 'thunder', 'beach', 'toy']
box_2 = ['charger', 'microwave', 'bird', 'cat']
box_3 = ['hat']
box_4 = ['towel']
box_5 = ['cup', 'desert', 'cloud', 'butterfly', 'ship']
box_6 = []
box_7 = ['grinder', 'river', 'bag']

# Remove the toy, beach, and scarf from Box 1
box_1.remove('toy')
box_1.remove('beach')
box_1.remove('scarf')

# Replace the towel with the octopus in Box 4
box_4.remove('towel')
box_4.append('octopus')

# Put the fridge, soap, and wig into Box 7
box_7.append('fridge')
box_7.append('soap')
box_7.append('wig')

# Move the bag from Box 7 to Box 6
box_6.append(box_7.pop(box_7.index('bag')))

# Swap the octopus in Box 4 with the candle in Box 0
box_0.remove('candle')
box_0.append('octopus')
box_4.remove('octopus')
box_4.append('candle')

# Replace the grinder and fridge with the gloves and magnet in Box 7
box_7.remove('grinder')
box_7.remove('fridge')
box_7.append('gloves')
box_7.append('magnet')

# Put the tiger into Box 6
box_6.append('tiger')

# Move the hat from Box 3 to Box 0
box_0.append(box_3.pop())

# Remove the river, magnet, and soap from Box 7
box_7.remove('river')
box_7.remove('magnet')
box_7.remove('soap')

# Remove the bag from Box 6
box_6.remove('bag')

# Empty Box 7
box_7 = []

# Replace the candle with the bell in Box 4
box_4.remove('candle')
box_4.append('bell')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)