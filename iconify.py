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

#make iconify function
def iconify(arg1:str):
	emojized = emoji.emojize(f":{icon_input.get()}:")
	entry_var.set(f"{arg1[0]}{emojized}{arg1[1]} {text_input.get()}")

#make copy iconified function
def copy_iconified():
	clipboard.copy(entry_var.get())
	msgbox.showinfo("Copied!", "Iconified text copied to clipboard! Made by Cheesehead")

#make the root
root = tk.Tk()

#make a title for the root
root.title("Iconifier")

#add font that supports emojis
emoji_font = font.Font(family='Segoe UI Emoji', size=10)

#resize to 300 by 350 and make it unresizable
root.geometry("350x300")
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

#make iconify button 「」
iconify_button = tk.Button(root, text="「」", command=lambda: iconify(corner_brackets), font=emoji_font)
iconify_button.grid(row=4, column=0)

#make iconify button 〘〙
iconify_button = tk.Button(root, text="〘〙", command=lambda: iconify(corner_brackets2), font=emoji_font)
iconify_button.grid(row=4, column=1)

#linebreak
tk.Label(root).grid(row=5)

#result
entry_var = tk.StringVar()
label_result = tk.Entry(root, font=emoji_font, state="disabled", textvariable=entry_var)
label_result.grid(row=6,sticky="ew")

#linebreak
tk.Label(root).grid(row=7)

#make copy button
copy_button = tk.Button(root, font=emoji_font, text="Copy", command=copy_iconified)
copy_button.grid(row=8)

#run the app
root.mainloop()
