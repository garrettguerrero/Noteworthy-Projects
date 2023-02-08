#include "Hash.h"

unsigned int Hash::PRH24(std::string s) {
  unsigned int p = 137;
  unsigned int m = 16777215;
  unsigned int hash = 0;

  unsigned int i = 0;
  unsigned int factor = 1;
  for (char c : s) {
    hash = (hash + (int(c) * factor)) % m;
    factor *= p;
    factor %= m;
    i++;
  }

  return hash;
}

// int main() {
//   std::cout << Hash::PRH24("this could be anything") << std::endl;
//   return 0;
// }
