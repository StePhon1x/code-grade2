#include <iostream>
using namespace std;

int reverseNumber(int n)
{
    int rev = 0;
    while(n!=0){
    int digit = n % 10;
    rev = rev * 10 + digit;
    n = n/10;
    }
    return rev;
}

int main()
{
    int N;
    cin >> N;
    int rel = reverseNumber(N);
    cout << rel << endl;

    return 0;
}