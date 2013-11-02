import wikipedia
import random
import util



def bfs(startNode, endNode):
    frontier = util.Queue()
    visited=set([])
    intialState = startNode

    movessofar = []

    frontier.push((initialState,[],0))

    while not frontier.isEmpty():
        (node,path,cost) = frontier.pop()
        if node not in visited:
            visited.add(node)

            if node == endNode:
                return path
            else:
                for link in wikipedia.page(startTopic).links:
                    npath = path[:]
                    npath.append(link)

                    frontier.push((link,npath,cost+1))
    return []


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
