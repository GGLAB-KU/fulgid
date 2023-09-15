box_0 = ['cat', 'pen']
box_1 = ['coral', 'brush', 'mixer']
box_2 = ['bus', 'toy', 'swimsuit', 'sun', 'fork']
box_3 = []
box_4 = []
box_5 = []
box_6 = ['drum', 'microscope', 'wire', 'rocket']
box_7 = ['doll', 'dog', 'button', 'boot']
box_8 = ['chair', 'harmonica', 'sculpture', 'wallet']
box_9 = []
box_10 = ['speaker', 'rock', 'apple', 'fish', 'perfume']
box_11 = ['lion', 'bell', 'shelf', 'jacket', 'microwave']
box_12 = []

# Move the toy and the swimsuit and the bus from Box 2 to Box 1
box_1.extend([box_2.pop(box_2.index('toy'))])
box_1.extend([box_2.pop(box_2.index('swimsuit'))])
box_1.extend([box_2.pop(box_2.index('bus'))])

# Replace the speaker and the perfume and the apple with the cat and the belt and the branch in Box 10
box_10.remove('speaker')
box_10.remove('perfume')
box_10.remove('apple')
box_10.extend(['cat', 'belt', 'branch'])

# Remove the sun and the fork from Box 2
box_2.remove('sun')
box_2.remove('fork')

# Put the shampoo and the bag into Box 5
box_5.extend(['shampoo', 'bag'])

# Move the dog and the doll from Box 7 to Box 12
box_12.extend([box_7.pop(box_7.index('dog'))])
box_12.extend([box_7.pop(box_7.index('doll'))])

# Replace the wire and the microscope and the rocket with the battery and the pot and the moon in Box 6
box_6.remove('wire')
box_6.remove('microscope')
box_6.remove('rocket')
box_6.extend(['battery', 'pot', 'moon'])

# Move the harmonica and the sculpture from Box 8 to Box 6
box_6.extend([box_8.pop(box_8.index('harmonica'))])
box_6.extend([box_8.pop(box_8.index('sculpture'))])

# Replace the rock and the cat with the helmet and the hat in Box 10
box_10.remove('rock')
box_10.remove('cat')
box_10.extend(['helmet', 'hat'])

# Remove the harmonica from Box 6
box_6.remove('harmonica')

# Empty Box 5
box_5.clear()

# Move the doll from Box 12 to Box 11
box_11.extend([box_12.pop(box_12.index('doll'))])

# Swap the dog in Box 12 with the boot in Box 7
box_12.extend([box_7.pop(box_7.index('dog'))])
box_7.extend([box_12.pop(box_12.index('boot'))])

# Move the bus and the coral from Box 1 to Box 11
box_11.extend([box_1.pop(box_1.index('bus'))])
box_11.extend([box_1.pop(box_1.index('coral'))])

# Swap the swimsuit in Box 1 with the microwave in Box 11
box_1.extend([box_11.pop(box_11.index('microwave'))])
box_11.extend([box_1.pop(box_1.index('swimsuit'))])

# Remove the pen and the cat from Box 0
box_0.remove('pen')
box_0.remove('cat')

# Replace the brush and the microwave and the toy with the scissors and the belt and the forest in Box 1
box_1.remove('brush')
box_1.remove('microwave')
box_1.remove('toy')
box_1.extend(['scissors', 'belt', 'forest'])

# Remove the chair and the wallet from Box 8
box_8.remove('chair')
box_8.remove('wallet')

# Move the forest and the scissors and the belt from Box 1 to Box 4
box_4.extend([box_1.pop(box_1.index('forest'))])
box_4.extend([box_1.pop(box_1.index('scissors'))])
box_4.extend([box_1.pop(box_1.index('belt'))])

# Put the horn and the star and the river into Box 3
box_3.extend(['horn', 'star', 'river'])

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