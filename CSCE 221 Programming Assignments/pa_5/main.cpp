#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <fstream>
using namespace std;

#include "Graph.h"

int main(int argc, const char * argv[]) {
    cout << "Filename of graph to load: ";

    // TODO: next five code snippets
    // Snippet 1: read filename and open file
    string filename;
    cin >> filename;
    // Snippet 2: get number graph size
    ifstream file;
    file.open(filename);
    int verts, edges;
    file >> verts >> edges;
    //cout << verts << edges << endl;;

    int v1, v2;
    float weight;
    vector<int> v1s, v2s;
    vector<float> weights;
    for (int i = 0; i < edges; i++) {
      file >> v1 >> v2 >> weight;
      v1s.push_back(v1);
      v2s.push_back(v2);
      weights.push_back(weight);
    }

    int start, end;
    file >> start >> end;
    //cout << start << end << endl;

    file.close();

    // Snippet 3: create graph

    Graph g;

    for (int i : v1s) {
      g.insertVertex(i);
    }

    for (int i : v2s) {
      g.insertVertex(i);
    }

    // Snippet 4: read edges

    for (int i = 0; i < edges; i++) {
      g.insertEdge(v1s[i], v2s[i], weights[i]);
    }

    // Snippet 5: read start and end of path

    cout << "Shortest path from " << start << " to " << end << ":" << endl;

    vector<Vertex*> path;
    path = g.shortestPath(start, end);

    // TODO: call shortest path on your graph for the sstart and end verices and save result to path

    for (auto i : path) { // this is a for-each loop
        cout << i->label << " ";
    }
    // cout endline at very end
    cout << endl;



    return 0;
}
