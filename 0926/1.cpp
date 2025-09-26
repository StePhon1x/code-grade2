#include <iostream>
using namespace std;
int n;
int main() {
    cin >> n;
    int a[n+1], mina;
    for(int i=0; i<n; i++){
        cin >> a[i];
    }
    mina = a[0];
    for(int i=0; i<n; i++){
        if(a[i] < mina){
            mina = a[i];
        }
    }
    cout << mina << endl;

    return 0;
}
