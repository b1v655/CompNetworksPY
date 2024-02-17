#!/usr/bin/env python


import json
import copy
import time

with open("cs1.json", "r") as read_file:
    data = json.load(read_file)
    
demands = data["simulation"]["demands"]
links = data["links"]
usedCircuits = []

lineCount = 1
for currTime in range (data["simulation"]["duration"]):
	for demand in demands:
		if (demand["end-time"] == currTime):
			for circuit in usedCircuits:
				if (circuit[0] == demand["end-points"][0] and circuit[-1] == demand["end-points"][1]):
					for currPoint in range (0, len(circuit)-1):
						reqLink = list(filter(lambda x: (x["points"][0] == circuit[currPoint] and x["points"][-1] == circuit[currPoint+1]) or (x["points"][0] == circuit[currPoint+1] and x["points"][-1] == circuit[currPoint]), links))
						index = links.index(reqLink[0])
						links[index]["capacity"] = link["capacity"]+demand["demand"]
					usedCircuits.remove(circuit)
					print "felszabaditas: " + demand["end-points"][0] + "<->" + demand["end-points"][1] + " st:" + str(currTime)
					lineCount += 1
					break
		if (demand["start-time"] == currTime):
			isFound = False
			for possibleCircuit in data["possible-cicuits"]:
				if (possibleCircuit[0] == demand["end-points"][0] and possibleCircuit[-1] == demand["end-points"][1]):
					for currPoint in range (0, len(possibleCircuit)-1):
						tempLinks = copy.deepcopy(links)
						isLinkGood = True
						index = 0
						for link in tempLinks:
							if ((link["points"][0] == possibleCircuit[currPoint] and link["points"][1] == possibleCircuit[currPoint+1]) or (link["points"][0] == possibleCircuit[currPoint+1] and link["points"][1] == possibleCircuit[currPoint])):
								if (link["capacity"]-demand["demand"] <0):
									isLinkGood = False
									break
								else:
									tempLinks[index]["capacity"] -= demand["demand"]
							index += 1
						if (isLinkGood and currPoint == len(possibleCircuit)-2):
							isFound = True
							links = tempLinks
							usedCircuits.append(possibleCircuit)
							break
				if (isFound):
					break
			answer = "foglalas: " + demand["end-points"][0] + "<->" + demand["end-points"][1] + " st:" + str(currTime) + " - "
			if(isFound):
				print answer + "sikeres"
			else:
				print answer + "sikertelen"
			lineCount += 1
		elif (demand["start-time"] > currTime):
			break
