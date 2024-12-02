#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

bool isSafe(const std::vector<int>& levels) {
    bool isIncreasing = true;
    bool isDecreasing = true;

    for (size_t i = 1; i < levels.size(); ++i) {
        int diff = levels[i] - levels[i - 1];
        if (std::abs(diff) < 1 || std::abs(diff) > 3) {
            return false;
        }
        if (diff > 0) {
            isDecreasing = false;
        }
        if (diff < 0) {
            isIncreasing = false;
        }
    }

    return isIncreasing || isDecreasing;
}

int countSafeReports(const std::string& filename) {
    std::ifstream file(filename);
    std::string line;
    int countSafe = 0;

    while (std::getline(file, line)) {
        std::istringstream iss(line);
        std::vector<int> levels((std::istream_iterator<int>(iss)), std::istream_iterator<int>());
        if (isSafe(levels)) {
            ++countSafe;
        }
    }

    return countSafe;
}

int countSafeReportsWithDampener(const std::string& filename) {
    std::ifstream file(filename);
    std::string line;
    int countSafe = 0;

    while (std::getline(file, line)) {
        std::istringstream iss(line);
        std::vector<int> levels((std::istream_iterator<int>(iss)), std::istream_iterator<int>());

        if (isSafe(levels)) {
            ++countSafe;
            continue;
        }

        for (size_t i = 0; i < levels.size(); ++i) {
            std::vector<int> modifiedLevels = levels;
            modifiedLevels.erase(modifiedLevels.begin() + i);
            if (isSafe(modifiedLevels)) {
                ++countSafe;
                break;
            }
        }
    }

    return countSafe;
}

int main() {
    std::string filename = "input.txt";

    int part1Result = countSafeReports(filename);
    int part2Result = countSafeReportsWithDampener(filename);

    std::cout << "Part 1: Number of safe reports: " << part1Result << std::endl;
    std::cout << "Part 2: Number of safe reports (with Problem Dampener): " << part2Result << std::endl;

    return 0;
}
