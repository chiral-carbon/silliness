#include <iostream>
#include <cstring>
using namespace std;
int main()
{
	string s;
	cin>>s;
	for(int i=0;i<=s.length()-3;i++)
	{
		int c=0;
		string t=s.substr(i,3);
		for(int j=i+3;j<=s.length()-3;j++)
		{
			string r=s.substr(j,3);
			if(r.compare(t)==0)
			{
				c++;
			}
		}
		cout<<t<<": "<<c<<endl;
	}
	return 0;
}		
