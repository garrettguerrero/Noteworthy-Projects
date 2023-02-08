#include <iostream>
#include <sstream>
#include "DoublyLinkedList.h"
#include "DNode.h"

template <typename T>
DoublyLinkedList<T>::DoublyLinkedList() : head(nullptr), tail(nullptr), length(0) {}

template <typename T>
DoublyLinkedList<T>::~DoublyLinkedList() {

  Node<T>* current_node = head;

  if (current_node == nullptr) {return;}

  // delete and reallocate first node until the end of the list
  while (current_node != nullptr) {
    // create a copy of the current node
    Node<T>* temp = current_node;
    // iterate
    current_node = current_node -> next;
    // sever copy from the list and delete
    temp -> next = nullptr;
    delete temp;
    // change head
    head = current_node;

  }
  delete head;
}

// copy constructor
template <typename T>
DoublyLinkedList<T>::DoublyLinkedList(const DoublyLinkedList<T>& other) {

  head = nullptr;
  tail = nullptr;
  length = 0;

  int index = 0;
  Node<T>* current_node = other.head;

  // take info from old list and insert them into a new one
  while (current_node != nullptr) {
    // insert takes care of the head and tail
    insert(current_node -> data, index);
    current_node = current_node -> next;
    index++;
    //std::cout << "head: " << (head -> data).data << " tail: " << (tail -> data).data << std::endl;
  }
}

// copy assignment
template <typename T>
DoublyLinkedList<T>& DoublyLinkedList<T>::operator=(const DoublyLinkedList<T>& other) {

  if (this == &other) {
    return *this;
  }

  head = nullptr;
  tail = nullptr;
  length = 0;

  int index = 0;
  Node<T>* current_node = other.head;

  // take info from old list and insert them into a new one
  while (current_node != nullptr) {
    // insert takes care of the head and tail
    insert(current_node -> data, index);
    current_node = current_node -> next;
    index++;
    //std::cout << "head: " << (head -> data).data << " tail: " << (tail -> data).data << std::endl;
  }

  // return the list so it can be assigned
  return *this;

}

template <typename T>
void DoublyLinkedList<T>::insert(T data, int index) {

  // if the index is out of range, throw an error
  if (index > length || index < 0) {
    throw std::out_of_range("index outside of bounds");
  }

  // create a new node
  Node<T>* to_insert = new Node<T>(data);
  //std::cout << "to_insert address: " << &to_insert << std::endl;

  // if no items in list, put it at the front
  if (length == 0) {
    std::cout << "adding to empty list" << std::endl;
    head = to_insert;
    tail = to_insert;
    tail -> next = nullptr;
    length++;
    return;
  }

  // iterate through the list until the node prior to the desired index is found
  Node<T>* current_node = head;
  for (int i = 0; i < index - 1; i++) {
    current_node = current_node -> next;
  }

  // assign pointers as needed
  //// beginning of list
  if (index == 0) {
    std::cout << "adding to beginning of list" << std::endl;
    to_insert -> next = head;
    head = to_insert;
    if (length == 1) {
      head -> next = tail;
      tail -> prev = head;
    }
    length++;
  }
  //// end of list
  else if (index == length) {
    std::cout << "adding to end of list" << std::endl;
    to_insert -> prev = current_node;
    current_node -> next = to_insert;
    tail = to_insert;
    tail -> next = nullptr;
    length++;
  }

  //// middle of list
  else {
    std::cout << "adding to middle of list" << std::endl;
    to_insert -> next = current_node -> next;
    to_insert -> prev = current_node;
    (current_node -> next) -> prev = to_insert;
    current_node -> next = to_insert;
    length++;
  }

}

template <typename T>
T DoublyLinkedList<T>::remove(int index) {

  Node<T>* current_node = head;
  T data_to_return;

  // catch indexing errors
  if (current_node == nullptr || index >= length || index < 0) {
    throw std::out_of_range("index outside of list bounds");
  }

  // if only one element, make head and tail null
  if (length == 1) {
    data_to_return = current_node -> data;

    head = nullptr;
    tail = nullptr;

    std::cout << "removing lone element" << std::endl;
    delete current_node;
    length--;
    return data_to_return;
  }

  // if at the front, change head and remove node
  if (index == 0) {
    data_to_return = current_node -> data;

    head = current_node -> next;
    current_node -> next = nullptr;

    std::cout << "removing from front" << std::endl;
    delete current_node;
    length--;
    if (length == 1) {
      tail = head;
      head -> next = nullptr;
      head -> prev = nullptr;
    }
    return data_to_return;
  }

  // if at the tail, change tail and remove node
  if (index == length - 1) {
    //std::cout << "length: " << length << " index: " << index << std::endl;
    //std::cout << "tail = " << (tail -> data).data << std::endl;
    data_to_return = tail -> data;
    tail = tail -> prev;
    //std::cout << (tail -> data).data << std::endl;
    delete tail -> next;
    tail -> next = nullptr;
    length--;
    std::cout << "removing from end" << std::endl;
    return data_to_return;
  }

  // if somewehere else, iterate through the list until the index in question
  for (int i = 0; i < index; i++) {
    current_node = current_node -> next;
  }

  // reassign surrounding pointers and delete node from list
  //// the next node's 'prev' gets the current node's 'prev'
  (current_node -> prev) -> next = current_node -> next;
  //// the previous node's 'next' gets the current node's 'next'
  (current_node -> next) -> prev = current_node -> prev;
  //// sever node from the list and delete
  current_node -> next = nullptr;
  current_node -> prev = nullptr;
  data_to_return = current_node -> data;
  std::cout << "removing from middle" << std::endl;
  delete current_node;
  //// update length
  length--;
  return data_to_return;
}

template <typename T>
std::string DoublyLinkedList<T>::toString() {
  std::stringstream node_info;

  Node<T>* current_node = head;
  while (current_node != nullptr) {
    node_info << current_node -> data << ' ';

    current_node = current_node -> next;
  }

  return node_info.str();
}

template class DoublyLinkedList<int>;
template class DoublyLinkedList<DNode*>;
