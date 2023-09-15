box_0 = ['card', 'motorcycle', 'plane', 'basket']
box_1 = ['planet', 'mixer', 'bag', 'plate', 'paint']
box_2 = []
box_3 = ['needle']
box_4 = ['shorts', 'meteor', 'piano']
box_5 = ['coin', 'tree']
box_6 = ['dolphin', 'fork']
box_7 = ['star', 'pillow']
box_8 = []
box_9 = []
box_10 = ['shoe', 'tiger']
box_11 = ['glove']

def print_box(box_index, box):
    if len(box) == 0:
        print(f"Box {box_index}: []")
    else:
        print(f"Box {box_index}: {box}")

# Put the elephant and the vase and the tape into Box 8
box_8.extend(['elephant', 'vase', 'tape'])
print_box(8, box_8)

# Put the island into Box 8
box_8.append('island')
print_box(8, box_8)

# Replace the shoe with the phone in Box 10
box_10.remove('shoe')
box_10.append('phone')
print_box(10, box_10)

# Swap the needle in Box 3 with the tape in Box 8
box_3.remove('needle')
box_8.remove('tape')
box_3.append('tape')
box_8.append('needle')
print_box(3, box_3)
print_box(8, box_8)

# Replace the shorts and the piano with the bicycle and the train in Box 4
box_4.remove('shorts')
box_4.remove('piano')
box_4.extend(['bicycle', 'train'])
print_box(4, box_4)

# Remove the train and the bicycle and the meteor from Box 4
box_4.remove('train')
box_4.remove('bicycle')
box_4.remove('meteor')
print_box(4, box_4)

# Put the tape and the forest and the grass into Box 3
box_3.extend(['tape', 'forest', 'grass'])
print_box(3, box_3)

# Put the dress and the cloud and the wig into Box 10
box_10.extend(['dress', 'cloud', 'wig'])
print_box(10, box_10)

# Empty Box 11
box_11.clear()
print_box(11, box_11)

# Empty Box 0
box_0.clear()
print_box(0, box_0)

# Move the fork and the dolphin from Box 6 to Box 9
box_6.remove('fork')
box_6.remove('dolphin')
box_9.extend(['fork', 'dolphin'])
print_box(6, box_6)
print_box(9, box_9)

# Move the tree and the coin from Box 5 to Box 3
box_5.remove('tree')
box_5.remove('coin')
box_3.extend(['tree', 'coin'])
print_box(5, box_5)
print_box(3, box_3)

# Swap the bag in Box 1 with the forest in Box 3
box_1.remove('bag')
box_3.remove('forest')
box_1.append('forest')
box_3.append('bag')
print_box(1, box_1)
print_box(3, box_3)

# Remove the planet from Box 1
box_1.remove('planet')
print_box(1, box_1)

# Swap the tiger in Box 10 with the star in Box 7
box_10.remove('tiger')
box_7.remove('star')
box_10.append('star')
box_7.append('tiger')
print_box(10, box_10)
print_box(7, box_7)

# Swap the paint in Box 1 with the needle in Box 8
box_1.remove('paint')
box_8.remove('needle')
box_1.append('needle')
box_8.append('paint')
print_box(1, box_1)
print_box(8, box_8)

# Move the mixer from Box 1 to Box 9
box_1.remove('mixer')
box_9.append('mixer')
print_box(1, box_1)
print_box(9, box_9)

# Put the bell and the shelf and the necklace into Box 11
box_11.extend(['bell', 'shelf', 'necklace'])
print_box(11, box_11)