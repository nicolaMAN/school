#include<iostream>
#include<list>
#include<iterator>
using namespace std;
class Num{
public:
    list<int> array;
    Num(){}
    Num& operator+=(const int n)
    {
        this->array.push_back(n);
        return *this;
    }
    Num& operator-=(int)
    {
        this->array.pop_front();
        return *this;
    }
    Num operator+(const int n)
    {
        list<int> newarray;
        newarray = array;
        newarray.push_back(n);
        this->array = newarray;
        return *this;
    }
    Num operator-(int)
    {
        list<int> newarray;
        newarray = array;
        newarray.pop_front();
        this->array = newarray;
        return *this;
    }
    Num operator*(int)
    {
        this->array.begin();
        return *this;
    }
    Num operator[](const int n)
    {
        list<int>::iterator it;
        return advance((it*), n);
    }
};
int main()
{

}