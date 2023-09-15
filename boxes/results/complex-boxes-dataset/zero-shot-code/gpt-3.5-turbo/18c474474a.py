box_0 = ['shoe', 'bracelet', 'phone']
box_1 = ['umbrella', 'shirt', 'motorcycle', 'tiger']
box_2 = ['beach', 'helmet', 'zipper', 'leaf', 'card']
box_3 = ['pants', 'button', 'bowl', 'earring', 'game']
box_4 = []
box_5 = ['speaker']

# Replace the umbrella and the tiger with the belt and the desert in Box 1
box_1[0] = 'belt'
box_1[3] = 'desert'

# Replace the speaker with the oven in Box 5
box_5[0] = 'oven'

# Move the belt and the desert and the shirt from Box 1 to Box 5
box_5.extend([box_1.pop(0), box_1.pop(1), box_1.pop(1)])

# Remove the bowl from Box 3
box_3.remove('bowl')

# Swap the phone in Box 0 with the motorcycle in Box 1
box_0[2], box_1[2] = box_1[2], box_0[2]

# Replace the phone with the speaker in Box 1
box_1[2] = 'speaker'

# Swap the button in Box 3 with the speaker in Box 1
box_3[1], box_1[2] = box_1[2], box_3[1]

# Move the bracelet and the motorcycle from Box 0 to Box 5
box_5.extend([box_0.pop(1), box_0.pop(1)])

# Remove the beach and the zipper and the card from Box 2
box_2.remove('beach')
box_2.remove('zipper')
box_2.remove('card')

# Print the final contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)