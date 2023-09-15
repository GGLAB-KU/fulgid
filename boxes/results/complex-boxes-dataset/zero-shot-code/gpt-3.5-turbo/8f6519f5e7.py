box_0 = ['shorts']
box_1 = ['grass']
box_2 = ['sculpture']
box_3 = []
box_4 = ['tie']
box_5 = []
box_6 = ['table', 'meteor', 'basket', 'button', 'guitar']
box_7 = ['pot', 'elephant', 'lipstick', 'camera']
box_8 = ['pants', 'dress', 'shelf', 'microscope']
box_9 = []

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
    print("Box 9:", box_9)

# Swap the guitar in Box 6 with the lipstick in Box 7
box_6.remove('guitar')
box_7.remove('lipstick')
box_6.append('lipstick')
box_7.append('guitar')

# Move the tie from Box 4 to Box 7
box_4.remove('tie')
box_7.append('tie')

# Swap the sculpture in Box 2 with the lipstick in Box 6
box_2.remove('sculpture')
box_6.remove('lipstick')
box_2.append('lipstick')
box_6.append('sculpture')

# Swap the meteor in Box 6 with the shorts in Box 0
box_6.remove('meteor')
box_0.remove('shorts')
box_6.append('shorts')
box_0.append('meteor')

# Remove the guitar and the elephant from Box 7
box_7.remove('guitar')
box_7.remove('elephant')

# Move the lipstick from Box 2 to Box 1
box_2.remove('lipstick')
box_1.append('lipstick')

# Move the shorts and the button and the sculpture from Box 6 to Box 8
box_6.remove('shorts')
box_6.remove('button')
box_6.remove('sculpture')
box_8.append('shorts')
box_8.append('button')
box_8.append('sculpture')

# Move the tie and the pot and the camera from Box 7 to Box 0
box_7.remove('tie')
box_7.remove('pot')
box_7.remove('camera')
box_0.append('tie')
box_0.append('pot')
box_0.append('camera')

# Remove the shelf from Box 8
box_8.remove('shelf')

# Move the grass from Box 1 to Box 3
box_1.remove('grass')
box_3.append('grass')

# Move the camera from Box 0 to Box 9
box_0.remove('camera')
box_9.append('camera')

# Remove the basket and the table from Box 6
box_6.remove('basket')
box_6.remove('table')

# Move the grass from Box 3 to Box 9
box_3.remove('grass')
box_9.append('grass')

# Replace the camera and the grass with the makeup and the boot in Box 9
box_9.remove('camera')
box_9.remove('grass')
box_9.append('makeup')
box_9.append('boot')

# Remove the dress and the sculpture and the shorts from Box 8
box_8.remove('dress')
box_8.remove('sculpture')
box_8.remove('shorts')

print_boxes()