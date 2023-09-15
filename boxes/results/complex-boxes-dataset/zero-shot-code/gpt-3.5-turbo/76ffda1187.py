box_0 = ['grass', 'sandals', 'piano']
box_1 = []
box_2 = ['fork', 'brush']
box_3 = ['shoe', 'scissors']
box_4 = ['usb']

box_4.remove('usb')
box_4.append('clock')

box_0 = ['jungle', 'needle', 'dress']
box_2 = []

box_3.remove('shoe')

box_4.remove('clock')
box_4.append('rain')

box_4.remove('rain')

box_0[2], box_3[1] = box_3[1], box_0[2]

boxes = [box_0, box_1, box_2, box_3, box_4]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")