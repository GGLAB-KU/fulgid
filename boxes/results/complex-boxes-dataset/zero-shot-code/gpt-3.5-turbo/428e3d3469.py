box_0 = ['moon', 'island']
box_1 = ['fork', 'truck', 'belt', 'drum']
box_2 = []
box_3 = ['grass', 'tiger', 'razor', 'branch']
box_4 = ['snow']

# Remove the moon from Box 0
box_0.remove('moon')

# Empty Box 1
box_1.clear()

# Put the toothbrush and the belt into Box 3
box_3.extend(['toothbrush', 'belt'])

# Move the island from Box 0 to Box 2
box_2.append(box_0.pop(0))

# Remove the snow from Box 4
box_4.clear()

# Put the shelf and the bird and the piano into Box 2
box_2.extend(['shelf', 'bird', 'piano'])

# Move the island and the bird from Box 2 to Box 3
box_3.append(box_2.pop(0))
box_3.append(box_2.pop(0))

# Move the bird and the belt and the tiger from Box 3 to Box 0
box_0.extend([box_3.pop(1), box_3.pop(1), box_3.pop(1)])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)