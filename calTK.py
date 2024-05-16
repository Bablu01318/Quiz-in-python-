from tkinter import *
from tkinter import ttk

y=0
a=ttk.Notebook()
# icon=PhotoImage(file="p2.png")

frame1=ttk.Frame(a)
frame2=ttk.Frame(a)
frame3=ttk.Frame(a)
frame4=ttk.Frame(a)
frame5=ttk.Frame(a)
frame6=ttk.Frame(a)
frame7=ttk.Frame(a)
frame8=ttk.Frame(a)
frame9=ttk.Frame(a)
frame10=ttk.Frame(a)

root=ttk.Frame(a) 
def quiz(y):
    a.add(frame1,text="Q1")
    a.add(frame2,text="Q2")
    a.add(frame3,text="Q3")
    a.add(frame4,text="Q4")
    a.add(frame5,text="Q5")
    a.add(frame6,text="Q6")
    a.add(frame7,text="Q7")
    a.add(frame8,text="Q8")
    a.add(frame9,text="Q9")
    a.add(frame10,text="Q10")
    #q1
    Label(frame1,text="Who develop python programming language?",font=("arial",20,"bold")).grid(row=2,column=2)
    Button(frame1,text="Wick van rossum",font=("arial",10,"bold"),bg="light blue",command=a1_wrong).grid(row=3,column=1)
    Button(frame1,text="Rasmus lardorf",font=("arial",10,"bold",),bg="light green",command=a1_wrong).grid(row=3,column=2)
    Button(frame1,text="Guido van rossum",font=("arial",10,"bold",),bg="light pink",command=a1_right).grid(row=3,column=3)
    Button(frame1,text="niene stom",font=("arial",10,"bold",),bg="red",command=a1_wrong).grid(row=3,column=4)

#q2
    Label(frame2,text="Which type of programming does python support?",font=("arial",20,"bold")).grid(row=2,column=2)
    Button(frame2,text="Object oriented programming",font=("arial",10,"bold"),bg="light blue",command=a2_wrong).grid(row=3,column=1)
    Button(frame2,text="Structured programming",font=("arial",10,"bold",),bg="light green",command=a2_wrong).grid(row=3,column=2)
    Button(frame2,text="Functional programming",font=("arial",10,"bold",),bg="light pink",command=a2_wrong).grid(row=3,column=3)
    Button(frame2,text="All of the mention",font=("arial",10,"bold",),bg="red",command=a2_right).grid(row=3,column=4)

#q3
    Label(frame3,text="All keyword in python are in_______",font=("arial",20,"bold")).grid(row=2,column=2)
    Button(frame3,text="Capitalized",font=("arial",10,"bold"),bg="light blue",command=a3_wrong).grid(row=3,column=1)
    Button(frame3,text="Lower case",font=("arial",10,"bold",),bg="light green",command=a3_right).grid(row=3,column=2)
    Button(frame3,text="UPPER CASE",font=("arial",10,"bold",),bg="light pink",command=a3_wrong).grid(row=3,column=3)
    Button(frame3,text="None of the mention",font=("arial",10,"bold",),bg="red",command=a3_wrong).grid(row=3,column=4)

#4
    Label(frame4,text="What will be the value of python expression?  4 + 3 % 5",font=("arial",20,"bold")).grid(row=2,column=2)
    Button(frame4,text="7",font=("arial",10,"bold"),bg="light blue",command=a4_right).grid(row=3,column=1)
    Button(frame4,text="4",font=("arial",10,"bold",),bg="light green",command=a4_wrong).grid(row=3,column=2)
    Button(frame4,text="2",font=("arial",10,"bold",),bg="light pink",command=a4_wrong).grid(row=3,column=3)
    Button(frame4,text="1",font=("arial",10,"bold",),bg="red",command=a4_wrong).grid(row=3,column=4)

#5
    Label(frame5,text="Which of the following is used to define a block of code in python language?",font=("arial",20,"bold")).grid(row=2,column=2)
    Button(frame5,text="Indentation",font=("arial",10,"bold"),bg="light blue",command=a5_right).grid(row=3,column=1)
    Button(frame5,text="Key",font=("arial",10,"bold",),bg="light green",command=a5_wrong).grid(row=3,column=2)
    Button(frame5,text="Brackets",font=("arial",10,"bold",),bg="light pink",command=a5_wrong).grid(row=3,column=3)
    Button(frame5,text="All of the mentioned",font=("arial",10,"bold",),bg="red",command=a5_wrong).grid(row=3,column=4)

#6
    Label(frame6,text="Whice keyword is used for function in python language?",font=("arial",20,"bold")).grid(row=2,column=2)
    Button(frame6,text="function",font=("arial",10,"bold"),bg="light blue",command=a6_wrong).grid(row=3,column=1)
    Button(frame6,text="def",font=("arial",10,"bold",),bg="light green",command=a6_right).grid(row=3,column=2)
    Button(frame6,text="fun",font=("arial",10,"bold",),bg="light pink",command=a6_wrong).grid(row=3,column=3)
    Button(frame6,text="define",font=("arial",10,"bold",),bg="red",command=a6_wrong).grid(row=3,column=4)

#7
    Label(frame7,text="Which of the following character is used to give single line comments in python?",font=("arial",20,"bold")).grid(row=2,column=2)
    Button(frame7,text="//",font=("arial",10,"bold"),bg="light blue",command=a7_wrong).grid(row=3,column=1)
    Button(frame7,text="#",font=("arial",10,"bold",),bg="light green",command=a7_right).grid(row=3,column=2)
    Button(frame7,text="!",font=("arial",10,"bold",),bg="light pink",command=a7_wrong).grid(row=3,column=3)
    Button(frame7,text="/*",font=("arial",10,"bold",),bg="red",command=a7_wrong).grid(row=3,column=4)

#8
    Label(frame8,text="Which of the following in not a core data type in python programming?",font=("arial",20,"bold")).grid(row=2,column=2)
    Button(frame8,text="Tuples",font=("arial",10,"bold"),bg="light blue",command=a8_wrong).grid(row=3,column=1)
    Button(frame8,text="Lists",font=("arial",10,"bold",),bg="light green",command=a8_wrong).grid(row=3,column=2)
    Button(frame8,text="Class",font=("arial",10,"bold",),bg="light pink",command=a8_right).grid(row=3,column=3)
    Button(frame8,text="Dictionary",font=("arial",10,"bold",),bg="red",command=a8_wrong).grid(row=3,column=4)

#q9
    Label(frame9,text="Which of the following function is a built_in function in python?",font=("arial",20,"bold")).grid(row=2,column=2)
    Button(frame9,text="factorial()",font=("arial",10,"bold"),bg="light blue",command=a9_wrong).grid(row=3,column=1)
    Button(frame9,text="print()",font=("arial",10,"bold",),bg="light green",command=a9_right).grid(row=3,column=2)
    Button(frame9,text="seed()",font=("arial",10,"bold",),bg="light pink",command=a9_wrong).grid(row=3,column=3)
    Button(frame9,text="sqrt()",font=("arial",10,"bold",),bg="red",command=a9_wrong).grid(row=3,column=4)

#q10
    Label(frame10,text="What will be the output of the following python program ?len(['hello'],2,4,6)- ",font=("arial",20,"bold")).grid(row=2,column=2)
    Button(frame10,text="Error",font=("arial",10,"bold"),bg="light blue",command=a10_wrong).grid(row=3,column=1)
    Button(frame10,text="6",font=("arial",10,"bold",),bg="light green",command=a10_wrong).grid(row=3,column=2)
    Button(frame10,text="4",font=("arial",10,"bold",),bg="light pink",command=a10_right).grid(row=3,column=3)
    Button(frame10,text="3",font=("arial",10,"bold",),bg="red",command=a10_wrong).grid(row=3,column=4)


#1
def a1_right():
    Label(frame1,text="Correct",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)
def a1_wrong():
    Label(frame1,text="Incorrect",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)

#2
def a2_right():
    Label(frame2,text="Correct",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)
def a2_wrong():
    Label(frame2,text="Incorrect",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)

#3
def a3_right():
    Label(frame3,text="Correct",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)
def a3_wrong():
    Label(frame3,text="Incorrect",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)

#4
def a4_right():
    Label(frame4,text="Correct",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)
def a4_wrong():
    Label(frame4,text="Incorrect",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)


#5
def a5_right():
    Label(frame5,text="Correct",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)
def a5_wrong():
    Label(frame5,text="Incorrect",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)


#6
def a6_right():
    Label(frame6,text="Correct",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)
def a6_wrong():
    Label(frame6,text="Incorrect",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)


#7
def a7_right():
    Label(frame7,text="Correct",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)
def a7_wrong():
    Label(frame7,text="Incorrect",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)


#8
def a8_right():
    Label(frame8,text="Correct",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)
def a8_wrong():
    Label(frame8,text="Incorrect",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)


#9
def a9_right():
    Label(frame9,text="Correct",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)
def a9_wrong():
    Label(frame9,text="Incorrect",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)


#10
def a10_right():
    Label(frame10,text="Correct",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)
def a10_wrong():
    Label(frame10,text="Incorrect",font=("arial",10,"bold"),background="green",fg="yellow").grid(row=1,column=2)

    


quiz(y)
a.pack()
a.mainloop()



