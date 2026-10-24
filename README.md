# 🍽️ Fitometer — AI-Powered Food Recognition & Nutrition Analysis

**Fitometer** is an AI-powered food recognition and nutrition analysis web application built using **Python, TensorFlow, and Streamlit**.

It allows users to upload an image of food, recognize the food using a deep learning model trained on the **Food-101 dataset**, and view estimated nutritional information based on the selected serving size.

---

## ✨ Features

- 📸 **AI Food Recognition**
  - Upload an image of a food item.
  - Identify the food using a deep learning model.

- 🥗 **Nutrition Analysis**
  - Get estimated values for:
    - Calories
    - Protein
    - Carbohydrates
    - Fat
    - Fiber
    - Sugar
    - Sodium

- ⚖️ **Serving Size Calculation**
  - Adjust nutritional values according to serving size.

- 📊 **Interactive Visualizations**
  - View nutrition information through interactive charts.

- 📋 **Nutrition Summary**
  - Get a clear and structured nutrition summary.

- 🎨 **Streamlit Web Interface**
  - Simple and user-friendly interface for food recognition and analysis.

---

## 🧠 Machine Learning

Fitometer uses a deep learning image-classification model trained using the **Food-101 dataset**.

### Food-101 Dataset

The Food-101 dataset contains:

- **101 food categories**
- **75,750 training images**
- **25,250 testing images**
- **101,000 images in total**

The model learns visual features from food images and predicts the most likely food category from an uploaded image.

### ML Pipeline

```text
Food Image
     ↓
Image Preprocessing
     ↓
Deep Learning Model
     ↓
Food Classification
     ↓
Recognized Food
     ↓
Nutrition Information
     ↓
Serving Size Adjustment
     ↓
Nutrition Analysis
```

---

## 🛠️ Tech Stack

### Programming
- Python

### Machine Learning & Deep Learning
- TensorFlow
- Scikit-learn
- NumPy
- Pandas

### Computer Vision
- OpenCV
- Pillow

### Web Application
- Streamlit

### Data Visualization
- Matplotlib
- Plotly

### Development Tools
- Jupyter Notebook
- VS Code
- Git
- GitHub

---

## 📂 Project Structure

```text
fitometer/
│
├── artifacts/
│   └── trained models and generated artifacts
│
├── config/
│   └── configuration files
│
├── datasets/
│   └── dataset-related files
│
├── notebooks/
│   └── experimentation and analysis
│
├── src/
│   ├── components/
│   ├── DataIngestion/
│   ├── DataTransformation/
│   └── ...
│
├── views/
│   └── Streamlit UI components
│
├── app.py
├── train.py
├── check_dataset.py
├── test.py
├── test_yml.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Subhasish-01/fitimeter.git
```

```bash
cd fitimeter
```

### 2. Create a Virtual Environment

Using Python:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Or using Conda:

```bash
conda create -p venv python=3.11 -y
```

Activate the environment:

```bash
conda activate ./venv
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📸 How Fitometer Works

### Step 1 — Upload Food Image

Upload an image of the food you want to analyze.

### Step 2 — AI Prediction

The TensorFlow model processes the image and predicts the food category.

### Step 3 — Nutrition Lookup

The predicted food is matched with its corresponding nutritional information.

### Step 4 — Select Serving Size

Choose the desired serving size.

### Step 5 — View Nutrition

Fitometer displays the estimated:

```text
Calories
Protein
Carbohydrates
Fat
Fiber
Sugar
Sodium
```

---

## 📊 Example Nutrition Output

| Nutrient | Amount |
|---|---:|
| 🔥 Calories | — kcal |
| 💪 Protein | — g |
| 🍚 Carbohydrates | — g |
| 🥑 Fat | — g |
| 🌾 Fiber | — g |
| 🍬 Sugar | — g |
| 🧂 Sodium | — mg |

> **Note:** Nutritional values are estimates and can vary depending on ingredients, preparation method, and serving size.

---

## 🎯 Project Objectives

The main objectives of Fitometer are:

- Apply deep learning to real-world food image classification.
- Build an AI-powered nutrition analysis application.
- Make food recognition simple and accessible.
- Provide useful nutritional estimates.
- Gain practical experience with TensorFlow and computer vision.
- Build and deploy a complete Streamlit-based ML application.

---

## 🔮 Future Improvements

Some planned improvements include:

- 🔍 Improve food recognition accuracy.
- 🍱 Detect multiple food items from a single image.
- 🧠 Experiment with more advanced deep learning architectures.
- 📱 Improve mobile responsiveness.
- 👤 Add user profiles and nutrition history.
- 📈 Add daily and weekly nutrition tracking.
- 🎯 Add personalized calorie and nutrition goals.
- 🏃 Integrate fitness and activity tracking.
- 💬 Add an AI nutrition assistant.
- ☁️ Deploy the application publicly.

---

## ⚠️ Disclaimer

Fitometer provides **estimated nutritional information** for educational and informational purposes only.

The predictions and nutrition values should not be considered a substitute for professional medical, dietary, or nutritional advice.

---

**GitHub Repository:**  
https://github.com/Subhasish-01/fitimeter
