#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n, k;
    int st=0, sf=0, nt=0, nf=0;
    cin >> n >> k;
    int a[n+1];
    for(int i=1; i<n+1; i++){
        a[i - 1] = i;
        if(a[i - 1] % k == 0){
            st+=a[i - 1];
            nt++;
        }
        else{
            sf+=a[i - 1];
            nf++;
        }
    }
    cout <<fixed <<setprecision(1) 
        << 1.0*st/nt << " " 
        << 1.0*sf/nf << endl;


    return 0;
}