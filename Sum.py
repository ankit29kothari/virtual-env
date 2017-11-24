# Program to produce inputs from KeyBoard
#sum fo the no & print to Console.


from __future__ import print_function

print("add 2 nos =")
print("hello")



import client as paho
broker="iot.eclipse.org"
port=1883
def on_publish(client,userdata,result):
    print("data published \n")
pass
client1= paho.Client("mqtteclipse/cmd")
client1.on_publish = on_publish
client1.connect(broker,port)
ret= client1.publish("mqtteclipse/cmd","on")                  
