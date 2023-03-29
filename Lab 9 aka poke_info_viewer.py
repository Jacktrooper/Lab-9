from tkinter import *
from tkinter import ttk
from poke_api import get_pokemon_info
from tkinter import messagebox

# Create the window
root = Tk()
root.title("Pokemon Info Viewer")
root.resizable(False, False)

# Add frames to window

frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, pady=(20, 10))

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky=N)

frm_btm_right = ttk.LabelFrame(root, text='Stats')
frm_btm_right.grid(row=1, column=1, padx=(20, 10), pady=(10, 20))

# Add wdeges to frames

lbl_name = ttk.Label(frm_top, text='Pokemon name:')
lbl_name.grid(row=0, column=0, pady=(10, 23))

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, padx=(20, 10), pady=(10, 20))

def handle_get_info():
    # Get the Pokemon name enterd by the user
    poke_name = ent_name.get()
    if len(poke_name) == 0:
        return
    # Get the pokemon info from PokeAPI
    poke_info = get_pokemon_info(poke_name)
    if poke_info is None:
        err_meg = f'Unable to fetch info for {poke_name.capitalize()} from the PokeAPI.'
        messagebox.showinfo(title='Error', message=err_meg, icon='error')

    # Populate the info values
    lbl_height_int['text'] = f"{poke_info['height']} dm"
    
    lbl_weight_int['text'] = f"{poke_info['weight']} hg"
    
    types_list = [t['type']['name'] for t in poke_info['types']]
    types = ', '.join(types_list).title()
    lbl_type_value['text'] = types 

    

    hp_bar['value'] = poke_info['stats'][0]['base_stat']
    bar_attack['value'] = poke_info['stats'][1]['base_stat']
    bar_defense['value'] = poke_info['stats'][2]['base_stat']
    bar_specical_attack['value'] = poke_info['stats'][3]['base_stat']
    bar_specical_def['value'] = poke_info['stats'][4]['base_stat']
    bar_speed['value'] = poke_info['stats'][5]['base_stat']
    return

btn_get_info = ttk.Button(frm_top, text='Get Info', command=handle_get_info)
btn_get_info.grid(row=0, column=2, padx=(10, 20), pady=(10, 20))

# Popeulate widget in the Info frame

lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0, sticky=E)

lbl_height_int = ttk.Label(frm_btm_left, text='TBD')
lbl_height_int.grid(row=0, column=1, sticky=W)

# TODO: Add weight and type
lbl_weight = ttk.Label(frm_btm_left, text='Weight:')
lbl_weight.grid(row=1, column=0, sticky=E)

lbl_weight_int = ttk.Label(frm_btm_left, text='TBD')
lbl_weight_int.grid(row=1, column=1, sticky=W)

lbl_type = ttk.Label(frm_btm_left, text='Type:')
lbl_type.grid(row=2, column=0, sticky=E)

lbl_type_value = ttk.Label(frm_btm_left, text='TBD')
lbl_type_value.grid(row=2, column=1, sticky=W)

# Popeulate widget in the Stats frame
lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, sticky=E)

hp_bar = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
hp_bar.grid(row=0, column=1)

lbl_attack = ttk.Label(frm_btm_right, text='Attack:')
lbl_attack.grid(row=1, column=0, sticky=E)

bar_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_attack.grid(row=1, column=1)

lbl_defense = ttk.Label(frm_btm_right, text='Defense:')
lbl_defense.grid(row=2, column=0, sticky=E)

bar_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_defense.grid(row=2, column=1)

lbl_specical_attack = ttk.Label(frm_btm_right, text='Specical Attack:')
lbl_specical_attack.grid(row=3, column=0, sticky=E)

bar_specical_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_specical_attack.grid(row=3, column=1)

lbl_specical_def = ttk.Label(frm_btm_right, text='Speciacl Defense:')
lbl_specical_def.grid(row=4, column=0, sticky=E)

bar_specical_def = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_specical_def.grid(row=4, column=1)

lbl_speed = ttk.Label(frm_btm_right, text='Speed:')
lbl_speed.grid(row=5, column=0, sticky=E)

bar_speed = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_speed.grid(row=5, column=1)

# Loop until window is closed

root.mainloop()