# background-traffic-gen
method to DoS your system / network. 

# Run
For Windows users, it's higly recommended to run this on Linux via Docker Container as windows ping offers less features. 

## Docker (using powershell / cmd)
1. First build the image
```
cd native-thread;docker build . -t packet-gen
```
2. Then run the container
```
docker run -e PING_DEST_IP={insert value here} -e PING_N_PROCESS={insert value here} packet-gen
```

## Without docker
```
python native-thread/main.py
```

