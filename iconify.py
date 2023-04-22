#iconify by cheesehead

#import modules for gui
import tkinter as tk
import tkinter.font as font
import clipboard
import tkinter.messagebox as msgbox

#make the corner brackets
corner_brackets = "「」"

#make iconify function
def iconify():
	entry_var.set(f"{corner_brackets[0]}{icon_input.get()}{corner_brackets[1]} {text_input.get()}")

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
icon_input.insert(0, "Emoji here...")
icon_input.pack(anchor="center")

#line break
tk.Label(root).pack(anchor="center")

#make text input
text_input = tk.Entry(root, font=emoji_font)
text_input.insert(0, "Text here...")
text_input.pack(anchor="center")

#line break
tk.Label(root).pack(anchor="center")

#make iconify button
iconify_button = tk.Button(root, text="Iconify!!", command=iconify, font=emoji_font)
iconify_button.pack(anchor="center")

#linebreak
tk.Label(root).pack(anchor="center")

#result
entry_var = tk.StringVar()
label_result = tk.Entry(root, font=emoji_font, state="disabled", textvariable=entry_var)
label_result.pack(anchor="center", fill="both")

#linebreak
tk.Label(root).pack(anchor="center")

#make copy button
copy_button = tk.Button(root, font=emoji_font, text="Copy", command=copy_iconified)
copy_button.pack(anchor="center")

#run the app
root.mainloop()
