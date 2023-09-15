box_0 = []
box_1 = ['dog', 'train', 'plane', 'bus']
box_2 = ['mountain', 'boot']
box_3 = []
box_4 = ['jungle', 'soap']
box_5 = ['hat', 'wig']
box_6 = ['bird']
box_7 = ['phone']
box_8 = []
box_9 = []
box_10 = ['grinder', 'branch']

def print_box(box_name, box_items):
    if len(box_items) == 0:
        print(f"Box {box_name}: []")
    else:
        print(f"Box {box_name}: {box_items}")

# Move the mirror from Box 6 to Box 4
box_4.append(box_6.pop())

# Swap the spoon in Box 1 with the boot in Box 2
box_1[1], box_2[1] = box_2[1], box_1[1]

# Remove the mixer and the spoon from Box 2
box_2.remove('mixer')
box_2.remove('spoon')

# Remove the towel and the shark from Box 5
box_5.remove('towel')
box_5.remove('shark')

# Replace the mirror and the pot with the towel and the hat in Box 4
box_4.remove('mirror')
box_4.remove('pot')
box_4.append('towel')
box_4.append('hat')

# Empty Box 1
box_1.clear()

# Put the jacket and the speaker and the horse into Box 5
box_5.append('jacket')
box_5.append('speaker')
box_5.append('horse')

# Empty Box 6
box_6.clear()

# Replace the elephant with the basket in Box 10
box_10.remove('elephant')
box_10.append('basket')

# Move the basket and the branch and the grinder from Box 10 to Box 7
box_7.extend(box_10)
box_10.clear()

# Move the basket from Box 7 to Box 10
box_10.append(box_7.pop())

# Put the sculpture into Box 9
box_9.append('sculpture')

# Remove the sculpture from Box 9
box_9.remove('sculpture')

# Empty Box 10
box_10.clear()

# Swap the jungle in Box 4 with the grinder in Box 7
box_4[0], box_7[0] = box_7[0], box_4[0]

# Replace the horse and the wig and the speaker with the controller and the starfish and the tiger in Box 5
box_5.remove('horse')
box_5.remove('wig')
box_5.remove('speaker')
box_5.append('controller')
box_5.append('starfish')
box_5.append('tiger')

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