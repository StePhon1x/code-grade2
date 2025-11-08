#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    if (N % 52 != 0) { // 判断是否能整除52
        cout << "No solution" << endl;
        return 0;
    }

    int target = N / 52; // 7*X + 21*K = N/52

    for (int X = 100; X >= 1; X--) {
        if ((target - 7 * X) % 21 == 0) { // 确保 K 是整数
            int K = (target - 7 * X) / 21;
            if (K > 0) { // 确保 K 是正整数
                cout << X << endl << K << endl;
                return 0;
            }
        }
    }

    cout << "No solution" << endl;
    return 0;
}
