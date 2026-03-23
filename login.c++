#include <iostream>
#include <string>

using namespace std;

int main() {
    string username, password;

    cout << "Enter your username: ";
    cin >> username;

    cout << "Enter your password: ";
    cin >> password;

    string admin = "adminKE";
    string passwordAdmin = "254Secure";


    if (username == admin && password == passwordAdmin) {
        cout << "Access granted!" << endl;
    } else {
        cout << "Invalid Credentials!" << endl;
    }

    return 0;
}