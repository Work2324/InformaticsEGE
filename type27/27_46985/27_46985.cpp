#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
int main(){
	int n = 0;
	ifstream fin("27-A.txt");
	fin >> n;
	//cout << n << endl;
	vector <int> m(n);
	
	for(int i=0;i< n; i++){
		fin >> m[i];
		//cout << m[i]<< endl;
	}
	
	int t = 0;
	long long sm = 0;
	for (int i = 0; i < n - 1; i++){
		sm = m[i];
		if(sm % 999 == 0){
			t++;
		}
		for(int k = i + 1; k < n; k++){
			sm = sm + m[k];
			if(sm % 999 == 0){
				t ++;
			}
		}
	}
	
	if(m[n-1] % 999 == 0){
		t++;
	}
	
	cout << t << endl;
	system("pause");
	return 0;
}
