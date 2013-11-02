import wikipedia
import random

myGraph = {}

def returnRandomLink(linkList):
    randIndex = random.randint(0,len(linkList)-1)
    return linkList[randIndex]


def getNext(startTopic):
    startPage = wikipedia.page(startTopic)
    return returnRandomLink(startPage.links)    

def genDict():
    startPage = wikipedia.page(startTopic)
    frontier = startPage.links
    visited = set()

    while len(frontier) != 0:
        current = frontier.pop(0)
        currentPage = wikipedia.page(current)
        if current not in visited:
            myGraph[current] = currentPage.links
            frontier = frontier + currentPage.links

def main():
    print "Enter Start Page:"
    startTopic = raw_input()
    print "Enter Jumps:"
    x = int(raw_input())
    currentTopic = startTopic
    print "Enter Target Page:"
    endTopic = raw_input()
       
    topiclist=[]

    genDict()

     i in xrange(x):
        topiclist.append(currentTopic)
        currentTopic = getNext(startTopic)
    topiclist.append(currentTopic)
    print "End Topic: " + currentTopic
    print "GO! Press enter to see answer."
    
    raw_input()
    print topiclist

if __name__ == '__main__':
    main()
