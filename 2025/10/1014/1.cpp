#include <iostream>
using namespace std;
int maxn = -1, minn = 1001;
int main() {
    int n;
    cin >> n;
    for(int i=1; i<=n; i++){
        int temp;
        cin >> temp;
        maxn = max(temp, maxn);
        minn = min(temp, minn);
    }
    cout << maxn - minn << endl;

    return 0;
}