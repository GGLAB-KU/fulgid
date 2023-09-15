box_0 = []
box_1 = ['flower', 'boat']
box_2 = []
box_3 = ['fork', 'microwave']
box_4 = []
box_5 = ['grass', 'lamp']
box_6 = ['scarf', 'dolphin', 'mirror', 'river', 'coral']
box_7 = ['swimsuit', 'apple', 'truck', 'toothbrush', 'oven']
box_8 = ['headphone', 'ship', 'octopus', 'scissors', 'belt']
box_9 = ['bell']
box_10 = ['zipper', 'jungle']
box_11 = ['card', 'cloud', 'dress', 'elephant']
box_12 = ['fridge', 'dog', 'mountain', 'train', 'pan']
box_13 = ['cup', 'razor', 'lipstick']
box_14 = ['pillow', 'bag', 'doll', 'phone', 'plane']

# Move the zipper and the jungle from Box 10 to Box 7
box_7.extend(box_10)
box_10.clear()

# Swap the scissors in Box 8 with the elephant in Box 11
box_8[3], box_11[3] = box_11[3], box_8[3]

# Put the console and the glove and the comb into Box 13
box_13.extend(['console', 'glove', 'comb'])

# Move the bell from Box 9 to Box 13
box_13.append(box_9.pop())

# Remove the fork and the microwave from Box 3
box_3.clear()

# Move the train and the mountain and the pan from Box 12 to Box 1
box_1.extend(box_12[2:])
box_12[2:] = []

# Remove the fridge and the dog from Box 12
box_12.remove('fridge')
box_12.remove('dog')

# Empty Box 8
box_8.clear()

# Replace the mountain and the pan with the dog and the bracelet in Box 1
box_1[2:] = ['dog', 'bracelet']

# Put the violin and the usb into Box 0
box_0.extend(['violin', 'usb'])

# Put the button and the lightning and the glasses into Box 0
box_0.extend(['button', 'lightning', 'glasses'])

# Replace the cloud and the scissors with the basket and the island in Box 11
box_11[1:3] = ['basket', 'island']

# Remove the card from Box 11
box_11.remove('card')

# Replace the swimsuit with the coat in Box 7
box_7[0] = 'coat'

# Swap the razor in Box 13 with the violin in Box 0
box_13[1], box_0[0] = box_0[0], box_13[1]

# Empty Box 0
box_0.clear()

# Empty Box 6
box_6.clear()

# Move the pillow and the bag and the phone from Box 14 to Box 5
box_5.extend(box_14[:3])
box_14[:3] = []

# Put the piano and the sun and the candle into Box 6
box_6.extend(['piano', 'sun', 'candle'])

# Remove the bell and the violin from Box 13
box_13.remove('bell')
box_13.remove('violin')

# Swap the lipstick in Box 13 with the lamp in Box 5
box_13[1], box_5[1] = box_5[1], box_13[1]

# Remove the candle and the sun from Box 6
box_6.remove('candle')
box_6.remove('sun')

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