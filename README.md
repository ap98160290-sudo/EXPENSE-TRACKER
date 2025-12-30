****FEATURES INCLUDED IN THIS****

Add Income and Expense transactions

Input validation handled in the backend

Automatic unique Transaction ID (UUID) for every transaction

Persistent storage (data saved to file)

View transaction history in DataFrame format

Safe delete with confirmation

Prevents accidental deletion using transaction identity, not row index

Clean Streamlit UI


expense_tracker/
│
├── GUI.py              # Streamlit app
├── tracker.py          # Backend validation + UUID generation
├── storage.py          # Load & save transactions
├── data.json           # Stored transactions (auto-created)
└── README.md           # Project documentation


**TECHNOLOGIES USED**

PYTHON
STREAMLIT
PANDAS 
DATETIME
UUID



******HOW TO RUN THE PROJECT******
INSTALLING DEPENDENCIES:
pip install pandas 

RUN THE STREAMLIT UI:
streamlit run GUI.py
