import wikipedia
import random


def bfs(startNode):
    currNode=

def returnRandomLink(linkList):
    randIndex = random.randint(0,len(linkList)-1)
    return linkList[randIndex]


def getNext(startTopic):
    startPage = wikipedia.page(startTopic)
    return returnRandomLink(startPage.links)

def main():
    print "Enter Start Page:"
    startTopic = raw_input()
    print "Enter Jumps:"
    x = int(raw_input())
    currentTopic = startTopic

    topiclist=[]

    for i in xrange(x):
        topiclist.append(currentTopic)
        currentTopic = getNext(startTopic)
    topiclist.append(currentTopic)
    print "End Topic: " + currentTopic
    print "GO! Press enter to see answer."

    raw_input()
    print topiclist

if __name__ == '__main__':
    main()
