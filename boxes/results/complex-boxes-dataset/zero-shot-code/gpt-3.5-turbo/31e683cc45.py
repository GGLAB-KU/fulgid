box_0 = ['sun', 'phone', 'comb', 'lock']
box_1 = ['needle', 'guitar', 'car', 'tape']
box_2 = ['truck', 'basket', 'star', 'planet', 'shoes']
box_3 = []
box_4 = ['leaf']
box_5 = ['octopus', 'train', 'toothbrush', 'cat']
box_6 = ['laptop']
box_7 = ['bowl']
box_8 = ['grinder', 'key', 'rain', 'lamp']
box_9 = []
box_10 = []

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

# Move the bowl from Box 7 to Box 8
box_8.append(box_7.pop(0))

# Remove the laptop from Box 6
box_6.pop(0)

# Remove the leaf from Box 4
box_4.pop(0)

# Move the guitar and the car from Box 1 to Box 3
box_3.extend([box_1.pop(1), box_1.pop(1)])

# Put the jungle into Box 1
box_1.append('jungle')

# Remove the comb and the lock and the sun from Box 0
box_0.remove('comb')
box_0.remove('lock')
box_0.remove('sun')

# Replace the bowl and the rain and the key with the telescope and the zipper and the moon in Box 8
box_8.remove('bowl')
box_8.remove('rain')
box_8.remove('key')
box_8.extend(['telescope', 'zipper', 'moon'])

# Swap the telescope in Box 8 with the octopus in Box 5
box_8.append(box_5.pop(0))
box_5.append('telescope')

# Move the jungle from Box 1 to Box 9
box_9.append(box_1.pop(3))

# Remove the phone from Box 0
box_0.remove('phone')

# Swap the planet in Box 2 with the train in Box 5
box_2.append(box_5.pop(2))
box_5.append('planet')

# Remove the lamp and the octopus from Box 8
box_8.remove('lamp')
box_8.remove('octopus')

# Put the zipper and the button and the ring into Box 9
box_9.extend(['zipper', 'button', 'ring'])

# Put the submarine and the shampoo into Box 3
box_3.extend(['submarine', 'shampoo'])

# Put the spoon and the bear and the toy into Box 4
box_4.extend(['spoon', 'bear', 'toy'])

# Move the ring and the zipper and the jungle from Box 9 to Box 8
box_8.extend([box_9.pop(2), box_9.pop(1), box_9.pop(0)])

# Replace the needle and the tape with the tiger and the razor in Box 1
box_1.remove('needle')
box_1.remove('tape')
box_1.extend(['tiger', 'razor'])

print("\nAfter modifications:")
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