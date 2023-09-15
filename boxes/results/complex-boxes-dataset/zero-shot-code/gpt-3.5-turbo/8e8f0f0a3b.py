box_0 = []
box_1 = ['usb', 'tiger', 'cloud']
box_2 = ['game', 'shirt', 'glove', 'branch', 'fridge']
box_3 = ['scissors', 'phone', 'makeup', 'dress']
box_4 = ['shark', 'watch', 'guitar', 'vase', 'cow']
box_5 = ['grass', 'pants', 'tie', 'sock', 'plate']
box_6 = ['butterfly', 'pot']
box_7 = ['magnet']
box_8 = ['chair', 'lock', 'bell', 'book', 'telescope', 'meteor']
box_9 = []
box_10 = ['shorts', 'fork', 'puzzle', 'violin', 'lipstick', 'sculpture']
box_11 = ['piano', 'mask']
box_12 = ['mountain', 'flower', 'bell']
box_13 = ['sandals', 'towel']

# Swap the mask in Box 11 with the sandals in Box 13
box_11.remove('mask')
box_13.remove('sandals')
box_11.append('sandals')
box_13.append('mask')

# Put the cloud into Box 1
box_1.append('cloud')

# Swap the tie in Box 5 with the vase in Box 4
box_5.remove('tie')
box_4.remove('vase')
box_5.append('vase')
box_4.append('tie')

# Move the bell from Box 8 to Box 7
box_8.remove('bell')
box_7.append('bell')

# Swap the magnet in Box 7 with the towel in Box 13
box_7.remove('magnet')
box_13.remove('towel')
box_7.append('towel')
box_13.append('magnet')

# Replace the scissors with the fridge in Box 3
box_3.remove('scissors')
box_2.remove('fridge')
box_3.append('fridge')

# Remove the pot and the butterfly from Box 6
box_6.remove('pot')
box_6.remove('butterfly')

# Swap the branch in Box 2 with the phone in Box 3
box_2.remove('branch')
box_3.remove('phone')
box_2.append('phone')
box_3.append('branch')

# Swap the tie in Box 4 with the vase in Box 5
box_4.remove('tie')
box_5.remove('vase')
box_4.append('vase')
box_5.append('tie')

# Remove the usb from Box 1
box_1.remove('usb')

# Remove the meteor from Box 11
box_11.remove('meteor')

# Put the flower and the bell into Box 12
box_12.append('flower')
box_12.append('bell')

# Remove the boot from Box 13
box_13.remove('boot')

# Put the lipstick and the sculpture into Box 10
box_10.append('lipstick')
box_10.append('sculpture')

# Move the game from Box 2 to Box 1
box_2.remove('game')
box_1.append('game')

# Put the meteor into Box 8
box_8.append('meteor')

# Swap the game in Box 1 with the mask in Box 13
box_1.remove('game')
box_13.remove('mask')
box_1.append('mask')
box_13.append('game')

# Remove the fridge from Box 2
box_2.remove('fridge')

# Remove the piano and the pen and the sandals from Box 11
box_11.remove('piano')
box_11.remove('pen')
box_11.remove('sandals')

# Put the mountain into Box 12
box_12.append('mountain')

# Move the magnet from Box 13 to Box 8
box_13.remove('magnet')
box_8.append('magnet')

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
print("Box 13:", box_13)