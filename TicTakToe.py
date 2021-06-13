#Подключаем библиотеки

from tkinter import *
import random

# Тут прописывается функция которая определяет чей ход будет следущий 

def next_turn(row, column):
	global player

	# Ставим условия при котрых текс в ячеке пустой и победитель не определен 

	if buttons[row][column]['text'] == "" and check_winner() is False:

		# Если игрок = 1 игроку то у него есть возможность поставить знак в ячеку крестик или нолик 

		if player == players[0]:

			buttons[row][column]['text'] = player

			#Если при поставлении знака игрок не выигрывает, то игрок = 2 игроку, и высвечивается команда = "Очередь 2 игрока"
			# И он может ставитб знак в пустую ячейку

			if check_winner() is False:
				player = players[1]
				label.config(text = (players[1] + " turn"))

				# Если после того как игрок 1 или 2 поставтл знак и он выйграл то высвечивается надпись "1 или 2 игрок победил"

			elif check_winner() is True:
				label.config(text = (players[0] + " wins"))

				# Если ничья то выходит надпись "Ничья"

			elif check_winner() == "Draw":
				label.config(text = ("Draw!"))

				# Просиходит такой же алгоритм только с другим игроком давая возможность играть по очереди

		else:

			buttons[row][column]['text'] = player

			if check_winner() is False:
				player = players[0]
				label.config(text = (players[0] + " turn"))

			elif check_winner() is True:
				label.config(text = (players[1] + " wins"))

			elif check_winner() == "Draw":
				label.config(text = ("Draw!"))

# В этой функции мы будем обьяснять когда игрок выигрывает, тоесть ставит 3 знака по горизонтали, по вертикали, по диагонали
def check_winner():


	# В этом случае выйгрышь происходит по вертикали тоесть | так ,также мы меняем цвет у всех 3 ячеек если они совпадают с условиями
	for row in range(3):
		if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
			buttons[row][0].config(bg = "green")
			buttons[row][1].config(bg = "green")
			buttons[row][2].config(bg = "green")
			return True

     #В этом случае выйгрышь происходит по горизонтали тоесть --- так
	for column in range(3):
		if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
			buttons[0][column].config(bg = "green")
			buttons[1][column].config(bg = "green")
			buttons[2][column].config(bg = "green")
			return True

	#В этом случае выйгрышь происходит по диагонали с левого верзнего угла по правый нижний угол
	if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
		buttons[0][0].config(bg = "green")
		buttons[1][1].config(bg = "green")
		buttons[2][2].config(bg = "green")
		return True
    # Тут с левого нижнего угла до правого верхнего угла по диагонали  
	if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
		buttons[0][2].config(bg = "green")
		buttons[1][1].config(bg = "green")
		buttons[2][0].config(bg = "green")
		return True
    
    # Если у нас все ячеки заполнены и нет победителя то происходит ничья и все ячейки становятся желтого цвета
	elif empty_space() is False:
		for row in range(3):
			for column in range(3):
				buttons[row][column].config(bg="yellow")
		return "Draw"

	else:
		return False

  # Функция отвечаюшая за свободное место в ячейках, всего 9 ячеек 
def empty_space():
	spaces = 9

	# Если любая кнопка не равняется пустой ячейке то количевство пустых ячеек обновляется и сокращается на 1

	for row in range(3):
		for column in range(3):
			if buttons[row][column]["text"] != "":
				spaces -= 1

	if spaces == 0:
		return False

	else:
		return True


    # Cоздаем функцию где будет логика при нажатии кнопки "Обновить"
def new_game():
	global player

    # При нажатии будет заново и рандомно выбираться игрок и знак
	player = random.choice(players)

	label.config(text=player + " turn")

	# И когда произойдет обновления все я чейки обновятся и удалят текс и цвет и будут пустыми и пригодными к новой игре

	for row in range(3):
		for column in range(3):
			buttons[row][column].config(text = "", bg = ("#F0F0F0"))



			
			# Тут мы создаем окно, название игры, что можно испоьзовать в качевстве знаков и поле игры 3 на 3

window = Tk()
window.title("Крестики-нолики")
players = ["x", "o"]
player = random.choice(players)
buttons =[[0,0,0],
   		  [0,0,0],
   		  [0,0,0]]

   # Создаем переменную которая отвечает за текст который находится навверху и гласит "Очередь 1 или 2 игрока"

label = Label(text = player + " turn", font = ("consolas", 40))
label.pack(side = "top")

   # Создаем кнопку сверху игры котрая твечает за оновление игры и гласит "Обновить"

reset_button = Button(text = "restart", font = ('consolas', 20), command = new_game)
reset_button.pack(side = "top")

   # Создаем рамку нашего приложения 

frame = Frame(window)
frame.pack()

    # Создаем разметку на нашем поле игры и обозначаем конпки по вертикали и по горизонтали 

for row in range(3):
	for column in range(3):
		buttons[row][column] = Button(frame,text="",font=('consolas',40), width=5, height=2, command= lambda row=row, column=column:next_turn(row, column))
		buttons[row][column].grid(row = row, column = column)

window.mainloop()