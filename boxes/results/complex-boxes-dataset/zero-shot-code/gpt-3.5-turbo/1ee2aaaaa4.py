box_0 = ['zipper', 'lipstick', 'gloves', 'note']
box_1 = ['candle', 'belt', 'skirt', 'coat', 'ship']
box_2 = ['comb']
box_3 = ['bag', 'rocket', 'frame', 'grinder', 'starfish']
box_4 = ['meteor', 'beach', 'makeup', 'scarf']
box_5 = ['rock']
box_6 = ['umbrella', 'ring', 'elephant', 'pillow', 'speaker']
box_7 = ['basket', 'telescope', 'fridge']
box_8 = ['truck', 'oven', 'shelf', 'toaster', 'dice']
box_9 = []
box_10 = ['wig', 'earring', 'jacket', 'mixer', 'planet']
box_11 = ['seaweed', 'bus']
box_12 = []

# Put the bracelet and the headphone into Box 6
box_6.extend(['bracelet', 'headphone'])

# Replace the shelf and the oven and the dice with the guitar and the wire and the dolphin in Box 8
box_8 = ['guitar', 'wire', 'dolphin']

# Swap the jacket in Box 10 with the comb in Box 2
box_10[2], box_2[0] = box_2[0], box_10[2]

# Swap the seaweed in Box 11 with the rock in Box 5
box_11[0], box_5[0] = box_5[0], box_11[0]

# Move the wire and the truck and the guitar from Box 8 to Box 5
box_5.extend(box_8)
box_8 = []

# Swap the bus in Box 11 with the meteor in Box 4
box_11[0], box_4[0] = box_4[0], box_11[0]

# Replace the frame and the rocket and the starfish with the rock and the cat and the sun in Box 3
box_3 = ['rock', 'cat', 'sun']

# Replace the comb and the earring with the wig and the bicycle in Box 10
box_10[0], box_10[1] = 'wig', 'bicycle'

# Remove the grinder from Box 3
box_3.remove('grinder')

# Move the cat and the sun and the bag from Box 3 to Box 10
box_10.extend(box_3[1:])
box_3 = box_3[:1]

# Move the fridge from Box 7 to Box 8
box_8.append(box_7.pop(2))

# Swap the skirt in Box 1 with the rock in Box 11
box_1[2], box_11[0] = box_11[0], box_1[2]

# Replace the truck and the guitar with the dress and the necklace in Box 5
box_5 = ['dress', 'necklace']

# Empty Box 10
box_10 = []

# Empty Box 4
box_4 = []

# Remove the basket and the telescope from Box 7
box_7 = []

# Move the seaweed and the dress from Box 5 to Box 3
box_3.extend(box_5[:1])
box_5 = box_5[1:]

# Remove the meteor from Box 11
box_11 = []

# Remove the ship and the rock and the belt from Box 1
box_1 = []

# Replace the lipstick and the note and the zipper with the guitar and the shoes and the bag in Box 0
box_0 = ['guitar', 'shoes', 'bag']

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