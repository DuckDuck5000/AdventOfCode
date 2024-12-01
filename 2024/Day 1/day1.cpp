#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <cmath>
#include <string>


using namespace std;

pair<int, int> process_file(const string& filename) {
    priority_queue<int, vector<int>, greater<int>> heap1, heap2;
    int total_distance = 0;
    unordered_map<int, int> freqMap;
    vector<int> nums;
    int final_num = 0;

    try {
        ifstream file(filename);
        if (!file.is_open()) {
            cerr << "File '" << filename << "' not found." << endl;
            return {0, 0};
        }

        string line;
        while (getline(file, line)) {
            stringstream ss(line);
            int part1, part2;

            if (ss >> part1 >> part2) {
                heap1.push(part1);
                heap2.push(part2);

                freqMap[part2]++;
                nums.push_back(part1);
            } else {
                cerr << "Skipping invalid line: " << line << endl;
            }
        }

        // Part 1
        while (!heap1.empty() && !heap2.empty()) {
            total_distance += abs(heap1.top() - heap2.top());
            heap1.pop();
            heap2.pop();
        }

        // Part 2
        for (int num : nums) {
            if (freqMap.find(num) != freqMap.end()) {
                final_num += num * freqMap[num];
            }
        }

        return {total_distance, final_num};

    } catch (const exception& e) {
        cerr << "An unexpected error occurred: " << e.what() << endl;
        return {0, 0};
    }
}

int main() {
    string filename = "input_day1.txt";
    auto [distance, final] = process_file(filename);

    if (distance != 0 || final != 0) {
        cout << "Part 1: Total Distance: " << distance << endl;
        cout << "Part 2: Final Number: " << final << endl;
    }

    return 0;
}
