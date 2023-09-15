box_0 = ['comet', 'dress', 'planet']
box_1 = ['button', 'ocean', 'shampoo']
box_2 = ['puzzle', 'bell']
box_3 = []
box_4 = ['doll', 'wire']
box_5 = ['necklace']
box_6 = ['helmet', 'rocket', 'harmonica', 'fish']
box_7 = ['tiger', 'car']
box_8 = []
box_9 = []
box_10 = ['makeup', 'piano']

box_4 = []

box_1.remove('ocean')
box_2.remove('puzzle')
box_1.append('puzzle')
box_2.append('ocean')

box_5.remove('necklace')
box_1.remove('shampoo')
box_5.append('shampoo')
box_1.append('necklace')

box_2.remove('bell')
box_8.append('bell')

box_6.extend(['paint', 'river'])

box_8.remove('bell')
box_1.append('bell')

box_2.remove('ocean')
box_2.append('dice')

box_5.extend(['perfume', 'ship', 'island'])

box_7.remove('tiger')

box_8.extend(['scissors', 'ring'])

box_5.extend(['toothpaste', 'toaster'])

box_3.extend(['scarf', 'polish', 'submarine'])

box_5.remove('toaster')
box_5.remove('ship')
box_5.remove('island')

box_6.extend(['leaf', 'glasses'])

box_8.remove('ring')
box_8.append('keyboard')

box_3.extend(['cow', 'shirt'])

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
print("Box 10:", box_10)