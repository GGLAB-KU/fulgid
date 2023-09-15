box_0 = []
box_1 = ['paint', 'pan', 'basket']
box_2 = ['beach', 'card', 'thunder']
box_3 = ['harmonica', 'dress', 'freezer', 'dice']
box_4 = ['grass', 'car']

# Put the mixer into Box 2
box_2.append('mixer')

# Remove the dice and the freezer and the harmonica from Box 3
box_3.remove('dice')
box_3.remove('freezer')
box_3.remove('harmonica')

# Empty Box 2
box_2 = []

# Put the moon and the cup and the star into Box 1
box_1.extend(['moon', 'cup', 'star'])

# Put the crown into Box 0
box_0.append('crown')

# Put the bag into Box 4
box_4.append('bag')

# Replace the grass and the car with the doll and the phone in Box 4
box_4.remove('grass')
box_4.remove('car')
box_4.extend(['doll', 'phone'])

# Remove the doll and the bag and the phone from Box 4
box_4.remove('doll')
box_4.remove('bag')
box_4.remove('phone')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)