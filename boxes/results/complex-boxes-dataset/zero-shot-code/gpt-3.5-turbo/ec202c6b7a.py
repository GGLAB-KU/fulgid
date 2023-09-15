box_0 = ['pan', 'boot', 'jungle', 'book', 'bear']
box_1 = ['branch']
box_2 = []
box_3 = ['shirt']
box_4 = ['razor', 'piano', 'controller']
box_5 = ['moon', 'seaweed', 'chair']
box_6 = []

# Replace the moon with the coin in Box 5
box_5[0] = 'coin'

# Remove the branch from Box 1
box_1.remove('branch')

# Remove the chair from Box 5
box_5.remove('chair')

# Put the gloves into Box 5
box_5.append('gloves')

# Empty Box 4
box_4.clear()

# Replace the pan and the bear with the tiger and the fridge in Box 0
box_0[0] = 'tiger'
box_0.append('fridge')

# Remove the fridge and the tiger and the boot from Box 0
box_0.remove('fridge')
box_0.remove('tiger')
box_0.remove('boot')

# Move the book from Box 0 to Box 1
box_1.append(box_0.pop(box_0.index('book')))

# Swap the coin in Box 5 with the jungle in Box 0
box_0[box_0.index('jungle')], box_5[box_5.index('coin')] = box_5[box_5.index('coin')], box_0[box_0.index('jungle')]

# Replace the shirt with the cup in Box 3
box_3[0] = 'cup'

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)