box_0 = ['grinder', 'flute', 'earring', 'battery']
box_1 = ['shark', 'cloud', 'table', 'bag', 'helmet']
box_2 = []
box_3 = ['magnet', 'bowl', 'sandals', 'thunder', 'note']
box_4 = ['speaker']
box_5 = ['laptop', 'sun', 'bicycle', 'frame']
box_6 = ['jacket', 'mask']
box_7 = ['tiger', 'car', 'doll', 'gloves']
box_8 = []
box_9 = ['shelf', 'horse', 'scissors', 'dolphin']
box_10 = []
box_11 = ['boat', 'forest', 'key', 'watch', 'drum']
box_12 = ['spoon', 'rocket', 'fork', 'soap']
box_13 = ['comb']
box_14 = ['mountain']

def print_box_contents(box_index, box):
    if len(box) == 0:
        print(f"Box {box_index}: []")
    else:
        print(f"Box {box_index}: {box}")

# Remove the speaker from Box 4
box_4.remove('speaker')

# Move the car from Box 7 to Box 11
car = box_7.pop(1)
box_11.append(car)

# Replace the jacket and the mask with the pen and the moon in Box 6
pen = box_6.pop(0)
moon = box_6.pop(0)
box_6.extend([pen, moon])

# Remove the battery from Box 0
box_0.remove('battery')

# Remove the cloud and the bag from Box 1
box_1.remove('cloud')
box_1.remove('bag')

# Remove the watch from Box 11
box_11.remove('watch')

# Replace the table and the shark with the makeup and the harmonica in Box 1
table = box_1.pop(0)
shark = box_1.pop(0)
makeup = 'makeup'
harmonica = 'harmonica'
box_1.extend([makeup, harmonica])

# Replace the comb with the note in Box 13
box_13.remove('comb')
note = 'note'
box_13.append(note)

# Move the pen from Box 6 to Box 7
pen = box_6.pop(0)
box_7.append(pen)

# Swap the mountain in Box 14 with the sun in Box 5
mountain = box_14.pop(0)
sun = box_5.pop(1)
box_14.append(sun)
box_5.append(mountain)

# Move the sun from Box 14 to Box 7
sun = box_14.pop(0)
box_7.append(sun)

# Remove the mountain from Box 5
box_5.remove('mountain')

# Empty Box 11
box_11.clear()

# Put the oven into Box 12
oven = 'oven'
box_12.append(oven)

# Move the note from Box 13 to Box 0
note = box_13.pop(0)
box_0.append(note)

# Remove the sun from Box 7
box_7.remove('sun')

# Replace the tiger and the gloves and the doll with the vase and the jacket and the sandals in Box 7
tiger = box_7.pop(0)
gloves = box_7.pop(1)
doll = box_7.pop(1)
vase = 'vase'
jacket = 'jacket'
sandals = 'sandals'
box_7.extend([vase, jacket, sandals])

# Replace the bicycle with the wire in Box 5
bicycle = box_5.pop(2)
wire = 'wire'
box_5.insert(2, wire)

# Remove the helmet from Box 1
box_1.remove('helmet')

# Move the earring from Box 0 to Box 5
earring = box_0.pop(2)
box_5.append(earring)

# Swap the rocket in Box 12 with the shelf in Box 9
rocket = box_12.pop(1)
shelf = box_9.pop(0)
box_12.append(shelf)
box_9.append(rocket)

# Swap the sandals in Box 3 with the frame in Box 5
sandals = box_3.pop(2)
frame = box_5.pop(3)
box_3.append(frame)
box_5.append(sandals)

# Print the contents of each box
print_box_contents(0, box_0)
print_box_contents(1, box_1)
print_box_contents(2, box_2)
print_box_contents(3, box_3)
print_box_contents(4, box_4)
print_box_contents(5, box_5)
print_box_contents(6, box_6)
print_box_contents(7, box_7)
print_box_contents(8, box_8)
print_box_contents(9, box_9)
print_box_contents(10, box_10)
print_box_contents(11, box_11)
print_box_contents(12, box_12)
print_box_contents(13, box_13)
print_box_contents(14, box_14)