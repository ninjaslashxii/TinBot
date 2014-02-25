import time
import Skype4Py
import random

print "|----------------------------------------------|\n";
print "|        Welcome To [TinBot]                     |\n";		 
print "|----------------------------------------------|\n";

def commands(Message, Status):
	if Status == 'SENT' or (Status == 'RECEIVED'): 
		
		if Message.Body == "!ping":
			cmd_ping(Message)
		
		elif Message.Body == "!rickroll":
			cmd_rickroll(Message)
		
		elif Message.Body == "!status":
			cmd_status(Message)
		
		elif Message.Body == "!celebrate":
			cmd_celebrate(Message)
		
		elif Message.Body == "!hammertime":
			cmd_hammertime(Message)
		
		elif Message.Body == "!credit":
			cmd_credit(Message)
		
		elif Message.Body == "!help":
			cmd_help(Message)
		
		elif Message.Body == "!Spam1":
			cmd_spam(Message)
		
		elif Message.Body == "!introduce":
			cmd_intro(Message)
		
		elif Message.Body == '!dice':
			cmd_dice(Message)
			
		elif Message.Body == '!suicide':
			cmd_suicide(Message)
			
		elif Message.Body == '!adminhelp':
			cmd_adminhelp(Message)
		
		elif Message.Body == '!kick':
			cmd_kick(Message)
			
                elif Message.Body == '!ninja':
                        cmd_ninja(Message)

		elif Message.Body == '!dick':
			cmd_dick(Message)

		elif Message.Body == '!love':
                        cmd_love(Message)
		
		elif Message.Body == '!stayinalive':
                        cmd_alive(Message)
						
		elif Message.Body == '!molly':
			cmd_molly(Message)

                elif Message.Body == '!love2':
                        cmd_love2(Message)

                elif Message.Body == '!slowdown':
                        cmd_slowdown(Message)

                elif Message.Body == 'wall':
                        cmd_wall(Message)

                elif Message.Body == '!bright':
                        cmd_bright(Message)
		else:
			pass
			
def cmd_slowdown(Message):
        Message.Chat.SendMessage('H-H-H-Holy shit!\n' + \
                                  'Slow down, grab the wall \n' + \
                                  'Wiggle like you tryna make yo ass fall off \n' + \
                                  'Hella thick I wanna smash \'em all, now \n' + \
                                  'Speed up, \n' + \
                                  'gas pedal \n' + \
                                  'gas pedal \n' + \
                                  'gas pedal \n' + \
                                  'gas pedal \n' + \
                                  'gas pedal \n')
        print "Slowdown Command recieved\n"
        
def cmd_wall(Message):
        Message.Chat.SendMessage('H-H-H-Holy shit!\n' + \
                                  'Slow down, grab the wall \n' + \
                                  'Wiggle like you tryna make yo ass fall off \n' + \
                                  'Hella thick I wanna smash \'em all, now \n' + \
                                  'Speed up, \n' + \
                                  'gas pedal \n' + \
                                  'gas pedal \n' + \
                                  'gas pedal \n' + \
                                  'gas pedal \n' + \
                                  'gas pedal \n')
        print "Slowdown Command recieved\n"

def cmd_alive(Message):
	 Message.Chat.SendMessage('i i i i stayin alive stayin alive\a' + ' http://www.netanimations.net/Stayin-alive.gif')
	 print "Alive Command Received\n"

def cmd_love2(Message):
	 Message.Chat.SendMessage('What is love?')
	 print "Love2 Command Received\n"	
	 
def cmd_molly(Message):
	 Message.Chat.SendMessage( 'MOLLY\n' +  'MOLLY')
	 print "Molly Command Received\n"
	 
def cmd_dick(Message):
	 Message.Chat.SendMessage('Which one is bigger?\n' + 'A. 8=====D\n' + 'B. 8=========D\n' + 'C. 8=D')
	 print "Dick Command Received\n"
	 
def cmd_kick(Message):
	 Message.Chat.SendMessage('Please use /kick instead!')
	 print "Kick Command Received\n"
def cmd_love2(Message):
        Message.Chat.SendMessage('What is love? \n' + \
                                 'Baby don\'t hurt me... \n' + \
                                 'Don\'t hurt me... \n' + \
                                 'No more... \n')
        print "LoveTwo COmmand Recieved \n"
	 
	 
def cmd_adminhelp(Message):
	Message.Chat.SendMessage('Admin Commands')
	Message.Chat.SendMessage('!mute')
	Message.Chat.SendMessage('!ban')
	Message.Chat.SendMessage('!kick')
	Message.Chat.SendMessage('!topic')
	print "Admin Help Command Received \n"

def cmd_ping(Message):
	Message.Chat.SendMessage('[TinBot]: Yes, I\'m still alive. :)')
	print "Ping Command Received \n"
	
def cmd_ninja(Message):
        Message.Chat.SendMessage('So this one time... \n' + \
                                 'at band camp... \n')
        print "Ninja Command Recieved \n"

def cmd_status(Message):
	Message.Chat.SendMessage('[TinBot]: Current Status: ONLINE!')
	print "Status Command Received \n"
	
def cmd_rickroll(Message):
	Message.Chat.SendMessage('[TinBot]: Never Gonna Give You Up! (dance) \n' + '[TinBot]: Never Gonna Let You Down! (dance) \n' + \
                                 '[TinBot]: Never Gonna Run Around and Desert You! (dance) \n' + '[TinBot]: Never Gonna Say Goodbye! (dance) \n' + \
                                 '[TinBot]: Never Gonna Tell A Lie! (dance) \n' + '[TinBot]: Or Hurt You! (dance) \n')
	print "Rick Command Received.\n"

def cmd_celebrate(Message):
	Message.Chat.SendMessage('[TinBot]: Good job! \n' + '[TinBot]: You did great! \n' + '[TinBot]: Keep up the good work! \n' + \
                                 '[TinBot]: (clap) \n' + 'You look like you love being a fgt. \n')
	print "Celebrate Command Received.\n"
	    
def cmd_hammertime(Message):
	Message.Chat.SendMessage('[TinBot]: EVERYONE! \n' + '[TinBot]: EVERYONE STOP WHAT YOU\'RE DOING! \n' + \
                                 '[TinBot]: DO YOU GUYS EVEN KNOW WHAT TIME IT IS!?!?!?!?!? \n' + '[TinBot]: HAMMERTIME!!!!!!!!(dance) \n')
	print "Hammer time Command Received.\n"

def cmd_credit(Message):
	Message.Chat.SendMessage('[TinBot]: Hi, I am TinBot. \n' + '[TinBot]: Everything on me was made by jeffg245, but Ninja came in with a vaccuum. \n' + \
                                 '[TinBot]: If you want to have a feature added let us know!  http://cloudfire.tk/index.html  \n')
	print "Credit Command Received.\n"

def cmd_help(Message):
	Message.Chat.SendMessage('[TinBot]: Type !ping to see if the bot is alive! \n' + \
                                 '[TinBot]: Type !celebrate to have a party! \n' + \
                                 '[TinBot]: Type !rickroll to rick roll someone! \n' + \
                                 '[TinBot]: Type !hammertime to stop, drop, and hammertime! \n' + \
                                 '[TinBot]: Type !credit to see who made me! \n' + \
                                 '[TinBot]: Type !dice for a fun game! \n' + \
                                 '[TinBot]: Type !status to see the status of the bot! \n' + \
                                 '[TinBot]: Type !slowdown to play slowdown.\n' + \
                                 '[TinBot]: Type !love to see love. \n' + \
                                 '[TinBot]: Type !love2 for what is love?')
                                 
	print 'Help Command Recieved.\n'
	
def cmd_bright(Message):
        Message.Chat.SendMessage('/me grabs the lube.')
        print "Bright Command Recieved.\n"

def cmd_love(Message):
        Message.Chat.SendMessage('ANNNDDDDD IIIIIIIII WILLLL ALLLWAAAYYYYSSSSSSSSSSS')
        Message.Chat.SendMessage('/me takes deep breath.')	
        Message.Chat.SendMessage('LOOOOVEEEE YYYYOOOOUUUUUUUUUUU!~')
        print "Love Command Recieved.\n"

def cmd_intro(Message):
	Message.Chat.SendMessage('[TinBot]: Hi!')
	time.sleep(2)
	Message.Chat.SendMessage('[TinBot]: My name is TinBot.')
	time.sleep(2)
	Message.Chat.SendMessage('[TinBot]: Techincally, I\'m a Bot!')
	time.sleep(2)
	Message.Chat.SendMessage('[TinBot]: Type !help to see what I can do. :)')
	print "Introduce Command Received.\n"

def cmd_dice(Message):
	Message.Chat.SendMessage('[TinBot]: Put a bet on numbers 1 through 12.')
	time.sleep(8)
	answer = random.randint(1,12)
	Message.Chat.SendMessage('/me rolls the dice.')
	time.sleep(2)
	Message.Chat.SendMessage('[TinBot]: The dice rolled the number')
	Message.Chat.SendMessage(answer)
	print "Someone's playing dice. \n"

def cmd_suicide(Message):
	Message.Chat.SendMessage('Ah fuck man I can\'t fucking do it shiiiiiiiit.')
	print "Ping Command Received \n"

skype = Skype4Py.Skype(); 
skype.OnMessageStatus = commands 

if skype.Client.IsRunning == False: 
    skype.Client.Start() 
skype.Attach();

print 'Skype Bot currently running on user',skype.CurrentUserHandle, "\n"

while True: 
    raw_input('')
