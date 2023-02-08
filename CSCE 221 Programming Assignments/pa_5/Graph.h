#ifndef GRAPH_H
#define GRAPH_H

#include "LocatorHeap.h"
#include <iostream>

#include <vector>
#include <map>
using std::map;
using std::vector;

class Edge;

class Vertex
{
public:
    int label;
    vector<Edge*> edges;

    // helpers stored inside a vertex to help with path finding
    // you can use different auxilliary structures if desired
    bool visited;
    float distanceTo;
    vector<Vertex*> pathTo;
    Heap<Vertex*>::Locator locator;
    bool operator < ( const Vertex &v ) const
    {
        return (this -> distanceTo < v.distanceTo);
    }

    Vertex ( int l ) : label (l) { }
};

class Edge
{
public:
    Vertex *v1, *v2;
    float weight;

    Edge ( Vertex *nv1, Vertex *nv2, float newWeight ) : v1 ( nv1 ), v2 ( nv2 ), weight ( newWeight ) { }
};


class Graph
{
protected:
    vector<Edge*> edges;
    vector<Vertex*> vertices;

    map<int, Vertex*> vertexMap;

public:
    Graph () {}

    ~Graph ()
    {
        clear_graph();
    }

    Graph (const Graph& other) {
      copy_graph(other);
    }

    Graph& operator=(const Graph& other) {
      copy_graph(other);
      return *this;
    }

    void copy_graph(const Graph& other) {
      clear_graph();
      for (Vertex* i : other.vertices) insertVertex(i -> label);
      for (Edge* i : other.edges) insertEdge(i -> v1 -> label, i -> v2 -> label, i -> weight);
    }

    void clear_graph() { // clears edges and vertices
      for (Edge* i : edges) {
        if (i) delete i;
      }
      edges.clear();

      for (Vertex* i : vertices) {
        if (i) delete i;
      }
      vertices.clear();

      vertexMap.clear();
    }

    void insertVertex ( int label )
    {
        //std::cout << "inserting " << label << std::endl;
        if (find_vertex(label)) return;
        Vertex* to_insert = new Vertex(label);
        vertexMap[label] = to_insert;
        vertices.push_back(to_insert);
    }

    Vertex* find_vertex(int label) { // helper for getting address of vertices
      return vertexMap[label];
      return nullptr;
    }

    void insertEdge ( int l1, int l2, float weight )
    {
        Vertex* v1 = find_vertex(l1);
        Vertex* v2 = find_vertex(l2);
        Edge* to_insert = new Edge(v1, v2, weight);
        edges.push_back(to_insert);
        v1 -> edges.push_back(to_insert);
        v2 -> edges.push_back(to_insert);
    }

    vector<Vertex*> shortestPath ( int start, int end )
    {
        Vertex* start_node = find_vertex(start);
        Vertex* end_node = find_vertex(end);
        if (!start_node || !end_node) return {};

        // step 1
        for (Vertex* v : vertices) {
          v -> visited = false;
          (v -> pathTo).clear();
          v -> distanceTo = std::numeric_limits<float>::max();
        }

        // step 2
        Vertex* curr = start_node;
        (curr -> pathTo).push_back(curr);
        curr -> distanceTo = 0;

        // step 3
        Heap<Vertex*> h;
        for (Vertex* v : vertices) v -> locator = h.insertElement(v);

        vector<Vertex*> to_return;
        while (!(end_node -> visited)) {
          // step 4
          curr = h.removeMin();

          for (Edge* e : curr -> edges) {
            Vertex* u;
            if (e -> v1 == curr) u = e -> v2;
            else u = e -> v1;

            if (u -> distanceTo > curr -> distanceTo + e -> weight) {
              u -> distanceTo = curr -> distanceTo + e -> weight;
              h.update(u -> locator);
              u -> pathTo = (curr -> pathTo);
              (u -> pathTo).push_back(u);
            }
          }
          //h.update(curr -> locator);
          // step 5
          to_return.push_back(curr);
          curr -> visited = true;
        }
        return curr -> pathTo;
    }
};

#endif
