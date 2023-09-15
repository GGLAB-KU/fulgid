box_0 = ['octopus', 'paint', 'lipstick']
box_1 = ['sun', 'charger', 'console', 'boat', 'basket']
box_2 = ['drum', 'zipper']
box_3 = ['tie', 'shoe', 'mixer', 'jungle']
box_4 = ['snow', 'telescope', 'car', 'bowl', 'comet']
box_5 = ['horse', 'necklace', 'puzzle', 'cat']
box_6 = ['desert', 'glove']
box_7 = ['swimsuit']
box_8 = []

box_0.remove('paint')
box_0.remove('lipstick')
box_0.append('polish')
box_0.append('tape')

box_1.remove('sun')
box_1.remove('console')
box_1.remove('basket')

box_7.remove('swimsuit')

box_6.remove('glove')

box_1.remove('charger')
box_1.remove('boat')

box_4.remove('comet')
box_4.remove('bowl')
box_4.append('rain')
box_4.append('shark')

box_2.remove('drum')

box_6, box_5 = box_5, box_6

box_2.clear()

box_5.append('truck')

box_1.append('lightning')
box_1.append('controller')

box_6.remove('desert')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)