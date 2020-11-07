import math
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import threading
import datetime
import time
import RPi.GPIO as GPIO
samplingtime=10
GPIO.setmode(GPIO.BCM)
sampRate =26
eeprom_array= []   #eeprom array to write to eeprom 
cnt=0
counter = 66600
second = 0    
minute = 0    
hours = 0 
def setup():
    GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_UP) #setup the 
    GPIO.add_event_detect(7,GPIO.FALLING, callback=change, bouncetime=200)
  
def stop_watch(): 
        global counter  
        tt = datetime.fromtimestamp(counter) 
        stopwatch = tt.strftime("%H:%M:%S") 
        counter+=1
        return stopwatch
 def current_time():
         
def back_up():
    global second, hours, minute
    print('\t\t\t\t  %d : %d : %d '%(hours,minute,second))      
    time.sleep(1)    
    second+=1    
    if(second == 60):    
        second = 0    
        minute+=1    
    if(minute == 60):    
        minute = 0    
        hour+=1;    
    os.system('cls')
    
def change(channel):
    dict ={10: 5,5: 1,1: 10} #create a dictionary to stores the 3 values for samplingtime
    global samplingtime
    if GPIO.event_detected(channel):#if the button is pressed 
       samplingtime=dict[samplingtime]#change the value of the sampling time depending on the current value
def save_temp(temp):
    global eeprom_array,cnt
    
    # include new score
    

    
                                                      #converting each character in the person's name to a a number 
    eeprom_array.append(temp)#append the the user sc
    cnt=cnt+1
    eeprom.write_block(1, eeprom_array)# write  to the eeprom
    cnt=0
    eeprom_array= [] 
        
    pass
    
def print_time_thread():
    """
    This function prints the time to the screen every five seconds
    """
    #start time recording
    start_time = time.process_time()
    
    thread = threading.Timer(5, print_time_thread)#implement a timer to start a new thread after every few second depending on what samplingtime is
    thread.daemon = True  # Daemon threads exit when the program does
    #start thread
    thread.start()
    
  
    output_string= str(math.trunc(start_time))+"s" #convert the time to a string
      #code supplied to us
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
    cs = digitalio.DigitalInOut(board.D5)
    mcp = MCP.MCP3008(spi, cs)
    chan = AnalogIn(mcp, MCP.P1)
    temp= round(((1000*chan.voltage)-500)/10)# formula used to find temperature
    save_temp(temp)
    time_out= stop_watch()
    print('{:10}'.format(time_out),'{:10}'.format(time_out),'{:10}'.format(str(chan.value)),'{:10}'.format(temp),"C") #print using string formatting
   

if __name__ == "__main__":
    print("Runtime    Temp Reading      Temp")
    setup()
    print_time_thread() # call it once to start the thread
    # Tell our program to run indefinitely
    while True:
       pass