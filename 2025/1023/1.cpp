// 题目描述
// 模仿例题，打印出不同方向的正方形，然后打印三角形矩阵。中间有个空行。

// 输入格式
// 输入矩阵的规模，不超过 9。

// 输出格式
// 输出矩形和三角形

// 输入输出样例
// 输入
// 4

// 输出
// 01020304
// 05060708
// 09101112
// 13141516

//       01
//     0203
//   040506
// 07080910

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int n;
    cin >> n;

    // 打印矩形方阵
    for (int i = 0, x = 1; i < n; i++)
    {
        for (int j = 0; j < n; j++, x++)
        {
            cout << setfill('0') << setw(2) << x;
        }
        cout << endl;
    }

    cout << endl;

    // 打印靠右三角形
    for (int i = 1, x = 1; i <= n; i++)
    {
        cout << string(2 * (n - i), ' ');
        for (int j = 0; j < i; j++, x++)
        {
            cout << setfill('0') << setw(2) << x;
        }
        cout << endl;
    }

    return 0;
}