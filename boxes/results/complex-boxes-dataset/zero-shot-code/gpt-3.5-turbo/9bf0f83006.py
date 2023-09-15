box_0 = ['spoon', 'jacket', 'jungle']
box_1 = ['brush', 'starfish']
box_2 = ['mountain', 'coral', 'helmet', 'paint']
box_3 = ['car', 'doll', 'wallet', 'tie']
box_4 = ['bird', 'cloud']
box_5 = ['coat', 'skirt']
box_6 = ['card']
box_7 = ['apple', 'usb', 'tiger']
box_8 = []
box_9 = ['makeup', 'freezer', 'blanket', 'branch', 'umbrella']
box_10 = ['boat', 'battery', 'swimsuit', 'vase', 'clock']
box_11 = ['sandals', 'moon', 'keyboard', 'gloves']
box_12 = ['dolphin']

def print_box(box_index, box_items):
    if len(box_items) == 0:
        print(f"Box {box_index}: []")
    else:
        print(f"Box {box_index}: {box_items}")

# Put the necklace into Box 0
box_0.append('necklace')

# Move the doll and the car and the wallet from Box 3 to Box 12
box_12.extend(box_3[1:])
box_3 = box_3[:1]

# Move the card from Box 6 to Box 5
box_5.append(box_6[0])
box_6 = []

# Remove the tiger and the apple and the usb from Box 7
box_7 = []

# Move the brush and the starfish from Box 1 to Box 5
box_5.extend(box_1)
box_1 = []

# Move the paint and the helmet from Box 2 to Box 3
box_3.extend(box_2[2:])
box_2 = box_2[:2]

# Remove the freezer and the blanket from Box 9
box_9 = box_9[:2] + box_9[3:]

# Replace the moon and the gloves and the keyboard with the flower and the bag and the bus in Box 11
box_11 = ['flower', 'bag', 'bus']

# Remove the doll and the wallet from Box 12
box_12 = box_12[:1]

# Replace the dolphin and the car with the speaker and the cup in Box 12
box_12 = ['speaker', 'cup']

# Swap the bird in Box 4 with the tie in Box 3
box_4[0], box_3[3] = box_3[3], box_4[0]

# Put the island into Box 10
box_10.append('island')

# Put the mixer and the toothpaste into Box 11
box_11.extend(['mixer', 'toothpaste'])

# Move the paint from Box 3 to Box 10
box_10.append(box_3[2])
box_3 = box_3[:2]

# Put the bird into Box 5
box_5.append(box_4[0])
box_4 = []

# Replace the tie and the cloud with the paint and the mountain in Box 4
box_4 = ['paint', 'mountain']

# Put the tiger into Box 6
box_6.append(box_7[2])
box_7 = []

# Move the bird and the helmet from Box 3 to Box 5
box_5.extend(box_3[1:3])
box_3 = box_3[:1]

# Move the toothpaste and the mixer and the flower from Box 11 to Box 2
box_2.extend(box_11[2:])
box_11 = box_11[:2]

# Put the cup into Box 7
box_7.append(box_2[3])
box_2 = box_2[:3]

# Print the contents of each box
print_box(0, box_0)
print_box(1, box_1)
print_box(2, box_2)
print_box(3, box_3)
print_box(4, box_4)
print_box(5, box_5)
print_box(6, box_6)
print_box(7, box_7)
print_box(8, box_8)
print_box(9, box_9)
print_box(10, box_10)
print_box(11, box_11)
print_box(12, box_12)