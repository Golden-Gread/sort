#include<bits/stdc++.h>
using namespace std;

vector<string> sp(vector<string> data){
	vector<string> l;
	for(auto it:data){
		int g_num,num_count;double t;
		sscanf(it.c_str(),"%d group, Data volume: %d %lf ms  Data Accept.       Accuracy: 100.000%%.",&g_num,&num_count,&t);
		l.push_back(to_string(t));
	}
	return l;
}

int main(){
	freopen("./in/data.txt","r",stdin);
	string s;vector<string> sl;
	while(getline(cin,s)){
		sl.push_back(s);
	}
	sl=sp(sl);
	
	for(auto i:sl){
		cout<<i<<endl;
	}
	
	return 0;
	
} 
