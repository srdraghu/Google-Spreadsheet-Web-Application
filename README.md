# Google Sheets Clone Documentation

**Author:** Raghu Dharsan S  
**GitHub Repository:** [Google-Spreadsheet-Web-Application](https://github.com/srdraghu/Google-Spreadsheet-Web-Application)

---

## Introduction
This project is a web application that closely mimics Google Sheets, built using Flask for the backend and React for the frontend. It supports data entry, mathematical operations, and key UI interactions similar to Google Sheets.

## Features
- Create and manage multiple sheets.
- Update individual cell values dynamically.
- Evaluate mathematical expressions.
- Simple spreadsheet UI with editable cells.

---

## Project Structure
```
google_sheets_clone/
│── backend/
│   ├── app.py        # Flask application
│   ├── models.py     # Database models (future expansion)
│   ├── routes.py     # API routes
│   ├── services.py   # Business logic
│   ├── requirements.txt  # Dependencies
│── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Spreadsheet.js  # Spreadsheet UI
│   │   │   ├── Cell.js         # Individual cell component
│   │   ├── pages/
│   │   │   ├── Home.js         # Home page
│   │   ├── App.js              # Main App Component
│   │   ├── index.js            # React entry point
│   ├── package.json            # Dependencies
│── database/
│   ├── schema.sql              # Database schema (future expansion)
│── README.md                   # Project documentation
```

---

## Backend (Flask)
The backend is built using Flask and provides the following API endpoints:

### Endpoints:
- **POST /sheets** – Create a new sheet.
- **GET /sheets/<sheet_id>** – Retrieve a sheet.
- **PUT /cells/<sheet_id>** – Update a specific cell.
- **POST /evaluate** – Evaluate a mathematical expression.

### Dependencies:
Install the required dependencies using:
```
pip install -r requirements.txt
```

Run the backend server:
```
python app.py
```

---

## Frontend (React)
The frontend is built using React and displays a simple spreadsheet interface.

### Setup & Run:
```
npm install
npm start
```

### Features:
- Editable table-like UI.
- Dynamically updates cell values.
- Calls backend API for processing.

---

## Future Enhancements
- Implement user authentication.
- Persistent database storage for sheets.
- Support for advanced formulas and functions.
- Real-time collaboration features.

---

## License
This project is open-source and free to use. Contributions are welcome!

---

## Contact


