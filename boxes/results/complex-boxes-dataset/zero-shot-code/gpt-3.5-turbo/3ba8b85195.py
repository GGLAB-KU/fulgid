box_0 = ['flute', 'card', 'snow', 'razor', 'toothpaste']
box_1 = ['moon', 'shark', 'toaster', 'towel', 'helmet']
box_2 = ['island', 'toothbrush', 'scissors', 'vase']
box_3 = ['pen', 'sculpture', 'doll', 'bear']
box_4 = ['candle', 'lion']
box_5 = ['note', 'boot', 'forest', 'jungle', 'grinder']
box_6 = ['fridge']
box_7 = []

# Swap the fridge in Box 6 with the island in Box 2
box_6[0], box_2[0] = box_2[0], box_6[0]

# Replace the candle with the shirt in Box 4
box_4[0] = 'shirt'

# Replace the shirt and the lion with the fork and the needle in Box 4
box_4 = ['fork', 'needle']

# Move the note and the jungle from Box 5 to Box 7
box_7.extend([box_5.pop(0), box_5.pop(2)])

# Put the wallet and the usb into Box 3
box_3.extend(['wallet', 'usb'])

# Remove the vase from Box 2
box_2.remove('vase')

# Put the octopus and the book and the grass into Box 5
box_5.extend(['octopus', 'book', 'grass'])

# Put the mask into Box 4
box_4.append('mask')

# Remove the razor from Box 0
box_0.remove('razor')

# Put the swimsuit and the phone and the zipper into Box 5
box_5.extend(['swimsuit', 'phone', 'zipper'])

# Remove the note and the jungle from Box 7
box_7 = []

# Swap the card in Box 0 with the towel in Box 1
box_0[1], box_1[3] = box_1[3], box_0[1]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)