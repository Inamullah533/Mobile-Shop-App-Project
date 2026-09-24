<img width="1877" height="829" alt="Screenshot_24-9-2026_3946_localhost" src="https://github.com/user-attachments/assets/d53ca100-bbbf-4d70-8906-4d4567f45c2b" />












# 🛒 Shop Management System — Python



## 📌 About the Project

**Shop Management System** is a simple command-line Python application designed to manage products and customer orders in a small shop.

The project uses a **JSON file (`data.json`) as a local database**, allowing product information to be stored and retrieved even after the program is closed.

This project is useful for beginners who are learning **Python classes, file handling, JSON, exception handling, lists, dictionaries, and basic CRUD-style operations**.

---

## ✨ Features

### 📦 1. Add Products

Add new products to the shop by entering:

* 🏷️ Product Name
* 🔢 Quantity
* 💰 Price

Product information is automatically saved to `data.json`.

### 👀 2. View Products

Display all products currently available in the shop, including:

* Product Name
* Available Quantity
* Product Price

### 🛍️ 3. Place an Order

Customers can select a product and specify the quantity they want.

The program:

* 🔎 Searches for the requested product
* 📊 Checks available stock
* 🧮 Calculates the total price
* 📉 Decreases the product quantity
* 💾 Saves the updated stock

### ❌ 4. Cancel an Order

The program is designed to allow previous orders to be cancelled.

When an order is cancelled, its quantity can be added back to the shop's inventory.

---

## 🧰 Technologies Used

| Technology            | Purpose                                |
| --------------------- | -------------------------------------- |
| 🐍 Python             | Main programming language              |
| 📄 JSON               | Local data storage                     |
| 📁 pathlib            | File and path handling                 |
| 🧱 OOP                | Shop management using a class          |
| ⚠️ Exception Handling | Handling invalid input and file errors |

---

## 📂 Project Structure

```text
Shop-Management-System/
│
├── 📄 main.py
├── 📄 data.json
└── 📄 README.md
```

---

## 🚀 How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2️⃣ Open the Project

```bash
cd Shop-Management-System
```

### 3️⃣ Run the Python Program

```bash
python main.py
```

---

## 🎮 Menu Options

When the program starts, you will see:

```text
Press 1 for Data Enter of Mobile Accessories
Press 2 for See Product of shop
Press 3 for Add the order
Press 4 for cancel order
```

### Example

```text
Tell ur response: 1

Product Name :- Charger
Quantity of Products :- 20
Price of Product :- 500
```

The product will then be stored in `data.json`.

---

## 💾 Data Storage

The project uses a JSON file instead of a traditional database.

Example:

```json
[
    {
        "Product_Name": "Charger",
        "Quantity": 20,
        "Price": 500
    },
    {
        "Product_Name": "USB Cable",
        "Quantity": 15,
        "Price": 300
    }
]
```

This makes the project simple and easy to understand for beginners.

---

## 🧠 Python Concepts Used

This project demonstrates several important Python concepts:

* 🏗️ Classes and Objects
* 📋 Lists
* 📖 Dictionaries
* 🔄 Loops
* 🔍 Conditional Statements
* 📂 File Handling
* 🗃️ JSON Serialization
* 🛡️ Exception Handling
* ⌨️ User Input
* 🧮 Basic Calculations
* 📁 `pathlib`
* 🔤 String Methods

---

## 🔮 Future Improvements

Some useful improvements that could be added later:

* 🔐 Admin login system
* 🧾 Generate invoices/receipts
* 📜 Proper persistent order history
* 🔎 Search products by name
* ✏️ Update product information
* 🗑️ Delete products
* 💰 Decimal prices instead of integers
* 📊 Sales reports
* 🛒 Multiple products in a single order
* 🖥️ GUI using Tkinter or PyQt
* 🗄️ SQLite/MySQL database integration

---

## 🎯 Project Goal

The main goal of this project is to practice Python programming by building a small but practical **shop inventory and order management system**.

It demonstrates how Python can be used to create a simple application that stores data, manages inventory, processes orders, and handles user input.

---

## 👨‍💻 Author

**Your Name**

⭐ If you find this project useful, consider giving the repository a star!

---

## 🏷️ Tags

`#Python` `#PythonProject` `#ShopManagement` `#InventoryManagement` `#JSON` `#OOP` `#BeginnerProject` `#FileHandling` `#CLI` `#Programming`
