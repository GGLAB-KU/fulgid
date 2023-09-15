box_0 = []
box_1 = ['card', 'star', 'bracelet']
box_2 = ['freezer', 'lightning', 'skirt', 'fish', 'razor']
box_3 = ['coin', 'boot', 'harmonica']
box_4 = ['train']
box_5 = ['scarf']

# Put the lion into Box 4
box_4.append('lion')

# Move the clock from Box 0 to Box 3
box_3.append(box_0.pop(0))

# Replace the fish and the lightning with the pot and the scissors in Box 2
box_2.remove('fish')
box_2.remove('lightning')
box_2.extend(['pot', 'scissors'])

# Move the scarf from Box 5 to Box 0
box_0.append(box_5.pop(0))

# Move the coin and the harmonica and the boot from Box 3 to Box 5
box_5.extend(box_3)
box_3.clear()

# Replace the coin with the pan in Box 5
box_5[box_5.index('coin')] = 'pan'

# Swap the boot in Box 5 with the card in Box 1
box_1[box_1.index('card')], box_5[box_5.index('boot')] = box_5[box_5.index('boot')], box_1[box_1.index('card')]

# Move the scarf from Box 0 to Box 3
box_3.append(box_0.pop(0))

# Remove the harmonica from Box 5
box_5.remove('harmonica')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)