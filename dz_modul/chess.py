import random


def chess_module(chessboard):
	for i in range(len(chessboard)):
		for j in range(i + 1, len(chessboard)):

			if chessboard[i][0] == chessboard[j][0] or chessboard[i][1] == chessboard[j][1] or abs(
					chessboard[i][0] - chessboard[j][0]) == abs(chessboard[i][1] - chessboard[j][1]):
				return True
	return False


chessboard = []

# for i in range(8):
row = list(random.randint(1, 8) for _ in range(8))
col = list(random.randint(1, 8) for _ in range(8))
# row, col = map(int, input("Введите координаты 8 ферзей в формате: x y ").split())
chessboard.append(row)
chessboard.append(col)
print(row, col, sep='\n')

if chess_module(chessboard):
	print("False")
else:
	print("True")

'''Проверяйте различный случайные варианты и выведите 4 успешных расстановки.'''
# [5, 6, 8, 1, 3, 2, 4, 5]
# [8, 2, 2, 3, 4, 2, 2, 5]
# True
# [8, 7, 6, 5, 2, 2, 8, 2]
# [1, 1, 6, 4, 3, 8, 2, 7]
# True
# [3, 6, 8, 6, 3, 1, 8, 1]
# [6, 1, 1, 5, 4, 3, 5, 1]
# True
# [7, 3, 7, 7, 5, 5, 6, 6]
# [4, 5, 6, 3, 1, 6, 7, 3]
# True
#
