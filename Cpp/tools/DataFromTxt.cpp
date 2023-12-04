#include "DataFromTxt.hpp"

#include <iostream>
#include <fstream>

using namespace std;

// Constructeur
DataFromTxt::DataFromTxt(string path) : m_path(path), m_data(vector<string>())
{
};

DataFromTxt::~DataFromTxt()
{
};

// Méthodes
string DataFromTxt::getPath() const
{
    return m_path;
};

vector<string> DataFromTxt::readLines(bool print)
{
    if(m_data.size() > 0)
    {
        return m_data;
    }
    else
    {
        ifstream data(m_path);
        if(data)
        {
            string line;
            while(getline(data, line))
            {
                m_data.push_back(line);
                if(print)
                {
                    cout << line << endl;
                }
            }
        }
        else
        {
            cerr << "ERROR: Can't open file." << endl;
        }

        return m_data;
    };
};
