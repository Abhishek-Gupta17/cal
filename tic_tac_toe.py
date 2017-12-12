a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9
print(' ',a,'|',b,'|',c)
print('-------------')
print(' ',d,'|',e,'|',f)
print('-------------')
print(' ',g,'|',h,'|',i)
print('\n')
j=1
while j!=10:
    if j%2==1 :
        pl_1= int(input('1st player enter the block no. :'))
        if (pl_1==1 and a!='O' and a!='X'):
            a='X'
        elif (pl_1==2 and b!='O' and b!='X'):
            b='X'
        elif (pl_1==3 and c!='O' and c!='X'):
            c='X'
        elif (pl_1==4 and d!='O' and d!='X'):
            d='X'
        elif (pl_1==5 and e!='O' and e!='X'):
            e='X'
        elif (pl_1==6 and f!='O' and f!='X'):
            f='X'
        elif (pl_1==7 and g!='O' and g!='X'):
            g='X'
        elif (pl_1==8 and h!='O' and h!='X'):
            h='X'
        elif (pl_1==9 and i!='O' and i!='X'):
            i='X'
        else:
            print('enter valid block no.')
            continue
        
        print(' ',a,'|',b,'|',c)
        print('-------------')
        print(' ',d,'|',e,'|',f)
        print('-------------')
        print(' ',g,'|',h,'|',i)

        if ((a=='X' and b=='X' and c=='X')or(d=='X' and e=='X' and f=='X')\
            or(g=='X' and h=='X' and i=='X')or(a=='X' and d=='X' and g=='X')\
            or(e=='X' and b=='X' and h=='X')or(f=='X' and i=='X' and c=='X')\
            or(a=='X' and e=='X' and i=='X')or(g=='X' and e=='X' and c=='X')) :
            print('1st player wins')
            break
    if j%2==0 :
        pl_1= int(input('2nd player enter the block no. :'))
        if (pl_1==1 and a!='O' and a!='X'):
            a='O'
        elif (pl_1==2 and b!='O' and b!='X'):
            b='O'
        elif (pl_1==3 and c!='O' and c!='X'):
            c='O'
        elif (pl_1==4 and d!='O' and d!='X'):
            d='O'
        elif (pl_1==5 and e!='O' and e!='X'):
            e='O'
        elif (pl_1==6 and f!='O' and f!='X'):
            f='O'
        elif (pl_1==7 and g!='O' and g!='X'):
            g='O'
        elif (pl_1==8 and h!='O' and h!='X'):
            h='O'
        elif (pl_1==9 and i!='O' and i!='X'):
            i='O'
        else:
            print('enter valid block no.')
            continue
        print(' ',a,'|',b,'|',c)
        print('-------------')
        print(' ',d,'|',e,'|',f)
        print('-------------')
        print(' ',g,'|',h,'|',i)

        if ((a=='O' and b=='O' and c=='O')or(d=='O' and e=='O' and f=='O')\
            or(g=='O' and h=='O' and i=='O')or(a=='O' and d=='O' and g=='O')\
            or(e=='O' and b=='O' and h=='O')or(f=='O' and i=='O' and c=='O')\
            or(a=='O' and e=='O' and i=='O')or(g=='O' and e=='O' and c=='O')) :
            print('2nd player wins')
            break                
    print('\n')
    if j==9:
        print('There is a draw')
    j=j+1
print('Thanks for playing, you are welcomed again..!!')

end=input('')
    
