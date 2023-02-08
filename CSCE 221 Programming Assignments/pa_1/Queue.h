#include <iostream>
#include <sstream>
#include "DoublyLinkedList.h"

class Queue {
public:
  Node* back;
  Node* front;
  int length;

  // constructor
  Queue() : back(nullptr), front(nullptr), length(0) {}

  // destructor
  ~Queue() {
    int temp = length;
    for (int i = 0; i < temp; i++) {
      std::cout << "Popping: " << pop_front().data << std::endl;
    }
  }

  // copy constructor
  Queue(const Queue& other) {}

  bool empty() {
    if (length == 0)
      return true;
    else
      return false;
  }

  void push_back(NetworkPacket data) {
    Node* to_insert = new Node(data);

    if (back == nullptr && length == 0) {
      back = to_insert;
      front = to_insert;
      length++;
      return;
    }

    to_insert -> prev = back;
    back = to_insert;
    (back -> prev) -> next = back;
    length++;

  }


  NetworkPacket pop_front() {
    if (front == nullptr) {
      throw std::out_of_range("index outside of list bounds");
    }

    NetworkPacket data_to_return = front -> data;

    if (length == 1) {
      delete front;
      front = nullptr;
      back = nullptr;
      length--;
      return data_to_return;
    }

    Node* temp = front;
    front = front -> next;
    delete temp;
    length--;
    return data_to_return;

  }

  std::string toString() {
    std::stringstream node_info;

    Node* current_node = front;
    while (current_node != nullptr) {
      node_info << "SRC: " << (current_node -> data).source <<
      ", DST: " << (current_node -> data).destination <<
      ", CKS: " << (current_node -> data).checksum <<
      ", Data: " << (current_node -> data).data << "\n ";

      current_node = current_node -> next;
    }

    return node_info.str();
  }


};
