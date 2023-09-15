box_0 = ['chair', 'lightning']
box_1 = ['star']
box_2 = ['piano', 'crown', 'rocket', 'spoon']
box_3 = ['candle', 'mixer']
box_4 = ['plate', 'necklace', 'paint']
box_5 = ['wallet', 'rock']
box_6 = ['toaster', 'car', 'tree', 'dog', 'table']
box_7 = ['whistle', 'comb', 'shampoo']
box_8 = []
box_9 = ['speaker', 'lion']
box_10 = ['shorts', 'cup', 'microwave']
box_11 = ['apple', 'submarine', 'clock', 'earring', 'rain']
box_12 = ['watch', 'button', 'bell']

# Replace the rain and the submarine and the apple with the microscope and the paint and the cup in Box 11
box_11.remove('rain')
box_11.remove('submarine')
box_11.remove('apple')
box_11.extend(['microscope', 'paint', 'cup'])

# Move the clock from Box 11 to Box 0
box_0.append('clock')
box_11.remove('clock')

# Replace the rocket and the spoon and the piano with the horse and the skirt and the bowl in Box 2
box_2.remove('rocket')
box_2.remove('spoon')
box_2.remove('piano')
box_2.extend(['horse', 'skirt', 'bowl'])

# Put the scissors and the dog into Box 7
box_7.extend(['scissors', 'dog'])

# Remove the microscope and the paint from Box 11
box_11.remove('microscope')
box_11.remove('paint')

# Replace the rock with the sandals in Box 5
box_5.remove('rock')
box_5.append('sandals')

# Replace the dog with the coin in Box 7
box_7.remove('dog')
box_7.append('coin')

# Remove the candle and the mixer from Box 3
box_3.remove('candle')
box_3.remove('mixer')

# Empty Box 9
box_9.clear()

# Swap the bell in Box 12 with the sandals in Box 5
box_12.remove('bell')
box_5.remove('sandals')
box_12.append('sandals')
box_5.append('bell')

# Put the horn and the meteor into Box 5
box_5.extend(['horn', 'meteor'])

# Move the cup and the earring from Box 11 to Box 7
box_7.extend(['cup', 'earring'])
box_11.remove('cup')
box_11.remove('earring')

# Swap the microwave in Box 10 with the toaster in Box 6
box_10.remove('microwave')
box_6.remove('toaster')
box_10.append('toaster')
box_6.append('microwave')

# Swap the shorts in Box 10 with the car in Box 6
box_10.remove('shorts')
box_6.remove('car')
box_10.append('car')
box_6.append('shorts')

# Swap the plate in Box 4 with the watch in Box 12
box_4.remove('plate')
box_12.remove('watch')
box_4.append('watch')
box_12.append('plate')

# Replace the clock with the phone in Box 0
box_0.remove('clock')
box_0.append('phone')

# Replace the cup and the car and the toaster with the harmonica and the doll and the card in Box 10
box_10.remove('cup')
box_10.remove('car')
box_10.remove('toaster')
box_10.extend(['harmonica', 'doll', 'card'])

# Replace the earring with the sock in Box 7
box_7.remove('earring')
box_7.append('sock')

# Remove the phone and the lightning and the chair from Box 0
box_0.remove('phone')
box_0.remove('lightning')
box_0.remove('chair')

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