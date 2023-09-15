box_0 = ['mask', 'cat']
box_1 = ['coat', 'lion', 'violin', 'moon']
box_2 = []
box_3 = ['watch', 'book', 'harmonica', 'soap', 'brush']
box_4 = ['tie', 'chair', 'doll', 'freezer']
box_5 = ['earring', 'thread', 'dice']
box_6 = []
box_7 = ['storm']
box_8 = ['wig']
box_9 = ['necklace']
box_10 = ['ring', 'forest', 'bear', 'jacket']
box_11 = ['shorts', 'planet']
box_12 = ['oven']
box_13 = ['magnet', 'hat', 'grinder', 'toy', 'paint']

def print_box(box_index):
    if box_index == 0:
        print("Box 0:", box_0)
    elif box_index == 1:
        print("Box 1:", box_1)
    elif box_index == 2:
        print("Box 2:", box_2)
    elif box_index == 3:
        print("Box 3:", box_3)
    elif box_index == 4:
        print("Box 4:", box_4)
    elif box_index == 5:
        print("Box 5:", box_5)
    elif box_index == 6:
        print("Box 6:", box_6)
    elif box_index == 7:
        print("Box 7:", box_7)
    elif box_index == 8:
        print("Box 8:", box_8)
    elif box_index == 9:
        print("Box 9:", box_9)
    elif box_index == 10:
        print("Box 10:", box_10)
    elif box_index == 11:
        print("Box 11:", box_11)
    elif box_index == 12:
        print("Box 12:", box_12)
    elif box_index == 13:
        print("Box 13:", box_13)
    else:
        print("Invalid box index")

# Initial state
print_box(0)
print_box(1)
print_box(2)
print_box(3)
print_box(4)
print_box(5)
print_box(6)
print_box(7)
print_box(8)
print_box(9)
print_box(10)
print_box(11)
print_box(12)
print_box(13)

# Perform operations
box_10.extend(['guitar', 'drum'])
box_1.extend(['magnet', 'sun'])
box_2.extend(['tie', 'storm', 'umbrella'])
box_3.remove('brush')
box_2.remove('umbrella')
box_2.remove('tie')
box_2.extend(['camera', 'usb'])
box_0.remove('cat')
box_0.append('wig')
box_10.remove('brush')
box_4.remove('tie')
box_4.append('camera')
box_8.extend(['chair', 'keyboard'])
box_8.remove('guitar')
box_1.append('chair')
box_4.remove('brush')
box_7.extend(['magnet', 'toy', 'grinder'])
box_11.remove('shorts')
box_11.remove('planet')
box_4.remove('brush')
box_7.remove('grinder')
box_5.remove('dice')
box_0.remove('mask')
box_8.remove('guitar')

# Final state
print_box(0)
print_box(1)
print_box(2)
print_box(3)
print_box(4)
print_box(5)
print_box(6)
print_box(7)
print_box(8)
print_box(9)
print_box(10)
print_box(11)
print_box(12)
print_box(13)