box_0 = []
box_1 = ['blender', 'zipper']
box_2 = ['candle']
box_3 = ['comet', 'swimsuit', 'coral', 'train', 'car']
box_4 = ['usb']
box_5 = ['fridge', 'rocket', 'pen']
box_6 = ['horse', 'boat', 'tiger', 'ship']
box_7 = ['rain', 'keyboard', 'mountain', 'harmonica', 'crown']
box_8 = []
box_9 = ['sculpture', 'thunder', 'jungle', 'spoon']
box_10 = ['key', 'frame', 'headphone']
box_11 = ['flute', 'earring', 'lock']
box_12 = ['cup']
box_13 = ['microwave', 'shorts', 'lipstick', 'mask']
box_14 = []

# Remove the frame from Box 10
box_10.remove('frame')

# Swap the zipper in Box 1 with the tiger in Box 6
box_1.remove('zipper')
box_6.remove('tiger')
box_1.append('tiger')
box_6.append('zipper')

# Remove the jungle and the sculpture and the spoon from Box 9
box_9.remove('jungle')
box_9.remove('sculpture')
box_9.remove('spoon')

# Swap the blender in Box 1 with the mountain in Box 7
box_1.remove('blender')
box_7.remove('mountain')
box_1.append('mountain')
box_7.append('blender')

# Put the bracelet into Box 4
box_4.append('bracelet')

# Swap the candle in Box 2 with the thunder in Box 9
box_2.remove('candle')
box_9.remove('thunder')
box_2.append('thunder')
box_9.append('candle')

# Remove the mountain from Box 1
box_1.remove('mountain')

# Move the bracelet from Box 4 to Box 14
box_4.remove('bracelet')
box_14.append('bracelet')

# Swap the usb in Box 4 with the lipstick in Box 13
box_4.remove('usb')
box_13.remove('lipstick')
box_4.append('lipstick')
box_13.append('usb')

# Move the rocket and the fridge from Box 5 to Box 6
box_5.remove('rocket')
box_5.remove('fridge')
box_6.append('rocket')
box_6.append('fridge')

# Empty Box 5
box_5 = []

# Remove the bracelet from Box 14
box_14.remove('bracelet')

# Swap the thunder in Box 2 with the tiger in Box 1
box_2.remove('thunder')
box_1.remove('tiger')
box_2.append('tiger')
box_1.append('thunder')

# Put the mirror into Box 2
box_2.append('mirror')

# Swap the lipstick in Box 4 with the candle in Box 9
box_4.remove('lipstick')
box_9.remove('candle')
box_4.append('candle')
box_9.append('lipstick')

# Put the scarf into Box 4
box_4.append('scarf')

# Replace the thunder with the tie in Box 1
box_1.remove('thunder')
box_1.append('tie')

# Swap the comet in Box 3 with the key in Box 10
box_3.remove('comet')
box_10.remove('key')
box_3.append('key')
box_10.append('comet')

# Replace the train and the coral and the swimsuit with the dice and the violin and the shelf in Box 3
box_3.remove('train')
box_3.remove('coral')
box_3.remove('swimsuit')
box_3.append('dice')
box_3.append('violin')
box_3.append('shelf')

# Move the lock from Box 11 to Box 12
box_11.remove('lock')
box_12.append('lock')

# Replace the scarf and the candle with the shampoo and the truck in Box 4
box_4.remove('scarf')
box_4.remove('candle')
box_4.append('shampoo')
box_4.append('truck')

# Replace the usb and the mask with the snow and the note in Box 13
box_13.remove('usb')
box_13.remove('mask')
box_13.append('snow')
box_13.append('note')

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
print("Box 14:", box_14)