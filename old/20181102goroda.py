import io
import random
import os
goroda=[]
used=[]
n_of_questions=int(input('Сколько городов будем делать?  <- '))

###making the towns list:
def split_goroda_database():
    for i in goroda_csv:
        i=i.split(',')
        goroda.append(i[1])
try:
    try:
        with open('goroda.csv', 'r') as goroda_csv:
            split_goroda_database()
    except:
        with io.open('goroda', mode='r', encoding='utf-8') as goroda_csv:
            split_goroda_database()
except:
    print('No database')
###making the towns list end


#goroda=['London','New York','Kazan','Suzdal','Los Angeles']
gorod_comp=random.choice(goroda)

for i in range(n_of_questions):
    os.system('cls')
    gorod_user=input(gorod_comp+': ')
    last_letter=gorod_comp.lower()[len(gorod_comp)-1]
    if last_letter in ['ъ','ы','ь']:
        last_letter=gorod_comp.lower()[len(gorod_comp)-2]
    first_letter=gorod_user.lower()[0]

    if last_letter==first_letter:
        if gorod_user not in used:
            if gorod_user in goroda:
                goroda.remove(gorod_comp)
                goroda.remove(gorod_user)
                used.append(gorod_comp)
                used.append(gorod_user)
                message='Молодца!'
            else:
                message='Опечатка или такого просто нету'                        
        else:
            message='Уже был :('
    else:
        message='Не та буква'
    print(message)
    input('Press ENTER')
        

    last_letter=gorod_user.lower()[len(gorod_user)-1]
    if last_letter in ['ъ','ы','ь']:
        last_letter=gorod_user.lower()[len(gorod_user)-2]
    first_letter=''
    
    while last_letter!=first_letter:
        gorod_comp=random.choice(goroda)
        first_letter=gorod_comp[0].lower()
        #print(gorod_comp,last_letter,first_letter)
        #print(last_letter!=first_letter)
    

