box_0 = ['seaweed', 'controller', 'toothbrush', 'console', 'dolphin']
box_1 = ['frame']
box_2 = ['octopus', 'grass', 'coin']
box_3 = ['truck', 'glove', 'river', 'cloud', 'forest']
box_4 = ['sculpture', 'rocket', 'needle', 'freezer']
box_5 = ['dice', 'shorts']
box_6 = ['zipper', 'plate', 'pot', 'gloves', 'pillow']
box_7 = ['button', 'tiger']
box_8 = ['card', 'star', 'grinder']
box_9 = ['phone', 'sock', 'crown', 'necklace', 'blender']
box_10 = ['perfume', 'headphone', 'violin']
box_11 = ['book']
box_12 = ['usb', 'boat', 'wig', 'meteor', 'vase']
box_13 = ['horn', 'elephant', 'flower', 'rain']

# Put the hat and the boot and the razor into Box 11
box_11.extend(['hat', 'boot', 'razor'])

# Remove the seaweed and the toothbrush from Box 0
box_0.remove('seaweed')
box_0.remove('toothbrush')

# Swap the razor in Box 11 with the wig in Box 12
box_11.remove('razor')
box_12.remove('wig')
box_11.append('wig')
box_12.append('razor')

# Put the octopus and the harmonica and the sculpture into Box 5
box_5.extend(['octopus', 'harmonica', 'sculpture'])

# Move the console and the dolphin and the controller from Box 0 to Box 12
box_12.extend(box_0)
box_0.clear()

# Swap the vase in Box 12 with the frame in Box 1
box_12.remove('vase')
box_1.remove('frame')
box_12.append('frame')
box_1.append('vase')

# Remove the coin and the grass and the octopus from Box 2
box_2.remove('coin')
box_2.remove('grass')
box_2.remove('octopus')

# Remove the pillow and the plate and the zipper from Box 6
box_6.remove('pillow')
box_6.remove('plate')
box_6.remove('zipper')

# Replace the crown and the blender and the necklace with the earring and the forest and the towel in Box 9
box_9.remove('crown')
box_9.remove('blender')
box_9.remove('necklace')
box_9.extend(['earring', 'forest', 'towel'])

# Move the phone from Box 9 to Box 0
box_0.append(box_9.pop(box_9.index('phone')))

# Swap the grinder in Box 8 with the tiger in Box 7
box_8.remove('grinder')
box_7.remove('tiger')
box_8.append('tiger')
box_7.append('grinder')

# Move the violin and the perfume and the headphone from Box 10 to Box 9
box_9.extend(box_10)
box_10.clear()

# Put the butterfly and the pot into Box 12
box_12.extend(['butterfly', 'pot'])

# Swap the perfume in Box 9 with the vase in Box 1
box_9.remove('perfume')
box_1.remove('vase')
box_9.append('vase')
box_1.append('perfume')

# Put the freezer and the star into Box 0
box_0.extend(['freezer', 'star'])

# Empty Box 5
box_5.clear()

# Replace the meteor and the razor and the pot with the coral and the desert and the button in Box 12
box_12.remove('meteor')
box_12.remove('razor')
box_12.remove('pot')
box_12.extend(['coral', 'desert', 'button'])

# Empty Box 1
box_1.clear()

# Put the lipstick into Box 8
box_8.append('lipstick')

# Move the button and the grinder from Box 7 to Box 9
box_9.extend([box_7.pop(box_7.index('button')), box_7.pop(box_7.index('grinder'))])

# Replace the forest and the towel and the violin with the meteor and the octopus and the swimsuit in Box 9
box_9.remove('forest')
box_9.remove('towel')
box_9.remove('violin')
box_9.extend(['meteor', 'octopus', 'swimsuit'])

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
print("Box 13:", box_13)