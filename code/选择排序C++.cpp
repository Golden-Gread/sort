#include<bits/stdc++.h>
#include"./random_data.h"

using namespace std;
using namespace std::chrono;

int main(){
	Random r;
	int x,y=100;
	freopen("./out/xzout.out","w",stdout);
	
	cout<<"input:";
	cin>>x;
	cout<<"选择排序：共"<<x<<"组，数据量："<<(1+x)*x*(y/2)<<endl;
	x++;
	
	for(int i=1;i<x;i++){
		auto start = high_resolution_clock::now();
		
		r.set_number(i*y);r.runRandom();
		vector<int> data=r.getRandomData();
		for(int k = 0; k < i * y - 1; k++){
			int minIndex = k;
			for(int j = k + 1; j < i * y; j++){
				if(data[j] < data[minIndex]){
					minIndex = j;
				}
			}
			swap(data[k], data[minIndex]);
		}
		
		
		auto end = high_resolution_clock::now();
		auto duration = end - start;
		bool b1=true;
		long long c=0;
		for(int k=0;k<i*y-1;k++){
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
