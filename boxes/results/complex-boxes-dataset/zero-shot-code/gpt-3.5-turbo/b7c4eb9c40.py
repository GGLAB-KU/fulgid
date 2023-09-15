box_0 = ['train', 'butterfly', 'pants', 'spoon', 'lipstick']
box_1 = ['tie']
box_2 = ['blender', 'necklace', 'glove']
box_3 = ['keyboard', 'cat', 'boat', 'moon']
box_4 = ['speaker', 'towel', 'magnet']
box_5 = ['cloud', 'plate', 'coral', 'frame', 'bird']
box_6 = ['cow', 'wire', 'shoe', 'shoes', 'microwave']
box_7 = ['harmonica']
box_8 = ['river', 'grinder', 'helmet', 'apple']
box_9 = ['watch', 'forest']
box_10 = ['gloves', 'toy', 'perfume']

# Put the apple and the key and the ship into Box 0
box_0.extend(['apple', 'key', 'ship'])

# Swap the harmonica in Box 7 with the pants in Box 0
box_0.remove('pants')
box_7.remove('harmonica')
box_0.append('harmonica')
box_7.append('pants')

# Put the speaker and the plate into Box 8
box_8.extend(['speaker', 'plate'])

# Move the ship from Box 0 to Box 3
box_0.remove('ship')
box_3.append('ship')

# Swap the toy in Box 10 with the speaker in Box 8
box_8.remove('speaker')
box_10.remove('toy')
box_8.append('toy')
box_10.append('speaker')

# Put the sandals and the starfish into Box 8
box_8.extend(['sandals', 'starfish'])

# Move the pants from Box 7 to Box 6
box_7.remove('pants')
box_6.append('pants')

# Replace the blender and the necklace and the glove with the card and the planet and the controller in Box 2
box_2.remove('blender')
box_2.remove('necklace')
box_2.remove('glove')
box_2.extend(['card', 'planet', 'controller'])

# Move the helmet and the sandals and the river from Box 8 to Box 9
box_8.remove('helmet')
box_8.remove('sandals')
box_8.remove('river')
box_9.extend(['helmet', 'sandals', 'river'])

# Put the pen and the dog into Box 10
box_10.extend(['pen', 'dog'])

# Put the shirt and the glasses into Box 2
box_2.extend(['shirt', 'glasses'])

# Swap the magnet in Box 4 with the speaker in Box 10
box_4.remove('magnet')
box_10.remove('speaker')
box_4.append('speaker')
box_10.append('magnet')

# Empty Box 4
box_4 = []

# Put the lion and the bird into Box 9
box_9.extend(['lion', 'bird'])

# Replace the coral and the plate with the basket and the tape in Box 5
box_5.remove('coral')
box_5.remove('plate')
box_5.extend(['basket', 'tape'])

# Put the shelf and the doll and the pants into Box 9
box_9.extend(['shelf', 'doll', 'pants'])

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