box_0 = ['whistle', 'lamp', 'mask', 'keyboard']
box_1 = ['mixer', 'sock', 'brush', 'bicycle']
box_2 = ['rocket']
box_3 = ['toaster', 'lightning', 'pillow', 'moon']
box_4 = []
box_5 = ['butterfly', 'jungle']
box_6 = ['book', 'phone']
box_7 = ['dress', 'umbrella', 'oven', 'jacket']
box_8 = ['microwave']

# Swap microwave in Box 8 with butterfly in Box 5
box_8.append(box_5.pop(box_5.index('butterfly')))

# Remove brush and bicycle from Box 1
box_1.remove('brush')
box_1.remove('bicycle')

# Replace mixer with microwave in Box 1
box_1.append(box_8.pop())

# Remove book from Box 6
box_6.remove('book')

# Remove keyboard from Box 0
box_0.remove('keyboard')

# Replace pillow with branch in Box 3
box_3[2] = 'branch'

# Replace rocket with rain in Box 2
box_2[0] = 'rain'

# Remove dress from Box 7
box_7.remove('dress')

# Remove rain from Box 2
box_2.remove('rain')

# Remove microwave from Box 5
box_5.remove('microwave')

# Move butterfly from Box 8 to Box 3
box_3.append(box_8.pop())

# Empty Box 6
box_6.clear()

# Remove jacket, oven, and umbrella from Box 7
box_7.remove('jacket')
box_7.remove('oven')
box_7.remove('umbrella')

# Remove sock and microwave from Box 1
box_1.remove('sock')
box_1.remove('microwave')

# Print the final contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)