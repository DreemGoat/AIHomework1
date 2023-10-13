#for number 1 of the assignment

#Graph
G = {
    "S": ["A"],
    "A": ["B"],
    "B": ["C"],
    "C": ["D", "E"],
    "D": [],
    "E": ["I","F","H"],
    "F": ["J"],
    "G": [],
    "H": ["N"],
    "I": [],
    "J": ["K"],
    "K": ["O"],
    "L": [],
    "M": [],
    "N": ["R"],
    "O": ["P"],
    "P": ["L","T"],
    "Q": ["U","M"],
    "R": ["V"],
    "T": ["Q","W"],
    "U": ["G"],
    "V": ["X"],
    "W": ["Y"],
    "X": ["U"],
    "Y": []
}

def BFS(G, start, target):
    #helper data structures
    visited = set()
    Q = []
    Q.append(start)

    #loop until Q is not empty
    while (Q != []):
        #picking the first node in the queue
        u = Q.pop(0)

        #keeps track of the visited nodes
        visited.add(u)
        print("visited: ", u)

        #check if the goal is reached
        if u == target:
            print("reached target: ", target)
            break

        for v in G[u]:
            if (v not in visited) and (v not in Q):
                Q.append(v)
                print("added neighbour: ", v)
                #print("Q: ", Q)

#run BFS
start = "S"
target = "G" 
BFS(G, start, target)