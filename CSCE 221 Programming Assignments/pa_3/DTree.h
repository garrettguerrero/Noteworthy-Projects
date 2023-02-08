#ifndef DTREE_H
#define DTREE_H
#include "DNode.h"
#include "DecisionLogic.h"
#include "MaxHeap.h"
#include "Queue.h"

#include <string>

class DTree {
private:
  DNode* root;
  int maxDepth = 10;
  double delta = 0.000005;

public:

  DTree(): root(nullptr) {}

  void clear(DNode* node) {

    if (node -> left)
      clear(node -> left);
    if (node -> right)
      clear(node -> right);
    delete node;


  }

  ~DTree() {
    if (!root) {
      return;
    }

    clear(root);

  }

  Decision getMaxInformationGain(
    vector<string>& attributes,
    vector< vector<double> >& data,
    vector<int>& outcomes,
    vector<int>& instances) {

      MaxHeap<Decision> h;

      for (int i = 0; i < attributes.size(); i++) {
        h.insert(getInformationGain(attributes.at(i), data.at(i), outcomes, instances));
      }

      return h.nodes.at(0);
    }

  void recursiveTrain(
    DNode* node,
    DNode* parent,
    int depth,
    vector<string>& attributes,
    vector< vector<double> >& data,
    vector<int>& outcomes) {

      // if node does not exist, depth is greater than maxDepth, or the information gain is less than delta, exit
      if (!node) return;
      node -> parent = parent;

      if (depth > maxDepth) return;
      if ((node -> key).informationGain < delta) return;

      // set parent


      vector<int> above = (node -> key).instancesAbove;
      vector<int> below = (node -> key).instancesBelow;

      if (below.size() > 0) { // using instancesBelow of the current node as the instances value for the left node (as long as below has values)

        Decision left_to_be = getMaxInformationGain(attributes, data, outcomes, below);
        DNode* left = new DNode(left_to_be);

        node -> left = left;
        left -> depth = depth + 1;

        recursiveTrain(left, node, left -> depth, attributes, data, outcomes);

      }

      if (above.size() > 0) { // using instancesAbove of the current node as the instances value for the right node (as long as above has values)
        Decision right_to_be = getMaxInformationGain(attributes, data, outcomes, above);
        DNode* right = new DNode(right_to_be);

        node -> right = right;
        right -> depth = depth + 1;

        recursiveTrain(right, node, right -> depth, attributes, data, outcomes);
      }
  }

  void train(
    vector<string>& attributes,
    vector< vector<double> >& data,
    vector<int>& outcomes,
    vector<int>& instances) {

      Decision root_to_be = getMaxInformationGain(attributes, data, outcomes, instances);
      root = new DNode(root_to_be);
      recursiveTrain(root, nullptr, 0, attributes, data, outcomes);

  }

  int classify(
    vector<string>& attributes,
    vector<double>& data) {return 1;}

  bool isInternal(DNode* node) {
    if (!(node -> left) && !(node -> right)) {
      return false;
    } else {
      return true;
    }
  }

  string levelOrderTraversal() {
    Queue<DNode*> q = Queue<DNode*>();
    std::stringstream ss;
    DNode* u = root;
    q.push_back(u);

    std::cout << root -> left << std::endl;
    while(!q.empty()) {
      //std::cout << u -> key << std::endl;
      u = q.pop_front();
      ss << string(u->depth,'\t') << u->key;
      if (isInternal(u)) {
        if (u -> left) {
          //std::cout << u -> left -> key << std::endl;
          q.push_back(u -> left);
        }
        if (u -> right){
          //std::cout << u -> left -> key << std::endl;
          q.push_back(u -> right);
        }
      }
    }
    return ss.str();
  }

};

#endif
