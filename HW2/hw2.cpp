#include <bits/stdc++.h>
#include <ctime>
#include "btree.h"
using namespace std;

#define Max_K 30
#define Max_Q 100000
const int Moder = pow(2, 30);
vector <int> arr;
set <int> bst;

int newNum(int num){
    return num % Moder + 1;
}

void insertArray(int num){
    int pos = lower_bound(arr.begin(), arr.end(),num) - arr.begin();
    if(arr[pos] != num){
        arr.push_back(0);
        for(int i=arr.size()-1;i>pos;i--){
            arr[i] = arr[i-1];
        }
        arr[pos] = num;
    }
}

double time_amoung(clock_t end, clock_t start){
    if(end != -1){
        return double(end - start)/CLOCKS_PER_SEC*1000;
    }else return -1;
}

int main(void){
    for(int k=29;k<=Max_K;k++){
        int seed = time(NULL);
        int n = pow(2, k);
        clock_t start_insert, end_insert, start_query, end_query;
        // sorted array
        /*arr.clear();
        arr.push_back(0);
        srand(seed);
        start_insert = clock();
        for(int i=0;i<n;i++){
            insertArray(newNum(rand()));
            end_insert = clock();
            if(end_insert - start_insert > 60*60*CLOCKS_PER_SEC){
                end_insert = -1;
                break;
            }
        }
        double arr_insert = time_amoung(end_insert, start_insert);   
        start_query = clock();
        for(int i=0;i<Max_Q;i++){
            lower_bound(arr.begin(), arr.end(), newNum(rand()));
            end_query = clock();
            if(end_query - start_query > 60*60*CLOCKS_PER_SEC){
                end_query = -1;
                break;
            }
        }
        double arr_query = time_amoung(end_query, start_query);   
        ofstream ans_arr;
        ans_arr.open("arr.csv", ios::app);
        // k insert query
        if(arr_insert == -1 && arr_query == -1)
            ans_arr << k << ",over time,over time\n";
        else if(arr_insert == -1)
            ans_arr << k << ",over time," << arr_query << endl;
        else if(arr_query == -1)
            ans_arr << k << "," << arr_insert << ",over time\n";
        else 
            ans_arr << k << "," << arr_insert << "," << arr_query << endl;
        ans_arr.close();*/
        // BST
        /*bst.clear();
        srand(seed);
        start_insert = clock();
        for(int i=0;i<n;i++){
            bst.insert(newNum(rand())); 
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
        ans_bst.open("bst.csv", ios::app);
        // k insert query
        if(bst_insert == -1 && bst_query == -1)
            ans_bst << k << ",over time,over time\n";
        else if(bst_insert == -1)
            ans_bst << k << ",over time," << bst_query << endl; 
        else if(bst_query == -1)
            ans_bst << k << "," << bst_insert << ",over time\n";
        else 
            ans_bst << k << "," << bst_insert << "," << bst_query << endl;
        ans_bst.close();*/
        // Btree
        // 建樹
        KeyType array[] = {}; 
        int length = sizeof(array)/sizeof(KeyType); 
        BTree tree = NULL; 
        BTree_create(&tree, array, length); 
        // 建樹完畢
        srand(seed);
        start_insert = clock();
        for(int i=0;i<n;i++){
            BTree_insert(&tree, newNum(rand())); 
            end_insert = clock();
            if(end_insert - start_insert > 60*60*CLOCKS_PER_SEC){
                end_insert = -1;
                break;
            }  
        }
        double btree_insert = time_amoung(end_insert, start_insert);   
        srand(seed);
        for(int i=0;i<Max_Q;i++){
            KeyType key = newNum(rand());
            test_BTree_search(tree,  key);
            end_query = clock();
            if(end_query - start_query > 60*60*CLOCKS_PER_SEC){
                end_query = -1;
                break;
            }
        }
        BTree_destroy(&tree);
        double btree_query = time_amoung(end_query, start_query);   
        ofstream ans_btree;
        ans_btree.open("btree.csv", ios::app);
        // k insert query
        if(btree_insert == -1 && btree_query == -1)
            ans_btree << k << ",over time,over time\n";
        else if(btree_insert == -1)
            ans_btree << k << ",over time," << btree_query << endl;
        else if(btree_query == -1)
            ans_btree << k << "," << btree_insert << ",over time\n";
        else 
            ans_btree << k << "," << btree_insert << "," << btree_query << endl;
        ans_btree.close();
    }
}