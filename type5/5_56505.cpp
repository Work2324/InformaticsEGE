#include <iostream>
#include <string.h>
#include <cstdlib>
using namespace std;

int por(int n){
	int t = 0;
	while (n > 0){
		n = n / 10;
		t ++;
		}
		
	return t;
}
int f(int n){
	int ln = por(n);
	char s[ln];
	itoa(n, s, 10);
	int sm = 0;
	for (int i = 0;i < ln; i++){
		sm += int(s[i]);
	}
	if (sm % 2 == 0){
		return n * 2;
	}
	else{
		return n * 2 + 1;
	}
	
}

int main(){
	int a = 123456789 / 8;
	int b = 1987654321 / 8;
	for (int i = a -1; i <= a + 2; i ++){
		if (f(f(f(i))) >= 123456789){
			a = i;
		}		
	}
	for (int i = b - 1; i <= b + 2; i ++){
		if (f(f(f(i))) <= 1987654321){
			b = i;
		}
	}
	cout << b - a + 1;
	
	
	system ("pause");
	return 0;
}
