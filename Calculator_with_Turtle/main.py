from tkinter import *

tk = Tk() # This is to create a basic window
tk.title("Calculator")

###################Starting with functions ####################
# 'button_click' function : 
# This Function continuously updates the 
# input field whenever you enter a number

def button_click(element):
    global final_string
    final_string = final_string + str(element)
    input_item.set(final_string)

# 'button_clear' function :This is used to clear 
# the input field

def button_clear():
    global final_string 
    final_string = "" 
    input_item.set("")

# 'button_equal':This method calculates the final_string 
# present in input field

def button_equal():
    global final_string
    try:
        res = str(eval("2 ** 8"))
        result = str(eval(final_string))+" "+res # 'eval':This function is used to evaluates the string final_string directly
    #print(final_string)
    except Exception as e:
        result = "Error: "+str(e)
    input_item.set(result)
    final_string = ""

final_string = ""

# 'StringVar()' :It is used to get the instance of input field

input_item = StringVar()

# Let us creating a frame for the input field

input_window = Frame(tk, width=295, height=50, bd=0, highlightbackground="olive", highlightcolor="green", highlightthickness=3)

input_window.pack(side=TOP)

#Let us create a input field inside the 'Frame'

input_section = Entry(input_window, font=('arial', 18, 'bold'), textvariable=input_item, width=50, bg="#eee", bd=0, justify=RIGHT)

input_section.grid(row=0, column=0)

input_section.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field

#Let us creating another 'Frame' for the button below the 'input_window'

btns_frame = Frame(tk, width=312, height=272.5, bg="olive")

btns_frame.pack()

# first row

clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "target", command = lambda: button_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "target", command = lambda: button_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

# second row

seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "target", command = lambda: button_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)

eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "target", command = lambda: button_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)

nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "target", command = lambda: button_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)

multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "target", command = lambda: button_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

# third row

four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "target", command = lambda: button_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)

five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "target", command = lambda: button_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)

six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "target", command = lambda: button_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)

minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "target", command = lambda: button_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

# fourth row

one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#EAFF73", cursor = "target", command = lambda: button_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)

two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#EAFF73", cursor = "target", command = lambda: button_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)

three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#EAFF73", cursor = "target", command = lambda: button_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)

plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "target", command = lambda: button_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

# fourth row

zero = Button(btns_frame, text = "0", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "target", command = lambda: button_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)

point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "target", command = lambda: button_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)

equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "target", command = lambda: button_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

#power = Button(btns_frame, text = "^", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "target", command = lambda: button_click("**")).grid(row = 4, column = 3, padx = 1, pady = 1)


tk.mainloop()
