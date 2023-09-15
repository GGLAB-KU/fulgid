box_0 = ['microwave', 'bear', 'bag', 'river', 'tiger']
box_1 = ['blender']
box_2 = ['card', 'rock']
box_3 = ['violin', 'shorts', 'shark', 'storm']
box_4 = []
box_5 = ['glove', 'dolphin', 'starfish']
box_6 = []
box_7 = ['usb', 'dress', 'flower', 'shampoo', 'sculpture']
box_8 = ['polish', 'lion', 'coral', 'scarf']
box_9 = ['scissors', 'chair', 'toothpaste']
box_10 = ['branch', 'camera', 'lamp', 'candle', 'shirt']

# Replace the card with the shoes in Box 2
box_2.remove('card')
box_2.append('shoes')

# Swap the scissors in Box 9 with the violin in Box 3
box_9.remove('scissors')
box_3.remove('violin')
box_9.append('violin')
box_3.append('scissors')

# Swap the dress in Box 7 with the microwave in Box 0
box_7.remove('dress')
box_0.remove('microwave')
box_7.append('microwave')
box_0.append('dress')

# Remove the blender from Box 1
box_1 = []

# Replace the glove with the plane in Box 5
box_5.remove('glove')
box_5.append('plane')

# Remove the shorts and the shark from Box 3
box_3.remove('shorts')
box_3.remove('shark')

# Move the shirt from Box 10 to Box 4
box_10.remove('shirt')
box_4.append('shirt')

# Move the shirt from Box 4 to Box 8
box_4.remove('shirt')
box_8.append('shirt')

# Swap the starfish in Box 5 with the rock in Box 2
box_5.remove('starfish')
box_2.remove('rock')
box_5.append('rock')
box_2.append('starfish')

# Move the toothpaste from Box 9 to Box 7
box_9.remove('toothpaste')
box_7.append('toothpaste')

# Swap the flower in Box 7 with the tiger in Box 0
box_7.remove('flower')
box_0.remove('tiger')
box_7.append('tiger')
box_0.append('flower')

# Put the mountain and the desert and the earring into Box 10
box_10.extend(['mountain', 'desert', 'earring'])

# Put the jacket and the frame and the horn into Box 2
box_2.extend(['jacket', 'frame', 'horn'])

# Replace the scissors with the ship in Box 3
box_3.remove('scissors')
box_3.append('ship')

# Move the river from Box 0 to Box 10
box_0.remove('river')
box_10.append('river')

# Move the ship from Box 3 to Box 6
box_3.remove('ship')
box_6.append('ship')

# Swap the shampoo in Box 7 with the dolphin in Box 5
box_7.remove('shampoo')
box_5.remove('dolphin')
box_7.append('dolphin')
box_5.append('shampoo')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10]):
    print(f"Box {i}: {box}")