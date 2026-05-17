//#pragma GCC optimize("O2")


#include<bits/stdc++.h>
#include"./random_data.h"

using namespace std;
using namespace std::chrono;

int main(){
	Random r;
	int x,y=100;
	

	fstream f;
	f.open("./out/mpout_O2.out",ios::app);
	
	cout<<"input:";
	cin>>x;
	for(int i=0;i<5;i++){cout<<"Bubble Sort: A total of "<<x<<" groups, data size: "<<(1+x)*x*(y/2)<<endl;
	f<<"Bubble Sort: A total of "<<x<<" groups, data size: "<<(1+x)*x*(y/2)<<endl;
	x++;
	
auto now = std::chrono::system_clock::now();
    std::time_t now_time = std::chrono::system_clock::to_time_t(now);
    
    // 转换为本地时间
    std::tm* local_time = std::localtime(&now_time);
    
    
    std::cout << std::put_time(local_time, "%Y-%m-%d %H:%M:%S") << std::endl;

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
		
		
		
		cout<<i<<"group "<<"data size: "<<i*y<<" "<<((double)duration_cast<microseconds>(duration).count())/1000<<" ms";
		f<<i<<"group "<<"data size: "<<i*y<<" "<<((double)duration_cast<microseconds>(duration).count())/1000<<" ms";
		if(b1) {cout<<"  Data Accept.";f<<"  Data Accept.";}
		else {cout<<"  Data Error.";f<<"  Data Error.";}
		cout<<"       accuracy: "<<((i*y-c)/(double)(i*y))*100<<"%.";
		cout<<endl;

		f<<"       accuracy:"<<((i*y-c)/(double)(i*y))*100<<"%.";
		f<<endl;
	}}
}
