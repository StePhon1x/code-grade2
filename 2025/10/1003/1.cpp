#include <iostream>
using namespace std;

int main() {
    int k, b = 0, s = 0, a = 0;
    cin >> k;
    int i = 1;
    while (s <= k) {
        s += i;
        a += i * i;
        i++;
    }
    cout << a - (i-1)*(s-k)  << endl;
    return 0;
}
