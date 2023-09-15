box_0 = []
box_1 = []
box_2 = ['zipper', 'coat', 'key']
box_3 = ['mixer', 'dog', 'meteor', 'thunder']
box_4 = ['charger', 'crown']
box_5 = []
box_6 = []
box_7 = ['toaster', 'dice']
box_8 = ['jacket', 'shirt', 'rock', 'butterfly']
box_9 = ['keyboard', 'drum', 'button']
box_10 = ['towel', 'makeup']
box_11 = ['chair', 'spoon', 'wallet', 'flute', 'controller']
box_12 = []

# Remove toaster and dice from Box 7
box_7.remove('toaster')
box_7.remove('dice')

# Put lipstick, umbrella, and planet into Box 1
box_1.append('lipstick')
box_1.append('umbrella')
box_1.append('planet')

# Swap towel in Box 10 with key in Box 2
box_10.remove('towel')
box_2.remove('key')
box_10.append('key')
box_2.append('towel')

# Move crown from Box 4 to Box 7
box_4.remove('crown')
box_7.append('crown')

# Remove makeup and key from Box 10
box_10.remove('makeup')
box_10.remove('key')

# Remove rock, jacket, and shirt from Box 8
box_8.remove('rock')
box_8.remove('jacket')
box_8.remove('shirt')

# Replace mixer and meteor with island and forest in Box 3
box_3.remove('mixer')
box_3.remove('meteor')
box_3.append('island')
box_3.append('forest')

# Remove island, forest, and dog from Box 3
box_3.remove('island')
box_3.remove('forest')
box_3.remove('dog')

# Move charger from Box 4 to Box 5
box_4.remove('charger')
box_5.append('charger')

# Put key and chair into Box 10
box_10.append('key')
box_10.append('chair')

# Swap wallet in Box 11 with umbrella in Box 1
box_11.remove('wallet')
box_1.remove('umbrella')
box_11.append('umbrella')
box_1.append('wallet')

# Remove key from Box 10
box_10.remove('key')

# Remove crown from Box 7
box_7.remove('crown')

# Move chair from Box 10 to Box 6
box_10.remove('chair')
box_6.append('chair')

# Put truck into Box 3
box_3.append('truck')

# Swap lipstick in Box 1 with charger in Box 5
box_1.remove('lipstick')
box_5.remove('charger')
box_1.append('charger')
box_5.append('lipstick')

# Replace lipstick with microwave in Box 5
box_5.remove('lipstick')
box_5.append('microwave')

# Swap keyboard in Box 9 with butterfly in Box 8
box_9.remove('keyboard')
box_8.remove('butterfly')
box_9.append('butterfly')
box_8.append('keyboard')

# Move spoon, controller, and umbrella from Box 11 to Box 0
box_11.remove('spoon')
box_11.remove('controller')
box_11.remove('umbrella')
box_0.append('spoon')
box_0.append('controller')
box_0.append('umbrella')

# Remove chair from Box 6
box_6.remove('chair')

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
print("Box 11:", box_11)
print("Box 12:", box_12)