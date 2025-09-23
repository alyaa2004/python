# Frameworks_Assignment

This project is a simplified analysis of the **CORD-19 research dataset** (metadata.csv) 
and a basic Streamlit app to explore COVID-19 research papers.

## 🚀 Project Structure
- `data/` → put the `metadata.csv` file here (from Kaggle)
- `notebooks/analysis.ipynb` → Jupyter notebook for data exploration
- `streamlit_app/app.py` → Streamlit app
- `requirements.txt` → required libraries

## 📦 Setup Instructions
1. Clone this repo or extract ZIP
2. Place `metadata.csv` inside `data/`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run Jupyter notebook for analysis:
   ```bash
   jupyter notebook notebooks/analysis.ipynb
   ```
5. Run Streamlit app:
   ```bash
   streamlit run streamlit_app/app.py
   ```

## ✅ Expected Outputs
- Basic stats & cleaning of dataset
- Visualizations (publications by year, top journals, etc.)
- Interactive Streamlit app
