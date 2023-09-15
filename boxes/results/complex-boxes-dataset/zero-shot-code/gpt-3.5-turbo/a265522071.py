box0 = ['sun', 'moon', 'plane', 'submarine']
box1 = ['shoes', 'cloud', 'whistle', 'car', 'drum']
box2 = []
box3 = ['thunder']

# Put the dice and the bell into Box 1
box1.extend(['dice', 'bell'])

# Move the sun and the submarine and the plane from Box 0 to Box 1
box1.extend(box0[:3])
box0 = box0[3:]

# Replace the thunder with the blanket in Box 3
box3 = ['blanket']

# Replace the moon with the plate in Box 0
box0[1] = 'plate'

# Put the flower and the sock into Box 3
box3.extend(['flower', 'sock'])

# Remove the plate from Box 0
box0.remove('plate')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)