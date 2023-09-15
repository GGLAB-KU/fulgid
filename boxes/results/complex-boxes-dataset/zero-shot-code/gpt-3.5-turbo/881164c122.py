box_0 = ['cat', 'card', 'polish', 'sun', 'pan']
box_1 = ['spoon']
box_2 = ['octopus', 'apple', 'shoes', 'lightning', 'tie']
box_3 = ['boot', 'bird', 'toaster', 'guitar', 'comet']
box_4 = ['needle', 'butterfly', 'lock', 'mixer', 'soap']
box_5 = ['necklace', 'skirt']
box_6 = ['fish', 'shark']

# Put the guitar and the helmet and the headphone into Box 2
box_2.extend(['guitar', 'helmet', 'headphone'])

# Swap the necklace in Box 5 with the spoon in Box 1
box_1[0], box_5[0] = box_5[0], box_1[0]

# Move the fish from Box 6 to Box 3
box_3.append(box_6.pop(0))

# Move the mixer and the butterfly from Box 4 to Box 3
box_3.extend([box_4.pop(3), box_4.pop(1)])

# Put the toothbrush and the coin and the watch into Box 1
box_1.extend(['toothbrush', 'coin', 'watch'])

# Empty Box 2
box_2 = []

# Move the shark from Box 6 to Box 4
box_4.append(box_6.pop(0))

# Put the dress and the laptop into Box 1
box_1.extend(['dress', 'laptop'])

# Move the skirt and the spoon from Box 5 to Box 4
box_4.extend([box_5.pop(1), box_5.pop(0)])

# Move the bird and the guitar and the mixer from Box 3 to Box 2
box_2.extend([box_3.pop(3), box_3.pop(1), box_3.pop(0)])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)