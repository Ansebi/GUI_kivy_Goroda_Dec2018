from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader
from kivy.clock import Clock


import io
import random
import os
import datetime
import time


class Goroda(App):
    def build(self):

###kivy constants
        Window.size=(1800,1000)
        text_color=[0.95,0.6,0.5,0.9]
        the_font_size=Window.width/13
        the_font_size_small=int(round(the_font_size/2,0))
        Window.left=80
        Window.top=40
###end kivy constants        
        
        
        
        ###program constants:
        goroda=[]
        used=[]
        #n_of_questions=int(input('Сколько городов будем делать?  <- '))
        n_of_questions=15
        ###program constants end
        

        ###global constants:
        def g():
            pass
        g.score=0
        g.correct=0
        g.incorrect=0
        g.message='Привет!'
        g.typing_counter=0
        g.start_time=0
        #g.time_limit=input('Time limit:   ')
        g.alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        g.alphabet+='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        g.alphabet+=' -'
        ###global constants end
        
        
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
            g.gorod_comp=random.choice(goroda)
            
            template='[ref=город]'            
            template+=g.gorod_comp
            template+='[/ref]'
            gorod_comp_label.text=template


        def change_gorod():            
            template='[ref=город]'            
            template+=g.gorod_comp
            template+='[/ref]'
            gorod_comp_label.text=template
            

        g.gorod_comp=random.choice(goroda)

        gorod_comp_label=Label(
            pos_hint={'y':0.35},
            text='[ref=город]'+g.gorod_comp+'[/ref]',
            markup=True,
            color=text_color,
            font_size=the_font_size
            )
        gorod_comp_label.bind(on_ref_press=change_gorod_onclick)

        message_label=Label(
            pos_hint={'y':0.05},
            text=g.message,
            markup=True,
            color=text_color,
            font_size=the_font_size_small
            )

        score_label=Label(
            pos_hint={'x':-0.42,'y':0.42},
            text='Счёт: '+str(g.score),
            markup=True,
            color=text_color,
            font_size=the_font_size_small
            )

        the_layout=FloatLayout()
        background=Image(source='map.jpg')

        def do_focus(event):
            textinput.focus = True
        def do_do_focus(event):
            Clock.schedule_once(do_focus)
        
        def on_enter(instance):
            gorod_user_error=False
            gorod_user=instance.text
            for symbol in gorod_user:
                if symbol not in g.alphabet:
                    gorod_user_error=True
            if gorod_user_error:
                gorod_user=False
            if gorod_user:
                last_letter=g.gorod_comp.lower()[len(g.gorod_comp)-1]
                if last_letter in ['ъ','ы','ь','й']:
                    last_letter=g.gorod_comp.lower()[len(g.gorod_comp)-2]
                    if last_letter in ['ъ','ы','ь','й']:
                        last_letter=g.gorod_comp.lower()[len(g.gorod_comp)-3]
                first_letter=gorod_user.lower()[0]

                if last_letter==first_letter:
                    if gorod_user not in used:
                        if gorod_user in goroda:
                            goroda.remove(g.gorod_comp)
                            goroda.remove(gorod_user)
                            used.append(g.gorod_comp)
                            used.append(gorod_user)
                            g.message='Молодца!'
                            sound=SoundLoader.load('cashreg.wav')
                            g.correct+=1
                        else:
                            g.message='Что-то неверно'
                            sound=SoundLoader.load('explode.wav')
                            g.incorrect+=1
                    else:
                        g.message='Уже был :('
                        sound=SoundLoader.load('explode.wav')
                        g.incorrect+=1
                else:
                    g.message='Не та буква'
                    sound=SoundLoader.load('explode.wav')
                    g.incorrect+=1
                g.score=g.correct-g.incorrect
                #print('Your score is:',g.score)
                message_label.text=g.message
                score_label.text=str(g.score)
                

                last_letter=gorod_user.lower()[len(gorod_user)-1]
                if last_letter in ['ъ','ы','ь','й']:
                    last_letter=gorod_user.lower()[len(gorod_user)-2]
                    if last_letter in ['ъ','ы','ь','й']:
                        last_letter=g.gorod_comp.lower()[len(g.gorod_comp)-3]
                first_letter=''
                
                while last_letter!=first_letter:
                    g.gorod_comp=random.choice(goroda)
                    first_letter=g.gorod_comp[0].lower()
                

                instance.foreground_color=[text_color[0],
                                  text_color[1],
                                  text_color[2],
                                  text_color[3]/2]
                instance.text=g.message
                change_gorod()
                #print(message)
                #print(time.clock(),time.asctime())
                time_message=str(datetime.datetime.now().hour)
                time_message+=':'
                time_message+=str(datetime.datetime.now().minute)
                time_message+=':'
                time_message+=str(datetime.datetime.now().second)
                print(time_message)
                sound.play()
            else:
                pass

        
            
        def on_focus(instance, value):
            if value:
                try:
                    sound.stop()
                except:
                    pass
                instance.text=''
                instance.foreground_color=text_color

        def on_text(instance, value):
            try:
                sound.stop()
            except:
                pass
            sound=SoundLoader.load('type.wav')
            sound.play()
            g.typing_counter+=1
            if g.typing_counter==2:
                g.start_time=datetime.datetime.now()
            
            


            
        textinput=TextInput(
            text='  пиши здесь:',
            foreground_color=[text_color[0],
                              text_color[1],
                              text_color[2],
                              text_color[3]/2],
            size_hint=(0.9,0.25),
            pos_hint={'x':0.05,'y':0.05},
            multiline=False,
            font_size=the_font_size,
            background_normal='',
            background_color=[0,0,0,0]
            )

        textinput.bind(text=on_text)
        textinput.bind(on_text_validate=do_do_focus)
        textinput.bind(on_text_validate=on_enter)
        textinput.bind(focus=on_focus)        
       
        
        the_layout.add_widget(background)
        the_layout.add_widget(gorod_comp_label)
        the_layout.add_widget(textinput)
        the_layout.add_widget(score_label)
        the_layout.add_widget(message_label)
###autofocus:
        Clock.schedule_once(do_focus)
###autofocus end
        

###time label:
        time_label=Label(
            pos_hint={'x':0.42,'y':0.42},
            text='',
            markup=True,
            color=text_color,
            font_size=the_font_size_small
            )
        the_layout.add_widget(time_label)
###time label end

        def change_time(a):
            try:
                time_elapsed=datetime.datetime.now()-g.start_time                
                time_label.text=str(time_elapsed)[2:7]
            except:
                pass
                
        Clock.schedule_interval(change_time, 1)

        
        return the_layout
            

if __name__=='__main__':
    Goroda().run()


    

