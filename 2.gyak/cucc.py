import json
with open("cs1.json","r") as readed_file:
    data=json.load(readed_file)
lista=list()
for i in range(data['simulation']['duration']):
    for demands in data['simulation']['demands']:
        if demands["start-time"]==i:
            j=0
            while not set(demands['end-points']).issubset(data['possible-cicuits'][j]):
                j=j+1
            k=1
            while not set(data['possible-cicuits'][j][k]).issubset(data["end-points"]):
                m=0
                while not [(string)data['possible-cicuits'][j][k]].append(data['possible-cicuits'][j][k-1]).issubset(data["links"]["points"][m]):
                    m=m+1
                if data["links"]["points"][m]['capacity'] == 0.0:
                    print 
                    break
                k=k+1
            k=1
            if not data["links"]["points"][m]['capacity'] == 0.0:
                while not set(data['possible-cicuits'][j][k]).issubset(data["end-points"]):
                    m=0
                    while not set(list().append(data['possible-cicuits'][j][k]).append(data['possible-cicuits'][j][k-1])).issubset(data["links"]["points"][m]):
                        m=m+1
                    data["links"]["points"][m]['capacity'] = 0.0
                    k=k+1
                print data['possible-cicuits'][j]
                lista.append(data['possible-cicuits'][j])
                data['possible-cicuits'].remove(data['possible-cicuits'][j])
                print 'letrejott'
            else:
                print 'nem jott letre'
        elif demands["end-time"]== i and not demands["demand"] == 0.0:
            j=0
            while not set(demands['end-points']).issubset(lista[j]):
                j=j+1
            data['possible-cicuits'].append(lista[j])
            lista.remove(lista[j])
print data['possible-cicuits']
           
