try:
   chislo = int (input ('Введите число: '))
   ss = int (input ('Введите целевую систему счисления: '))
except ValueError:
      print ('Ошибка') 
else:

    b = ' '

    def dvoich():
       global chislo 
       global b 
       while chislo > 0:
            b = str (chislo % 2) + b
            chislo = chislo // 2
       print (b)


    def vosmir():
       global chislo 
       global b 
       while chislo>0:
            b = str (chislo % 8) + b
            chislo = chislo // 8
       print (b)
     
      
    if ss == 2:
      dvoich()
    elif ss == 8:
      vosmir()
    else: 
      print ('Ошибка')