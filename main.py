"""
Description:
    Name: Link Shortner Bot
    Author: Md SiFaT IsLaM
    GitHub: https://github.com/cyber-programer

Note:
    This Script is Open Source
    You can Use any Code.
    But consider giving Credit!
    
"""


import telebot
import os 
import platform
import requests as req

# Capture the bot api
x = 0

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')

def runBot(api):
    # Starting Bot Coding...
    bot = telebot.TeleBot(api)
    
    # Start Command
    @bot.message_handler(commands=['start'])
    def start_command(message):
        # Which message you want to send ~ 
        sent_message = 'Welcome To This Bot\nType /help for get help'
        bot.send_message(message.chat.id, sent_message)
    
    # Help Command
    @bot.message_handler(commands=['help'])
    def help_command(message):
        sent_message = '''<< URL SHORTENER BOT >>
        
$ By Using This Bot You Can Short Any Long URL

$ For Using This Bot Type:
    /short1 <Your Long URL>
    /short2 <Your Long URL>
    /short3 <Your Long URL>
    /short4 <Your Long URL>
    /short5 <Your Long URL>
    /short6 <Your Long URL>
    /short7 <Your Long URL>
    
                '''
        bot.send_message(message.chat.id, sent_message)
    
    
    # 1st short program
    @bot.message_handler(commands=['short1'])
    def short_1(message):
        try:
            
            if len(message.text.split(' ')) <= 1:  # fixed the condition for checking the length
                
                # Error Message (wrong input)
                error_message = '[ ! ] Invalid Input'
                bot.send_message(message.chat.id, error_message)
                
            else:
                # Long link which collect from user ~
                link = message.text.split(' ')[1]  # fixed accessing the text and splitting correctly
                
                try:
                    
                    api = f'http://tinyurl.mobi/create.php?url={link}'
        
                    res = req.get(api)
                    short_url = res.url.replace('/show','')


                    # message which bot send
                    sent_message = f'''
                    
    Your Url Is Shorted Done!
    
    $ Long Url : {message.text}
    $ Short Url : {short_url}
    
    Thanks For Using This tool 
    
    Type /help For more option's
                    
                    '''
                    
                    bot.send_message(message.chat.id, sent_message)                    
                    

                    
                except Exception as e:
                    bot.send_message(message.chat.id , f'[!] Eroor : {e}')
                
                
        except Exception as e:
            bot.send_message(message.chat.id, f'[!] Error: {e}')

    
    # 2nd short program
    @bot.message_handler(commands=['short2'])
    def short_2(message):
        try:
            
            if len(message.text.split(' ')) <= 1:  # fixed the condition for checking the length
                
                # Error Message (wrong input)
                error_message = '[ ! ] Invalid Input'
                bot.send_message(message.chat.id, error_message)
                
            else:
                # Long link which collect from user ~
                link = message.text.split(' ')[1]
                
                api = f'https://is.gd/create.php?format=simple&url={link}'
                res = req.get(api)
                
                # message which bot will send
                sent_message = f'''
                    
    Your Url Is Shorted Done!
    
    $ Long Url : {message.text}
    $ Short Url : {res.text}
    
    Thanks For Using This tool 
    
    Type /help For more option's
                    
                    '''
                    
                bot.send_message(message.chat.id,sent_message)
            
        except Exception as e:
            bot.send_message(message.chat.id, f'[!] Error: {e}')
    
    
    # 3nd short program
    @bot.message_handler(commands=['short3'])
    def short_3(message):
        
        try:
            
            
            if len(message.text.split(' ')) <= 1:  # fixed the condition for checking the length
                
                # Error Message (wrong input)
                error_message = '[ ! ] Invalid Input'
                bot.send_message(message.chat.id, error_message)
                
            else:
                # Long link which collect from user ~
                link = message.text.split(' ')[1]
                
                api = f'https://cutt.ly/api/api.php?key=af8c6a9bebc3a7415ffe7d7f493c784f45718&short={link}'

                response = req.get(api)
                data = response.json()

                # Check if the request was successful (status 7)
                if data["url"]["status"] == 7:
                    short_link = data["url"]["shortLink"]
                    
                    
                    # message which bot will send
                    sent_message = f'''
                    
                    Your Url Is Shorted Done!
                    
                    $ Long Url : {message.text}
                    $ Short Url : {short_link}
                    
                    Thanks For Using This tool 
                    
                    Type /help For more option's
                    
                    '''
                    
                    bot.send_message(message.chat.id,sent_message)
                    
                else:
                    bot.send_message(message.chat.id,f"Error: Unable to shorten the link. Status: {data['url']['status']}")
            
            
        except Exception as e:
            bot.send_message(message.chat.id, f'[!] Error: {e}')


    # 4nd short program
    @bot.message_handler(commands=['short4'])
    def short_4(message):
        try:
            
            
            if len(message.text.split(' ')) <= 1:  # fixed the condition for checking the length
                
                # Error Message (wrong input)
                error_message = '[ ! ] Invalid Input'
                bot.send_message(message.chat.id, error_message)
                
            else:
                # Long link which collect from user ~
                link = message.text.split(' ')[1]
                api = f'https://v.gd/create.php?format=simple&url={link}'
                res = req.get(api)

                sent_message = f'''
                    
    Your Url Is Shorted Done!
    
    $ Long Url : {message.text}
    $ Short Url : {res.text}
    
    Thanks For Using This tool 
    
    Type /help For more option's
                    
                    '''
                bot.send_message(message.chat.id,sent_message)
            
        except Exception as e:
            bot.send_message(message.chat.id, f'[!] Error: {e}')


    # 5nd short program
    @bot.message_handler(commands=['short5'])
    def short_5(message):
        try:
            
            if len(message.text.split(' ')) <= 1:  # fixed the condition for checking the length
                
                # Error Message (wrong input)
                error_message = '[ ! ] Invalid Input'
                bot.send_message(message.chat.id, error_message)
                
            else:
                # Long link which collect from user ~
                link = message.text.split(' ')[1]
                api = f'http://bitly.ws/create.php?url={link}'
                res = req.get(api)
                short_url = res.url.replace('/show','')
                
                sent_message = f'''
                    
    Your Url Is Shorted Done!
    
    $ Long Url : {message.text}
    $ Short Url : {short_url}
    
    Thanks For Using This tool 
    
    Type /help For more option's
                    
                    '''
                bot.send_message(message.chat.id,sent_message)
                
        except Exception as e:
            bot.send_message(message.chat.id, f'[!] Error: {e}')


    # 6nd short program
    @bot.message_handler(commands=['short6'])
    def short_6(message):
        try :
            
            if len(message.text.split(' ')) <= 1:  # fixed the condition for checking the length
                
                # Error Message (wrong input)
                error_message = '[ ! ] Invalid Input'
                bot.send_message(message.chat.id, error_message)
                
            else:
                # Long link which collect from user ~
                link = message.text.split(' ')[1]
                api = f'http://xy2.eu/create.php?url={link}'
                res = req.get(api)
                short_url = res.url.replace('/show','')
                
                sent_message = f'''
                    
    Your Url Is Shorted Done!
    
    $ Long Url : {message.text}
    $ Short Url : {short_url}
    
    Thanks For Using This tool 
    
    Type /help For more option's
                    
                    '''
                bot.send_message(message.chat.id,sent_message)
                   
        except Exception as e:
            bot.send_message(message.chat.id, f'[!] Error: {e}')

    # 7nd short program
    @bot.message_handler(commands=['short7'])
    def short_7(message):
        try:
            
            
            if len(message.text.split(' ')) <= 1:  # fixed the condition for checking the length
                
                # Error Message (wrong input)
                error_message = '[ ! ] Invalid Input'
                bot.send_message(message.chat.id, error_message)
                
            else:
                # Long link which collect from user ~
                link = message.text.split(' ')[1] 
                
                api = "https://snip.ly/pub/snip"
                data = {"url": link, "cta_message": "Sign up and customize the CTA!", "button_url": "https://sniply.io/pricing/"}
                response = req.post(api, json=data)
                
                shortUrl = response.json()["snip_url"]
                
                sent_message = f'''
                    
                    Your Url Is Shorted Done!
                    
                    $ Long Url : {message.text}
                    $ Short Url : {shortUrl}
                    
                    Thanks For Using This tool 
                    
                    Type /help For more option's
                    
                    '''
                bot.send_message(message.chat.id,sent_message)
            
            
        except Exception as e:
            bot.send_message(message.chat.id, f'[!] Error: {e}')
    
    
    try:
        bot.polling()
    except Exception as e:
        print(f"Error in polling: {e}")
        pass
    






def ck_file():
    if os.path.exists('api.txt'):
        with open('api.txt', 'r') as file:
            api = file.read().strip()  # Strip whitespace characters
            if api == '':
                print('[!] I Cant Find Any Bot API')
                print('[~] Please Enter Your Bot API')
                botApi = input('=> ')
                if botApi:
                    num, token = botApi.split(':')
                    if len(num) > 5 and len(token) > 20:  # No need for separate checks, combine them
                        clear_screen()
                        print('[ok] Your Bot Token Is ok. Wait For Adding It On File.')
                        with open('api.txt', 'w') as file:
                            file.write(botApi)
                            return botApi
                    else:
                        print("[!] Token or ID is invalid.")
                        return None
                else:
                    print("[!] Bot API not provided.")
                    return None
            else:
                num, token = api.split(':')
                if len(num) > 5 and len(token) > 20:  # No need for separate checks, combine them
                    clear_screen()
                    print('[ok] Bot Token Is Ok, Wait For Starting Bot')
                    return api
                else:
                    print("[!] Token or ID is invalid.")
                    return None
    else:
        with open('api.txt', 'w') as file:
            file.write('')
        return None

def main():
    try:
        print('[#] Bot Is Running..')
        api = ck_file()
        if api:
            print('[#] Bot Is Runing....')
            runBot(api)
        else:
            print("[!] Bot API is not valid.")
    except KeyboardInterrupt:
        print('[$] You Turned Off This Bot')
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == '__main__':
    main()

    
# 6403032614:AAFwAWVGC9mKmBLx3y2ucXHAHPukwG7q6mo