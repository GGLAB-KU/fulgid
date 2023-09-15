box_0 = ['phone', 'oven', 'keyboard', 'pan']
box_1 = ['controller']
box_2 = ['brush']
box_3 = ['necklace', 'table', 'lipstick']
box_4 = ['bicycle']
box_5 = ['grinder', 'plane', 'butterfly', 'forest', 'motorcycle']
box_6 = ['laptop']
box_7 = ['ship']
box_8 = ['toaster', 'submarine']

# Replace the lipstick with the mask in Box 3
box_3.remove('lipstick')
box_3.append('mask')

# Replace the toaster with the coat in Box 8
box_8.remove('toaster')
box_8.append('coat')

# Swap the pan in Box 0 with the motorcycle in Box 5
box_0.remove('pan')
box_5.remove('motorcycle')
box_0.append('motorcycle')
box_5.append('pan')

# Replace the oven and the motorcycle and the keyboard with the horse and the tiger and the lion in Box 0
box_0.remove('oven')
box_0.remove('motorcycle')
box_0.remove('keyboard')
box_0.append('horse')
box_0.append('tiger')
box_0.append('lion')

# Move the brush from Box 2 to Box 1
box_2.remove('brush')
box_1.append('brush')

# Remove the brush from Box 1
box_1.remove('brush')

# Put the octopus and the sock and the spoon into Box 7
box_7.extend(['octopus', 'sock', 'spoon'])

# Replace the tiger with the ocean in Box 0
box_0.remove('tiger')
box_0.append('ocean')

# Put the lightning and the lock into Box 6
box_6.extend(['lightning', 'lock'])

# Replace the mask and the necklace with the book and the dog in Box 3
box_3.remove('mask')
box_3.remove('necklace')
box_3.append('book')
box_3.append('dog')

# Put the shorts and the headphone into Box 6
box_6.extend(['shorts', 'headphone'])

# Put the basket into Box 8
box_8.append('basket')

# Swap the controller in Box 1 with the octopus in Box 7
box_1.remove('controller')
box_7.remove('octopus')
box_1.append('octopus')
box_7.append('controller')

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