box_0 = ['watch', 'perfume', 'makeup']
box_1 = ['frame', 'cow', 'chair', 'rock', 'bicycle']
box_2 = []
box_3 = ['pot', 'piano', 'freezer']
box_4 = ['toy', 'towel', 'glove', 'flower']
box_5 = ['seaweed', 'island', 'truck']
box_6 = ['train']
box_7 = ['dice']
box_8 = ['lamp', 'usb']
box_9 = ['motorcycle', 'drum', 'toothpaste', 'rocket', 'gloves']
box_10 = ['game', 'whistle', 'scissors']
box_11 = ['scarf']
box_12 = ['oven']
box_13 = ['submarine', 'boat', 'sock', 'mask', 'console']
box_14 = ['toothbrush', 'pillow', 'cup', 'jacket', 'rain']

# Swap the frame in Box 1 with the train in Box 6
box_1.remove('frame')
box_6.remove('train')
box_1.append('train')
box_6.append('frame')

# Move the pot and the freezer from Box 3 to Box 5
box_3.remove('pot')
box_3.remove('freezer')
box_5.append('pot')
box_5.append('freezer')

# Remove the pot and the seaweed from Box 5
box_5.remove('pot')
box_5.remove('seaweed')

# Remove the oven from Box 12
box_12.remove('oven')

# Swap the flower in Box 4 with the cow in Box 1
box_4.remove('flower')
box_1.remove('cow')
box_4.append('cow')
box_1.append('flower')

# Replace the makeup and the watch and the perfume with the shampoo and the bus and the headphone in Box 0
box_0.remove('makeup')
box_0.remove('watch')
box_0.remove('perfume')
box_0.append('shampoo')
box_0.append('bus')
box_0.append('headphone')

# Move the motorcycle and the gloves from Box 9 to Box 2
box_9.remove('motorcycle')
box_9.remove('gloves')
box_2.append('motorcycle')
box_2.append('gloves')

# Move the cow and the toy and the towel from Box 4 to Box 3
box_4.remove('cow')
box_4.remove('toy')
box_4.remove('towel')
box_3.append('cow')
box_3.append('toy')
box_3.append('towel')

# Replace the bus with the moon in Box 0
box_0.remove('bus')
box_0.append('moon')

# Swap the jacket in Box 14 with the usb in Box 8
box_14.remove('jacket')
box_8.remove('usb')
box_14.append('usb')
box_8.append('jacket')

# Move the drum and the toothpaste and the rocket from Box 9 to Box 0
box_9.remove('drum')
box_9.remove('toothpaste')
box_9.remove('rocket')
box_0.append('drum')
box_0.append('toothpaste')
box_0.append('rocket')

# Remove the scarf from Box 11
box_11.remove('scarf')

# Move the rock and the bicycle from Box 1 to Box 5
box_1.remove('rock')
box_1.remove('bicycle')
box_5.append('rock')
box_5.append('bicycle')

# Put the telescope and the lipstick and the fork into Box 14
box_14.append('telescope')
box_14.append('lipstick')
box_14.append('fork')

# Swap the dice in Box 7 with the motorcycle in Box 2
box_7.remove('dice')
box_2.remove('motorcycle')
box_7.append('motorcycle')
box_2.append('dice')

# Swap the glove in Box 4 with the console in Box 13
box_4.remove('glove')
box_13.remove('console')
box_4.append('console')
box_13.append('glove')

# Put the pen and the microscope and the laptop into Box 1
box_1.append('pen')
box_1.append('microscope')
box_1.append('laptop')

# Move the microscope from Box 1 to Box 5
box_1.remove('microscope')
box_5.append('microscope')

# Swap the mask in Box 13 with the frame in Box 6
box_13.remove('mask')
box_6.remove('frame')
box_13.append('frame')
box_6.append('mask')

# Replace the shampoo and the headphone and the moon with the button and the ocean and the octopus in Box 0
box_0.remove('shampoo')
box_0.remove('headphone')
box_0.remove('moon')
box_0.append('button')
box_0.append('ocean')
box_0.append('octopus')

# Put the cat and the book and the sock into Box 12
box_12.append('cat')
box_12.append('book')
box_12.append('sock')

# Move the whistle from Box 10 to Box 9
box_10.remove('whistle')
box_9.append('whistle')

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
print("Box 14:", box_14)