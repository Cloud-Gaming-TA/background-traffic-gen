import os
import sys
import threading

from aioping import ping

def run(ip, n_job):
    ping(ip, timeout=0.01, count=n_job, delay=0, packet_size=1400)
    
    
if __name__ == "__main__":
    ip = os.getenv("PING_DEST_ADDR") if os.getenv("PING_DEST_ADDR") != "" else "127.0.0.1"
    n_thread = os.getenv("PING_N_THREADS") if os.getenv("PING_N_THREADS") else 4
    
    try:
        n_thread = int(n_thread)
    except ValueError:
        n_thread = 4
    
    n_job = 10000
    n_thread = 4

    threads = [threading.Thread(target=run, args=(ip, n_job, ), daemon=True)]
    
    for t in threads:
        t.start()
        
    
    try:
        for i, t in enumerate(threads):
            if not t.is_alive():
                t = threading.Thread(target=run, args=(ip, n_job, ), daemon=True)
                t.start()
                threads[i] = t
    except KeyboardInterrupt:
        pass
    finally:
        for t in threads:
            t.join(timeout=1)
            
        sys.exit(0)