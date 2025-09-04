#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int m, t, s;
    cin >> m >> t >> s;

    if (t == 0) {
        cout << 0 << endl;
        return 0;
    }

    int eaten = min(m, (int)ceil((double)s / t));
    cout << m - eaten << endl;

    return 0;
}


// 小 B 喜欢吃苹果。她现在有 m（1≤m≤100）个苹果，吃完一个苹果需要花费 t（0≤t≤100）分钟，吃完一个后立刻开始吃下一个。现在时间过去了 s（1≤s≤10000）分钟，请问她还有几个完整的苹果？

// 输入格式
// 输入三个非负整数表示 m,t,s。

// 输出格式
// 输出一个整数表示答案。