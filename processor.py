#I Make a Software for Sortex Machine
import time as T
import os as o

o.system("clear")
print("Loding...")
T.sleep(3)
print("\n\n\n")
print("+------|| Sortex T.01 ||-------+")
print("|  ON                          |")
print("|  OFF                         |")
print("+------------------------------+")

T.sleep(2)
G = int(input("\n"))
if(G==1):
    print("\n")
    print("Cleaning for starting Machine...")
    T.sleep(6)
    o.system("clear")
    print("Machine Ready for Start")
    T.sleep(2)
    o.system("clear")
    print("Checking Some System Info...")
    T.sleep(2)
    o.system("clear")
    print("Test 1 : Pass")
    T.sleep(0.3)
    print("Test 2 : Pass")
    T.sleep(0.3)
    print("Test 3 : Pass")
    T.sleep(0.3)
    S = o.system("lscpu")
    T.sleep(0.3)
    o.system("clear")
    print("Loding...")
    T.sleep(3)
    A = o.system("lsblk")

elif(G==2):
    print("Loding...")
    T.sleep(2)
    o.system("clear")
    print("\n\nShutDown....")
    T.sleep(2.3)
    o.system("exit 110")

    
else:
    print("Saving Parameter..")
    
R = int(input("Red: "))




