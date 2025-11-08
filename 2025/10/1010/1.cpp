#include <iostream>
using namespace std;

int reverseNumber(int n)
{
    int rev = 0;
    while (n != 0)
    {
        int digit = n % 10;
        rev = rev * 10 + digit;
        n = n / 10;
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

// 题目描述
// 给定一个整数 N，请将该数各个位上数字反转得到一个新数。新数也应满足整数的常见形式，即除非给定的原数为零，否则反转后得到的新数的最高位数字不应为零（参见样例 2）。

// 输入格式
// 一个整数 N。

// 输出格式
// 一个整数，表示反转后的新数。