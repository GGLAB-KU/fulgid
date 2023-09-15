box0 = ['plane', 'jungle', 'pen']
box1 = ['comet']
box2 = []
box3 = []

def print_boxes():
    print("Box 0:", box0)
    print("Box 1:", box1)
    print("Box 2:", box2)
    print("Box 3:", box3)

# Put the helmet into Box 1
box1.append('helmet')
print_boxes()

# Move the helmet from Box 1 to Box 0
box0.append(box1.pop())
print_boxes()

# Put the shoes and the laptop into Box 0
box0.extend(['shoes', 'laptop'])
print_boxes()

# Empty Box 1
box1.clear()
print_boxes()

# Put the harmonica and the cloud into Box 0
box0.extend(['harmonica', 'cloud'])
print_boxes()

# Move the plane and the shoes from Box 0 to Box 1
box1.append(box0.pop(0))
box1.append(box0.pop(1))
print_boxes()