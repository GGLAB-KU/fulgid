box_0 = ['shark', 'controller', 'jacket', 'plate', 'seaweed']
box_1 = []
box_2 = []
box_3 = ['starfish', 'toothpaste', 'scarf']
box_4 = ['paint', 'coral', 'violin', 'phone', 'glasses']
box_5 = ['lightning']
box_6 = []
box_7 = ['spoon', 'shoes', 'tape', 'apple', 'speaker']

# Replace the controller with the guitar in Box 0
box_0[1] = 'guitar'

# Remove the paint and the violin from Box 4
box_4.remove('paint')
box_4.remove('violin')

# Remove the apple and the speaker from Box 7
box_7.remove('apple')
box_7.remove('speaker')

# Replace the scarf with the star in Box 3
box_3[2] = 'star'

# Move the lightning from Box 5 to Box 6
box_6.append(box_5.pop())

# Remove the tape and the shoes and the spoon from Box 7
box_7.remove('tape')
box_7.remove('shoes')
box_7.remove('spoon')

# Remove the lightning from Box 6
box_6.pop()

# Replace the toothpaste with the headphone in Box 3
box_3[1] = 'headphone'

# Move the shark from Box 0 to Box 4
box_4.append(box_0.pop(0))

# Put the shark and the seaweed into Box 3
box_3.extend([box_0.pop(0), box_0.pop(0)])

# Replace the seaweed and the headphone with the mirror and the bell in Box 3
box_3[2:4] = ['mirror', 'bell']

# Empty Box 4
box_4 = []

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)