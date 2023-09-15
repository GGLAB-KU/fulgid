box_0 = ['fridge']
box_1 = ['cow', 'card']
box_2 = ['desert', 'doll', 'storm', 'scarf', 'lock']
box_3 = []
box_4 = ['keyboard', 'mask']
box_5 = ['bus', 'clock', 'swimsuit']
box_6 = []
box_7 = ['sock']
box_8 = ['drum', 'earring', 'game', 'bird', 'magnet']
box_9 = ['oven', 'console', 'belt']
box_10 = []
box_11 = []

# Remove the clock and the swimsuit from Box 5
box_5.remove('clock')
box_5.remove('swimsuit')

# Move the mask and the keyboard from Box 4 to Box 6
box_4.remove('mask')
box_6.extend(['mask'])
box_4.remove('keyboard')
box_6.extend(['keyboard'])

# Put the horn and the perfume into Box 9
box_9.extend(['horn', 'perfume'])

# Swap the keyboard in Box 6 with the card in Box 1
box_6.remove('keyboard')
box_1.remove('card')
box_6.extend(['card'])
box_1.extend(['keyboard'])

# Put the bicycle and the toaster and the clock into Box 10
box_10.extend(['bicycle', 'toaster', 'clock'])

# Move the cow from Box 1 to Box 4
box_1.remove('cow')
box_4.extend(['cow'])

# Replace the sock with the mixer in Box 7
box_7.remove('sock')
box_7.extend(['mixer'])

# Move the cow from Box 4 to Box 10
box_4.remove('cow')
box_10.extend(['cow'])

# Remove the mixer from Box 7
box_7.remove('mixer')

# Empty Box 2
box_2 = []

# Empty Box 10
box_10 = []

# Remove the perfume and the belt and the console from Box 9
box_9.remove('perfume')
box_9.remove('belt')
box_9.remove('console')

# Move the fridge from Box 0 to Box 5
box_0.remove('fridge')
box_5.extend(['fridge'])

# Move the keyboard from Box 1 to Box 6
box_1.remove('keyboard')
box_6.extend(['keyboard'])

# Swap the drum in Box 8 with the horn in Box 9
box_8.remove('drum')
box_9.remove('horn')
box_8.extend(['horn'])
box_9.extend(['drum'])

# Swap the mask in Box 6 with the drum in Box 9
box_6.remove('mask')
box_9.remove('drum')
box_6.extend(['drum'])
box_9.extend(['mask'])

# Remove the magnet and the earring from Box 8
box_8.remove('magnet')
box_8.remove('earring')

# Replace the bird and the game and the horn with the thunder and the freezer and the piano in Box 8
box_8.remove('bird')
box_8.remove('game')
box_8.remove('horn')
box_8.extend(['thunder', 'freezer', 'piano'])

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