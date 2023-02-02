# test_node.py
# Script to test Node class functionality

import node

row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 0]

n1 = node.Node(row1, row2, row3)
print(n1)

new_rows = n1.blank_up()
n2 = node.Node(new_rows[0], new_rows[1], new_rows[2])
print('After moving the blank up:')
print(n2)

new_rows = n2.blank_up()
n3 = node.Node(new_rows[0], new_rows[1], new_rows[2])
print('After moving the blank up again:')
print(n3)

new_rows = n3.blank_left()
n4 = node.Node(new_rows[0], new_rows[1], new_rows[2])
print('After moving the blank left:')
print(n4)

new_rows = n4.blank_left()
n5 = node.Node(new_rows[0], new_rows[1], new_rows[2])
print('After moving the blank left again:')
print(n5)

new_rows = n5.blank_down()
n6 = node.Node(new_rows[0], new_rows[1], new_rows[2])
print('After moving the blank down:')
print(n6)

new_rows = n6.blank_down()
n7 = node.Node(new_rows[0], new_rows[1], new_rows[2])
print('After moving the blank down again:')
print(n7)

new_rows = n7.blank_right()
n8 = node.Node(new_rows[0], new_rows[1], new_rows[2])
print('After moving the blank right:')
print(n8)

new_rows = n8.blank_right()
n9 = node.Node(new_rows[0], new_rows[1], new_rows[2])
print('After moving the blank right again:')
print(n9)