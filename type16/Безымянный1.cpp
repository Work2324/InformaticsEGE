#include <iostream>
using namespace std;

int f(int n){
    if (n == 0){
       return (0);
    }
    if (n % 2 == 1){
       return (f(n - 1) + 1);
    }
    if (n > 0 and n % 2 == 0){
       return (f(n / 2));
    }
    


}
int main(){
    int t = 0;
    for (int i = 0; i < 1000000000; i++){
        if (f(i) == 2){
           t++;
        }
    }
    
cout << t;
system("pause");
return 0;
}
