#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int n)
{
    if (n < 2)
        return 0;
    if (n == 2)
        return 1;
    if (n % 2 == 0)
        return 0;

    // 找n是否在(2，√n]之间有因数 有即不是质数
    for (int i = 3; i <= sqrt(n); i+=2)
    {
        if (n % i == 0)
            return 0;
    }
    return 1;
}
int top, a[1000050], s, ts;
int main()
{
    int L;
    cin >> L;
    a[++top] = 2;
    for (int i = 3; i < 1000000; i += 2)
    {
        if (isPrime(i))
        {
            a[++top] = i;
        }
    }
    for (int i = 1; i <= top; i++)
    {
        s += a[i];
        if (s > L)
            break;
        ts++;
    }
    for (int i = 1; i <= ts; i++)
    {
        cout << a[i] << endl;
    }
    cout << ts;
    return 0;
}

// 题目描述
// 小 A 有一个质数口袋，里面可以装各个质数。他从 2 开始，依次判断各个自然数是不是质数，如果是质数就会把这个数字装入口袋。

// 口袋的负载量就是口袋里的所有数字之和。

// 但是口袋的承重量有限，装的质数的和不能超过 L。给出 L，请问口袋里能装下几个质数？将这些质数从小往大输出，然后输出最多能装下的质数的个数，数字之间用换行隔开。

// 输入格式
// 一行一个正整数 L。

// 输出格式
// 将这些质数从小往大输出，然后输出最多能装下的质数个数。