"""
    App: BabyWikiRace
    Version 1.0

    How to wikirace without Friends

    Copyright (C) 2013 Brandon Lum & Esther Wang

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>
    App: BabyWikiRace
"""


import wikipedia
import random
import imp

util = imp.load_source('util', 'lib/util.py')

"""
returnRandomLink

desc: Takes in a list and returns a random element
of it and None if nothing.

in:
    linkList - the list of links
out:
    ele - the random elemnt of the list or None is empty

"""

def returnRandomLink(linkList):
    if len(linkList)>0:
        randIndex = random.randint(0,len(linkList)-1)
        return linkList[randIndex]
    else:
        return None

"""
getNext

Given a page, get a random page which can be reached from
the current page via links

in:
    startTopic - the starting page
out:
    nextLink - the next link to go to
"""
def getNext(startTopic):
    try:
        startPage = wikipedia.page(startTopic)
    except:
        print "Page doesn't exists!"
        exit(1)
    nextLink = returnRandomLink(startPage.links)
    return nextLink


"""
function getTarget

desc: Takes in a start topic and the number of jumps and
a number of jumps and returns a target which is that
number of jumps away, together with the path to the
target

in:
    startTopic - the start node to jump from
    jumps - number of jumps
    @assert jumps >= 0
out:
    ( endTarget, path )

    endTarget - the target page
    path - the path from startTopic to endTarget

"""
def getTarget(startTopic, jumps):
    currentTopic = startTopic
    topiclist=[]

    for i in xrange(jumps):
        # Add to path
        topiclist.append(currentTopic)

        # Get next topic
        nextTopic = getNext(startTopic)

        # Break if no more links
        if currentTopic == None:
            break
        else:
            currentTopic = nextTopic

    if currentTopic != None:
        topiclist.append(currentTopic)

    return (currentTopic, topiclist)


def main():


    print """
    Copyright (C) 2013 Brandon Lum & Esther Wang

    This program comes with ABSOLUTELY NO WARRANTY;
    This is free software, and you are welcome to redistribute it under certain conditions;
    """

    try:
        print "Enter Start Page:"
        startTopic = raw_input()
        print "Enter Jumps:"
        x = int(raw_input())
    except:
        print "Parsing Exceptions"
        exit(1)

    if x < 0:
        print "Jumps must be non-negative."
        exit(1)

    (endTopic, path) = getTarget(startTopic, x)
    print "End Topic: " + endTopic
    print "GO! Press enter to see answer."

    raw_input()
    print path


if __name__ == '__main__':
    main()
