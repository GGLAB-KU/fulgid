box_0 = ['makeup']
box_1 = ['violin', 'sun']
box_2 = ['ship', 'piano', 'shark', 'skirt']
box_3 = ['octopus', 'hat', 'towel', 'cup', 'dolphin']

# Remove the octopus from Box 3
box_3.remove('octopus')

# Move the makeup from Box 0 to Box 2
box_2.append(box_0.pop(0))

# Move the sun from Box 1 to Box 2
box_2.append(box_1.pop(1))

# Empty Box 2
box_2.clear()

# Empty Box 3
box_3.clear()

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)