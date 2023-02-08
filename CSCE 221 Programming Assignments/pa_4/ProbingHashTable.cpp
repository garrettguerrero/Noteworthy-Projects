#include "ProbingHashTable.h"
#include "Hash.h"
#include <fstream>

unsigned int ProbingHashTable::hash(std::string key) {  // get hash in scope of capacity
  return Hash::PRH24(key) % capacity;
}

void ProbingHashTable::insert(std::string key, int val) { // add in a new cell with number of words present

  unsigned int h = hash(key) % capacity;

  for (int i = h; i < capacity; i++) { // loop through last half of list
    if (table[i].key == "") { // if a spot is empty, update cell values
      table[i] = Cell<std::string, int>(key, val);
      size++;
      return;
    } else if (table[i].key == key) { // if they key is already in the list, update value of that key
      table[i].value++;
      return;
    }
  }

  for (int i = 0; i < h; i++) { // loop through first half of list and repeat
    if (table[i].key == "") {
      table[i] = Cell<std::string, int>(key, val);
      size++;
      return;
    } else if (table[i].key == key) {
      table[i].value++;
      return;
    }
  }
}

int ProbingHashTable::remove(std::string key) { // remove a cell from the list

  unsigned int h = hash(key) % capacity;
  int to_return;

  for (int i = h; i < capacity; i++) { // loop though last half of list
    if (table[i].key == key) { // if the key exists, return it
      to_return = table[i].value;
      table[i] = Cell<std::string, int>();
      size--;
      return to_return;
    }
    else if (table[i].key == "") throw std::runtime_error("word not in list"); // if an empty string is happened upon, the word does not exist
  }

  for (int i = 0; i < h; i++) { // loop through first half of list and repeat
    if (table[i].key == key) {
      to_return = table[i].value;
      table[i] = Cell<std::string, int>();
      size--;
      return to_return;
    }
    else if (table[i].key == "") throw std::runtime_error("word not in list");
  }

  throw std::runtime_error("word not in list"); // if nothing is found in either half of the list, the word does not exist
}


int ProbingHashTable::get(std::string key) { // obtain value given a key
  unsigned int h = hash(key) % capacity;

  for (int i = h; i < capacity; i++) { // loop through second half of list
    if (table[i].key == key) return table[i].value; // if the key is found, return its value
    else if (table[i].key == "") return 0; // else, if a space is found, the word is not in the list
  }

  for (int i = 0; i < h; i++) { // loop through first half of list and repeat
    if (table[i].key == key) return table[i].value;
    else if (table[i].key == "") return 0;
  }
  return 0; // if nothing is found in the entire list, return 0
}

void ProbingHashTable::printAll(std::string filename) { // print values of each cell whose key is not an empty string to a file
  std::ofstream file;
  file.open (filename);
  if (file.is_open()) {
    for (Cell<std::string, int> c : table) {
      if (c.key != "") file << c.key << " " << c.value << std::endl;
    }
  }
  file.close();
}
