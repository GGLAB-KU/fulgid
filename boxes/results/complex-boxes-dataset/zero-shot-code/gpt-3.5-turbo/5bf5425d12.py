box_0 = ['violin', 'wig']
box_1 = []
box_2 = ['zipper', 'shorts', 'battery']
box_3 = ['umbrella', 'watch']
box_4 = ['shark', 'tape', 'clock']
box_5 = ['fork', 'horn', 'microwave', 'oven', 'camera']
box_6 = ['brush']
box_7 = ['branch', 'pot', 'beach', 'polish']
box_8 = ['seaweed']
box_9 = []
box_10 = []

def print_boxes():
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

# Move the shorts, zipper, and battery from Box 2 to Box 9
box_9.extend(box_2[1:])
box_2 = []

# Remove the shorts, battery, and zipper from Box 9
box_9 = []

# Replace the oven, fork, and camera with the lamp, umbrella, and branch in Box 5
box_5 = ['lamp', 'umbrella', 'branch']

# Swap the lamp in Box 5 with the wig in Box 0
box_0[1], box_5[0] = box_5[0], box_0[1]

# Empty Box 5
box_5 = []

# Remove the brush from Box 6
box_6 = []

# Replace the violin and lamp with the drum and dolphin in Box 0
box_0 = ['drum', 'dolphin']

# Move the pot, branch, and beach from Box 7 to Box 0
box_0.extend(box_7[:3])
box_7 = box_7[3:]

# Move the umbrella from Box 3 to Box 9
box_9.append(box_3.pop(1))

# Remove the dolphin and beach from Box 0
box_0 = []

# Swap the umbrella in Box 9 with the branch in Box 0
box_9[0], box_0.append(box_9[0])

# Replace the polish with the spoon in Box 7
box_7[3] = 'spoon'

# Remove the watch from Box 3
box_3.pop(1)

# Put the shoes, button, and console into Box 1
box_1.extend(['shoes', 'button', 'console'])

# Empty Box 8
box_8 = []

# Put the thread into Box 7
box_7.append('thread')

# Replace the thread and spoon with the brush and frame in Box 7
box_7[3], box_7[4] = 'brush', 'frame'

print_boxes()