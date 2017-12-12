import tkinter as tk

app= tk.Tk()
app.title('Calculator')
w=0

var_title=tk.Label(app,text='Value',width=10)
var_title.grid(row=0,column=0)

var2_title=tk.Label(app,text='Result',width=10)
var2_title.grid(row=0,column=10)

var= tk.StringVar()

opt='0'

label= tk.Label(app, textvariable=var, width=10)
label.grid(row=1,column=0)
var.set(w)
result=0

var2=tk.StringVar()
dis= tk.Label(app, textvariable=var2, width=10)
dis.grid(row=1,column=10)
var2.set(str(result))
def one() :
	global w,var
	w= w*10 + 1
	var.set(str(w))
	
def two() :
	global w,var
	w= w*10 + 2
	var.set(str(w))

def three() :
	global w,var
	w= w*10 + 3
	var.set(str(w))

def four() :
	global w,var
	w= w*10 + 4
	var.set(str(w))

def five() :
	global w,var
	w= w*10 + 5
	var.set(str(w))

def six() :
	global w,var
	w= w*10 + 6
	var.set(str(w))

def seven() :
	global w,var
	w= w*10 + 7
	var.set(str(w))

def eight() :
	global w,var
	w= w*10 + 8
	var.set(str(w))

def nine() :
	global w,var
	w= w*10 + 9
	var.set(str(w))

def zero() :
	global w,var
	w= w*10 + 0
	var.set(str(w))

def add() :
	global w,result,var2,opt
	if opt!='+':
		equal()
	result=result+w
	var2.set(str(result))

	opt='+'
	w=0
	var.set(0)
	

def minus():
        global w,result,var2,opt
        if opt!='-':
        	equal()
        if opt=='0' and result==0:
        	result=w
        if opt=='-':
        	result = result - w
        var.set(0)
        opt='-'
        w=0
        var2.set(str(result))

def divide():
	global w,result,opt
	if opt!='/':
		equal()
	if result==0 and w==0:
		result=w
	if opt=='/' and w!=0:
		result=round(result/w)
	opt='/'
	w=0
	var2.set(str(result))
	var.set(0)

def equal():
        global opt
        if opt=='+':
                add()
        if opt=='-':
                minus()
        if opt=='/':
        	divide()
        opt='0'        

def delete():
	global w
	w=int(w/10)
	var.set(w)

def CE():
	global result,w
	w=0
	result=0
	var.set(w)
	var2.set(result)

b1=tk.Button(app,text='1',width=10,command=one)
b1.grid(row=2,column=0)

b2=tk.Button(app,text='2',width=10,command=two)
b2.grid(row=2,column=1)

b3=tk.Button(app,text='3',width=10,command=three)
b3.grid(row=2,column=2)

b4=tk.Button(app,text='4',width=10,command=four)
b4.grid(row=3,column=0)

b5=tk.Button(app,text='5',width=10,command=five)
b5.grid(row=3,column=1)

b6=tk.Button(app,text='6',width=10,command=six)
b6.grid(row=3,column=2)

b7=tk.Button(app,text='7',width=10,command=seven)
b7.grid(row=4,column=0)

b8=tk.Button(app,text='8',width=10,command=eight)
b8.grid(row=4,column=1)

b9=tk.Button(app,text='9',width=10,command=nine)
b9.grid(row=4,column=2)

b0=tk.Button(app,text='0',width=10,command=zero)
b0.grid(row=5,column=1)

b_add=tk.Button(app,text='+',width=10,command=add)
b_add.grid(row=2,column=10)

b_minus=tk.Button(app,text='-',width=10,command=minus)
b_minus.grid(row=3,column=10)

b_divide=tk.Button(app,text='/',width=10,command=divide)
b_divide.grid(row=4,column=10)

b_equal=tk.Button(app,text='=',width=10,command=equal)
b_equal.grid(row=5,column=10)

b_delete=tk.Button(app,text='delete',width=10,command=delete)
b_delete.grid(row=5,column=2)

b_CE=tk.Button(app,text='AC',width=10,command=CE)
b_CE.grid(row=5,column=0)

app.mainloop()
