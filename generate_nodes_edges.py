import json

def fileToJson(pathToFile):
    with open(pathToFile, 'r') as graph:
        return json.load(graph)

def getNodes(obj):
    nodes = []
    for key in obj:
        nodes.append({
            'id' : obj[key]["id"],
            'label' : obj[key]["data"]["name"].split('.')[1].strip()
        })
    return nodes

def getEdges(obj):
    edges = []
    for key in obj:
        id = obj[key]['id']
        children = obj[key]["children"]
        for node in children:
            edges.append({
                'id' : id,
                'source' : obj[key]['id'],
                'target' : node
            })
    return edges

obj = fileToJson('graph.json')

with open('nodes.js', 'w') as nodes:
    json.dump(getNodes(obj), nodes, indent=4)


with open('edges.js', 'w') as edges:
    json.dump(getEdges(obj), edges, indent=4)


# print(getNodes(obj))

# print(getEdges(obj))