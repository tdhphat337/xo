import pygame

# khởi tạo pygame
pygame.init()
RED=(255,0,0)
BLUE=(0,0,255)
# Setting up the game window
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Caro Chess Game")

# định nghĩa các biến toàn cục
board_size = 15
board = [[0 for x in range(board_size)] for y in range(board_size)]
player = 1

font=pygame.font.SysFont('san',40)
# Defining game functions
def draw_board():
	# vẽ bàn cờ
	for x in range(board_size):
		for y in range(board_size):
			pygame.draw.rect(window, (255, 255, 255), (x * 40, y * 40, 40, 40), 1)

def draw_pieces():
	# vẽ các mãnh của bàn cờ
	for x in range(board_size):
		for y in range(board_size):
			if board[x][y] == 1:
				pygame.draw.circle(window, (0, 0, 255), (x * 40 + 20, y * 40 + 20), 18)
			elif board[x][y] == 2:
				pygame.draw.circle(window, (255, 255, 255), (x * 40 + 20, y * 40 + 20), 18)

def place_piece(x, y):
	# Đặt một mảnh trò chơi trên bảng
	global player
	if board[x][y] == 0:
		board[x][y] = player
		if player == 1:
			player = 2
		else:
			player = 1

def check_game_over():
	# Check nếu trò chơi kết thúc
	for x in range(board_size):
		for y in range(board_size):
			if board[x][y] == 0: return False
	return True

def check_horizontal_win():
	# Check for thắng theo chiều ngang
	for x in range(board_size - 4):
		for y in range(board_size):
			if board[x][y] == board[x+1][y] == board[x+2][y] == board[x+3][y] == board[x+4][y] and board[x][y] != 0: 
				return True
	return False

def check_vertical_win():
	# kiểm tra thắng dọc
	for x in range(board_size):
		for y in range(board_size - 4):
			if board[x][y] == board[x][y+1] == board[x][y+2] == board[x][y+3] == board[x][y+4] and board[x][y] != 0:
				return True
	return False
def check_diagonal_win():
	# kiểm tra thắng chéo
	for x in range(board_size - 4):
		for y in range(board_size - 4):
			if board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3] == board[x+4][y+4] and board[x][y] != 0:
				return True
	for x in range(4, board_size):
		for y in range(board_size - 4):
			if board[x][y] == board[x-1][y+1] == board[x-2][y+2] == board[x-3][y+3] == board[x-4][y+4] and board[x][y] != 0:
				player=0
				return True
	return False

# Main game loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x, y = event.pos
			x = x // 40
			y = y // 40
			place_piece(x, y)

	# vẽ bàn cờ và mãnh
	draw_board()
	draw_pieces()

	# kiểm tra nếu game kết thúc và điều kiện để dành chiến thắng
	if check_game_over():
		player = 0
		print("Game over")
		running = False
	elif check_horizontal_win() or check_vertical_win() or check_diagonal_win():
		
		win_txt = font.render("Player "+str(player)+" wins", True, BLUE)
		window.blit(win_txt, (610, 260))
		game_over_txt = font.render("Game Over!!!", True, RED)
		window.blit(game_over_txt, (610, 200))

	pygame.display.update()

pygame.quit()