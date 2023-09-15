box_0 = ['fridge', 'magnet', 'phone', 'coin']
box_1 = ['apple', 'sock', 'planet', 'drum', 'horse']
box_2 = []
box_3 = ['toaster', 'thunder']
box_4 = ['controller']
box_5 = ['wire']
box_6 = ['storm', 'vase']
box_7 = ['coat', 'octopus', 'comb', 'boot']
box_8 = ['flute', 'shoe', 'starfish', 'shoes', 'earring']
box_9 = ['laptop']
box_10 = ['umbrella', 'beach']
box_11 = []
box_12 = ['console', 'towel', 'island']

box_4 = ['controller']
box_1.remove('drum')
box_5 = ['wire']
box_7[2] = 'controller'
box_8[0] = 'wire'
box_6[0] = 'apple'
box_8[2:4] = ['game', 'rain']
box_7.remove('comb')
box_10.clear()
box_0.append('toaster')
box_0[3] = 'bicycle'
box_9 = []
box_0.append('laptop')
box_8[1] = 'thunder'
box_1.clear()
box_11.append('laptop')
box_12[1] = 'wallet'
box_1[2] = 'violin'
box_12.remove('wallet')
box_3[1] = 'fish'
box_3.remove('fish')

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")