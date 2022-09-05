from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout





class Goroda(App):
    def build(self):

###kivy constants
        Window.size=(900,500)
        text_color=[0.95,0.6,0.5,0.9]
        the_font_size=Window.width/9
###end kivy constants
        
        
        import io
        import random
        import os
        goroda=[]
        used=[]
        #n_of_questions=int(input('Сколько городов будем делать?  <- '))
        n_of_questions=15

        def g():
            pass
        
        
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


        def change_gorod_onclick(instance, value):
            #print(value)
            gorod_comp=random.choice(goroda)
            
            template='[ref=город]'            
            template+=gorod_comp
            template+='[/ref]'
            gorod_comp_label.text=template

        def change_gorod():
            global gorod_comp
            #print(value)
            gorod_comp=random.choice(goroda)            
            template='[ref=город]'            
            template+=gorod_comp
            template+='[/ref]'
            gorod_comp_label.text=template

        gorod_comp=random.choice(goroda)

        gorod_comp_label=Label(
            pos_hint={'y':0.35},
            text='[ref=город]'+gorod_comp+'[/ref]',
            markup=True,
            color=text_color,
            font_size=the_font_size
            )
        gorod_comp_label.bind(on_ref_press=change_gorod_onclick)

        the_layout=FloatLayout()
        background=Image(source='map.jpg')
        
        def on_enter(instance):
            #if instance.text==gorod_comp:
             #   instance.text='  Molodec!'

            gorod_user=instance.text
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
                        message='Опечатка или такого нет'                        
                else:
                    message='Уже был :('
            else:
                message='Не та буква'

            instance.text=message
            change_gorod()
            print(message)
            

        def on_focus(instance, value):
            if value:
                instance.text=''
            else:
                print('User defocused', instance)



            
        textinput=TextInput(
            text='  пиши здесь:',
            foreground_color=[text_color[0],
                              text_color[1],
                              text_color[2],
                              text_color[3]/2],
            size_hint=(0.8,0.25),
            pos_hint={'x':0.1,'y':0.05},
            multiline=False,
            font_size=the_font_size,
            background_normal='',
            background_color=[0,0,0,0]
            )
        
        textinput.bind(on_text_validate=on_enter)
        textinput.bind(focus=on_focus)
        
        the_layout.add_widget(background)
        the_layout.add_widget(gorod_comp_label)
        the_layout.add_widget(textinput)

        
        return the_layout

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

            

if __name__=='__main__':
    Goroda().run()


    

