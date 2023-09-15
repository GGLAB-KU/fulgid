box_0 = []
box_1 = ['vase']
box_2 = ['lion', 'book', 'comb']
box_3 = ['shelf', 'river', 'moon', 'lightning', 'bag']
box_4 = ['key']
box_5 = ['dice', 'boot', 'jacket']
box_6 = ['dog', 'storm', 'button']
box_7 = ['shampoo', 'apple']
box_8 = []
box_9 = ['lipstick']

box_9.remove('lipstick')
box_3[0], box_5[1] = box_5[1], box_3[0]
box_7.extend(['belt', 'bicycle', 'sculpture'])
box_6.extend(['chair', 'grass'])
box_5[0] = 'seaweed'
box_2.remove('lion')
box_3[2], box_2[2] = box_2[2], box_3[2]
box_5.extend(['toaster', 'clock', 'button'])
box_9.append('makeup')
box_0.extend(['car', 'needle'])
box_9[0] = 'shark'
box_7[0], box_7[1] = 'cow', 'snow'
box_9.remove('shark')
box_8.append('rain')
box_0.append(box_2.pop(1))

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)