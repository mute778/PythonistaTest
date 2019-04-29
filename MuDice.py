import ui
import random

# Const
MIN_CELL = 2
MAX_CELL = 100
MIN_DICE_NUM = 1
MAX_DICE_NUM = 100

# Values
Cell = 6
DiceNum = 1
ResultCell = []

def change_cell(sender):
	value = int(sender.title)
	global Cell
	Cell += value
	if Cell < MIN_CELL:
		Cell = MIN_CELL
	elif Cell > MAX_CELL:
		Cell = MAX_CELL
	O_cellText.text = str(Cell)
	
def change_dice_num(sender):
	value = int(sender.title)
	global DiceNum
	DiceNum += value
	if DiceNum < MIN_DICE_NUM:
		DiceNum = MIN_DICE_NUM
	elif  DiceNum > MAX_DICE_NUM:
		DiceNum = MAX_DICE_NUM
	O_diceNumText.text = str(DiceNum)
	
def roll_dice(sender):
	totalValue = 0
	for cnt in range(DiceNum):
		roll = random.randint(1, Cell)
		totalValue += roll
	O_totalText.text = str(totalValue)
	
def update_player_life():
	O_p1lp.text = "{:,}".format(Player01LP)
	O_p2lp.text = "{:,}".format(Player02LP)
	
def change_life_value(target, value):
	if target == PLAYER_01:
		Player01LP = Player01LP + value
	elif target == PLAYER_02:
		Player02LP = Player02LP + value
	update_player_life()
		
def init_setting():
	update_player_life()
	
#init_setting()

v = ui.load_view()
v.present('sheet')
O_debug = v['text_debug']
O_cellText = v['text_cell']
O_diceNumText = v['text_diceNum']
O_totalText = v['text_total']

O_cellText.text = str(Cell)
O_diceNumText.text = str(DiceNum)

