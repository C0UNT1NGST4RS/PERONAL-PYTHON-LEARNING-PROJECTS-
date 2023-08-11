from socket import *
import time 

starttime =time.time()

if __name__ == '__main__':
    target = int(input("enter the Host to scan:"))
    t_ip = gethostbyname(target) 
    print("Strating scan on host :", t_ip)

    for i in range(1,500):
        s = socket(AF_INET , SOCK_STREAM)
        conn = s.connect_ex((t_ip,i))

        if conn ==0:
            print("PORT", i ,"is OPEN")
        s.close()
        
print("Scan completed")
print("Total time taken :",time.time()-starttime)


