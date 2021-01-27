   

def eval_temperature(temp):
    if temp>=50:
        print(temp, "=> Very HOT")
    elif temp<50 and temp>=30:
        print(temp, "=> HOT")
    elif temp<30 and temp>=10:
        print(temp, "=> WARM")
    elif temp<10 and temp>=0:
        print(temp, "=> SO GOOD OUTSIDE")
    elif temp<0 and temp >=-20:
        print(temp, "=> COLD")
    elif temp<-20 and temp>= -50:
        print(temp, "=> MEDIUM COLD")
    elif temp<-50 :
        print(temp, "=>VERY COLD")
    

eval_temperature(int(input("What's the temperature outside?")))
    
