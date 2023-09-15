box_0 = ['cow', 'fridge', 'wig', 'shelf', 'motorcycle']
box_1 = []
box_2 = ['button', 'shark', 'seaweed']
box_3 = []
box_4 = ['note']
box_5 = ['guitar', 'watch', 'horn']
box_6 = ['star']
box_7 = ['microwave', 'fork', 'butterfly']
box_8 = ['vase', 'desert', 'table', 'submarine', 'cup']

def print_boxes():
    print("Box 0:", box_0)
    print("Box 1:", box_1)
    print("Box 2:", box_2)
    print("Box 3:", box_3)
    print("Box 4:", box_4)
    print("Box 5:", box_5)
    print("Box 6:", box_6)
    print("Box 7:", box_7)
    print("Box 8:", box_8)

# Put the horse into Box 3
box_3.append('horse')

# Put the rocket and the microscope and the meteor into Box 8
box_8.extend(['rocket', 'microscope', 'meteor'])

# Remove the basket and the seaweed from Box 2
box_2.remove('basket')
box_2.remove('seaweed')

# Swap the microwave in Box 7 with the shelf in Box 0
box_7.remove('microwave')
box_0.remove('shelf')
box_7.append('shelf')
box_0.append('microwave')

# Remove the note from Box 4
box_4.remove('note')

# Remove the microscope and the submarine from Box 8
box_8.remove('microscope')
box_8.remove('submarine')

# Move the butterfly and the fork and the shelf from Box 7 to Box 2
box_7.remove('butterfly')
box_7.remove('fork')
box_2.extend(['butterfly', 'fork', 'shelf'])

# Remove the vase and the rocket and the cup from Box 8
box_8.remove('vase')
box_8.remove('rocket')
box_8.remove('cup')

# Move the horse from Box 3 to Box 6
box_3.remove('horse')
box_6.append('horse')

# Put the clock and the shoe and the brush into Box 1
box_1.extend(['clock', 'shoe', 'brush'])

# Put the car and the leaf and the phone into Box 6
box_6.extend(['car', 'leaf', 'phone'])

# Remove the phone from Box 6
box_6.remove('phone')

# Swap the horn in Box 5 with the table in Box 8
box_5.remove('horn')
box_8.remove('table')
box_5.append('table')
box_8.append('horn')

# Replace the meteor with the earring in Box 8
box_8.remove('meteor')
box_8.append('earring')

# Print the final state of the boxes
print_boxes()