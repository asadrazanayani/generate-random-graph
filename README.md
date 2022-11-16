# Generate random DAG in JSON

> Generates a random directed acyclic graph and serializes it in JSON

## Installation

1. `git clone https://gist.github.com/flekschas/0ea70dec4d92bc706e61 random-graph-json && cd random-graph-json`
2. `mkvirtualenv -a $(pwd) random-graph-json` [Optional but recommended]
3. `pip install -r requirements.txt`

## Usage
### Generating graph.json
```bash
$ ./generate-graph.py -n 1000 -p 0.005 -o ./graph.json
```

You don't like male first names? Just add `-f` or `--female` and you get female
random first names.

**Parameters:**

- `-n` or `--nodes`: Number of nodes to be generated. [Int]
- `-p` pr `--probability`: Probability to create an edge. between two nodes. [Float, 0-1]
- `-f` or `--female`: Use female random first names instead of male first names to name nodes.

### Generating Edges and Nodes
```bash
$ python3 generate_nodes_edges.py
```