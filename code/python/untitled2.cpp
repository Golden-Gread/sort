#include<bits/stdc++.h>
using namespace std;


int main(){
	freopen("./in.txt","r",stdin);
	string s;
	while(getline(cin,s)){
		int c,size;double t=0;
		sscanf(s.c_str(),"Group %d Data Size:%d Time: %lfms.",&c,&size,&t);
		cout<<t<<endl;
	}
	return 0;
	
} 
