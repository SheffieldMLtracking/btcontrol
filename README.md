# btcontrol
A tool for controlling multiple tracking systems, rsyncing the data off them, etc.

# Examples
First need to get a list of all the systems on the network:
```
$ btcontrol --scan
Rescanning...

http://192.168.112.207:5000/getid
Our IP address: 192.168.112.95

                 IP Address    | Port 22 | Port 5k | Comments        | Last Command
                192.168.112.95 |    open |  closed |   this computer |  - 
               192.168.112.110 |  closed |  closed |                 |  - 
   http://192.168.112.207:8000 |    open |    open |          Box 13 |  ok 
```

Download all the images from all the boxes to ~/beedata:
```
btcontrol --rsync ~/beedata --pwfile /home/mike/Documents/Research/rsync_bee/pw.txt
```
pw.txt is a plaintext file containing the ssh password for the boxes.

Start all the camera systems taking photos:
```
btcontrol --start
```

Stop all the camera systems taking photos:
```
btcontrol --stop
```

# Usage
```
usage: btcontrol [-h] [--scan] [--start] [--stop] [--rsync RSYNC] [--pwfile PWFILE]

Controls multiple tracking systems.

options:
  -h, --help       show this help message and exit
  --scan           Refresh the scan cache
  --start          Start all boxes
  --stop           Start all boxes
  --rsync RSYNC    Copy all photos from box to local computer
  --pwfile PWFILE  Path to file containing ssh password
```
