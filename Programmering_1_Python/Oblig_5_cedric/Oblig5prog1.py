import tkinter as tk

def save_game():
    title = ent_game_title.get()
    type = ent_game_type.get()
    year = int(ent_game_year.get())

    key = f"({year}) {title}"
    games[key] = {'title': title, 'type': type, 'year': year}
    listbox_games.insert(tk.END, key)

def item_selected(game_list, listbox_games, ent_game_title, ent_game_type, ent_game_year):
    cur_selection = listbox_games.curselection()
    print(cur_selection)
    if cur_selection:
        global current_game_title
        game_id = listbox_games.get(listbox_games.curselection())
        game = game_list[game_id]
        current_game_title.set(game['title'])
        #ent_movie_title.delete(0, tk.END)
        ent_game_type.delete(0, tk.END)
        ent_game_year.delete(0, tk.END)
        #ent_movie_title.insert(0, movie['title'])
        ent_game_type.insert(0, game['type'])
        ent_game_year.insert(0, game['year'])

def clear_movie_entries(*entries):
    ent_game_title.delete(0, tk.END)
    ent_game_type.delete(0, tk.END)
    ent_game_year.delete(0, tk.END)

    for entry in entries:
        entry.delete(0, tk.END)

def delete_game(game_list, listbox_games):
    cur_selection = listbox_games.curselection()
    print(cur_selection)
    if cur_selection:
        game_id = listbox_games.get(cur_selection)
        game_list.pop(game_id)
        listbox_games.delete(listbox_games.curselection())
        clear_movie_entries()

        top = tk.Toplevel()
        top.attributes("-topmost", True)
        top.title('Game has been Deleted')
        tk.Label(top, text=f"{game_id} deleted").pack()
        tk.Button(top, text="OK", command=top.destroy).pack(padx=100)


games = {'(2012) CSGO': {'title': 'Counter-strike: Global Offensive', 'type': 'FPS', 'year': 2012},
         '(2009) LoL': {'title': 'League of Legends', 'type': 'MOBA', 'year': 2009},
         '(2015) RL': {'title': 'Rocket League', 'type': 'MMO', 'year': 2015}}

window = tk.Tk()

main_frame = tk.Frame()
list_frame = tk.Frame()

game_list = tk.StringVar(value=list(games.keys()))
listbox_games = tk.Listbox(list_frame, listvariable=game_list)

listbox_games.pack()
list_frame.pack(side=tk.LEFT)

lbl_game_title = tk.Label(main_frame, text="Title:")
lbl_game_type = tk.Label(main_frame, text="Type:")
lbl_game_year = tk.Label(main_frame, text="Year:")

current_game_title = tk.StringVar()
ent_game_title = tk.Entry(main_frame, textvariable=current_game_title)
ent_game_type = tk.Entry(main_frame)
ent_game_year = tk.Entry(main_frame)

btn_save = tk.Button(main_frame, text="Add", command=save_game)
btn_delete = tk.Button(list_frame, text="Delete", command=lambda: delete_game(games, listbox_games))

lbl_game_title.grid(row=0, column=0)
lbl_game_type.grid(row=1, column=0)
lbl_game_year.grid(row=2, column=0)
ent_game_title.grid(row=0, column=1)
ent_game_type.grid(row=1, column=1)
ent_game_year.grid(row=2, column=1)
btn_save.grid(row=3, column=0, columnspan=2)


clicked = tk.StringVar()


drop = tk.OptionMenu(window, clicked, "MOBA", "MMO", "FPS", "RPG")
drop.pack()

btn_delete.pack()
main_frame.pack(padx=20, pady=20)

listbox_games.bind('<<ListboxSelect>>', lambda event: item_selected(games, listbox_games, ent_game_title, ent_game_type, ent_game_year))

window.mainloop()