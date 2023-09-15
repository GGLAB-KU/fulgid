box_0 = ['star', 'truck']
box_1 = ['mask', 'beach', 'pot', 'bus']
box_2 = ['blender', 'tape']
box_3 = ['glove', 'planet', 'note', 'guitar', 'oven']
box_4 = ['fork', 'flute', 'drum', 'scissors']
box_5 = ['cow', 'vase']
box_6 = ['microscope', 'perfume', 'elephant', 'earring']
box_7 = ['shorts', 'storm', 'phone', 'motorcycle', 'usb']
box_8 = ['soap', 'polish', 'key']

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

def put_item_in_box(item, box_index):
    if box_index == 0:
        box_0.append(item)
    elif box_index == 1:
        box_1.append(item)
    elif box_index == 2:
        box_2.append(item)
    elif box_index == 3:
        box_3.append(item)
    elif box_index == 4:
        box_4.append(item)
    elif box_index == 5:
        box_5.append(item)
    elif box_index == 6:
        box_6.append(item)
    elif box_index == 7:
        box_7.append(item)
    elif box_index == 8:
        box_8.append(item)

def remove_item_from_box(item, box_index):
    if box_index == 0:
        box_0.remove(item)
    elif box_index == 1:
        box_1.remove(item)
    elif box_index == 2:
        box_2.remove(item)
    elif box_index == 3:
        box_3.remove(item)
    elif box_index == 4:
        box_4.remove(item)
    elif box_index == 5:
        box_5.remove(item)
    elif box_index == 6:
        box_6.remove(item)
    elif box_index == 7:
        box_7.remove(item)
    elif box_index == 8:
        box_8.remove(item)

def swap_items(box_index_1, item_1, box_index_2, item_2):
    remove_item_from_box(item_1, box_index_1)
    remove_item_from_box(item_2, box_index_2)
    put_item_in_box(item_1, box_index_2)
    put_item_in_box(item_2, box_index_1)

# Initial state
print_boxes()

# Perform operations
put_item_in_box('boot', 3)
swap_items(7, 'storm', 4, 'storm')
remove_item_from_box('glove', 3)
remove_item_from_box('cow', 5)
swap_items(2, 'tape', 7, 'usb')
swap_items(3, 'oven', 4, 'flute')
put_item_in_box('table', 8)
put_item_in_box('toothbrush', 3)
put_item_in_box('coat', 3)
put_item_in_box('clock', 3)
put_item_in_box('star', 7)
put_item_in_box('drum', 3)
swap_items(1, 'book', 4, 'fork')

# Final state
print_boxes()