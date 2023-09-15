box_0 = ['sock']
box_1 = ['razor', 'seaweed']
box_2 = ['shampoo', 'shorts', 'pan', 'crown']
box_3 = ['rain', 'mirror', 'comet', 'shirt']
box_4 = ['chair', 'piano']
box_5 = ['motorcycle', 'toy']
box_6 = ['shark']

# Move the shark from Box 6 to Box 4
box_4.append(box_6.pop())

# Move the sock from Box 0 to Box 2
box_2.append(box_0.pop())

# Move the razor from Box 1 to Box 4
box_4.append(box_1.pop())

# Put the coat into Box 3
box_3.append('coat')

# Empty Box 1
box_1 = []

# Empty Box 4
box_4 = []

# Put the belt and the oven into Box 6
box_6.extend(['belt', 'oven'])

# Put the bird and the comb and the toy into Box 4
box_4.extend(['bird', 'comb', 'toy'])

# Remove the comb and the bird from Box 4
box_4.remove('comb')
box_4.remove('bird')

# Move the belt and the oven from Box 6 to Box 2
box_2.extend(box_6)
box_6 = []

# Replace the coat and the shirt with the forest and the microscope in Box 3
box_3.remove('coat')
box_3.remove('shirt')
box_3.extend(['forest', 'microscope'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)