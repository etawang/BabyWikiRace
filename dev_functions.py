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



