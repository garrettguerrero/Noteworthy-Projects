#include "ChainingHashTable.h"
#include "Hash.h"
#include <fstream>

unsigned int ChainingHashTable::hash(std::string key) { // return the hash within the scope of the capacity

  return Hash::PRH24(key) % capacity;

}

void ChainingHashTable::insert(std::string key, int val) { // insert a word with a given value

  unsigned int h = hash(key);

  if (table[h][0].key == "") { // if the first element at the hash position is empty, add in a new cell
    table[h][0] = Cell<std::string, int>(key, val);
    return;
  }

  for (int i = 0; i < table[h].size(); i++) { // else, loop through the list and see if the key already exists within the list
    if (table[h][i].key == key) {
      table[h][i].value++;
      return;
    }
  }

  table[h].push_back(Cell<std::string, int>(key, val)); // otherwise, insert it at the back of the list

}

int ChainingHashTable::remove(std::string key) { // find the key and remove it

  unsigned int h = hash(key);
  int to_return;

  for (int i = 0; i < table[h].size(); i++) { // loop through the list at hash
    if (table[h][i].key == key) { // if the key is found, remove the cell and return its value
      to_return = table[h][i].value;
      table[h][i] = Cell<std::string, int>();
      return to_return;
    }
  }

  throw std::runtime_error("string not in table"); // if the word is not found, throw an exception

}

int ChainingHashTable::get(std::string key) { // obtain the value of a given word

  unsigned int h = hash(key);

  for (Cell<std::string, int> c : table[h]) { // iterate through the cells at hash
    if (c.key == key) { // return value if key is found
      return c.value;
    }
  }
  return 0;
}

void ChainingHashTable::printAll(std::string filename) { // print all values in table where key is not equal to empty string
  std::ofstream file;
  file.open(filename);
  if (file.is_open()) {
    for (std::vector<Cell<std::string, int>> v : table) {
      for (Cell<std::string, int> c : v) {
        if (c.key != "") file << c.key << " " << c.value << std::endl;
      }
    }
  }
}
