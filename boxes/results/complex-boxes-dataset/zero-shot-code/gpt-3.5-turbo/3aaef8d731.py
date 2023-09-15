box_0 = []
box_1 = ['blender']
box_2 = ['moon', 'magnet', 'harmonica', 'paint', 'coat']
box_3 = ['polish', 'sculpture', 'bear', 'hat', 'grinder']
box_4 = ['bowl', 'flute', 'toothpaste', 'skirt', 'car']
box_5 = ['spoon', 'rock', 'plane', 'shark', 'island']
box_6 = ['horse', 'doll']
box_7 = ['umbrella', 'telescope', 'whistle']

# Swap the skirt in Box 4 with the spoon in Box 5
box_4[3], box_5[0] = box_5[0], box_4[3]

# Move the doll from Box 6 to Box 3
box_3.append(box_6.pop())

# Put the speaker into Box 5
box_5.append('speaker')

# Swap the car in Box 4 with the horse in Box 6
box_4[4], box_6[0] = box_6[0], box_4[4]

# Remove the hat from Box 3
box_3.remove('hat')

# Remove the rock and the speaker from Box 5
box_5.remove('rock')
box_5.remove('speaker')

# Swap the whistle in Box 7 with the plane in Box 5
box_7[2], box_5[2] = box_5[2], box_7[2]

# Put the tie into Box 5
box_5.append('tie')

# Put the leaf and the wallet into Box 1
box_1.extend(['leaf', 'wallet'])

# Move the plane and the telescope from Box 7 to Box 5
box_5.extend(box_7[1:3])
box_7[1:3] = []

# Put the cat into Box 4
box_4.append('cat')

# Move the flute from Box 4 to Box 0
box_0.append(box_4.pop(1))

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)