#include <bits/stdc++.h>
#include <ctime>

using namespace std;

#define Max_K 30
#define Max_Q 100000
const int Moder = pow(2, 30);
vector <int> arr;
set <int> bst;
unordered_set <int> hashtable;

int newNum(int num){
    return num % Moder + 1;
}

double time_amoung(clock_t end, clock_t start){
    if(end != -1){
        return double(end - start)/CLOCKS_PER_SEC*1000;
    }else return -1;
}

int main(void){
    for(int k=10;k<=Max_K;k++){
        int seed = time(NULL);
        int n = pow(2, k);
        clock_t start_insert, end_insert, start_query, end_query;
        // Hashtable
        hashtable.clear();
        srand(seed);
        start_insert = clock();
        for(int i=0;i<n;i++){
            hashtable.insert(newNum(rand())); 
            end_insert = clock();
            if(end_insert - start_insert > 60*60*CLOCKS_PER_SEC){
                end_insert = -1;
                break;
            }   
        }
        double bst_insert = time_amoung(end_insert, start_insert);   
        start_query = clock();
        for(int i=0;i<Max_Q;i++){
            bst.find(newNum(rand()));
            end_query = clock();
            if(end_query - start_query > 60*60*CLOCKS_PER_SEC){
                end_query = -1;
                break;
            }
        }
        double bst_query = time_amoung(end_query, start_query);   
        ofstream ans_bst;
        ans_bst.open("hashtable.csv", ios::app);
        // k insert query
        if(bst_insert == -1 && bst_query == -1)
            ans_bst << k << ",over time,over time\n";
        else if(bst_insert == -1)
            ans_bst << k << ",over time," << bst_query << endl; 
        else if(bst_query == -1)
            ans_bst << k << "," << bst_insert << ",over time\n";
        else 
            ans_bst << k << "," << bst_insert << "," << bst_query << endl;
        ans_bst.close();
    }
}