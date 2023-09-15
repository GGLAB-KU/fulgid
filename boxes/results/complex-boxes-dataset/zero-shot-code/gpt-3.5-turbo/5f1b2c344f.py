box_0 = ['beach', 'coin', 'thunder', 'bowl', 'makeup']
box_1 = ['coral', 'basket', 'guitar', 'cup']
box_2 = ['earring']
box_3 = []
box_4 = ['blanket', 'phone']
box_5 = ['pillow']
box_6 = ['puzzle', 'key', 'toothbrush', 'table']
box_7 = []
box_8 = ['desert', 'ring', 'boot', 'bracelet', 'microscope']

# Remove coral from Box 1
box_1.remove('coral')

# Swap earring in Box 2 with blanket in Box 4
earring = box_2.pop(0)
blanket = box_4.pop(0)
box_2.append(blanket)
box_4.append(earring)

# Move cup, guitar, and basket from Box 1 to Box 6
box_6.extend(box_1)
box_1.clear()

# Empty Box 6
box_6.clear()

# Remove coin from Box 0
box_0.remove('coin')

# Move phone from Box 4 to Box 5
phone = box_4.pop(0)
box_5.append(phone)

# Move blanket from Box 2 to Box 8
blanket = box_2.pop(0)
box_8.append(blanket)

# Move bowl from Box 0 to Box 6
bowl = box_0.pop(box_0.index('bowl'))
box_6.append(bowl)

# Remove bracelet from Box 8
box_8.remove('bracelet')

# Put mirror, coral, and dice into Box 5
box_5.extend(['mirror', 'coral', 'dice'])

# Put usb into Box 6
box_6.append('usb')

# Swap earring in Box 4 with blanket in Box 8
earring = box_4.pop(0)
blanket = box_8.pop(box_8.index('blanket'))
box_4.append(blanket)
box_8.append(earring)

# Swap microscope in Box 8 with blanket in Box 4
microscope = box_8.pop(box_8.index('microscope'))
blanket = box_4.pop(0)
box_8.append(blanket)
box_4.append(microscope)

# Put paint and beach into Box 6
box_6.extend(['paint', 'beach'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)