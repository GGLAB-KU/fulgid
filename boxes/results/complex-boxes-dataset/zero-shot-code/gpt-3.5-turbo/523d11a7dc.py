box_0 = ['sock', 'lion', 'wire', 'tiger', 'towel']
box_1 = ['bird', 'shark']
box_2 = ['watch', 'paint', 'horse']
box_3 = ['lightning', 'drum', 'toaster', 'crown', 'bus']
box_4 = ['needle']
box_5 = ['shirt', 'meteor', 'rain', 'glove']
box_6 = ['jacket', 'dog', 'basket']
box_7 = ['phone', 'wallet', 'ocean']

# Put the wire and the razor and the horse into Box 0
box_0.extend(['wire', 'razor', 'horse'])

# Remove the watch and the paint and the horse from Box 2
box_2.remove('watch')
box_2.remove('paint')
box_2.remove('horse')

# Remove the bird from Box 1
box_1.remove('bird')

# Swap the shirt in Box 5 with the phone in Box 7
box_5.remove('shirt')
box_7.remove('phone')
box_5.append('phone')
box_7.append('shirt')

# Replace the shark with the cow in Box 1
box_1.remove('shark')
box_1.append('cow')

# Move the needle from Box 4 to Box 0
box_4.remove('needle')
box_0.append('needle')

# Move the toaster and the lightning from Box 3 to Box 4
box_3.remove('toaster')
box_3.remove('lightning')
box_4.extend(['toaster', 'lightning'])

# Remove the crown and the bus and the drum from Box 3
box_3.remove('crown')
box_3.remove('bus')
box_3.remove('drum')

# Put the oven into Box 7
box_7.append('oven')

# Swap the dog in Box 6 with the phone in Box 5
box_6.remove('dog')
box_5.remove('phone')
box_6.append('phone')
box_5.append('dog')

# Replace the meteor and the rain with the sandals and the button in Box 5
box_5.remove('meteor')
box_5.remove('rain')
box_5.extend(['sandals', 'button'])

# Remove the cow from Box 1
box_1.remove('cow')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)