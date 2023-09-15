box_0 = ['horse', 'lamp', 'book']
box_1 = []
box_2 = ['frame', 'chair', 'coin', 'boat']
box_3 = ['mountain', 'shirt', 'glasses', 'tape', 'thread']
box_4 = ['spoon', 'camera', 'submarine', 'pot', 'pan']
box_5 = ['lightning', 'rock', 'coral']
box_6 = []
box_7 = ['charger']
box_8 = ['vase']
box_9 = ['pillow', 'boot', 'truck', 'toothpaste', 'makeup']
box_10 = ['soap', 'mixer', 'keyboard']
box_11 = ['bag', 'wallet', 'shelf', 'note', 'clock']
box_12 = ['guitar', 'shorts', 'piano', 'speaker']

# Remove the charger from Box 7
box_7.remove('charger')

# Swap the bag in Box 11 with the horse in Box 0
box_0.remove('horse')
box_11.remove('bag')
box_0.append('bag')
box_11.append('horse')

# Put the tie into Box 7
box_7.append('tie')

# Swap the vase in Box 8 with the pot in Box 4
box_8.remove('vase')
box_4.remove('pot')
box_8.append('pot')
box_4.append('vase')

# Put the piano into Box 0
box_0.append('piano')

# Replace the piano and the speaker and the guitar with the shelf and the fridge and the game in Box 12
box_12.remove('guitar')
box_12.remove('piano')
box_12.remove('speaker')
box_12.append('shelf')
box_12.append('fridge')
box_12.append('game')

# Swap the submarine in Box 4 with the rock in Box 5
box_4.remove('submarine')
box_5.remove('rock')
box_4.append('rock')
box_5.append('submarine')

# Remove the soap from Box 10
box_10.remove('soap')

# Remove the mixer from Box 10
box_10.remove('mixer')

# Put the skirt and the lock into Box 9
box_9.append('skirt')
box_9.append('lock')

# Remove the note from Box 11
box_11.remove('note')

# Remove the shelf and the fridge and the game from Box 12
box_12.remove('shelf')
box_12.remove('fridge')
box_12.remove('game')

# Remove the tie from Box 7
box_7.remove('tie')

# Replace the rock and the vase and the pan with the mountain and the plate and the tape in Box 4
box_4.remove('rock')
box_4.remove('vase')
box_4.remove('pan')
box_4.append('mountain')
box_4.append('plate')
box_4.append('tape')

# Move the wallet and the clock from Box 11 to Box 3
box_11.remove('wallet')
box_11.remove('clock')
box_3.append('wallet')
box_3.append('clock')

# Put the freezer into Box 5
box_5.append('freezer')

# Replace the skirt and the toothpaste and the pillow with the mixer and the clock and the truck in Box 9
box_9.remove('skirt')
box_9.remove('toothpaste')
box_9.remove('pillow')
box_9.append('mixer')
box_9.append('clock')
box_9.append('truck')

# Replace the coral and the lightning with the keyboard and the blender in Box 5
box_5.remove('coral')
box_5.remove('lightning')
box_5.append('keyboard')
box_5.append('blender')

# Put the microscope and the toy into Box 12
box_12.append('microscope')
box_12.append('toy')

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