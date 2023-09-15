box_0 = ['clock', 'usb', 'puzzle']
box_1 = ['ocean']
box_2 = ['crown', 'chair', 'shoes', 'storm']
box_3 = ['grinder', 'rock', 'wire']
box_4 = ['coat', 'phone', 'toy']
box_5 = ['book', 'drum', 'magnet', 'comb']
box_6 = ['rain', 'harmonica']
box_7 = ['branch']
box_8 = ['beach']
box_9 = []
box_10 = ['helmet']

box_3 = ['plane', 'polish', 'fish']
box_1.extend(['charger', 'fork'])
box_10 = ['helmet']
box_1.remove('fork')
box_1.remove('ocean')
box_6.remove('harmonica')
box_6.extend(['crown', 'storm', 'chair'])
box_7.remove('branch')
box_9.append('umbrella')
box_4.remove('toy')
box_10.extend(['brush', 'flower', 'usb'])
box_1[1], box_2[2] = box_2[2], box_1[1]
box_10[0], box_4[1] = box_4[1], box_10[0]
box_5 = ['leaf', 'shelf', 'card']
box_2 = ['blender']
box_6.remove('crown')
box_8.extend(['speaker', 'pan'])
box_8[1], box_8[0] = box_8[0], box_8[1]

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")