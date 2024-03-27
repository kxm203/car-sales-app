# Classic Mustang Sales App

## Overview

*The Car Sales App is an intuitive web application for users to buy, sell, and bid on classic Mustang cars. With an integrated Object-Relational Mapping (ORM) functionality, the Car Sales Web App efficiently stores, retrieves, and updates valuable car and user information, ensuring an effortless and engaging user experience.*


---

## Features

- User-friendly interface: A clean, intuitive, and responsive user interface for desktop and mobile devices.
- ORM Integration: Leverage the power of the ORM system to efficiently store, update, and retrieve car and user data from the integrated database.
- Car Sales and Bidding: Access features that allow users to browse classic Mustang cars, place bids, and execute sales.

---

## Components

The Car Sales App comprises four essential components:

- Car
- User
- Bids
- Sales
Each component handles their respective underlying functionalities, enabling a smooth user experience and efficient marketplace interaction.


---
## Mustang
The Card component manages details related to a single classic Mustang car, and communicates with the 'cars' table in the SQLite database. The component handles the following attributes:

- Year
- Make
- Model
- Color
- Condition
- User ID
The component supports Create, Read, Update, and Delete (CRUD) operations, while also providing methods for finding and joining car records.


---


## User

The User class manages user information and maintains a connection with the 'users' table in the SQLite database. The component handles the following attributes:

- Name
- Age
The User class supports CRUD operations, allowing users to modify personal details and create car listings.

---

## Bid

The Bid class manages individual bids by users on car listings, and interacts with the 'bids' table in the SQLite database. The component handles the following attributes:

- ID
- User ID
- Car ID
- Bid Amount
- The Bid class allows users to track and modify existing bids on their car listings.
---

## Contributors

Kenny McClelland\
Isaac Cotton\
TaKeya McFadden

---
