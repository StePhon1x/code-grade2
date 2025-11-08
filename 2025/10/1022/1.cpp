// 题目描述
// 已知正整数 n 是两个不同的质数的乘积，试求出两者中较大的那个质数。

// 输入格式
// 输入一个正整数 n。

// 输出格式
// 输出一个正整数 p，即较大的那个质数。

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n;
    cin >> n;
    for (int i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
        {
            cout << n / i << endl;
            break;
        }
    }

    return 0;
}


