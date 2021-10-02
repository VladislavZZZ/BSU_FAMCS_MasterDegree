#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;
#define ITEM_SIZE 5


vector<int> get_pair_value(int val){
    if (val%2 == 0){
            return {val,1,0,0,0};
        }else{
            return {0,0,val,1,0};
        }
}

void build(vector<vector<int> >& tree, vector<int>& data, int v, int tl, int tr) {
	if (tl == tr){
        tree[v] = get_pair_value(data[tl]);
    }else {
		int tm = (tl + tr) / 2;
		build (tree, data, v*2, tl, tm);
		build (tree, data, v*2+1, tm+1, tr);
		tree[v] = {tree[v*2][0] + tree[v*2+1][0], tree[v*2][1] + tree[v*2+1][1],tree[v*2][2] + tree[v*2+1][2],tree[v*2][3] + tree[v*2+1][3],0};
	}
}

// int get_sum(vector<vector<int> >& tree, int v, int tl, int tr, int l, int r, bool is_odd) {
// 	if (l > r)
// 		return 0;
// 	if (l == tl && r == tr)
//         if (is_odd){
//             return tree[v].first.first+ tree[v].second;
//         }else{
//             return tree[v].first.second+ tree[v].second;
//         }
// 	int tm = (tl + tr) / 2;

// 	return get_sum (tree, v*2, tl, tm, l, min(r,tm), is_odd)
// 		+ get_sum (tree, v*2+1, tm+1, tr, max(l,tm+1), r, is_odd);
// }

void update(vector<vector<int> >& tree, int v, int tl, int tr, int pos, int new_val) {
	if (tl == tr)
		tree[v] = get_pair_value(new_val);
	else {
		int tm = (tl + tr) / 2;
		if (pos <= tm)
			update (tree,v*2, tl, tm, pos, new_val);
		else
			update (tree,v*2+1, tm+1, tr, pos, new_val);
		tree[v] = {tree[v*2][0] + tree[v*2+1][0], tree[v*2][1] + tree[v*2+1][1],tree[v*2][2] + tree[v*2+1][2],tree[v*2][3] + tree[v*2+1][3],0};
	}
}

void increment_area(vector<vector<int> >& tree, int v, int tl, int tr, int l, int r){
    if (l > r)
		return;
	if (l == tl && r == tr){
        cout<<tl<<endl<<tr;
        return;
    }
	int tm = (tl + tr) / 2;
	increment_area(tree, v*2, tl, tm, l, min(r,tm));
    increment_area(tree, v*2+1, tm+1, tr, max(l,tm+1), r);
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ifstream in("input.txt");
    string data;
    string delimiter = " ";
    int n,q;
    size_t pos;
    getline(in,data);
    pos = data.find(delimiter);
    n = stoi(data.substr(0, pos));
    data.erase(0, pos + delimiter.length());
    q = stoi(data);
    getline(in,data);

    vector<int> arr;
    // vector<pair<int,int> > tree(4*n);
    vector<vector<int> > tree(4*n);


    while ((pos = data.find(delimiter)) != string::npos) {
        arr.push_back(stoi(data.substr(0, pos)));
        data.erase(0, pos + delimiter.length());
    }
    arr.push_back(stoi(data));
    build(tree, arr, 1, 0, n-1);

    for (int i = 0; i< q; i++){
        getline(in,data);
        arr.clear();
        while ((pos = data.find(delimiter)) != string::npos) {
            arr.push_back(stoi(data.substr(0, pos)));
            data.erase(0, pos + delimiter.length());
        }
        arr.push_back(stoi(data));
        switch (arr[0])
        {
        case 1:
            update(tree, 1,0,n-1, arr[1], arr[2]);
            break;
        case 2:
            increment_area(tree, int 1, 0, n-1, arr[1], arr[2])
            /* code */
            break;
        case 3:
            /* code */
            break;
        
        case 4:
            /* code */
            break;
        
        }
    }

    return 0;
}