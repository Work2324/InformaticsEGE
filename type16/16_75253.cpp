#include <iostream>
#include <cmath>
using namespace std;

int f(int n){
	if(n == 0){
	return 0;
	}
	if ((n > 0) and (n % 4) < 2){
		return f(n / 4)+ n % 4;
	}
	if((n > 0) and (n % 4) >= 2){
		return f(n / 4) + n % 4 -1;
	}
}

int main(){
	
	for(int i = 1000;i <= 10000000000; i++){
		if (f(i) == 27 and f(i+1) == 16){
			cout << i;
			break;
		}
	}
	
	system("pause");
	return 0;
}

//изи катка, но решение для затупков
