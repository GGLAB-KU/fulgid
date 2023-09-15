box_0 = ['flower', 'dolphin']
box_1 = ['rocket', 'dice', 'shorts', 'shoe']
box_2 = ['wire', 'console', 'magnet', 'bus']
box_3 = ['fridge']
box_4 = ['bear', 'microwave', 'storm', 'ocean', 'glasses']
box_5 = ['starfish', 'fish', 'sun', 'fork']
box_6 = ['scissors', 'makeup']
box_7 = ['toothbrush', 'mirror', 'piano', 'planet', 'horn']
box_8 = []
box_9 = ['rock', 'whistle', 'frame', 'oven', 'skirt']
box_10 = []
box_11 = ['belt', 'wig', 'brush', 'car']
box_12 = ['jungle', 'headphone']

# Swap the planet in Box 7 with the flower in Box 0
box_0[0], box_7[3] = box_7[3], box_0[0]

# Swap the fridge in Box 3 with the horn in Box 7
box_3[0], box_7[4] = box_7[4], box_3[0]

# Move the horn from Box 3 to Box 5
box_5.append(box_3.pop(0))

# Move the fork from Box 5 to Box 7
box_7.append(box_5.pop(3))

# Replace the skirt and the whistle and the rock with the lion and the rain and the tiger in Box 9
box_9 = ['lion', 'rain', 'tiger']

# Put the controller and the storm into Box 5
box_5.extend(['controller', 'storm'])

# Remove the planet and the dolphin from Box 0
box_0 = []

# Put the dolphin into Box 2
box_2.append('dolphin')

# Empty Box 5
box_5 = []

# Empty Box 11
box_11 = []

# Swap the shorts in Box 1 with the scissors in Box 6
box_1[2], box_6[0] = box_6[0], box_1[2]

# Move the makeup from Box 6 to Box 5
box_5.append(box_6.pop(1))

# Put the sun and the desert into Box 11
box_11.extend(['sun', 'desert'])

# Remove the glasses from Box 4
box_4.remove('glasses')

# Remove the makeup from Box 5
box_5 = []

# Put the moon into Box 10
box_10.append('moon')

# Replace the headphone with the clock in Box 12
box_12[1] = 'clock'

# Put the fish into Box 10
box_10.append('fish')

# Move the desert and the sun from Box 11 to Box 7
box_7.extend(box_11.pop(1))
box_7.extend(box_11.pop(0))

# Output
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
print("Box 11:", box_11)
print("Box 12:", box_12)