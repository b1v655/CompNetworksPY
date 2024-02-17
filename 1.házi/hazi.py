from collections import deque
from subprocess import PIPE, Popen
from multiprocessing.dummy import Pool as ThreadPool
import json
import platform
import datetime
import timeit

start = timeit.default_timer()


def beolvas():
    data=list()
    with open("top-1m.csv","r") as f:
        for i in range(100):
            data.append(f.readline())
        for line in deque(f,100):
            data.append(line)
    return data

def levag(data):
    data2=list()
    for line in data:
        data2.append(line.rstrip().split(',')[1])
    return data2
def ping(url):
    p = Popen(["ping", '-n', '10', url], stdout=PIPE, shell=True)
    data['pings'].append({  
        'target': url,
        'output': p.communicate()[0]
    })
    p.stdout.close()
def tracert(url):
    p = Popen(["tracert", url], stdout=PIPE, shell=True)
    data['traces'].append({  
        'target': url,
        'output': p.communicate()[0]
    })
    p.stdout.close()
#ping
data={}
data['date']=str(datetime.datetime.today()).split()[0]
data['system']=platform.system()
data['pings']=[]
pool = ThreadPool(500) 
pool.map(ping, levag(beolvas()))
with open("ping.json", "w") as write_file:
    json.dump(data,write_file, indent=4, separators=(',', ': '))
print "lefutott a pingprogram"
#trace
data={}
data['date']=str(datetime.datetime.today()).split()[0]
data['system']=platform.system()
data['traces']=[]
pool.map(tracert, levag(beolvas()))
with open("traceroute.json", "w") as write_file:
    json.dump(data,write_file,indent=4, separators=(',', ': '))
print "lefutott a traceprogram"

stop = timeit.default_timer()

print str((stop - start)/60)+':'+str((stop-start)%60)
