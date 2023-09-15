box_0 = ['button', 'scissors', 'blender']
box_1 = ['polish', 'cat']
box_2 = ['horn', 'guitar']
box_3 = ['shelf']
box_4 = ['seaweed', 'leaf', 'necklace']
box_5 = []
box_6 = ['mountain']
box_7 = ['coin', 'camera', 'cow', 'sun', 'fridge']
box_8 = ['snow', 'branch', 'rain', 'wire', 'speaker']
box_9 = ['gloves', 'ocean', 'pot']
box_10 = ['storm', 'sandals']

# Swap the blender in Box 0 with the sandals in Box 10
box_0.remove('blender')
box_10.remove('sandals')
box_0.append('sandals')
box_10.append('blender')

# Move the blender from Box 10 to Box 8
box_10.remove('blender')
box_8.append('blender')

# Swap the cow in Box 7 with the mountain in Box 6
box_7.remove('cow')
box_6.remove('mountain')
box_7.append('mountain')
box_6.append('cow')

# Put the dog and the butterfly and the grinder into Box 6
box_6.extend(['dog', 'butterfly', 'grinder'])

# Put the perfume into Box 2
box_2.append('perfume')

# Put the fridge and the coral and the shorts into Box 5
box_5.extend(['fridge', 'coral', 'shorts'])

# Replace the blender and the wire and the speaker with the necklace and the coin and the starfish in Box 8
box_8.remove('blender')
box_8.remove('wire')
box_8.remove('speaker')
box_8.extend(['necklace', 'coin', 'starfish'])

# Swap the perfume in Box 2 with the fridge in Box 7
box_2.remove('perfume')
box_7.remove('fridge')
box_2.append('fridge')
box_7.append('perfume')

# Replace the storm with the violin in Box 10
box_10.remove('storm')
box_10.append('violin')

# Put the freezer into Box 9
box_9.append('freezer')

# Remove the branch and the starfish and the necklace from Box 8
box_8.remove('branch')
box_8.remove('starfish')
box_8.remove('necklace')

# Remove the polish and the cat from Box 1
box_1.remove('polish')
box_1.remove('cat')

# Swap the gloves in Box 9 with the grinder in Box 6
box_9.remove('gloves')
box_6.remove('grinder')
box_9.append('grinder')
box_6.append('gloves')

# Put the wallet into Box 4
box_4.append('wallet')

# Put the wire and the moon into Box 5
box_5.extend(['wire', 'moon'])

# Empty Box 6
box_6 = []

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