box_0 = ['console', 'button', 'whistle', 'controller']
box_1 = ['plane', 'note', 'key', 'game', 'cloud']
box_2 = []
box_3 = ['scissors', 'book', 'razor', 'cow']
box_4 = ['pillow', 'mixer', 'oven', 'doll']
box_5 = ['horn', 'motorcycle', 'earring']
box_6 = ['card', 'rocket', 'desert', 'bicycle', 'telescope']
box_7 = ['charger']
box_8 = ['bell', 'helmet', 'chair']
box_9 = ['battery']
box_10 = ['shoes', 'cup', 'dice', 'violin', 'mirror']
box_11 = ['cat', 'sock', 'table', 'microscope', 'needle']
box_12 = []

# Move the plane from Box 1 to Box 9
box_9.append(box_1.pop(box_1.index('plane')))

# Remove the cat and the needle and the sock from Box 11
box_11.remove('cat')
box_11.remove('needle')
box_11.remove('sock')

# Put the snow and the tie into Box 12
box_12.extend(['snow', 'tie'])

# Swap the table in Box 11 with the controller in Box 0
box_11[box_11.index('table')], box_0[box_0.index('controller')] = box_0[box_0.index('controller')], box_11[box_11.index('table')]

# Swap the book in Box 3 with the bicycle in Box 6
box_3[box_3.index('book')], box_6[box_6.index('bicycle')] = box_6[box_6.index('bicycle')], box_3[box_3.index('book')]

# Put the lion and the planet and the sculpture into Box 6
box_6.extend(['lion', 'planet', 'sculpture'])

# Move the key from Box 1 to Box 6
box_6.append(box_1.pop(box_1.index('key')))

# Remove the cloud from Box 1
box_1.remove('cloud')

# Replace the horn and the earring and the motorcycle with the usb and the coral and the bus in Box 5
box_5[box_5.index('horn')] = 'usb'
box_5[box_5.index('earring')] = 'coral'
box_5[box_5.index('motorcycle')] = 'bus'

# Remove the snow from Box 12
box_12.remove('snow')

# Replace the coral and the usb and the bus with the shirt and the toy and the rain in Box 5
box_5[box_5.index('coral')] = 'shirt'
box_5[box_5.index('usb')] = 'toy'
box_5[box_5.index('bus')] = 'rain'

# Put the key into Box 11
box_11.append('key')

# Replace the whistle and the table with the shoe and the truck in Box 0
box_0[box_0.index('whistle')] = 'shoe'
box_0[box_0.index('table')] = 'truck'

# Move the toy and the shirt and the rain from Box 5 to Box 2
box_2.extend([box_5.pop(box_5.index('toy')), box_5.pop(box_5.index('shirt')), box_5.pop(box_5.index('rain'))])

# Put the shark and the lipstick and the thunder into Box 7
box_7.extend(['shark', 'lipstick', 'thunder'])

# Remove the sculpture and the key and the planet from Box 6
box_6.remove('sculpture')
box_6.remove('key')
box_6.remove('planet')

# Empty Box 12
box_12.clear()

# Put the shoe into Box 4
box_4.append(box_0.pop(box_0.index('shoe')))

# Move the oven and the doll from Box 4 to Box 3
box_3.extend([box_4.pop(box_4.index('oven')), box_4.pop(box_4.index('doll'))])

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
print("Box 11:", box_11)
print("Box 12:", box_12)