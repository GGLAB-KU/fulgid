box_0 = ['sculpture', 'blanket']
box_1 = ['basket', 'glove', 'glasses', 'car', 'blender']
box_2 = ['sandals', 'moon', 'controller']
box_3 = ['hat']
box_4 = ['mixer']
box_5 = ['dolphin', 'shampoo', 'book', 'helmet']

# Replace the blanket with the dress in Box 0
box_0.remove('blanket')
box_0.append('dress')

# Move the glasses and the blender from Box 1 to Box 3
box_1.remove('glasses')
box_1.remove('blender')
box_3.append('glasses')
box_3.append('blender')

# Replace the mixer with the horse in Box 4
box_4.remove('mixer')
box_4.append('horse')

# Remove the sculpture from Box 0
box_0.remove('sculpture')

# Remove the hat and the blender and the glasses from Box 3
box_3.remove('hat')
box_3.remove('blender')
box_3.remove('glasses')

# Swap the car in Box 1 with the horse in Box 4
box_1.remove('car')
box_4.remove('horse')
box_1.append('horse')
box_4.append('car')

# Swap the dress in Box 0 with the dolphin in Box 5
box_0.remove('dress')
box_5.remove('dolphin')
box_0.append('dolphin')
box_5.append('dress')

# Put the toy and the dog into Box 2
box_2.append('toy')
box_2.append('dog')

# Empty Box 4
box_4 = []

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)