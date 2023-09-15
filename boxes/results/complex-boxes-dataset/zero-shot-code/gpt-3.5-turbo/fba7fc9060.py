box_0 = ['umbrella', 'river', 'octopus', 'scarf']
box_1 = ['bag', 'whistle', 'coral', 'mountain', 'bird']
box_2 = ['beach', 'shorts', 'brush', 'telescope', 'pot']
box_3 = ['bell']
box_4 = ['boot', 'mixer', 'dress', 'flute', 'oven']
box_5 = ['lightning']
box_6 = []

# Replace the umbrella with the coin in Box 0
box_0.remove('umbrella')
box_0.append('coin')

# Put the lipstick and the train and the earring into Box 6
box_6.extend(['lipstick', 'train', 'earring'])

# Remove the mixer and the boot from Box 4
box_4.remove('mixer')
box_4.remove('boot')

# Put the forest into Box 2
box_2.append('forest')

# Remove the coin and the octopus from Box 0
box_0.remove('coin')
box_0.remove('octopus')

# Swap the lipstick in Box 6 with the scarf in Box 0
box_0.remove('scarf')
box_6.remove('lipstick')
box_0.append('lipstick')
box_6.append('scarf')

# Replace the bag and the bird and the mountain with the piano and the microscope and the storm in Box 1
box_1.remove('bag')
box_1.remove('bird')
box_1.remove('mountain')
box_1.extend(['piano', 'microscope', 'storm'])

# Swap the river in Box 0 with the dress in Box 4
box_0.remove('river')
box_4.remove('dress')
box_0.append('dress')
box_4.append('river')

# Move the shorts and the forest and the beach from Box 2 to Box 3
box_2.remove('shorts')
box_2.remove('forest')
box_2.remove('beach')
box_3.extend(['shorts', 'forest', 'beach'])

# Swap the earring in Box 6 with the dress in Box 0
box_6.remove('earring')
box_0.remove('dress')
box_6.append('dress')
box_0.append('earring')

# Swap the forest in Box 3 with the earring in Box 0
box_3.remove('forest')
box_0.remove('earring')
box_3.append('earring')
box_0.append('forest')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)