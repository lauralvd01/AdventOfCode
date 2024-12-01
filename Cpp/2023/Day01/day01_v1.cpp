#include <iostream>
#include <string>
#include <vector>

#include "../../../../tools/DataFromTxt.hpp"

using namespace std;

// Day 1 - Part 1 of Advent of Code 2023

int main()
{
    //string path = "D:/.Documents/AdventOfCode/Data/2023/day01_test1.txt";
    string path = "D:/.Documents/AdventOfCode/Data/2023/day01.txt";
    DataFromTxt data(path);
    vector<string> lines = data.readLines();

    string num("1234567890");

    int sum = 0;
    for (string line : lines)
    {
        size_t first_num = line.find_first_of(num);
        size_t last_num = line.find_last_of(num);
        sum += stoi(string {line[first_num],line[last_num]});
    }

    cout << "Result : " << sum << endl;
    // Result : 53194
}