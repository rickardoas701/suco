import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11,GPIO.OUT)
pin=23

def rc_time (pin):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, GPIO.LOW)
    time.sleep(0.5)

    #Change the pin back to input
    GPIO.setup(23, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(23) == GPIO.LOW):
        count += 1
    return count

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    #print 'Muestra\t','Boton\t','LDR'
    btn=0
    #fo.write('Muestra\t'+'Boton\t'+'LDR\n\r')
    for i in range(1,31):
        estado=GPIO.input(13)
        btn=0
        GPIO.output(11,False)
        if estado==False:
            btn=1
            GPIO.output(11,True)
        val=str (rc_time(pin))
        #print i,'\t',btn,'\t',rc_time(pin)
        #fo.write(str(i)+'\t'+str(btn)+'\t'+val+'\n\r')
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
