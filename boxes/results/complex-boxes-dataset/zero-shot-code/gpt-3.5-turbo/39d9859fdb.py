box_0 = ['camera']
box_1 = ['thunder', 'car', 'dress']
box_2 = ['swimsuit', 'flower', 'perfume', 'lipstick']
box_3 = ['razor', 'bus']
box_4 = ['jacket', 'sock']
box_5 = []
box_6 = ['glasses', 'tree', 'cup', 'lightning']
box_7 = ['bicycle', 'mirror']
box_8 = ['bear', 'brush']
box_9 = ['flute', 'pillow', 'submarine', 'horn']
box_10 = ['branch', 'sun']
box_11 = []
box_12 = ['planet', 'rocket', 'paint']

def print_box(box_num):
    if box_num == 0:
        print("Box 0:", box_0)
    elif box_num == 1:
        print("Box 1:", box_1)
    elif box_num == 2:
        print("Box 2:", box_2)
    elif box_num == 3:
        print("Box 3:", box_3)
    elif box_num == 4:
        print("Box 4:", box_4)
    elif box_num == 5:
        print("Box 5:", box_5)
    elif box_num == 6:
        print("Box 6:", box_6)
    elif box_num == 7:
        print("Box 7:", box_7)
    elif box_num == 8:
        print("Box 8:", box_8)
    elif box_num == 9:
        print("Box 9:", box_9)
    elif box_num == 10:
        print("Box 10:", box_10)
    elif box_num == 11:
        print("Box 11:", box_11)
    elif box_num == 12:
        print("Box 12:", box_12)
    else:
        print("Invalid box number")

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

# Update state
box_9 = ['controller']
box_0 = ['fish']
box_4.remove('sock')
box_11.append('sock')
box_12.remove('paint')
box_6.remove('tree')
box_6.remove('lightning')
box_2.remove('flower')
box_12.append('flower')
box_6.remove('cup')
box_6.remove('glasses')
box_3.remove('razor')
box_8.append('razor')
box_3.remove('bus')
box_5.append('bus')
box_1.remove('dress')
box_1.remove('thunder')
box_1.append('planet')
box_1.append('soap')
box_7.remove('bicycle')
box_7.remove('mirror')
box_12.append('bicycle')
box_12.append('game')
box_8 = []
box_5.append('horn')
box_5.append('lightning')
box_5.append('thunder')
box_0.remove('fish')

# Updated state
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