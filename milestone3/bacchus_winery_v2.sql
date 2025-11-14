CREATE DATABASE IF NOT EXISTS bacchus_winery;
USE bacchus_winery;

DROP TABLE IF EXISTS Department;

CREATE TABLE Department (
	Dept_ID INT PRIMARY KEY AUTO_INCREMENT,
    Dept_Name VARCHAR(50) NOT NULL,
    Location VARCHAR(100),
    Contact_Info VARCHAR(100)
);

-- SELECT * FROM Department;

INSERT INTO Department (Dept_Name, Location, Contact_Info)
VALUES
('Finance', 'Main Office', 'jcollins@bacchus.com'),
('Marketing', 'Downtown Office', 'rmurphy@bacchus.com'),
('Production', 'Winery Floor', 'hdoyle@bacchus.com'),
('Distribution', 'Shipping Office', 'mcostanza@bacchus.com');

DROP TABLE IF EXISTS Employee;

CREATE TABLE Employee (
    Employee_ID INT PRIMARY KEY AUTO_INCREMENT,
    First_Name VARCHAR(50) NOT NULL,
    Last_Name VARCHAR(50) NOT NULL,
    Dept_ID INT,
    Supervisor_ID INT,
    Job_Title VARCHAR(50),
    Hire_Date DATE,
    Contact_Info VARCHAR(100),
    Salary DECIMAL(10,2),
    FOREIGN KEY (Dept_ID) REFERENCES Department(Dept_ID)
);

ALTER TABLE Employee
ADD CONSTRAINT fk_supervisor
FOREIGN KEY (Supervisor_ID)
REFERENCES Employee(Employee_ID);

SET FOREIGN_KEY_CHECKS = 1;
INSERT INTO Employee
(First_Name, Last_Name, Dept_ID, Supervisor_ID, Job_Title, Hire_Date, Contact_Info, Salary)
VALUES
('Janet', 'Collins', 1, NULL, 'Finance & Payroll Manager', '2019-03-16', 'jcollins@bacchus.com', 68000.00),
('Roz', 'Murphy', 2, NULL, 'Marketing Manager', '2022-10-02', 'rmuphy@bacchus.com', 75000.00),
('Bob', 'Ulrich', 2, 2, 'Marketing Assistant', '2022-11-10', 'bobulrich@bacchus.com', 50000.00),
('Henry', 'Doyle', 3, NULL, 'Production Manager', '2008-01-06', 'hdoyle@bacchus.com', 96000.00),
('Maria', 'Costanza', 4, NULL, 'Distribution Manager', '2017-06-22', 'mcostanza@bacchus.com', 68000.00);

-- SELECT * FROM Employee;

DROP TABLE IF EXISTS Employee_Hour;

CREATE TABLE Employee_Hour (
	Hours_ID INT PRIMARY KEY AUTO_INCREMENT,
    Employee_ID INT,
    Quarter ENUM('Q1','Q2','Q3','Q4') NOT NULL,
    Year YEAR NOT NULL,
    Hours_Worked DECIMAL(6,2) NOT NULL,
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
);

-- SELECT * FROM Employee_Hour;

DROP TABLE IF EXISTS Supplier;

CREATE TABLE Supplier (
	Supplier_ID INT PRIMARY KEY AUTO_INCREMENT,
    Supplier_Name VARCHAR(100) NOT NULL,
    Item_Supplied VARCHAR(100),
    Contact_Info VARCHAR(100),
    Address VARCHAR(150),
    City VARCHAR(50),
    State CHAR(2),
    Zip CHAR(10)
);

INSERT INTO Supplier
(Supplier_Name, Item_Supplied, Contact_Info, Address, City, State, Zip)
VALUES
('Closure Craftsman', 'Bottles and Corks', 'sales@closurecraftsman.com', '150 Port Circle Dr.', 'Fairfield', 'CA', '94534'),
('The Vinculum Print House', 'Labels and Boxes', 'orders@vinculumprint.com', '88 Production Way', 'Tualatin', 'OR', '97062'),
('CellarFlow Equipment', 'Vats and Tubing', 'info@cellarflow.net', '201 Industry Blvd.', 'Woodinville', 'WA', '98072');

-- SELECT * FROM Supplier;

DROP TABLE IF EXISTS Distributor;

CREATE TABLE Distributor (
	Distributor_ID INT PRIMARY KEY AUTO_INCREMENT,
    Distributor_Name VARCHAR(100) NOT NULL,
    Region VARCHAR(100),
    Contact_Info VARCHAR(100),
    Address VARCHAR(150),
    City VARCHAR(50),
    State CHAR(2),
    Zip CHAR(10)
);

-- SELECT * FROM Distributor;

DROP TABLE IF EXISTS Product;

CREATE TABLE Product (
	Product_ID INT PRIMARY KEY AUTO_INCREMENT,
    Product_Name VARCHAR(100) NOT NULL,
    Wine_Type ENUM('Merlot','Cabernet','Chablis','Chardonnay') NOT NULL,
    Vintage_Year YEAR NOT NULL,
    Quantity_Produced INT NOT NULL,
    Retail_Price DECIMAL(10,2),
    Supplier_ID INT,
    Description VARCHAR(255),
	FOREIGN KEY (Supplier_ID) REFERENCES Supplier(Supplier_ID)
);

-- SELECT * FROM Product;

DROP TABLE IF EXISTS Shipment;

CREATE TABLE Shipment (
	Shipment_ID INT PRIMARY KEY AUTO_INCREMENT,
    Supplier_ID INT NOT NULL,
    Distributor_ID INT NOT NULL,
    Shipment_Date DATE,
    Expected_Delivery DATE NOT NULL,
    Actual_Delivery DATE,
    Delivery_Status ENUM('Pending','In Transit','Delivered','Delayed'),
    FOREIGN KEY (Supplier_ID) REFERENCES Supplier(Supplier_ID),
    FOREIGN KEY (Distributor_ID) REFERENCES Distributor(Distributor_ID)
);

-- SELECT * FROM Shipment;

DROP TABLE IF EXISTS Shipment_Detail;

CREATE TABLE Shipment_Detail (
	ShipmentDetail_ID INT PRIMARY KEY AUTO_INCREMENT,
    Shipment_ID INT NOT NULL,
    Product_ID INT NOT NULL,
    Quantity INT NOT NULL,
    Unit_Price DECIMAL(10,2) NOT NULL,
    Subtotal DECIMAL(12,2),
    FOREIGN KEY (Shipment_ID) REFERENCES Shipment(Shipment_ID),
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID)
);

-- SELECT * FROM Shipment_Detail;

DROP TABLE IF EXISTS Inventory;

CREATE TABLE Inventory (
	Inventory_ID INT PRIMARY KEY AUTO_INCREMENT,
    Product_ID INT NOT NULL,
    Quantity_On_Hand INT NOT NULL,
    Last_Updated DATE NOT NULL,
    Location VARCHAR(50),
    Reorder_Level INT,
    Reorder_Date DATE,
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID)
);

-- SELECT * FROM Inventory;

/* DROP TABLE IF EXISTS Customer;

 CREATE TABLE Customer (
	Customer_ID INT PRIMARY KEY AUTO_INCREMENT,
    Customer_Name VARCHAR(100) NOT NULL,
    Contact_Info VARCHAR(100),
    Address VARCHAR(150),
    City VARCHAR(50),
    State CHAR(2),
    Zip CHAR(10)
);

-- SELECT * FROM Customer;
*/
