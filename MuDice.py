import ui

PLAYER_01 = 0
PLAYER_02 = 1
DAMAGE = 0
RECOVERY = 1
Player01LP = 2500
Player02LP = 2500

v = ui.load_view()
v.present('sheet')

O_p1lp = v['label4']
O_p2lp = v['label6']

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
	
init_setting()
