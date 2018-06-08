#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys
import vk_api
import random
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
print('\n')
print('БОТ СОЗДАН vk.com/yanduditsky')
print('-------------------------------')
vk = vk_api.VkApi(login = 'log', password = 'pass') #Логин
print('Идет авторизация...')
vk.auth()
print('-------------------------------')
print('АВТОРИЗАЦИЯ ЗАКОНЧЕНА. БОТ ГОТОВ!\n')
print('\n')
print('\n')
print('\n')
print('\n')



values = {'out': 0,'count': 100,'time_offset':60}

#MAIN
#Функция отправки сообщений.
def write_msg(string):
        try:
                vk.method('messages.send', {'chat_id':item[u'chat_id'] ,'message':string})
                print('Выведено сообщение от бота :' + string)
        except:
                print('CAPTCHA')
#end.


#GetMessage
while True:
    try:
        response = vk.method('messages.get', values)
    except:
                print('neterror\nRETYPE YOUR MESSAGE')
    if response['items']:
        usid = response['items'][0]['user_id']
        values['last_message_id'] = response['items'][0]['id']
        #ПЕРЕМЕННЫЕ
        #Дата
        date = str(response['items'][0]['date'])
        #Сообщение
        textmsg = response['items'][0]['body']
        #Название конфы
        confname = response['items'][0][u'title']
        try:
                fullname = vk.method('users.get', {'user_ids':usid,'name_case':'nom'})
                firstname = fullname[0]['first_name'] 
                lastname = fullname[0]['last_name']
        except:
                print('APIHTTPERROR')

    for item in response['items']:
        if (len(textmsg) < 1):
                textmsg='|Картинка/Стикер/Пересланное сообщение/Сообщение беседы|'
        print('>>'+'[' + confname.translate(non_bmp_map) + '] ' + str(firstname + ' ' + lastname) + ': ' + textmsg.translate(non_bmp_map))
        
        # БАЗА
#     --ПРИМЕР СООБЩЕНИЯ--
# if 'команда' in textmsg:
#    write_msg(u'Вывод')

                                    

    

                time.sleep(1)
