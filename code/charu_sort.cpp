#include<bits/stdc++.h>
#include"./random_data.h"
using namespace std;
using namespace std::chrono;
int main(){
	Random r;
	int x,y=100;
	freopen("./out/crout.out","w",stdout);
	
	cout<<"input:";
	cin>>x;
	cout<<"插入排序：共"<<x<<"组，数据量："<<(1+x)*x*(y/2)<<endl;
	x++;
	
	for(int i=1;i<x;i++){
		auto start = high_resolution_clock::now();
		
		r.set_number(i*y);r.runRandom();
		vector<int> data=r.getRandomData();
		vector<int> data_temp={};
		//代码块
		data_temp.push_back(*data.begin());
		
		
		for(auto it=data.begin()+1;it!=data.end();it++){
			bool is_insert=0;
			for(auto ind=data_temp.begin();ind!=data_temp.end();ind++){
				if(*ind>*it){data_temp.insert(ind,*it);is_insert=1;break;}
			}
			if(!is_insert){data_temp.push_back(*it);}
		}
		
		data = data_temp;
		
		
		auto end = high_resolution_clock::now();
		auto duration = end - start;
		bool b1=true;
		long long c=0;
		for(int k=0;k<i*y;k++){
			if(data[k]>data[k+1]){
				b1=false;c++;
			}
		}
		
		
		
		cout<<"第"<<i<<"组 "<<"数据量："<<i*y<<" "<<((double)duration_cast<microseconds>(duration).count())/1000<<" ms";
		if(b1) cout<<"  Data Accept.";
		else cout<<"  Data Error.";
		cout<<"       准确率："<<((i*y-c)/(double)(i*y))*100<<"%.";
		cout<<endl;
		
	}
}
