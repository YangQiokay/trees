# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 23:19:34 2016

@author: yangqi
"""

import matplotlib.pyplot as plt

decisionNode = dict(boxstyle = "sawtooth", fc = "0.8")
leafNode = dict(boxstyle = "round4", fc = "0.8")
arrow_args = dict(arrowstyle = "<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy = parentPt, xycoords = 'axes fraction',\
    xytext = centerPt, textcoords = 'axes fraction', \
    va = "center", ha = "center", bbox = nodeType, arrowprops = arrow_args)    
    
def createPlot():
    fig = plt.figure(1, facecolor = 'white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon = False)
    plotNode('decisionNode', (0.5, 0.1),(0.1, 0.5), decisionNode)
    plotNode('leafNode', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()
    
def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = myTree.keys()[0]
   # print firstStr
    secondDict = myTree[firstStr]
   # print secondDict
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
             numLeafs += 1 
      #       print numLeafs
    return numLeafs
    
def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else: thisDepth = 1
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth
    
def retrieveTree(i):
    listOfTrees = [{'no surfacing':{0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                   {'no surfacing':{0: 'no', 1:{'flippers':{0:{'head':{0: 'no', 1: 'yes'}}, 1: 'no'}}}}]
    return listOfTrees[i]
    
def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1])/2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString, rotation = 30)
    
def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = getNumLeafs(myTree)
  #  print numLeafs
    depth = getTreeDepth(myTree)
 #   print depth
    firstStr = myTree.keys()[0]
    #print firstStr
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
  #  print cntrPt
    plotMidText(cntrPt, parentPt, nodeTxt)
   # print plotMidText
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
   # print plotNode
    secondDict = myTree[firstStr]
  #  print secondDict
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
   # print plotTree.yOff
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
     #       print plotTree.xOff
     #       print plotTree.yOff
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD
    #print plotTree.yOff
    
def createPlot(inTree):
    fig = plt.figure(1, facecolor ='white')
    fig.clf()
    axprops = dict(xticks = [], yticks = [])
  #  print axprops
    createPlot.ax1 = plt.subplot(111, frameon = False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
 #   print plotTree.totalW
 #   print plotTree.totalD
    plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0;
 #   print plotTree.xOff
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()
    
