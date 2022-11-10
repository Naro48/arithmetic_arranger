def arithmetic_arranger(L,answer=False):
    n=len(L)
    #errors
    if n>=5:
        print("Error: too many problems \n")
    for i in range(0,n):
        m=L[i]
        y=m.split(" ")
        if (y[1]!='+') and (y[1]!='-') :
            print("Error: Operator must be '+' or '-' \n")
            break
    ops1=[]
    ops2=[]
    opers=[]        
    for i in range(0,n):
        m=L[i]
        y=m.split(" ")
        op1=y[0]
        op2=y[2]
        oper=y[1]
        tailleop1=len(y[0])
        tailleop2=len(y[2])
        ops1.append(op1)
        ops2.append(op2)
        opers.append(oper)
        if tailleop1>4 or tailleop2>4:
            print("Error: Numbers cannot be more than four digits\n")
            break
        for i in range(0,tailleop1):
            if ord(op1[i])>57 or ord(op1[i])<48: #digit's ascii code is between 48 and 57
                print("Error : Numbers must only contain digits\n")
                break
        for i in range(0,tailleop2):
            if ord(op2[i])>57 or ord(op2[i])<48: #digit's ascii code is between 48 and 57
                print("Error : Numbers must only contain digits\n")
                break
    esp=0
    for i in range(0,n):
        #ligne 1
        if len(ops2[i])>len(ops1[i]):
            esp=len(ops2[i])-len(ops1[i])+1
            print(' '*esp,ops1[i],end='    ')
        if len(ops2[i])<=len(ops1[i]):
            esp=len(ops1[i])-len(ops2[i])+1
            print(' ',ops1[i],end='    ')
    #ligne 2
    for i in range(0,n):
        if i==0:
            if len(ops2[i])>len(ops1[i]):
                print('\n',opers[i],' ',ops2[i],sep='',end='    ')
            else:
                esp=len(ops1[i])-len(ops2[i])+1
                print('\n',esp*' ',ops2[i],end='    ')
        else:
            if len(ops2[i])>len(ops1[i]):
                print(opers[i],' ',ops2[i],sep='',end='    ')
            else:
                esp=len(ops1[i])-len(ops2[i])+1
                print(opers[i],esp*' ',ops2[i],sep='',end='    ')
    #ligne 3
    for i in range(0,n):
        if i==0:
            lg=max(len(ops1[i]),len(ops2[i]))
            print('\n','-'*(lg+2),sep='',end='    ')
        else:
            lg=max(len(ops1[i]),len(ops2[i]))
            print('-'*(lg+2),sep='',end='    ')

    #ligne4:resultat 
    if answer==True:
        for i in range(0,n):
            res=0
            x=int(ops1[i])
            y=int(ops2[i])
            if opers[i]=='+':res=x+y
            elif opers[i]=='-':res=x-y
            add=str(res)
            l=len(add)
            lgg=max(len(ops1[i]),len(ops2[i]))+2
            espace=lgg-l
            if i==0:
                print('\n',' '*espace,add,sep='',end='    ')
            else:
                print(' '*espace,add,sep='',end='    ')






        



                




        
    
arithmetic_arranger(['45 + 322','22 - 234','2 + 78','233 + 475'],True)


        
