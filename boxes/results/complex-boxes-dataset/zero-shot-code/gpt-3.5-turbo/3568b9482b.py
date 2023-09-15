box_0 = ['needle', 'ring', 'puzzle']
box_1 = ['ocean']
box_2 = []
box_3 = ['wig']
box_4 = ['microwave', 'fish', 'shoes', 'coat']
box_5 = []
box_6 = ['speaker', 'helmet']
box_7 = ['violin', 'forest', 'tree']
box_8 = ['leaf', 'toothpaste']
box_9 = []
box_10 = ['soap', 'zipper', 'guitar', 'cloud', 'ship']

# Swap the wig in Box 3 with the helmet in Box 6
box_3.remove('wig')
box_6.remove('helmet')
box_3.append('helmet')
box_6.append('wig')

# Put the skirt and the bag and the dog into Box 5
box_5.extend(['skirt', 'bag', 'dog'])

# Put the perfume into Box 2
box_2.append('perfume')

# Put the apple and the shark and the bag into Box 9
box_9.extend(['apple', 'shark', 'bag'])

# Move the shark and the bag and the apple from Box 9 to Box 2
box_2.extend(box_9)
box_9.clear()

# Remove the ocean from Box 1
box_1.clear()

# Empty Box 3
box_3.clear()

# Move the dog and the skirt and the bag from Box 5 to Box 3
box_3.extend(box_5)
box_5.clear()

# Replace the leaf and the toothpaste with the butterfly and the mountain in Box 8
box_8.remove('leaf')
box_8.remove('toothpaste')
box_8.extend(['butterfly', 'mountain'])

# Remove the wig and the speaker from Box 6
box_6.remove('wig')
box_6.remove('speaker')

# Remove the perfume from Box 2
box_2.remove('perfume')

# Replace the apple and the bag with the whistle and the plate in Box 2
box_2.remove('apple')
box_2.remove('bag')
box_2.extend(['whistle', 'plate'])

# Swap the shoes in Box 4 with the tree in Box 7
box_4.remove('shoes')
box_7.remove('tree')
box_4.append('tree')
box_7.append('shoes')

# Put the starfish into Box 7
box_7.append('starfish')

# Replace the butterfly with the toothpaste in Box 8
box_8.remove('butterfly')
box_8.append('toothpaste')

# Remove the zipper and the cloud from Box 10
box_10.remove('zipper')
box_10.remove('cloud')

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