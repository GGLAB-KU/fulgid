box_0 = ['fish', 'star', 'river', 'lightning']
box_1 = ['cat', 'toothpaste', 'tape', 'coin', 'wire']
box_2 = ['tiger', 'planet']
box_3 = ['shark', 'sun', 'lion', 'boot']
box_4 = []
box_5 = ['toy']
box_6 = ['table', 'dress', 'drum', 'tie', 'seaweed']
box_7 = ['horn', 'doll', 'swimsuit', 'plane', 'shampoo']

# Put the phone and the snow into Box 0
box_0.extend(['phone', 'snow'])

# Replace the seaweed and the tie with the vase and the sun in Box 6
box_6.remove('seaweed')
box_6.remove('tie')
box_6.extend(['vase', 'sun'])

# Remove the boot and the shark from Box 3
box_3.remove('boot')
box_3.remove('shark')

# Move the lightning and the phone and the star from Box 0 to Box 4
box_4.extend(['lightning', 'phone', 'star'])
box_0.remove('lightning')
box_0.remove('phone')
box_0.remove('star')

# Remove the tiger from Box 2
box_2.remove('tiger')

# Move the wire and the cat and the tape from Box 1 to Box 6
box_6.extend(['wire', 'cat', 'tape'])
box_1.remove('wire')
box_1.remove('cat')
box_1.remove('tape')

# Move the toy from Box 5 to Box 0
box_0.append('toy')
box_5.remove('toy')

# Put the lion and the ship into Box 3
box_3.extend(['lion', 'ship'])

# Move the lightning and the star from Box 4 to Box 3
box_3.extend(['lightning', 'star'])
box_4.remove('lightning')
box_4.remove('star')

# Swap the phone in Box 4 with the planet in Box 2
box_4.remove('phone')
box_2.remove('planet')
box_4.append('planet')
box_2.append('phone')

# Swap the toothpaste in Box 1 with the sun in Box 3
box_1.remove('toothpaste')
box_3.remove('sun')
box_1.append('sun')
box_3.append('toothpaste')

# Remove the doll and the shampoo from Box 7
box_7.remove('doll')
box_7.remove('shampoo')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)