# Titanic - Exploratory Data Analysis (EDA) 🚢  
This project analyzes the Titanic dataset to uncover survival patterns based on factors like age, gender, and class. It includes data cleaning, visualization,  using Pandas, Matplotlib, and Seaborn.


## 📊 Dataset  
The dataset is sourced from the `sns.load_dataset("titanic")` function in Seaborn.  
It contains the following columns:  

- `survived` → Survival status (0 = No, 1 = Yes)  
- `pclass` → Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)  
- `sex` → Gender of passenger  
- `age` → Age of passenger  
- `sibsp` → Number of siblings/spouses aboard  
- `parch` → Number of parents/children aboard  
- `fare` → Ticket fare  
- `embarked` → Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)  
- `who` → Categorization of passenger (man, woman, child)  
- `deck` → Deck level (A, B, C, etc.)  
- `alone` → Whether the passenger was alone (True/False)  
## 🛠 Technologies Used  
- Python  
- Pandas  
- Seaborn  
- Matplotlib  
- NumPy

- ### ** EDA Process & Key Insights**  
```md 
- **Data Cleaning**:  
  - Handling missing values in `age`, `deck`, and `embarked` columns.  
- **Data Visualization**:  
  - Survival rate by gender → Women had a higher survival rate.  
  - Survival rate by ticket class → 1st-class passengers had a higher survival rate.  
  - Age distribution → Most passengers were between 20-40 years old.  
  - Correlation analysis → `pclass` and `fare` significantly impact survival.  

- Jupyter Notebook  
