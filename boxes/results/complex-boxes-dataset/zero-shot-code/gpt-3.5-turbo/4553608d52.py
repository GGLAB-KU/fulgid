box_0 = ['motorcycle', 'sun', 'shark', 'wire']
box_1 = ['needle', 'toy']
box_2 = ['console', 'fish', 'soap', 'lamp', 'drum']
box_3 = []
box_4 = []
box_5 = ['coin', 'sculpture', 'shelf', 'zipper', 'perfume']
box_6 = ['skirt']
box_7 = ['shirt', 'razor', 'makeup']
box_8 = ['tie', 'dress', 'boot', 'hat']
box_9 = ['dog', 'leaf', 'toothbrush']
box_10 = ['seaweed', 'bird', 'charger', 'card']

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

# Empty Box 5
box_5 = []

# Replace the dog with the blanket in Box 9
box_9.remove('dog')
box_9.append('blanket')

# Move the shirt and the razor from Box 7 to Box 8
box_7.remove('shirt')
box_7.remove('razor')
box_8.append('shirt')
box_8.append('razor')

# Replace the card with the shirt in Box 10
box_10.remove('card')
box_10.append('shirt')

# Put the harmonica into Box 4
box_4.append('harmonica')

# Replace the skirt with the headphone in Box 6
box_6.remove('skirt')
box_6.append('headphone')

# Remove the harmonica from Box 4
box_4.remove('harmonica')

# Swap the fish in Box 2 with the boot in Box 8
box_2.remove('fish')
box_8.remove('boot')
box_2.append('boot')
box_8.append('fish')

# Replace the shirt with the comb in Box 10
box_10.remove('shirt')
box_10.append('comb')

# Put the car into Box 2
box_2.append('car')

# Move the toothbrush and the blanket from Box 9 to Box 10
box_9.remove('toothbrush')
box_9.remove('blanket')
box_10.append('toothbrush')
box_10.append('blanket')

# Remove the makeup from Box 7
box_7.remove('makeup')

# Remove the headphone from Box 6
box_6.remove('headphone')

# Put the shorts and the shirt and the tree into Box 1
box_1.append('shorts')
box_1.append('shirt')
box_1.append('tree')

# Swap the shark in Box 0 with the tree in Box 1
box_0.remove('shark')
box_1.remove('tree')
box_0.append('tree')
box_1.append('shark')

# Put the battery into Box 4
box_4.append('battery')

# Print the final state of the boxes
print_boxes()