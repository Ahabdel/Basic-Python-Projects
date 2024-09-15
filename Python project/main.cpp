#include <iostream>
#include <cmath>

using namespace std;

int main() {
    cout << "Enter Sales: $";
    double sales;
    cin >> sales;

    const double stateTaxRate = 0.04;
    const double countyTaxRate = 0.02;
    double stateTax = sales * stateTaxRate;
    double countyTax = sales * countyTaxRate;
   
    double TotalTaxes = countyTax + stateTax;
    cout << "Taxes: $" << TotalTaxes << endl;

    double profits = sales - stateTax - countyTax;
    cout << "Income: $" << profits << endl;


    return 0;

}