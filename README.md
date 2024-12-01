# Budget Bliss

## Personal Finance Management Tool

**Budget Bliss** is an intuitive Python-based personal finance management tool that enables users to effortlessly track and manage their expenses, set up monthly budgets, and visualize their spending patterns. The system is designed to provide detailed financial insights through interactive visualizations and automated calculations, helping users stay on top of their financial goals.

![Budget Bliss Logo](images/logo.png)  <!-- Add your project logo image here -->

---

## Features

### 1. **Budget & Expense Management**
   - Set an initial monthly budget.
   - Track and categorize planned and unplanned expenses throughout the month.
   - Dynamically adjust your budget based on new data inputs.

### 2. **Loan Tracking**
   - Manage loans by recording details such as the lender's name, loan amount, and return date.
   - Get reminders of upcoming loan repayment deadlines.

### 3. **Daily Spending Plan**
   - Automatically calculate your daily spending limits based on the total monthly budget.
   - Adjust your daily plan if your budget changes during the month.

### 4. **Financial Analytics**
   - Get real-time calculations for:
     - Total money spent
     - Remaining balance
     - Rate of waste (how much you're overspending compared to your planned budget)
     - Total deposits
   - Gain insights into financial habits and make data-driven decisions.

### 5. **Interactive Dashboard with Visualizations**
   - Beautiful, user-friendly dashboard displaying key metrics like:
     - Total available funds
     - Total expenses
     - Remaining balance
   - Data visualizations such as:
     - **Pie charts** to visualize expenses categories
     - **Bar charts** for monthly expense comparisons
     - **Line graphs** to track the progress of your financial goals over time

---

## Technologies Used

- **Python**: The core programming language for financial calculations and logic.
- **Pandas**: Used for handling and processing financial data.
- **Matplotlib**: For creating data visualizations, such as pie charts, bar charts, and line graphs.
- **CSV**: For storing and importing data for persistent record-keeping.
- **Tkinter** (Optional): For adding additional graphical user interface elements (GUI).

---

## Installation

### 1. **Clone the Repository**

Clone the project to your local machine using Git:

```bash
git clone https://github.com/your-username/Budget-Bliss.git
2. Set Up a Virtual Environment
It's recommended to use a virtual environment to manage your project dependencies:

On Windows:
bash
Copy code
python -m venv venv
.\venv\Scripts\activate
On macOS/Linux:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Once the virtual environment is activated, install the required Python libraries using the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
This will install all necessary dependencies, including:

pandas for handling financial data.
matplotlib for creating visualizations.
Tkinter (if needed) for GUI elements.
4. Run the Application
Once the dependencies are installed, you can run the application:

bash
Copy code
python main.py
This will start the Budget Bliss application and you can interact with the system to track and manage your expenses.

Project Structure
The project follows a modular structure for easy navigation and maintenance:

plaintext
Copy code
budget-bliss/
│
├── main.py                  # Main entry point for the application
├── expense_tracker.py       # Handles budget and expense management
├── dashboard.py             # Handles visualizations and analytics
├── requirements.txt         # List of project dependencies
├── README.md                # Project documentation
└── assets/                  # Contains charts and other resources
