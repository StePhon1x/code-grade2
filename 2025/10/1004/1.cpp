#include <iostream>
using namespace std;

int main()
{
    int n, s = 0;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        s += i;
    }
    cout << s << endl;

    return 0;
}

// 题目描述
// 计算 1+2+3+⋯+(n−1)+n 的值，其中正整数 n 不大于 100。由于你没有高斯聪明，所以你不被允许使用等差数列求和公式直接求出答案。

// 输入格式
// 输入一个正整数 n。

// 输出格式
// 输出一个正整数，表示最后求和的答案。