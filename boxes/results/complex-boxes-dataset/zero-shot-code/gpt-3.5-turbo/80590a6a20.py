box_0 = ['shoe', 'river', 'cat', 'flute']
box_1 = ['vase', 'beach', 'truck', 'wig', 'mixer']
box_2 = []
box_3 = ['flower', 'scissors', 'camera', 'coat']
box_4 = ['zipper', 'doll', 'dog', 'microscope']
box_5 = []
box_6 = []

# Put the laptop and the pen and the beach into Box 4
box_4.extend(['laptop', 'pen', 'beach'])

# Empty Box 3
box_3.clear()

# Put the motorcycle and the sandals into Box 0
box_0.extend(['motorcycle', 'sandals'])

# Put the mixer and the bird and the note into Box 0
box_0.extend(['mixer', 'bird', 'note'])

# Remove the flute from Box 0
box_0.remove('flute')

# Put the lipstick and the rock into Box 1
box_1.extend(['lipstick', 'rock'])

# Remove the zipper and the pen from Box 4
box_4.remove('zipper')
box_4.remove('pen')

# Replace the mixer and the wig with the flute and the keyboard in Box 1
box_1.remove('mixer')
box_1.remove('wig')
box_1.extend(['flute', 'keyboard'])

# Replace the shoe with the clock in Box 0
box_0.remove('shoe')
box_0.append('clock')

# Replace the river with the plate in Box 0
box_0.remove('river')
box_0.append('plate')

# Remove the mixer and the cat and the note from Box 0
box_0.remove('mixer')
box_0.remove('cat')
box_0.remove('note')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)