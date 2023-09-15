box_0 = ['elephant', 'grass', 'dress']
box_1 = ['bear', 'watch']
box_2 = ['hat', 'desert', 'scarf', 'cup']
box_3 = []
box_4 = ['skirt', 'shark', 'tape', 'bag', 'console']
box_5 = ['seaweed', 'forest']
box_6 = ['belt', 'plate', 'lock', 'vase', 'sock']

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)

# Move the bear and the watch from Box 1 to Box 6
box_6.extend(box_1)
box_1.clear()

# Replace the seaweed and the forest with the makeup and the snow in Box 5
box_5 = ['makeup', 'snow']

# Remove the watch and the bear from Box 6
box_6.remove('watch')
box_6.remove('bear')

# Move the vase and the lock from Box 6 to Box 1
box_1.extend(['vase', 'lock'])
box_6.remove('vase')
box_6.remove('lock')

# Swap the sock in Box 6 with the bag in Box 4
box_6.remove('sock')
box_4.append('sock')
box_4.remove('bag')
box_6.append('bag')

# Move the lock and the vase from Box 1 to Box 2
box_2.extend(['lock', 'vase'])
box_1.remove('lock')
box_1.remove('vase')

# Move the dress and the grass and the elephant from Box 0 to Box 2
box_2.extend(box_0)
box_0.clear()

# Swap the console in Box 4 with the dress in Box 2
box_4.remove('console')
box_2.append('console')
box_2.remove('dress')
box_4.append('dress')

# Remove the bag from Box 6
box_6.remove('bag')

# Put the shampoo and the magnet and the elephant into Box 3
box_3.extend(['shampoo', 'magnet', 'elephant'])

print("\nAfter modifications:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)