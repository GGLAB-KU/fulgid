box_0 = ['mixer']
box_1 = ['drum', 'shampoo', 'butterfly', 'zipper', 'submarine']
box_2 = ['cat']
box_3 = []
box_4 = ['flute', 'grinder', 'rocket']
box_5 = []
box_6 = ['microwave', 'toothpaste', 'bus']
box_7 = ['coin', 'starfish', 'horse', 'harmonica', 'wallet']
box_8 = ['lipstick', 'sandals']
box_9 = ['moon']
box_10 = []
box_11 = []
box_12 = ['bracelet', 'necklace', 'headphone']

box_2.remove('cat')
box_2.append('pillow')
box_2.remove('pillow')
box_2.append('ring')
box_12.remove('headphone')
box_6.remove('toothpaste')
box_6.extend(['doll', 'storm'])
box_0.remove('mixer')
box_0.append('star')
box_8.remove('lipstick')
box_8.append('shorts')
box_6.remove('microwave')
box_6.append('star')
box_12.remove('bracelet')
box_1.append('bracelet')
box_4.clear()
box_8.remove('sandals')
box_8.append('basket')
box_8.append('tree')
box_0.remove('star')
box_8.remove('microwave')
box_8.append('microwave')
box_12.extend(['lightning', 'controller', 'tie'])
box_3.extend(['car', 'belt'])
box_3.remove('car')
box_8.remove('microwave')
box_8.append('car')
box_5.append('spoon')
box_9.remove('moon')
box_9.append('keyboard')
box_3.remove('belt')
box_12.remove('microwave')
box_12.append('belt')
box_7.remove('horse')
box_7.remove('harmonica')
box_7.append('bird')
box_7.append('desert')
box_11.append('bowl')

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
print("Box 11:", box_11)
print("Box 12:", box_12)