import json

def fileToJson(pathToFile):
    with open(pathToFile, 'r') as graph:
        return json.load(graph)

def getNodes(obj):
    nodes = []
    for key in obj:
        nodes.append({
            'id' : "N"+obj[key]["id"],
            'label' : obj[key]["data"]["name"].split('.')[1].strip()
        })
    return nodes

def getEdges(obj):
    i = 0
    edges = []
    for key in obj:
        id = obj[key]['id']
        children = obj[key]["children"]
        for node in children:
            edges.append({
                'id' : "E"+ str(i),
                'source' : "N"+obj[key]['id'],
                'target' : "N"+node
            })
            i=i+1
    return edges

obj = fileToJson('graph.json')

with open('nodes.json', 'w') as nodes:
    json.dump(getNodes(obj), nodes, indent=4)


with open('edges.json', 'w') as edges:
    json.dump(getEdges(obj), edges, indent=4)


# print(getNodes(obj))

# print(getEdges(obj))