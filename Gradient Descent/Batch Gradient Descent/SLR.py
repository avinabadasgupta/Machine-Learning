#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;
int main()
{
    std::ifstream  data("train.csv");
    std::string line;
    std::getline(data,line);
    std::string::size_type sz; 
    int train_Data_Size=700;
    double X_train[train_Data_Size],Y_train[train_Data_Size];
    int i=0;
    while(std::getline(data,line))
    {
        std::stringstream lineStream(line);
        std::string cell;
        bool flag=true;
        while(std::getline(lineStream,cell,','))
        {
            std::string temp=cell;
            if(flag)
                X_train[i]=std::stod(temp,&sz);
            else
                Y_train[i]=std::stod(temp,&sz);
            flag=!flag;
        }
        ++i;
    }
    std::ifstream  data_2("test.csv");
   	std::getline(data_2,line);
    int test_Data_Size=300;
    double X_test[test_Data_Size],Y_test[test_Data_Size];
    i=0;
    while(std::getline(data_2,line))
    {
        std::stringstream lineStream(line);
        std::string cell;
        bool flag=true;
        while(std::getline(lineStream,cell,','))
        {
            std::string temp=cell;
            if(flag)
                X_test[i]=std::stod(temp,&sz);
            else
                Y_test[i]=std::stod(temp,&sz);
            flag=!flag;
        }
        ++i;
    }
    double X_max=X_train[0],X_min=X_train[0];
    double Y_max=Y_train[0],Y_min=Y_train[0];
    for(int i=0;i<train_Data_Size;++i){
        if(X_train[i]>X_max)
            X_max=X_train[i];
        if(X_train[i]<X_min)
            X_min=X_train[i];
        if(Y_train[i]>Y_max)
            Y_max=Y_train[i];
        if(Y_train[i]<Y_min)
            Y_min=Y_train[i];
    }
    for(int i=0;i<train_Data_Size;++i){
        X_train[i]=(X_train[i]-X_min)/(X_max-X_min);
        Y_train[i]=(Y_train[i]-Y_min)/(Y_max-Y_min);
    }
    X_max=X_test[0],X_min=X_test[0];
    Y_max=Y_test[0],Y_min=Y_test[0];
    for(int i=0;i<test_Data_Size;++i){
        if(X_test[i]>X_max)
            X_max=X_test[i];
        if(X_test[i]<X_min)
            X_min=X_test[i];
        if(Y_test[i]>Y_max)
            Y_max=Y_test[i];
        if(Y_test[i]<Y_min)
            Y_min=Y_test[i];
    }
    for(int i=0;i<test_Data_Size;++i){
        X_test[i]=(X_test[i]-X_min)/(X_max-X_min);
        Y_test[i]=(Y_test[i]-Y_min)/(Y_max-Y_min);
    }
    double b_0=.45,b_1=.65;
    double MSE[2]={0};
    while(1){
        double y_pred[train_Data_Size];
	    for(int i=0;i<train_Data_Size;++i){
	    	y_pred[i]=b_0 + (b_1 * X_train[i]);
	    }
	    MSE[1]=0;
	    for(int i=0;i<train_Data_Size;++i)
	    	MSE[1]+=pow(Y_train[i]-y_pred[i],2);
	    MSE[1]/=train_Data_Size;
	    if(fabs(MSE[0]-MSE[1])<0.00001)
	    	break;
	    MSE[0]=MSE[1];
	    double error_gradient_b_0=0, error_gradient_b_1=0;
	    for(int i=0;i<train_Data_Size;++i){
	    	error_gradient_b_0+=(y_pred[i]-Y_train[i]);
	    	error_gradient_b_1+=(y_pred[i]-Y_train[i])*X_train[i];
	    }
	    error_gradient_b_0/=train_Data_Size;
	    error_gradient_b_1/=train_Data_Size;
	    double learning_Rate=0.0001;
	    b_0=b_0 - learning_Rate*error_gradient_b_0;
	    b_1=b_1 - learning_Rate*error_gradient_b_1;
	}
	double y_pred[test_Data_Size];
	for(int i=0;i<test_Data_Size;++i){
		y_pred[i]=b_0 + b_1*X_test[i];
	}
	for(int i=0;i<test_Data_Size;++i){
		cout<<Y_test[i]<<" -> "<<y_pred[i]<<endl;
	}
    return 0;
 }
