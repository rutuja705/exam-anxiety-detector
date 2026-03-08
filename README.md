# AI Based Exam Anxiety Detector

This project aims to detect exam anxiety levels from text using a fine-tuned BERT model. It includes a FastAPI backend for model inference and a Streamlit frontend for an interactive user interface.

## Project Structure

```
exam_anxiety_project/
│
├── dataset/
│   └── sample_dataset.csv         # Sample dataset containing text and anxiety labels
│
├── notebooks/
│   └── Model_Training.ipynb       # Google Colab notebook for BERT model training
│
├── backend/
│   └── main.py                    # FastAPI application for serving the trained model
│
├── frontend/
│   └── app.py                     # Streamlit application for the user interface
│
├── requirements.txt               # Required Python dependencies
├── .gitignore                     # Git ignore file
└── README.md                      # Project documentation
```

## Setup Instructions

### 1. Environment Setup

Make sure you have Python 3.8+ installed.

```bash
# Clone the repository (if on GitHub)
git clone <your-github-repo-url>
cd exam_anxiety_project

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Model Training (Google Colab)

To train the model:
1. Upload the `notebooks/Model_Training.ipynb` to Google Colab.
2. Upload the `dataset/sample_dataset.csv` to the Colab environment.
3. Run all the cells in the notebook.
4. Once training is complete, download the saved model folder (e.g., `saved_model/`) and place it inside the `backend/` directory. 

*Note: For the backend to work locally, you must have the trained model saved in `backend/saved_model/`.*

### 3. Running the Backend API

The backend uses FastAPI. Ensure the `saved_model` directory is present in the `backend` folder.

```bash
cd backend
uvicorn main:app --reload
```
The backend API will be running at `http://127.0.0.1:8000`. You can access the Swagger UI documentation at `http://127.0.0.1:8000/docs`.

### 4. Running the Frontend UI

Open a new terminal window, activate the virtual environment, and run the Streamlit app.

```bash
cd frontend
streamlit run app.py
```
The frontend UI will be running at `http://localhost:8501`.

## Uploading to GitHub

1. Initialize git in the root folder: `git init`
2. Add files: `git add .`
3. Commit: `git commit -m "Initial commit"`
4. Link to your repository: `git remote add origin <your-repo-url>`
5. Push the code: `git push -u origin main`

*Important: Add `backend/saved_model/` to your `.gitignore` if the model files are too large for GitHub. You can use Git LFS for large files.*

## Model Download

The trained model file is hosted on Google Drive due to GitHub's 100MB file limit.

Download here:
https://drive.google.com/file/d/183S8QUx9eY30ZoabqWzvvIEljNlA9FBT/view?usp=sharing
