import tkinter as tk

class calculator():
	"""docstring for calculator"""
	
	def __init__(self,master):
		self.master=master
		master.title('Calculator')

	def button(self,text,width,row,column):
		self.text=text
		self.width=width
		self.row=row
		self.column=column
		self.butn=tk.Button(self.master,text=self.text,width=self.width,command=lambda: self.num(text))
		self.butn.grid(row=self.row,column=self.column)

	def num(self,text):
		global w,var,result,var2
		if text=='+':
			self.add()
		elif text=='-':
			self.minus()
		elif text=='=':
			self.equal()
		elif text=='/':
			self.divide()
		elif text=='del':
			self.delete()
		elif text=='CE':
			self.CE()			
		else :		
			w=w*10 +int(text)
			var.set(w)
		
		var2.set(result)

	def add(self) :
		global w,result,opt,var
		if opt!='+':
			self.equal()
		result=result+w
		opt='+'
		w=0
		var.set(0)

	def minus(self):
        global w,result,opt,var
        if opt!='-':
        	self.equal()
        if opt=='0' and result==0:
        	result=w
        if opt=='-':
        	result = result - w
        var.set(0)
        opt='-'
        w=0

	def divide(self):
		global w,result,opt,var
		if opt!='/':
			self.equal()
		if result==0 and w==0:
			result=w
		if opt=='/' and w!=0:
			result=round(result/w)
		opt='/'
		w=0
		var.set(0)

	def equal(self):
        global opt
        if opt=='+':
                self.add()
        if opt=='-':
                self.minus()
        if opt=='/':
        	self.divide()
        opt='0'        

	def delete(self):
		global w,var
		w=int(w/10)
		var.set(w)

	def CE(self):
		global result,w,var
		w=0
		result=0
		var.set(w)

w=0
opt='0'
app=tk.Tk()
my_app=calculator(app)
var_title=tk.Label(app,text='Value',width=10)
var_title.grid(row=0,column=0)

var2_title=tk.Label(app,text='Result',width=10)
var2_title.grid(row=0,column=10)

var= tk.StringVar()

label= tk.Label(app, textvariable=var, width=10)
label.grid(row=1,column=0)
var.set(w)
result=0

var2=tk.StringVar()
dis= tk.Label(app, textvariable=var2, width=10)
dis.grid(row=1,column=10)
var2.set(str(result))

my_app.button(1,10,2,0)
my_app.button(2,10,2,1)
my_app.button(3,10,2,2)
my_app.button(4,10,3,0)
my_app.button(5,10,3,1)
my_app.button(6,10,3,2)
my_app.button(7,10,4,0)
my_app.button(8,10,4,1)
my_app.button(9,10,4,2)
my_app.button(0,10,5,1)
my_app.button('+',10,2,3)
my_app.button('-',10,3,3)
my_app.button('/',10,4,3)
my_app.button('=',10,5,3)
my_app.button('del',10,5,0)
my_app.button('CE',10,5,2)
app.mainloop()