import wikipedia
import random
import util





def returnRandomLink(linkList):
    randIndex = random.randint(0,len(linkList)-1)
    return linkList[randIndex]


def getNext(startTopic):
    startPage = wikipedia.page(startTopic)
    return returnRandomLink(startPage.links)

def getTarget(startTopic, jumps):
    currentTopic = startTopic

    topiclist=[]

    for i in xrange(jumps):
        topiclist.append(currentTopic)
        currentTopic = getNext(startTopic)
    topiclist.append(currentTopic)
    return (currentTopic, topiclist)


def main():
    print "Enter Start Page:"
    startTopic = raw_input()
    print "Enter Jumps:"
    x = int(raw_input())

    (endTopic, path) = getTarget(startTopic, x)
    print "End Topic: " + endTopic
    print "GO! Press enter to see answer."

    raw_input()
    print path



if __name__ == '__main__':
    main()
