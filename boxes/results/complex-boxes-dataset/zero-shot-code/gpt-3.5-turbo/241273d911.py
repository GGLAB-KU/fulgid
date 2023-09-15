box_0 = ['skirt', 'violin', 'rocket']
box_1 = ['freezer', 'flute', 'watch', 'harmonica', 'moon']
box_2 = ['meteor', 'jungle', 'shoe']
box_3 = ['controller', 'fridge', 'boot']
box_4 = ['desert', 'sculpture', 'mountain']
box_5 = ['bicycle']
box_6 = ['oven', 'plane', 'bear', 'camera', 'plate']
box_7 = ['tiger', 'jacket', 'snow', 'thread', 'needle']
box_8 = ['truck', 'earring', 'table', 'coin']
box_9 = ['coral']
box_10 = ['guitar', 'mixer', 'planet']

# Move the bicycle from Box 5 to Box 3
box_3.append(box_5.pop(0))

# Put the necklace and the note and the horse into Box 4
box_4.extend(['necklace', 'note', 'horse'])

# Move the mixer and the guitar and the planet from Box 10 to Box 7
box_7.extend(box_10[1:])
box_10 = box_10[:1]

# Move the note and the mountain and the sculpture from Box 4 to Box 6
box_6.extend(box_4[1:])
box_4 = box_4[:1]

# Replace the rocket and the violin with the pot and the battery in Box 0
box_0 = ['pot', 'battery']

# Put the shoes and the brush into Box 0
box_0.extend(['shoes', 'brush'])

# Replace the pot with the dress in Box 0
box_0[0] = 'dress'

# Move the necklace and the desert and the horse from Box 4 to Box 7
box_7.extend(box_4[:1] + box_4[1:])
box_4 = []

# Put the pot and the bus into Box 5
box_5.extend(['pot', 'bus'])

# Put the lipstick and the pot into Box 3
box_3.extend(['lipstick', 'pot'])

# Replace the jacket and the planet and the snow with the bicycle and the comb and the rock in Box 7
box_7 = ['bicycle', 'comb', 'rock']

# Move the bus from Box 5 to Box 3
box_3.append(box_5.pop())

# Swap the rock in Box 7 with the bear in Box 6
box_7[2], box_6[2] = box_6[2], box_7[2]

# Swap the coral in Box 9 with the freezer in Box 1
box_9[0], box_1[0] = box_1[0], box_9[0]

# Remove the dress and the battery from Box 0
box_0 = []

# Put the seaweed and the beach and the bear into Box 10
box_10.extend(['seaweed', 'beach', 'bear'])

# Replace the meteor and the shoe and the jungle with the guitar and the bracelet and the frame in Box 2
box_2 = ['guitar', 'bracelet', 'frame']

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