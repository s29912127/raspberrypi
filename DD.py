import time
import RPi.GPIO as GPIO
import mcp3008
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_ILED = 5
print "Dust Sensor"
start=time.time()
stop=time.time()
sum=0
counter=0
try:
    while stop-start<10:
        counter+=1
        GPIO.setup(GPIO_ILED,GPIO.OUT)
        GPIO.output(GPIO_ILED, False)
        time.sleep(0.5)
        GPIO.output(GPIO_ILED, True)
        adc = mcp3008.MCP3008()
        time.sleep(0.00028) #SamplingTime: highest at 0.28ms
        voMeasured = adc.read([mcp3008.CH1])
        time.sleep(0.00004) #deltaTime
        GPIO.output(GPIO_ILED, False)
        time.sleep(0.009680) #sleepTime
        adc.close()
        print"- Dust Density: ",voMeasured[0],"ug/m3"
        sum+=voMeasured[0]
        stop = time.time()
        time.sleep(0.5)
    if sum/counter<=15:
        print"- Average Dust Density: \033[1;37;40m",sum/counter,"ug/m3"
    if sum/counter>=16 and sum/counter<41:
        print"- Average Dust Density: \033[1;36;40m",sum/counter,"ug/m3"
    if sum/counter>=40 and sum/counter<66:
        print"- Average Dust Density: \033[1;32;40m",sum/counter,"ug/m3"
    if sum/counter>=65 and sum/counter<151:
        print"- Average Dust Density: \033[1;33;40m",sum/counter,"ug/m3"
    if sum/counter>=150 and sum/counter<251:
        print"- Average Dust Density: \033[1;31;40m",sum/counter,"ug/m3"
    if sum/counter>=250:
        print"- Average Dust Density: \033[1;35;40m",sum/counter,"ug/m3"

    print"\033[0mPM2.5 Standard Level:"
    print"\033[1;37;40m  0-15    Good\033[0m"
    print"\033[1;36;40m  16-40   Moderate\033[0m"
    print"\033[1;32;40m  40-65   Unhealthy for Sensitive Froups\033[0m"
    print"\033[1;33;40m  65-150  Unhealthy\033[0m"
    print"\033[1;31;40m  150-250 Very Unhealthy\033[0m"
    print"\033[1;35;40m  250-500 Hazardous\033[0m"
    print""

except Exception,e:
    print str(e)



    






