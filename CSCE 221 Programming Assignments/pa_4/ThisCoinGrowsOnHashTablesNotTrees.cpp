#include "Block.h"
#include "Hash.cpp"

std::string mining(std::string transaction, Block* b, char c) {
  std::string contents = transaction + b -> get_prev_hash() + b -> nonce;
  while (!validate_hash(Hash::PRH24(contents))) { // loop until a valid hash is produced
    contents += c;
  }
  return std::to_string(Hash::PRH24(contents));
}

int main() {
  Block* tail = nullptr;

  std::string line;
  std::getline(std::cin, line);

  while (line != "") { // loop until nothing is received from console
    tail = new Block(line, tail);
    char c = '0';
    std::string to_nonce = mining(line, tail, c);
    while (!(tail -> sign_block(to_nonce))) { // try nonces until new block can be signed
      to_nonce = mining(line, tail, c);
      c++;
    }
    std::getline(std::cin, line);
  }

  Block* curr = tail;
  Block* temp;
  while (curr != nullptr) { // ~ThisCoinGrowsOnHashTablesNotTrees()
    std::cout << *curr;
    temp = curr -> get_prev();
    delete curr;
    curr = temp;
  }
}
