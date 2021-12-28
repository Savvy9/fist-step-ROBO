#include <iostream>
#include <vector>
#include <time.h>
#include <stdlib.h>
using namespace std;
vector<int> a;
int get_random(int x,int y){
	srand(time(NULL));

	///rand() Y-X+1  X
	return rand()%(y-x+1)+x; 
}
int main(){
	cout<<"Enter the intervals between which numbers you want:"<<endl;
	int x,y;
	cin>>x>>y;
	cout<<"Do you have any preferance which numbers to include(Y/N)"<<endl;
	char choice;
	cin>>choice;
	if(choice=='y' || choice=='Y'){
		cout<<"How many:"<<endl;
		int numb;
		cin>>numb;
		cout<<"Plese enter the numbers:"<<endl;
		while(numb--){
			int n;
			cin>>n;
			if(x<n && n<y){
				a.push_back(n);
			}else{
				cout<<"Please enter a valid number that is in the interval:"<<endl;
			}
		}
	}
	while(1){
		bool isnonvalid = false;
		int c = get_random(x,y);
		for(int i = 0;i<a.size();i++){
			if(c==a[i]){
				isnonvalid = true;
			}
		}
		if(isnonvalid==false){
			cout<<"Your random numb is:"<<c<<endl;
			break;
		}
	}
	return 0;
}