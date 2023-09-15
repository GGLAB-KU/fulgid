box_0 = ['sandals', 'clock']
box_1 = []
box_2 = ['doll', 'oven', 'mask']
box_3 = ['key', 'dog', 'shorts', 'shampoo']
box_4 = []
box_5 = ['lamp']
box_6 = ['glove']
box_7 = ['horse', 'toothbrush', 'tie']
box_8 = ['guitar', 'boot', 'charger', 'candle']
box_9 = ['headphone', 'lightning', 'spoon', 'dice']
box_10 = ['camera', 'laptop', 'helmet']

# Move the spoon from Box 9 to Box 10
box_10.append(box_9.pop(box_9.index('spoon')))

# Move the clock and the sandals from Box 0 to Box 10
box_10.extend([box_0.pop(box_0.index('clock')), box_0.pop(box_0.index('sandals'))])

# Replace the lamp with the sock in Box 5
box_5.pop()
box_5.append('sock')

# Remove the tie and the toothbrush from Box 7
box_7.remove('tie')
box_7.remove('toothbrush')

# Move the horse from Box 7 to Box 3
box_3.append(box_7.pop(box_7.index('horse')))

# Empty Box 5
box_5.clear()

# Remove the doll and the mask and the oven from Box 2
box_2.remove('doll')
box_2.remove('mask')
box_2.remove('oven')

# Put the basket and the toaster into Box 2
box_2.extend(['basket', 'toaster'])

# Remove the toaster and the basket from Box 2
box_2.remove('toaster')
box_2.remove('basket')

# Put the console and the mixer into Box 7
box_7.extend(['console', 'mixer'])

# Move the dice from Box 9 to Box 1
box_1.append(box_9.pop(box_9.index('dice')))

# Move the shorts and the horse from Box 3 to Box 7
box_7.extend([box_3.pop(box_3.index('shorts')), box_3.pop(box_3.index('horse'))])

# Put the piano and the button into Box 0
box_0.extend(['piano', 'button'])

# Move the dog and the shampoo and the key from Box 3 to Box 9
box_9.extend([box_3.pop(box_3.index('dog')), box_3.pop(box_3.index('shampoo')), box_3.pop(box_3.index('key'))])

# Put the cat and the book into Box 4
box_4.extend(['cat', 'book'])

# Put the polish into Box 7
box_7.append('polish')

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