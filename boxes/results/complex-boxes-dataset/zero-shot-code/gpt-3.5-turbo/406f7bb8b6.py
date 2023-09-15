box_0 = []
box_1 = ['desert', 'rocket', 'dice', 'island', 'star']
box_2 = ['car', 'belt', 'frame', 'toy']
box_3 = ['shorts', 'dolphin', 'flower']
box_4 = ['submarine', 'needle', 'skirt', 'ocean', 'comb']
box_5 = ['doll', 'piano', 'cloud']
box_6 = []
box_7 = ['pan', 'clock', 'charger', 'helmet', 'fish']
box_8 = ['ship', 'shelf', 'pot', 'dog']
box_9 = ['guitar', 'blender', 'thread', 'shampoo', 'makeup']
box_10 = ['lamp']

# Put the doll and the soap and the motorcycle into Box 7
box_7.extend(['doll', 'soap', 'motorcycle'])

# Move the comb from Box 4 to Box 0
box_0.append(box_4.pop(box_4.index('comb')))

# Remove the submarine and the needle from Box 4
box_4.remove('submarine')
box_4.remove('needle')

# Move the toy and the belt and the car from Box 2 to Box 10
box_10.extend(box_2)
box_2.clear()

# Move the makeup and the guitar and the blender from Box 9 to Box 6
box_6.extend(box_9)
box_9.clear()

# Replace the frame with the dog in Box 2
box_2.append('dog')
box_2.remove('frame')

# Put the blender and the truck and the lock into Box 1
box_1.extend(['blender', 'truck', 'lock'])

# Move the dog from Box 2 to Box 1
box_1.append(box_2.pop(box_2.index('dog')))

# Put the sandals and the toaster into Box 9
box_9.extend(['sandals', 'toaster'])

# Remove the blender and the makeup from Box 6
box_6.remove('blender')
box_6.remove('makeup')

# Empty Box 7
box_7.clear()

# Replace the shampoo and the sandals and the toaster with the console and the rain and the car in Box 9
box_9 = ['console', 'rain', 'car']

# Swap the comb in Box 0 with the guitar in Box 6
box_0.append(box_6.pop(box_6.index('guitar')))
box_6.append('comb')

# Swap the console in Box 9 with the truck in Box 1
box_9.append(box_1.pop(box_1.index('truck')))
box_1.append('console')

# Replace the car and the belt and the lamp with the thread and the rocket and the keyboard in Box 10
box_10.extend(['thread', 'rocket', 'keyboard'])
box_10.remove('car')
box_10.remove('belt')
box_10.remove('lamp')

# Replace the piano with the butterfly in Box 5
box_5.remove('piano')
box_5.append('butterfly')

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