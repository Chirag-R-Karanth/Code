#include <iostream>
using namespace std;

class stack
{
    private : int stack_array[1000], limit, top;

    public : 
            void push();
            void pop();
            void peek();
};

stack::stack()
{
    top = -1;
}

void stack::push()
{
    if(top == limit)
    cout<<"Please enter limit:";
    cin>>limit;
    for(int i=0; i<limit; i++)
    {
        cin>>stack_array[i];
    }
}

void stack::peek()
{
    
}

int main()
{
    stack s;
    int num;
    cin>>num;
    while(1)
    {
        switch(num)
        {
            case 1:
                s.push();
                break;
        }
    }
    
}