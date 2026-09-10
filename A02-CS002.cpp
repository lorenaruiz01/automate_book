#include <iostream>

int main()
{
    int saved_cents, total_cents, quarters, dimes, nickels, pennies;

    std::cout << "Please enter a number greater than 500: ";
    std:: cin >> total_cents;
    saved_cents = total_cents; //preserving the original value so we can print at the end.

    quarters = total_cents / 25; //figures out how many quarters
    total_cents - total_cents - (quarters * 25); //figures out how mny cents remain.

    
}