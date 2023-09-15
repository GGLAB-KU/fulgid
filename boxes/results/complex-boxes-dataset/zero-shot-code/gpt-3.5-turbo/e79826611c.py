box_0 = ['snow', 'lipstick', 'thread']
box_1 = ['helmet', 'dog', 'pot', 'horn']
box_2 = ['plate']
box_3 = []
box_4 = []
box_5 = ['mountain', 'towel', 'fridge']
box_6 = ['cat', 'rain', 'starfish', 'bus', 'jungle']
box_7 = ['flute', 'vase', 'sandals', 'headphone', 'wire']
box_8 = ['shelf']
box_9 = ['apple']

box_9.extend(['keyboard', 'sun', 'forest'])
box_3.append('island')
box_8.remove('shelf')
box_5.remove('mountain')
box_8.append('towel')
box_8.remove('towel')
box_8.append('violin')
box_8.extend(box_6.pop(0))
box_8.extend(box_6.pop(-1))
box_5.remove('fridge')
box_6.remove('jungle')
box_6.remove('rain')
box_6.extend(['headphone', 'sock'])
box_1.remove('dog')
box_1.remove('pot')
box_1.remove('horn')
box_9.remove('forest')
box_8.clear()
box_7.append(box_2.pop(0))
box_4.append(box_1.pop(0))
box_7.remove('sandals')
box_7.remove('plate')
box_7.remove('wire')
box_7.extend(['usb', 'dice', 'blender'])

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")