#iconify by cheesehead

#import modules for gui
import tkinter as tk
import tkinter.font as font
import clipboard
import emoji
import tkinter.messagebox as msgbox

#make the corner brackets
corner_brackets = "「」"
corner_brackets2 = "〘〙"

#make options list
options = [
	corner_brackets,
	corner_brackets2,
	"(none)",
]

#make iconify function
def iconify(arg1:str):
	emojized = emoji.emojize(f":{icon_input.get()}:", variant="emoji_type")
	if arg1 == "(none)":
		entry_var.set(f" {emojized}  {text_input.get()}")
	else:
		entry_var.set(f"{arg1[0]}{emojized}{arg1[1]} {text_input.get()}")

#make copy iconified function
def copy_iconified():
	clipboard.copy(entry_var.get())
	msgbox.showinfo("Copied!", "Iconified text copied to clipboard! Made by Cheesehead")

#make the root
root = tk.Tk()

#make selected var
selected = tk.StringVar()
selected.set(options[2])

#make a title for the root
root.title("Iconifier")

#add font that supports emojis
emoji_font = font.Font(family='Segoe UI Emoji', size=10)

#make root unresizable
root.resizable(0,0)

#make icon input
icon_input = tk.Entry(root, font=emoji_font)
icon_input.insert(0, "Emoji name here...")
icon_input.grid(row=0)

#line break
tk.Label(root).grid(row=1)

#make text input
text_input = tk.Entry(root, font=emoji_font)
text_input.insert(0, "Text here...")
text_input.grid(row=2)

#line break
tk.Label(root).grid(row=3)

#make a menu
dropdown = tk.OptionMenu(root, selected, *options)
dropdown.grid(row=4)

#linebreak
tk.Label(root).grid(row=5)

#make iconify button
copy_button = tk.Button(root, font=emoji_font, text="Iconify", command=lambda: iconify(selected.get()))
copy_button.grid(row=6)

#linebreak
tk.Label(root).grid(row=7)

#result
entry_var = tk.StringVar()
label_result = tk.Entry(root, font=emoji_font, state="disabled", textvariable=entry_var)
label_result.grid(row=8)

#linebreak
tk.Label(root).grid(row=9)

#make copy button
copy_button = tk.Button(root, font=emoji_font, text="Copy", command=copy_iconified)
copy_button.grid(row=10)

#run the app
root.mainloop()
