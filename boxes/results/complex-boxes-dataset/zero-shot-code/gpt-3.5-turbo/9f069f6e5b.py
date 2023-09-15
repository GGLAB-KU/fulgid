box_0 = ['coin', 'spoon']
box_1 = ['rock']
box_2 = ['desert', 'leaf', 'keyboard', 'shark']
box_3 = ['dress', 'console', 'cat', 'laptop']
box_4 = ['coat', 'toaster', 'candle', 'microscope']
box_5 = ['truck', 'paint', 'bowl', 'speaker']
box_6 = ['moon', 'shampoo', 'butterfly', 'jacket']
box_7 = ['submarine', 'belt', 'shelf', 'shorts']
box_8 = []
box_9 = ['ring']
box_10 = ['watch', 'wallet', 'mask']

# Replace laptop and dress with usb and apple in Box 3
box_3.remove('laptop')
box_3.remove('dress')
box_3.extend(['usb', 'apple'])

# Put the island into Box 8
box_8.append('island')

# Swap the moon in Box 6 with the submarine in Box 7
box_6.remove('moon')
box_7.remove('submarine')
box_6.append('submarine')
box_7.append('moon')

# Swap the paint in Box 5 with the wallet in Box 10
box_5.remove('paint')
box_10.remove('wallet')
box_5.append('wallet')
box_10.append('paint')

# Empty Box 4
box_4 = []

# Move the coin from Box 0 to Box 4
box_0.remove('coin')
box_4.append('coin')

# Move the spoon from Box 0 to Box 7
box_0.remove('spoon')
box_7.append('spoon')

# Swap the shampoo in Box 6 with the rock in Box 1
box_6.remove('shampoo')
box_1.remove('rock')
box_6.append('rock')
box_1.append('shampoo')

# Empty Box 7
box_7 = []

# Move the ring from Box 9 to Box 0
box_9.remove('ring')
box_0.append('ring')

# Put the leaf and the coin and the island into Box 6
box_6.extend(['leaf', 'coin', 'island'])

# Replace the ring with the vase in Box 0
box_0.remove('ring')
box_0.append('vase')

# Put the sock into Box 0
box_0.append('sock')

# Empty Box 1
box_1 = []

# Remove the truck and the speaker from Box 5
box_5.remove('truck')
box_5.remove('speaker')

# Move the rock and the butterfly and the leaf from Box 6 to Box 10
box_6.remove('rock')
box_6.remove('butterfly')
box_6.remove('leaf')
box_10.extend(['rock', 'butterfly', 'leaf'])

# Print the contents of each box
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