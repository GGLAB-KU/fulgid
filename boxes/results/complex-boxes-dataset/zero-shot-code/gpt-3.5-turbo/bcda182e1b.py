box_0 = []
box_1 = ['rock', 'planet', 'shelf']
box_2 = ['wire', 'cow', 'mixer', 'dice']
box_3 = ['tape', 'tree', 'clock', 'headphone']
box_4 = ['bear']
box_5 = []
box_6 = ['horn', 'violin', 'usb', 'freezer']
box_7 = ['dress', 'pants', 'spoon', 'paint']
box_8 = ['controller', 'book']
box_9 = ['submarine', 'button']
box_10 = ['telescope', 'leaf', 'shirt', 'helmet', 'moon']
box_11 = ['thread', 'storm', 'snow', 'motorcycle']
box_12 = []
box_13 = ['brush', 'microscope', 'soap']
box_14 = ['microwave', 'boot', 'seaweed']

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
    elif box_num == 13:
        print("Box 13:", box_13)
    elif box_num == 14:
        print("Box 14:", box_14)

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
print_box(14)

box_4.extend(['controller', 'jungle', 'wig'])
box_3.extend(['camera', 'shampoo'])
box_4.remove('controller')
box_4.remove('wig')
box_8_index = box_8.index('book')
box_2_index = box_2.index('wire')
box_8[box_8_index], box_2[box_2_index] = box_2[box_2_index], box_8[box_8_index]
box_3.extend(['makeup', 'necklace'])
box_14.append('tiger')
box_14.extend(['glove', 'branch'])
box_2.clear()
box_3.remove('tree')
box_3.remove('camera')
box_3.remove('necklace')
box_7.extend(['makeup', 'tape'])
box_14_index = box_14.index('microwave')
box_4_index = box_4.index('jungle')
box_14[box_14_index], box_4[box_4_index] = box_4[box_4_index], box_14[box_14_index]
box_4_index = box_4.index('microwave')
box_8.append(box_4.pop(box_4_index))
box_3_index = box_3.index('clock')
box_2_index = box_2.index('horn')
box_3[box_3_index], box_2[box_2_index] = box_2[box_2_index], box_3[box_3_index]
box_14.extend(['microwave', 'controller', 'wire'])
box_2.extend(['lion', 'comet', 'boot'])
box_6_index = box_6.index('freezer')
box_1.append(box_6.pop(box_6_index))
box_1.remove('rock')
box_1.remove('freezer')
box_1.extend(['piano', 'cow'])
box_11.remove('motorcycle')
box_11.remove('snow')
box_11.remove('thread')

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
print_box(14)