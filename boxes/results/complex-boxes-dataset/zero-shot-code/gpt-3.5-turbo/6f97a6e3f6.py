box_0 = ['drum', 'note', 'mixer', 'sun']
box_1 = ['train', 'plate']
box_2 = ['thunder']
box_3 = ['toy', 'bowl', 'phone', 'butterfly', 'charger']
box_4 = []

# Remove the blender from Box 0
box_0.remove('blender')

# Replace the toy and the charger with the doll and the bird in Box 3
box_3.remove('toy')
box_3.remove('charger')
box_3.append('doll')
box_3.append('bird')

# Remove the bowl and the doll from Box 3
box_3.remove('bowl')
box_3.remove('doll')

# Put the pillow and the flower into Box 1
box_1.append('pillow')
box_1.append('flower')

# Replace the thunder with the shelf in Box 2
box_2.remove('thunder')
box_2.append('shelf')

# Replace the butterfly with the skirt in Box 3
box_3.remove('butterfly')
box_3.append('skirt')

# Put the shark into Box 0
box_0.append('shark')

# Replace the plate and the pillow with the cup and the towel in Box 1
box_1.remove('plate')
box_1.remove('pillow')
box_1.append('cup')
box_1.append('towel')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)