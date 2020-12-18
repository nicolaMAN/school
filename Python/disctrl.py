import enquiries
import os
import sys
import screen_brightness_control as sbc
import array
from termcolor import colored

def checkfunc(options,index):
    curr_b = int(sbc.get_brightness(display=index))
    if curr_b == 100:
        options.pop(1)
        return
    elif curr_b == 35:
        options.pop(0)
        return
    else:
        if options[0]!='lower -':
            options.insert(0,'lower -')
            return
        elif options[1]!='higher +':
            options.insert(1,'higher +')
            return

def change(display_name, index ,array):
    options = ['lower -', 'higher +',array[0],array[1]]
    percentage = int(sbc.get_brightness(display=index)) / 5
    while True:
        sys.stdout.write('\r')
        sys.stdout.write(colored(display_name,'blue'))
        sys.stdout.write( "[%-20s] %d%% \n" % ('●' * int(percentage), 5 * int(percentage)))

        checkfunc(options,index)

        response = enquiries.choose('Choose one of these options: ', options)

        if response == 'lower -':
            sbc.set_brightness('-5', display = index)
            percentage = percentage-1

        elif response == 'higher +':
            sbc.set_brightness('+5', display = index)
            percentage = percentage+1

        elif response == array[0]:
            sbc.set_brightness('100', display = index)
            percentage = 20

        elif response == array[1]:
            os.system('clear')
            quit()

        os.system('clear')

check_monitors = os.popen("xrandr --listactivemonitors").read()
count = int(check_monitors.split()[1])
display_list = []*count
temp = 1

for i in range(count):
    display_list.insert(0, check_monitors.split()[temp+4])
    temp = temp + 4

array = [colored('restore','yellow'), colored('exit','red')]
display_list.append(array[1])
choice = enquiries.choose('Display for change: ', display_list)
if choice == array[1]:
    os.system('clear')
    quit()
os.system('clear')
change( choice, display_list.index(choice), array)
os.system('clear')