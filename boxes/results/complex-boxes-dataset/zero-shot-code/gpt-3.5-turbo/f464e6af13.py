box_0 = ['guitar', 'dress', 'dog']
box_1 = ['card', 'scarf', 'shorts', 'mountain', 'whistle']
box_2 = ['desert', 'wire', 'thunder', 'seaweed', 'skirt']
box_3 = ['glasses', 'rocket', 'cow', 'note']
box_4 = ['magnet', 'charger', 'tiger', 'snow', 'rock']
box_5 = ['necklace']
box_6 = ['sculpture', 'horn', 'telescope']
box_7 = ['horse', 'wig', 'microwave', 'star']
box_8 = []
box_9 = ['ocean']
box_10 = ['shoe', 'needle']
box_11 = ['sandals', 'cat', 'truck']
box_12 = ['console', 'toaster', 'lion', 'drum']

def print_box(box_index, box):
    print(f"Box {box_index}: {box}")

# Put the coral into Box 11
box_11.append('coral')
print_box(11, box_11)

# Move the needle from Box 10 to Box 6
needle = box_10.pop()
box_6.append(needle)
print_box(10, box_10)
print_box(6, box_6)

# Replace the dog and the dress and the guitar with the pillow and the shark and the snow in Box 0
box_0 = ['pillow', 'shark', 'snow']
print_box(0, box_0)

# Replace the magnet with the thunder in Box 4
box_4[0] = 'thunder'
print_box(4, box_4)

# Swap the shark in Box 0 with the rock in Box 4
box_0[1], box_4[4] = box_4[4], box_0[1]
print_box(0, box_0)
print_box(4, box_4)

# Remove the rocket and the glasses and the note from Box 3
box_3.remove('rocket')
box_3.remove('glasses')
box_3.remove('note')
print_box(3, box_3)

# Put the meteor and the pants and the button into Box 6
box_6.extend(['meteor', 'pants', 'button'])
print_box(6, box_6)

# Move the pants from Box 6 to Box 9
pants = box_6.pop(1)
box_9.append(pants)
print_box(6, box_6)
print_box(9, box_9)

# Swap the cow in Box 3 with the mountain in Box 1
box_3[2], box_1[3] = box_1[3], box_3[2]
print_box(3, box_3)
print_box(1, box_1)

# Put the plane and the horn into Box 0
box_0.extend(['plane', 'horn'])
print_box(0, box_0)

# Move the mountain from Box 3 to Box 7
mountain = box_3.pop(2)
box_7.append(mountain)
print_box(3, box_3)
print_box(7, box_7)

# Swap the button in Box 6 with the coral in Box 11
box_6[2], box_11[1] = box_11[1], box_6[2]
print_box(6, box_6)
print_box(11, box_11)

# Put the camera and the fish and the bird into Box 1
box_1.extend(['camera', 'fish', 'bird'])
print_box(1, box_1)

# Replace the necklace with the boat in Box 5
box_5[0] = 'boat'
print_box(5, box_5)

# Remove the tiger and the charger and the thunder from Box 4
box_4.remove('tiger')
box_4.remove('charger')
box_4.remove('thunder')
print_box(4, box_4)

# Empty Box 10
box_10.clear()
print_box(10, box_10)

# Put the mixer and the whistle into Box 6
box_6.extend(['mixer', 'whistle'])
print_box(6, box_6)

# Swap the snow in Box 4 with the cow in Box 1
box_4[3], box_1[2] = box_1[2], box_4[3]
print_box(4, box_4)
print_box(1, box_1)

# Put the shirt and the storm and the battery into Box 7
box_7.extend(['shirt', 'storm', 'battery'])
print_box(7, box_7)

# Remove the pants and the ocean from Box 9
box_9.remove('pants')
box_9.remove('ocean')
print_box(9, box_9)