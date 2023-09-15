box_0 = ['bell', 'headphone', 'dog', 'book', 'speaker']
box_1 = ['dice', 'wig']
box_2 = ['telescope', 'microwave']
box_3 = []
box_4 = ['boot']
box_5 = ['charger', 'rain', 'freezer', 'bear']
box_6 = []
box_7 = ['storm', 'note', 'train', 'lamp']
box_8 = ['drum', 'toothbrush', 'cup', 'pants']
box_9 = ['bicycle', 'magnet', 'tie']
box_10 = ['coral']

# Replace the bicycle with the microscope in Box 9
box_9.remove('bicycle')
box_9.append('microscope')

# Move the dog from Box 0 to Box 9
box_0.remove('dog')
box_9.append('dog')

# Swap the pants in Box 8 with the boot in Box 4
box_8.remove('pants')
box_4.remove('boot')
box_8.append('boot')
box_4.append('pants')

# Replace the charger and the rain with the toothpaste and the zipper in Box 5
box_5.remove('charger')
box_5.remove('rain')
box_5.append('toothpaste')
box_5.append('zipper')

# Remove the microscope from Box 9
box_9.remove('microscope')

# Replace the coral with the fish in Box 10
box_10.remove('coral')
box_10.append('fish')

# Replace the toothpaste and the bear with the leaf and the sandals in Box 5
box_5.remove('toothpaste')
box_5.remove('bear')
box_5.append('leaf')
box_5.append('sandals')

# Swap the pants in Box 4 with the drum in Box 8
box_4.remove('pants')
box_8.remove('drum')
box_4.append('drum')
box_8.append('pants')

# Swap the leaf in Box 5 with the speaker in Box 0
box_5.remove('leaf')
box_0.remove('speaker')
box_5.append('speaker')
box_0.append('leaf')

# Remove the telescope from Box 2
box_2.remove('telescope')

# Put the dress and the oven into Box 9
box_9.append('dress')
box_9.append('oven')

# Remove the dress and the oven from Box 9
box_9.remove('dress')
box_9.remove('oven')

# Remove the microwave from Box 2
box_2.remove('microwave')

# Swap the drum in Box 4 with the train in Box 7
box_4.remove('drum')
box_7.remove('train')
box_4.append('train')
box_7.append('drum')

# Move the freezer and the sandals from Box 5 to Box 1
box_5.remove('freezer')
box_5.remove('sandals')
box_1.append('freezer')
box_1.append('sandals')

# Remove the cup and the toothbrush and the pants from Box 8
box_8.remove('cup')
box_8.remove('toothbrush')
box_8.remove('pants')

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