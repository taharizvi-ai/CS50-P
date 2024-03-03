exp=input('Expression:')
exp=exp.split(' ')
x=int(exp[0])
z=int(exp[2])
y=exp[1]
match y:
    case '+':
        ans=float(x)+float(z)
        print(round(ans,1))
    case '-':
        ans=float(x)-float(z)
        print(round(ans,1))
    case '/':
        ans=float(x)/float(z)
        print(round(ans,1))
    case '*':
        ans=float(x)*float(z)
        print(round(ans,1))