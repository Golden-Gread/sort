#include<bits/stdc++.h>
#include"./random_data.h"



using namespace std;
using namespace std::chrono;

int main(){
	Random r;
	int x,y=100;
	freopen("./out/tout.out","a",stdout);
	
	cout<<"input:";
	cin>>x;
	for(int i=0;i<5;i++){
	cout<<"Bucket Sort: A total of "<<x<<" groups, data volume: "<<(1+x)*x*(y/2)<<endl;
	x++;
	cout<<fixed<<setprecision(3);
	
	auto now = std::chrono::system_clock::now();
    std::time_t now_time = std::chrono::system_clock::to_time_t(now);
    
    // 转换为本地时间
    std::tm* local_time = std::localtime(&now_time);
    
    
    std::cout << std::put_time(local_time, "%Y-%m-%d %H:%M:%S") << std::endl;

	for(int i=1;i<x;i++){

		auto start = high_resolution_clock::now();
		r.set_number(i*y);r.runRandom();
		vector<int> data=r.getRandomData();
		int it=-1;
		for(int i:data){
			it=max(it,i);
		}
		
		vector<int> num(it+2,0);
		for(auto it=data.begin();it!=data.end();it++){
			num[*it]++;
		}
		vector<int> data1={};
		for(int i=0;i<=it+1;i++){
			for(int j=0;j<num[i];j++){
				data1.push_back(i);
			}
		}
		
		
		
		
		auto end = high_resolution_clock::now();
		auto duration = end - start;
		bool b1=true;
		long long c=0;
		for(int k=0;k<i*y-1;k++){
			if(data1[k]>data1[k+1]){
				b1=false;c++;
			}
		}
		
		
		
		cout<<i<<" group,  "<<"Data volume: "<<i*y<<" "<<((double)duration_cast<microseconds>(duration).count())/1000<<" ms";
		if(b1) cout<<"  Data Accept.";
		else cout<<"  Data Error.";
		cout<<"       Accuracy: "<<((i*y-c)/(double)(i*y))*100<<"%.";
		cout<<endl;
		
	}
}
}
