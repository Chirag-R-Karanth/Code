#include "iostream"
#include <math.h>
using namespace std;

class Rps
{
    //private: int rock,paper,scissors;

    public:
        int choice();
};

int Rps::choice()
{
    int choice;
    cin >> choice;
    return choice;
}

int main()
{
    int rock = 1;
    int paper = 2;
    int scissors = 3;
    Rps game;
    int choice = game.choice();
    int result = math.random();
}
