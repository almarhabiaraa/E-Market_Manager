# E-Market_Manager: Python E-commerce Program

**Course:** GCS150 – Principles of Computing, Data and Algorithms  
**Language:** Python  
**Team Members:** Araa, Rania, Yara  



## Introduction

This project is a basic **Python-based E-commerce management system**. It allows users to manage items in a virtual marketplace using a menu-driven interface. The program is built around several functions, each responsible for handling a specific task related to item management such as adding, updating, deleting, and viewing items.



## Code Overview

### Main Function

- Verifies the password entered by the user.
- Upon successful login, prompts the user to enter the name of a text file.
- Displays a menu of options for the user to choose from.
- Each option is linked to a separate function for better readability and modularity.



### Function Descriptions

#### ➤ `option_1`: Add New Item
- Asks the user for item name, type, and quantity.
- Stores the new item details in the text file.

#### ➤ `option_2`: Classify Items by Type
- Reads items from the text file.
- Classifies and displays them based on item type.

#### ➤ `option_3`: Update Item Quantity
- Reads current item data from the file.
- Prompts the user for the item name and new quantity.
- Updates the file with the new quantity.

#### ➤ `option_4`: Delete Item
- Displays all items to the user.
- Allows the user to choose an item to delete.
- Removes the selected item from the file.

#### ➤ `option_5`: Add Another Item
- Similar to `option_1`.
- Lets the user add more items by entering name, type, and quantity.

#### ➤ `option_6`: Sort Items
- Allows the user to sort items in **ascending (`a`)** or **descending (`d`)** order.
- Displays the sorted list to the user.


## Features

- Password-protected access
- Easy-to-use menu interface
- Persistent data storage using a text file
- Ability to add, update, delete, classify, and sort items
- Modular design using Python functions



## How to Set Up

1. Make sure you have Python installed on your system.
2. Run the program using:

```bash
python code.py
```
3. Follow the prompts to log in and manage your e-market.

## Contributors
1. Araa Almarhabi
2. Rania Altahawi
3. Yara Jarwan 

