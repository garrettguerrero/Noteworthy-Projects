
probing: ProbingHashTable.o runner_probing.o Hash.o
	g++ -std=c++17 ProbingHashTable.cpp runner_probing.cpp Hash.cpp -o probing

chaining: ChainingHashTable.o runner_chaining.o Hash.o
	g++ -std=c++17 ChainingHashTable.cpp runner_chaining.cpp Hash.cpp -o chaining

ThisCoinGrowsOnHashTablesNotTrees: ThisCoinGrowsOnHashTablesNotTrees.o
	g++ -std=c++17 ThisCoinGrowsOnHashTablesNotTrees.cpp -o ThisCoinGrowsOnHashTablesNotTrees

clean:
	rm *.o probing chaining
