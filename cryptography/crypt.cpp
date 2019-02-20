#include <iostream>
#include <cstring>
using namespace std;
int main()
{
	string s, t;
	cin>>s;
	for(int i=0;i<s.length();i++)
	{
	
		int c=s[i]-65;
		cout<<c<<" ";
	}
	//cout<<t<<endl;
	return 0;
}
