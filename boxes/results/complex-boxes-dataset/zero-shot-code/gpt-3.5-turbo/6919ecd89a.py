box_0 = ['basket', 'bear']
box_1 = ['whistle', 'rocket']
box_2 = ['candle', 'planet', 'branch', 'chair', 'sun']
box_3 = ['butterfly', 'pan', 'blender', 'button']
box_4 = ['wallet', 'piano']
box_5 = ['plate', 'shark', 'grass']
box_6 = ['glove', 'gloves', 'belt', 'dolphin']
box_7 = ['makeup', 'mountain', 'microscope', 'rain', 'seaweed']
box_8 = []
box_9 = ['cow', 'starfish', 'perfume', 'flute', 'elephant']
box_10 = ['wig', 'shelf', 'headphone']

# Replace the whistle and the rocket with the vase and the beach in Box 1
box_1 = ['vase', 'beach']

# Move the chair and the planet and the sun from Box 2 to Box 0
box_0.extend(['chair', 'planet', 'sun'])
box_2 = []

# Put the truck and the usb into Box 3
box_3.extend(['truck', 'usb'])

# Swap the glove in Box 6 with the grass in Box 5
box_5[box_5.index('grass')] = 'glove'
box_6[box_6.index('glove')] = 'grass'

# Move the beach from Box 1 to Box 9
box_9.append('beach')
box_1.remove('beach')

# Swap the vase in Box 1 with the button in Box 3
box_1[box_1.index('vase')] = 'button'
box_3[box_3.index('button')] = 'vase'

# Replace the shark with the button in Box 5
box_5[box_5.index('shark')] = 'button'

# Replace the mountain and the rain and the makeup with the sock and the snow and the cat in Box 7
box_7[box_7.index('mountain')] = 'sock'
box_7[box_7.index('rain')] = 'snow'
box_7[box_7.index('makeup')] = 'cat'

# Move the wallet from Box 4 to Box 3
box_3.append('wallet')
box_4.remove('wallet')

# Replace the vase and the usb with the pillow and the cup in Box 3
box_3[box_3.index('vase')] = 'pillow'
box_3[box_3.index('usb')] = 'cup'

# Remove the headphone from Box 10
box_10.remove('headphone')

# Replace the shelf and the wig with the snow and the rock in Box 10
box_10[box_10.index('shelf')] = 'snow'
box_10[box_10.index('wig')] = 'rock'

# Move the button from Box 1 to Box 2
box_2.append('button')
box_1.remove('button')

# Remove the planet and the basket from Box 0
box_0.remove('planet')
box_0.remove('basket')

# Move the sock and the cat from Box 7 to Box 2
box_2.extend(['sock', 'cat'])
box_7.remove('sock')
box_7.remove('cat')

# Empty Box 5
box_5 = []

# Move the candle from Box 2 to Box 5
box_5.append('candle')

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