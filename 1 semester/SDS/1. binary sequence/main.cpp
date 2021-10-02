#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
#include<vector>
#include<cmath>
#include <numeric>
#include<bitset>

using namespace std;

unsigned long long gcd (unsigned long long a, unsigned long long b) {
	while (b) {
		a %= b;
		swap(a, b);
	}
	return a;
}

string removeSpaces(string str)
{
    stringstream s(str);
    string temp;
    str = "";
    while (getline(s, temp, ' ')) {
        str = str + temp;
    }
    return str;
}

unsigned long long changes_after_increment(vector<unsigned long long>& res, unsigned long long number, int bit_size){
    unsigned long long t = 0;
    for (int i = 0; i<bit_size; i++){
        unsigned long long p = pow(2,i);
        unsigned long long tt = number/p;
        t+=tt;
        res[i] = tt;
    }
    return t;
}

int count_diffenence(vector<unsigned long long>& res1, vector<unsigned long long>& res2, int num_bits){
    int differences = 0;
    for (int i =0; i< num_bits; i++){
        if (res2[i]>res1[i]){
            differences +=1;
        }
    }
    return differences;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // ifstream in("input.txt");
    string temp;
    getline(cin, temp);
    int num_of_digits = stoi(temp);
    getline(cin, temp);
    temp = removeSpaces(temp);
    unsigned long long num = stoull(temp,0,2);

    getline(cin, temp);
    unsigned long long num_of_increments = stoull(temp);

    unsigned long long incremented_num = num + num_of_increments;

    vector<unsigned long long> res1(num_of_digits);
    vector<unsigned long long> res2(num_of_digits);

    unsigned long long count1 = changes_after_increment(res1, num, num_of_digits);
    unsigned long long count2 = changes_after_increment(res2, incremented_num, num_of_digits);

    int changes = count_diffenence(res1,res2, num_of_digits);

    unsigned long long k = gcd(count2-count1, num_of_increments);

    cout << changes<<"\n";
    cout << (count2-count1)/k<< "/"<< num_of_increments/k;

    return 0;
}