box0 = ['lock', 'dog']
box1 = []
box2 = ['oven', 'shoe']
box3 = ['magnet', 'frame', 'horse', 'spoon', 'jacket']
box4 = ['camera']
box5 = ['train']
box6 = []

# Swap the train in Box 5 with the magnet in Box 3
box5, box3 = box3, box5

# Swap the magnet in Box 5 with the train in Box 3
box5, box3 = box3, box5

# Remove the train from Box 5
box5 = []

# Move the camera from Box 4 to Box 0
box0.append(box4.pop(0))

# Move the camera and the dog from Box 0 to Box 2
box2.extend([box0.pop(1), box0.pop(0)])

# Remove the dog and the shoe and the oven from Box 2
box2 = []

# Put the gloves into Box 5
box5.append('gloves')

# Move the frame and the jacket and the magnet from Box 3 to Box 0
box0.extend([box3.pop(1), box3.pop(0), box3.pop(0)])

# Replace the magnet and the jacket with the coin and the microwave in Box 0
box0[0] = 'coin'
box0.append('microwave')

# Swap the coin in Box 0 with the spoon in Box 3
box0[0], box3[3] = box3[3], box0[0]

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)