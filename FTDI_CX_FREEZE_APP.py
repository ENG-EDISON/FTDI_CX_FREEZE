import serial
import keyboard
from serial.tools import list_ports
import time
from tkinter import Tk,Label,Button

root=Tk()
Distance_Label=Label(root)
Temp_Label=Label(root)
Led_Freq=Label(root)
Temp_Label.pack()
Distance_Label.pack()
Led_Freq.pack()
Button_pressed=False


def Add_Speed():
    global Button_pressed
    s.write(b'1')
    Button_pressed=True

def print_ports_info():
    for port in list_ports.comports():
        print("Device :",port.device)
        try:
            print("Vid:",hex(port.vid),"pid:",hex(port.pid))
        except:
          print("Vid:",port.vid,"pid:",port.pid)
        print("Serial Number:",port.serial_number)
        print("Name: ",port.name)
        print("hiw: ",port.hwid)
        print("Description: ",port.description)
        print("Interface:",port.interface)
        print("Location:",port.location)
        print("Manufacturer: ",port.manufacturer)
        print("Product Id: ",port.product)


def scan_for_picos(verbose=False):
    picos=[]
    for port in list_ports.comports():
        if verbose:
            print("Checking",port.device)
        if port.manufacturer !=None:
            if "USB Serial Device" in port.description:
                picos.append(port.device)
    return picos
        
picos=scan_for_picos()
pico1=print_ports_info()
print("Picos Found:")
for pico in picos:
    print(pico)
s=serial.Serial(pico,baudrate=115200)
Timer_B=Button(root,text='Speed+',command=Add_Speed)
Timer_B.pack()
Query=[b'd',b't',b'f']
if __name__ == '__main__':
    while True:
        root.update()
        try:
            s.open()
        except:
            if keyboard.is_pressed("a"):
                exit(1)
            if Button_pressed==True:
                k=s.read_until(b'\n')
                k=k.decode('utf-8')
                print(k)
                time.sleep(1)
                Button_pressed=False

