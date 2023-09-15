box_0 = ['soap']
box_1 = ['camera', 'pants', 'tiger', 'cloud', 'brush']
box_2 = ['piano', 'storm', 'cow']
box_3 = []
box_4 = ['oven', 'forest']
box_5 = ['plane', 'boat', 'book', 'fork']
box_6 = ['mixer', 'starfish', 'tie']
box_7 = ['lipstick']
box_8 = ['bag', 'controller']
box_9 = []
box_10 = ['wig', 'violin', 'thread']
box_11 = []
box_12 = []

def print_box(box_num):
    if box_num == 0:
        print("Box 0:", box_0)
    elif box_num == 1:
        print("Box 1:", box_1)
    elif box_num == 2:
        print("Box 2:", box_2)
    elif box_num == 3:
        print("Box 3:", box_3)
    elif box_num == 4:
        print("Box 4:", box_4)
    elif box_num == 5:
        print("Box 5:", box_5)
    elif box_num == 6:
        print("Box 6:", box_6)
    elif box_num == 7:
        print("Box 7:", box_7)
    elif box_num == 8:
        print("Box 8:", box_8)
    elif box_num == 9:
        print("Box 9:", box_9)
    elif box_num == 10:
        print("Box 10:", box_10)
    elif box_num == 11:
        print("Box 11:", box_11)
    elif box_num == 12:
        print("Box 12:", box_12)
    else:
        print("Invalid box number")

# Swap the soap in Box 0 with the brush in Box 1
box_0[0], box_1[box_1.index('brush')] = box_1[box_1.index('brush')], box_0[0]

# Move the mixer and the starfish from Box 6 to Box 11
box_11.extend([box_6.pop(box_6.index('mixer')), box_6.pop(box_6.index('starfish'))])

# Empty Box 5
box_5.clear()

# Move the tie from Box 6 to Box 12
box_12.append(box_6.pop(box_6.index('tie')))

# Put the harmonica into Box 5
box_5.append('harmonica')

# Move the bag and the controller from Box 8 to Box 2
box_2.extend([box_8.pop(box_8.index('bag')), box_8.pop(box_8.index('controller'))])

# Replace the lipstick with the comb in Box 7
box_7[box_7.index('lipstick')] = 'comb'

# Put the headphone and the cup into Box 7
box_7.extend(['headphone', 'cup'])

# Remove the bag and the cow from Box 2
box_2.remove('bag')
box_2.remove('cow')

# Swap the pants in Box 1 with the tie in Box 12
box_1[box_1.index('pants')], box_12[0] = box_12[0], box_1[box_1.index('pants')]

# Move the forest from Box 4 to Box 2
box_2.append(box_4.pop(box_4.index('forest')))

# Empty Box 10
box_10.clear()

# Move the comb from Box 7 to Box 10
box_10.append(box_7.pop(box_7.index('comb')))

# Remove the harmonica from Box 5
box_5.remove('harmonica')

# Put the glasses and the magnet into Box 7
box_7.extend(['glasses', 'magnet'])

# Swap the mixer in Box 11 with the comb in Box 10
box_11[box_11.index('mixer')], box_10[0] = box_10[0], box_11[box_11.index('mixer')]

# Move the brush from Box 0 to Box 11
box_11.append(box_0.pop(box_0.index('brush')))

# Move the brush and the starfish from Box 11 to Box 6
box_6.extend([box_11.pop(box_11.index('brush')), box_11.pop(box_11.index('starfish'))])

# Move the brush and the starfish from Box 6 to Box 12
box_12.extend([box_6.pop(box_6.index('brush')), box_6.pop(box_6.index('starfish'))])

# Swap the cloud in Box 1 with the piano in Box 2
box_1[box_1.index('cloud')], box_2[box_2.index('piano')] = box_2[box_2.index('piano')], box_1[box_1.index('cloud')]

# Print the contents of each box
print_box(0)
print_box(1)
print_box(2)
print_box(3)
print_box(4)
print_box(5)
print_box(6)
print_box(7)
print_box(8)
print_box(9)
print_box(10)
print_box(11)
print_box(12)