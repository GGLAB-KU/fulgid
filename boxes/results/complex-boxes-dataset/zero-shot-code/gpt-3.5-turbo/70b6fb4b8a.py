box_0 = []
box_1 = ['towel', 'doll', 'pot', 'comb']
box_2 = ['bus', 'guitar', 'dice']
box_3 = []
box_4 = ['hat']
box_5 = ['razor']
box_6 = ['apple', 'coat', 'rain']
box_7 = ['storm']
box_8 = ['bird']
box_9 = []
box_10 = []
box_11 = ['horn', 'phone']
box_12 = ['mirror', 'forest']
box_13 = []

box_2 = ['shoes', 'motorcycle']
box_2 = ['bus', 'guitar']
box_6 = ['apple', 'coat', 'rain']
box_7 = ['storm']
box_9 = []
box_1.extend(['scissors', 'pot', 'comb'])
box_8.extend(['toaster', 'river', 'pan'])
box_1.extend(['needle', 'basket', 'bracelet'])
box_11.extend(['horn', 'phone'])
box_12, box_11 = box_11, box_12
box_2.append('dice')
box_3 = []
box_12.extend(['wallet', 'forest'])
box_5 = ['razor']
box_8.extend(['coat', 'bird'])
box_7, box_12 = box_12, box_7

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")