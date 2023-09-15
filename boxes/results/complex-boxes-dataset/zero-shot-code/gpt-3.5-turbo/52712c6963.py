box_0 = ['perfume', 'needle', 'thunder']
box_1 = ['planet', 'starfish', 'sock', 'thread', 'truck']
box_2 = ['river', 'glove', 'moon', 'gloves', 'blender']
box_3 = ['book']
box_4 = []
box_5 = ['dress', 'rock', 'note', 'boat']
box_6 = ['battery', 'glasses']
box_7 = ['bell', 'shelf', 'skirt']
box_8 = []
box_9 = ['rain', 'coral', 'storm']
box_10 = ['brush', 'lightning', 'jacket', 'bowl', 'helmet']

def print_box(box_index, box_items):
    if len(box_items) == 0:
        print(f"Box {box_index}: []")
    else:
        print(f"Box {box_index}: {box_items}")

# Remove the bowl and the brush from Box 10
box_10.remove('bowl')
box_10.remove('brush')

# Swap the gloves in Box 2 with the perfume in Box 0
box_0.remove('perfume')
box_2.remove('glove')
box_0.append('glove')
box_2.append('perfume')

# Swap the storm in Box 9 with the dress in Box 5
box_5.remove('dress')
box_9.remove('storm')
box_5.append('storm')
box_9.append('dress')

# Remove the thunder from Box 0
box_0.remove('thunder')

# Swap the gloves in Box 0 with the jacket in Box 10
box_10.remove('jacket')
box_0.remove('glove')
box_10.append('glove')
box_0.append('jacket')

# Put the comb into Box 2
box_2.append('comb')

# Move the book from Box 3 to Box 10
box_10.append(box_3.pop())

# Put the belt into Box 8
box_8.append('belt')

# Remove the needle and the jacket from Box 0
box_0.remove('needle')
box_0.remove('jacket')

# Empty Box 7
box_7.clear()

# Move the perfume and the glove and the comb from Box 2 to Box 10
box_10.extend([box_2.pop(box_2.index('perfume')), box_2.pop(box_2.index('glove')), box_2.pop(box_2.index('comb'))])

# Empty Box 1
box_1.clear()

# Swap the book in Box 10 with the glasses in Box 6
box_10.remove('book')
box_6.remove('glasses')
box_10.append('glasses')
box_6.append('book')

# Replace the glove with the boat in Box 10
box_10.remove('glove')
box_10.append('boat')

# Replace the belt with the river in Box 8
box_8.remove('belt')
box_8.append('river')

# Replace the rain and the dress with the car and the makeup in Box 9
box_9.remove('rain')
box_9.remove('dress')
box_9.extend(['car', 'makeup'])

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