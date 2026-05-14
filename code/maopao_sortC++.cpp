#pragma GCC optimize("O2")


#include<bits/stdc++.h>
#include"./random_data.h"

using namespace std;
using namespace std::chrono;

int main(){
	Random r;
	int x,y=100;
	

	fstream f;
	f.open("./out/mpout-O2.out",ios::out);
	
	cout<<"input:";
	cin>>x;
	cout<<"冒泡排序：共"<<x<<"组，数据量："<<(1+x)*x*(y/2)<<endl;
	f<<"冒泡排序：共"<<x<<"组，数据量："<<(1+x)*x*(y/2)<<endl;
	x++;
	
	for(int i=1;i<x;i++){
		auto start = high_resolution_clock::now();
		
		r.set_number(i*y);r.runRandom();
		vector<int> data=r.getRandomData();
		bool b=false;
		for(;!b;){
			b=true;
			for(int k=0;k<i*y;k++){
				if(data[k]>data[k+1]){
					swap(data[k],data[k+1]);
					b=false;
				}
			}
		}
		
		
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
		f<<"第"<<i<<"组 "<<"数据量："<<i*y<<" "<<((double)duration_cast<microseconds>(duration).count())/1000<<" ms";
		if(b1) {cout<<"  Data Accept.";f<<"  Data Accept.";}
		else {cout<<"  Data Error.";f<<"  Data Error.";}
		cout<<"       准确率："<<((i*y-c)/(double)(i*y))*100<<"%.";
		cout<<endl;

		f<<"       准确率："<<((i*y-c)/(double)(i*y))*100<<"%.";
		f<<endl;
	}
}
