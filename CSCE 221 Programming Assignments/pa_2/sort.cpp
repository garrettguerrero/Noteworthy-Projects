#include "lib/SortLib.h"
#include "lib/MergeSort.cpp"
#include "lib/BucketSort.cpp"
#include "lib/BubbleSort.cpp"
#include <iostream>
#include <string>
#include <fstream>
#include <chrono>

void sort(std::string algorithm, int* arr, int size) {
	for (int i = 0; i < algorithm.size(); i++) {
		algorithm[i] = std::tolower(algorithm[i]);
	}

	if (algorithm == "bubble") {
		SortLib::BubbleSort(arr, size);
	}

	if (algorithm == "merge") {
		SortLib::MergeSort(arr, size);
	}

	if (algorithm == "bucket") {
		SortLib::BucketSort(arr, size);
	}
}

int main(int argc, char* argv[]) {

	if (argc < 3) { // must have at least 3 arguments for ./sort -a <algorithm>
		std::cerr << "Usage: " << argv[0] << " -a <algorithm> [-i <infile> -o <outfile> -t]" << std::endl;
		return 1;
	}

	int size;
	int* arr;

	// check each argument and assign file/algorithm names
	bool a, i, o, t = false;
	std::string algorithm, infile, outfile;

	for (int j = 0; j < argc; j++) {
		std::string current_arg = argv[j];
		//std::cout << current_arg << std::endl;
		if (current_arg == "-a") {
			a = true;
			//std::cout << "a" << std::endl;
			algorithm = argv[j+1];
		}
		if (current_arg == "-i") {
			i = true;
			//std::cout << "i" << std::endl;
			infile = argv[j+1];
		}
		if (current_arg == "-o") {
			o = true;
			//std::cout << "o" << std::endl;
			outfile = argv[j+1];
		}
		if (current_arg == "-t"){
			t = true;
			//std::cout << "t" << std::endl;
		}
	}


	// Parse the arguments
	// You can assume if -a is present, so is the algorithm
	// And if -i is present, so is the filename, and so on


	// Read the input data
	if (i) {	// If a file was provided with -i, read from the file
		std::ifstream input(infile);
		if (input.is_open()) {

			input >> size;
			arr = new int[size];
			int j = 0;
			std::string line;

			while (input.good() && j < size)
				input >> arr[j++];
			input.close();

		} else { // if file does not exist, print an error message
			std::cerr << "Unable to open input file." << std::endl;
			return 1;
		}

	} else {	// Else, read from stdin (cin)

		std::cin >> size;
		arr = new int[size];

		for (int j = 0; j < size; j++) {
			std::cin >> arr[j];
		}
	}

	// Write the output data
	if (o && a) { // If a file was provided with -o, write to that file

		auto start = std::chrono::high_resolution_clock::now();
		sort(algorithm, arr, size);
		auto stop = std::chrono::high_resolution_clock::now();

		std::ofstream exit_file (outfile);
		if (exit_file.is_open()) {
			for (int j = 0; j < size - 1; j++) {
				exit_file << arr[j] << ' ';
			}
			exit_file << arr[size - 1] << std::endl;

			if (t) { // If -t was set, print the elapsed time as "Elapsed Time: <duration>"
				auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
				std::cout << "Elapsed Time: " << duration.count() << std::endl;
			}
			exit_file.close();

		} else { // if an error occurs during the process, print out an error message
			std::cerr << "Unable to open output file." << std::endl;
			return 1;
		}

	} else { // Else, write to stdout (cout)
		auto start = std::chrono::high_resolution_clock::now();
		sort(algorithm, arr, size);
		auto stop = std::chrono::high_resolution_clock::now();

		for (int j = 0; j < size - 1; j++) {
			std::cout << arr[j] << ' ';
		}
		std::cout << arr[size - 1] << std::endl;
		
		if (t) { // If -t was set, print the elapsed time as "Elapsed Time: <duration>"
			auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
			std::cout << "Elapsed Time: " << duration.count() << std::endl;
		}
	}


	// Cleanup; remember to delete your dynamic data array!
	if (arr != nullptr)
		delete[] arr;
	return 0;
}
