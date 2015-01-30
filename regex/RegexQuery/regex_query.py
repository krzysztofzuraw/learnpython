import re
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys
import time



def regex_query_tool(*args):
    """
    Regex
    """
    start = time.clock()
    try:
        rules = rule.get()
        expressions = expression.get()
        if ignore.get() == "":
            special = 0
        else:
            special = int(ignore.get())
        regex = re.compile(rules, special)
        r = regex.search(expressions)
        result.set(regex.findall(expressions))
    except:
        messagebox.showerror("Error", sys.exc_info()[1])
        
    finish = time.clock()
    times.set("{:.4f} seconds".format(finish - start))
    
root =  Tk()
root.title("Regex Query Tool")

mainframe = ttk.Frame(root, padding="4 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

expression = StringVar()
rule = StringVar()
result = StringVar()
ignore = StringVar()
dot = StringVar()
times = StringVar()

expression_entry = ttk.Entry(mainframe, width=20, textvariable=expression)
expression_entry.grid(column=2, row=1, sticky=(W, E))
rule_entry = ttk.Entry(mainframe, width=7, textvariable=rule)
rule_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Do it", command=regex_query_tool).grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, textvariable=result).grid(column=2, row=3, sticky=(W, E))
ignore_check = ttk.Checkbutton(mainframe, text="Ignore case", variable = ignore, onvalue = 2 ).grid(column=4, row =1, sticky=E)

ttk.Label(mainframe, textvariable = times).grid(column = 2, row = 4, sticky = W)

ttk.Label(mainframe, text="expression").grid(column=3, row=1,sticky=W)
ttk.Label(mainframe, text="rule").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="result").grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
    
expression_entry.focus()
root.bind('<Return>', regex_query_tool)

root.mainloop()


