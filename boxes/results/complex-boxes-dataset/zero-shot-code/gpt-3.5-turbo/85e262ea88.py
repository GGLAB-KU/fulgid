box_0 = ['cat', 'telescope', 'glove']
box_1 = ['truck']
box_2 = ['seaweed', 'bear', 'moon', 'sock']
box_3 = ['bowl', 'umbrella']
box_4 = ['horse', 'rock', 'gloves']
box_5 = ['cloud', 'forest', 'book']

# Swap the moon in Box 2 with the forest in Box 5
box_2[box_2.index('moon')] = 'forest'
box_5[box_5.index('forest')] = 'moon'

# Replace the horse and the rock and the gloves with the mask and the cloud and the wig in Box 4
box_4 = ['mask', 'cloud', 'wig']

# Swap the truck in Box 1 with the wig in Box 4
box_1[box_1.index('truck')] = 'wig'
box_4[box_4.index('wig')] = 'truck'

# Swap the bear in Box 2 with the wig in Box 1
box_2[box_2.index('bear')] = 'wig'
box_1[box_1.index('wig')] = 'bear'

# Swap the bear in Box 1 with the moon in Box 5
box_1[box_1.index('bear')] = 'moon'
box_5[box_5.index('moon')] = 'bear'

# Remove the sock from Box 2
box_2.remove('sock')

# Remove the bowl from Box 3
box_3.remove('bowl')

# Remove the umbrella from Box 3
box_3.remove('umbrella')

# Swap the moon in Box 1 with the wig in Box 2
box_1[box_1.index('moon')] = 'wig'
box_2[box_2.index('wig')] = 'moon'

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)