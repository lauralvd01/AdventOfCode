#ifndef DATA_FROM_TXT_HPP
#define DATA_FROM_TXT_HPP

#include <string>
#include <vector>

class DataFromTxt
{
private:
    std::string m_path;
    std::vector<std::string> m_data;

public:
    DataFromTxt(std::string path);
    ~DataFromTxt();

    std::string getPath() const;
    std::vector<std::string> readLines(bool print=false);
};

#endif // DATA_FROM_TXT_HPP