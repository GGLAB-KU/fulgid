box_0 = ['scarf']
box_1 = []
box_2 = ['shirt', 'phone', 'star', 'hat', 'mixer']
box_3 = ['card']

# Put the coin and the pot into Box 1
box_1.extend(['coin', 'pot'])

# Put the seaweed and the mirror and the usb into Box 0
box_0.extend(['seaweed', 'mirror', 'usb'])

# Swap the seaweed in Box 0 with the star in Box 2
box_0.remove('seaweed')
box_2.remove('star')
box_0.append('star')
box_2.append('seaweed')

# Remove the card from Box 3
box_3.remove('card')

# Swap the coin in Box 1 with the star in Box 0
box_1.remove('coin')
box_0.remove('star')
box_1.append('star')
box_0.append('coin')

# Remove the phone from Box 2
box_2.remove('phone')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)