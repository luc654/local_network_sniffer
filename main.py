import gpiod
import time
import subprocess

# Add ip's you want to block here.
blockedList = [""]


def checkBlock(item):
     if item in blockedList:
          return False
     return True
def compare(list1, list2, text, led):

    set1 = {tuple(row) for row in list1}
    set2 = {tuple(row) for row in list2}

    difference = set2 - set1

    for item in difference:
        if checkBlock(item[0]):
            print(f"{text} {item[0]}, {item[1]}")
            led.set_value(1)

    print("")

def turnOff():
    redled.set_value(0)
    greenled.set_value(0)


LED_PIN_RED = 18
LED_PIN_GREEN = 23

chip = gpiod.Chip('gpiochip4')
redled = chip.get_line(LED_PIN_RED)
greenled = chip.get_line(LED_PIN_GREEN)
redled.request(consumer='LED', type=gpiod.LINE_REQ_DIR_OUT)
greenled.request(consumer='LED', type=gpiod.LINE_REQ_DIR_OUT)

prevAmount = 0
prevList = []

turnOff()


ipaddr = 0

try:
        command = "ip a | grep 'e wlan0' | awk '{print $4}'"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        ipaddr = result.stdout.strip()

except e:
        print("program does not have terminal permissions")

while True:

    try:
        command = "sudo nmap -sn "+ipaddr+"/24 | grep 'Nmap scan'"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout.strip()
        turnOff()

        Dlist = output.split('\n')
        Clist = []
        for row in Dlist:
            Elist = row.split(" ")
            Alist = [Elist[5], Elist[4]]
            Clist.append(Alist)


        amount =  len(Clist)
        if amount > prevAmount:
            compare(prevList, Clist, "Connected:", redled)

        elif amount < prevAmount:
            compare(Clist, prevList, "Disconnected:", greenled)


        prevAmount = amount
        prevList = Clist


    except KeyboardInterrupt:

                redled.release()
                greenled.release()
                chip.close()
