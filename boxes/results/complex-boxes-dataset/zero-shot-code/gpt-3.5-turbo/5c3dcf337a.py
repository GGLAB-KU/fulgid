box_0 = ['lion', 'pillow', 'helmet', 'belt']
box_1 = ['magnet', 'button']
box_2 = ['bell', 'console', 'hat', 'razor', 'glasses']
box_3 = ['toothbrush', 'guitar', 'table']
box_4 = []
box_5 = []
box_6 = ['telescope', 'rock', 'vase', 'dog', 'river']
box_7 = ['mask', 'wire', 'bag', 'shark', 'rain']

# Swap the magnet in Box 1 with the guitar in Box 3
box_1[0], box_3[1] = box_3[1], box_1[0]

# Move the rain and the bag from Box 7 to Box 5
box_5.extend([box_7.pop(4), box_7.pop(2)])

# Replace the console and the razor and the hat with the brush and the pen and the keyboard in Box 2
box_2[1:4] = ['brush', 'pen', 'keyboard']

# Remove the rain from Box 5
box_5.remove('rain')

# Swap the guitar in Box 1 with the pillow in Box 0
box_0[1], box_1[0] = box_1[0], box_0[1]

# Replace the keyboard with the zipper in Box 2
box_2[2] = 'zipper'

# Swap the glasses in Box 2 with the wire in Box 7
box_2[3], box_7[1] = box_7[1], box_2[3]

# Move the button and the pillow from Box 1 to Box 5
box_5.extend([box_1.pop(1), box_1.pop(0)])

# Remove the guitar and the lion and the helmet from Box 0
box_0.clear()

# Put the ship into Box 6
box_6.append('ship')

# Move the belt from Box 0 to Box 5
box_5.append(box_0.pop(3))

# Move the brush and the zipper from Box 2 to Box 0
box_0.extend([box_2.pop(1), box_2.pop(2)])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)