"""
    How to wikirace without Friends

    Copyright (C) <year>  <name of author>

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
"""



def bfs(startNode, endNode):
    frontier = util.Queue()
    visited=set([])
    initialState = startNode

    movessofar = []

    frontier.push((initialState,[],0))

    while not frontier.isEmpty():
        (node,path,cost) = frontier.pop()
        if node not in visited:
            visited.add(node)

            if node == endNode:
                return path
            else:
                for link in wikipedia.page(node).links:
                    npath = path[:]
                    npath.append(link)

                    frontier.push((link,npath,cost+1))
    return []



def areTheseRelated(startPage, endPage):
    path = bfs(startPage,endPage)
    if len(path) == 0:
        print "No relation between " +startPage + " and " +endPage
    else:
        print startPage + " and " + endPage +" are related."
        for node in path:
            print node



