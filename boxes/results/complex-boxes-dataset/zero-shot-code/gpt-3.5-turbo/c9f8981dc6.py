box0 = ['moon', 'hat', 'scissors']
box1 = ['keyboard']
box2 = ['microwave']
box3 = ['car', 'octopus', 'thunder', 'clock']
box4 = ['makeup']
box5 = []
box6 = []

# Move the makeup from Box 4 to Box 3
box3.extend(box4)
box4 = []

# Replace the microwave with the plane in Box 2
box2 = ['plane']

# Empty Box 0
box0 = []

# Put the zipper and the starfish into Box 5
box5.extend(['zipper', 'starfish'])

# Put the lightning and the wig into Box 6
box6.extend(['lightning', 'wig'])

# Put the cat into Box 5
box5.append('cat')

# Empty Box 3
box3 = []

# Move the cat from Box 5 to Box 0
box0.append(box5.pop(box5.index('cat')))

# Put the apple into Box 2
box2.append('apple')

# Remove the plane from Box 2
box2 = []

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)