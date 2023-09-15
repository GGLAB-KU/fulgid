box_0 = ['leaf']
box_1 = ['watch', 'keyboard', 'mountain', 'fish']
box_2 = ['table', 'button', 'book', 'telescope', 'dolphin']
box_3 = ['horse', 'microwave']
box_4 = ['flower', 'tiger', 'shoe', 'lion']

box_2.remove('dolphin')
box_2.remove('table')
box_4.remove('tiger')
box_4.remove('lion')
box_1.remove('keyboard')
box_1.remove('mountain')
box_2 = []
box_1.append('note')
box_1.remove('watch')
box_1.extend(box_3)
box_3 = []
box_4[box_4.index('grass')] = 'microwave'

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)