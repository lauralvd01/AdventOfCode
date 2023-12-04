#include <iostream>
#include <string>
#include <vector>

#include "../../tools/DataFromTxt.hpp"

using namespace std;

// Day 1 - Part 2 of Advent of Code 2023

int main()
{
    string path = "D:/.Documents/AdventOfCode/Data/day01_test2.txt";
    //string path = "D:/.Documents/AdventOfCode/Data/day01.txt";
    DataFromTxt data(path);
    vector<string> lines = data.readLines(true);

    string cifers[10] = {"zero","one","two","tree","four","five","six","seven","eight","nine"};
    string num("1234567890");

    int sum = 0;
    for (string line : lines)
    {
        size_t first_num = line.find_first_of(num);
        size_t first_cif(line.size()+1);
        string first_number;
        for (int j(0); j<10; ++j)
        {
            size_t i = line.find(cifers[j]);
            if(i != string::npos)
            {
                first_cif = min(first_cif,i);
                first_number = to_string(j);
            }
        }
        if(first_num < first_cif)
        {
            first_number = line[first_num];
        }

        size_t last_num = line.find_last_of(num);
        size_t last_cif(0);
        string last_number;
        for (int j(0); j<10;++j)
        {
            size_t i = line.rfind(cifers[j]);
            if(i != string::npos)
            {
                first_cif = max(first_cif,i);
                last_number = to_string(j);
            }
        }
        if(last_num > last_cif)
        {
            last_number = line[last_num];
        }
        cout << first_number << last_number << endl;
        sum += stoi(first_number+last_number);
    }

    cout << "Result : " << sum << endl;
    // Result : 54249
}