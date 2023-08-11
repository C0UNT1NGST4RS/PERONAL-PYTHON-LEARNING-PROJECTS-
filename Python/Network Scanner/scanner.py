from socket import *
import time 
from tqdm import tqdm


starttime =time.time()

if __name__ == '__main__':
    target = input("enter the Host to scan:")
    t_ip = gethostbyname(target) 
    print("Strating scan on host :", t_ip)
    
    port_range = range(1,100)
    progress_bar = tqdm(port_range, unit='port', desc='Scanning')

    for i in range(1,100):
        s = socket(AF_INET , SOCK_STREAM)
        conn = s.connect_ex((t_ip,i))
        
   
        for i in progress_bar:
            s = socket(AF_INET, SOCK_STREAM)

            if conn ==0:
                print ('Port %d: OPEN' % (i,))
            s.close()

print("Scan completed")
print("Total time taken :",time.time()-starttime)


