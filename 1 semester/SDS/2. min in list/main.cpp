#include<iostream>
#include<stack>
#include<fstream>
#include<string>

using namespace std;

int push_elem(int elem, stack<pair<int,int> >& st1, stack<pair<int,int> >& st2){
    if (st1.empty()){
        st1.push(make_pair(elem, elem));
    }else{
        st1.push(make_pair(elem, min(elem,st1.top().second)));
    }
    if (st2.empty()){
            return st1.top().second;
    }else{
        return min(st1.top().second,st2.top().second);
    }
}

void move_stacks_value(stack<pair<int,int> >& import_st, stack<pair<int,int> >& export_st){
    stack<pair<int,int> > st3;
    int st_size = import_st.size() / 2;
    for (int i=0; i< st_size; i++){
        pair<int,int> val = import_st.top();
        import_st.pop();
        st3.push(val);
    }
    while (!import_st.empty()){
        pair<int,int> val = import_st.top();
        import_st.pop();
        int m = push_elem(val.first, export_st, import_st);
    }
    while (!st3.empty()){
        pair<int,int> val = st3.top();
        st3.pop();
        int m = push_elem(val.first, import_st, st3);
    }
}

int pop_elem(stack<pair<int,int> >& left_st, stack<pair<int,int> >& right_st, bool is_left){
    if (is_left){
        if (left_st.empty()){
            move_stacks_value(right_st, left_st);
        }
        left_st.pop();
    }else{
        if (right_st.empty()){
            move_stacks_value(left_st, right_st);
        }
        right_st.pop();
    }
    if (left_st.empty() && right_st.empty()){
        return -1;
    }else if (left_st.empty()){
        return right_st.top().second;
    }else if (right_st.empty()){
        return left_st.top().second;
    }else{
        return min(right_st.top().second, left_st.top().second);
    }
}


int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    string data;
    std::ifstream in("input.txt");
    stack<pair<int,int> > lm_stack;
    stack<pair<int,int> > rm_stack;
    getline(in, data);
    int req_num= stoi(data);
    string req;
    for (int i=0; i < req_num; i++){
        int minimum = 0;
        getline(in,req);
        if (req[0] == '-'){
            if (req[1] == 'L'){
                 minimum = pop_elem(lm_stack, rm_stack, true);
            }else{
                minimum = pop_elem(lm_stack, rm_stack, false);
            }
        }else{
            int value  = stoi(req.substr(3, req.length() - 3));
            if (req[1] == 'L'){
                minimum = push_elem(value, lm_stack, rm_stack);
            }else{
                minimum = push_elem(value, rm_stack, lm_stack);
            }
        }
        cout << minimum<<"\n";
    }
    return 0;
}