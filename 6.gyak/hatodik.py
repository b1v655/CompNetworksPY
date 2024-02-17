from heapdict import heapdict
import json
with open("graph.json","r") as readed_file:
    data=json.load(readed_file)
def w(s,v):
    for link in data["links"]:
        if link['points'][0]==v and link['points'][1]==s or link['points'][0]==s and link['points'][1]==v:
            return link['weight']

    return 1000
def adj(s):
    sett2=[]
    
    for link in data["links"]:
        if link["points"][0]==s:
            sett2.append(link["points"][1])
        if link["points"][1]==s:
            sett2.append(link["points"][0])
    return list(set(sett2))
Evesszo={}
sett=[]
for link in data["links"]:
    sett.append(link["points"][0])
    sett.append(link["points"][1])
    
d={}
ready={}
for elem in set(sett):
    if elem==data["start-point"]:
        d[data["start-point"]]=0
        ready[data["start-point"]]=True
    else:
        d[elem]=1000
        ready[elem]=False
   

Q=heapdict()
pred={}
for v in adj(data["start-point"]):
    pred[v]=data["start-point"]
    d[v]=w(data["start-point"],v)
    Q[v]=d[v]
true=True    
while not len(Q)==0:
    v=Q.popitem()[0]
    Evesszo[pred[v]]=v
    ready[v]=true
    for u in adj(v):
        if u in Q and (d[v]+w(v,u))<d[u]:
            pred[u]=v
            d[u]=d[v]+w(v,u)
            Q[u]=d[u]
        elif u not in Q and not ready[u]:
            pred[u]=v
            d[u]=d[v]+w(v,u)
            Q[u]=d[u]
print(Evesszo)
print(d)

