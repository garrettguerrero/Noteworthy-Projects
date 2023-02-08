#ifndef DNODE_H
#define DNODE_H

#include "DecisionLogic.h"

class DNode {
public:

  DNode() : parent(nullptr), left(nullptr), right(nullptr), depth(0) {}
  DNode(Decision k) : key(k), parent(nullptr), left(nullptr), right(nullptr), depth(0) {}

  Decision key;
  int depth;

  DNode* parent;
  DNode* left;
  DNode* right;

};

#endif
