#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Please input n (1<=n<=20): ";
    cin >> n;

    long long fact = 1;
    long long S = 0;

    for(int i=1;i<=n;i++){
        fact *= i;  // 计算 i!
        S += fact;  // 累加到总和
    }

    cout << S << endl;
    return 0;
}
