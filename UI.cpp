// This file manages the UI

#include <iostream>
#include "../tools/Python/Functions.h"


// This function launches the main UI
bool launchGUI()
{
    // Load the python Gui file
    ReturnList<bool>* gui = new ReturnList<bool>("table", "main", "./GUI/table.py");

    bool* ret = gui->callFunction();

    if (ret == NULL)
    {
        std::cout << "Something went wrong function returned null\n";
        return false;
    }
    else
    {
        // Yay or nay?
        return *ret;
    }
}

// This function runs the login screen written in python, gets
// a yay or nay signal and passes it back to C++ who then either 
// closes or carries on executing the app
int userLogin()
{
    // Load the python login file 
    ReturnList<int>* login = new ReturnList<int>("login", "main", "./GUI/login.py");

    // Execute it
    int* ret = login->callFunction();

    if (ret == NULL)
    {
        std::cout << "Something went wrong function returned null\n";
        return false;
    }
    else
    {
        // Yay or nay?
        return *ret;
    }

}

/* This wont be in the final version since there is only one main()
 function per C++ program but it will be commented out later and used
 as a guide on how to use the functions defined here
int main()
{
    ReturnList<int>* login = new ReturnList<int>("login", "main");

    int* ret = login->callFunction();

    if (ret == NULL)
    {
        std::cout << "Something went wrong function returned null\n";
    }
    else
    {
        std::cout << ret[0] << ret[1] << ret[2] << std::endl;
    }

    return 0;
} */
