#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>
#include <fstream>

#include "../../../../tools/DataFromTxt.hpp"

using namespace std;

// Day 1 - Part 2 of Advent of Code 2023

int main()
{
    string path = "D:/.Documents/AdventOfCode/Data/2023/day01_test2.txt";
    //string path = "D:/.Documents/AdventOfCode/Data/2023/day01.txt";
    DataFromTxt data(path);
    vector<string> lines = data.dataToVector(true);

    string cifers[10] = {"zero","one","two","tree","four","five","six","seven","eight","nine"};
    string num("0123456789");

    int sum = 0;
    for (string line : lines)
    {
        string first;
        size_t first_it = string::npos;
        int i(0);
        while (first_it == string::npos && i<10)
        {
            size_t it = line.find(cifers[i]);
            if(it != string::npos && it < first_it)
            {
                first_it = it;
                break;
            }
            ++i;
        }
        size_t it = line.find_first_of(num);
        if( first_it < it)
        {
            first = to_string(i);
        }
        else
        {
            first = line[it];
        }

        string last;
        size_t last_it = string::npos;
        i = 0;
        while (last_it == string::npos && i<10)
        {
            size_t it = line.rfind(cifers[i]);
            if(last_it > it)
            {
                last_it = it;
                break;
            }
            ++i;
        }
        it = line.find_last_of(num);
        if(last_it > it)
        {
            last = to_string(i);
        }
        else
        {
            last = line[it];
        }
        
        cout << first << " " << last << endl;

    /*
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
    */
        sum += stoi(first+last);
    }

    cout << "Result : " << sum << endl;
    // Result : 54249
}
