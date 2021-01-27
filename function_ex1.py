# define the function
def hi(lang):
    # function body
    if lang=="en":
        print("Hello!!!")
    elif lang=="ro":
        print("Salut!!!")
    elif lang=="ru":
        print("Привет!!!")
    else:
        print(lang,":SORRY, WE DON'T KNOW THIS LANGUAGE")
    


def bye(lang):
    if lang=="en":
        print("Good bye!!!")
    elif lang=="ro":
        print("O zi buna!!!")
    elif lang=="ru":
        print("Досвидания!!!")
    else:
        print(lang,":THIS LANGUAGE IS UNKNOWN FOR US. WE ARE SORRY!!!")
   


# call the function
hi("ru")
hi("ro")
hi("en")
hi("fr")
bye("ru")
bye("ro")
bye("en")
bye("fr")