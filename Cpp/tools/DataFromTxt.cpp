#include "DataFromTxt.hpp"

#include <iostream>
#include <algorithm>
#include <vector>
#include <iterator>
#include <fstream>

using namespace std;

// Constructeur
DataFromTxt::DataFromTxt(string path) : m_path(path), m_data(vector<string>())
{
    ifstream fichier(m_path);
    
    istream_iterator<string> it(fichier);
    istream_iterator<string> fin;
    back_insert_iterator<vector<string> > it2(m_data);
    
    copy(it, fin, it2);
};

DataFromTxt::~DataFromTxt()
{
};

// Méthodes
vector<string> DataFromTxt::dataToVector(bool print)
{
    if(print)
    {
        copy(m_data.begin(), m_data.end(), ostream_iterator<string>(cout, "\n"));
    }
    return m_data;
};