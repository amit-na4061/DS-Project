# Second-Hand Car Price Prediction Using ANN  
This repository contains a machine learning project to predict the price of second-hand cars using Artificial Neural Networks (ANN) with the CRISP-DM methodology. The model achieved a **training accuracy of 89%** and a **test accuracy of 93%**, demonstrating its strong performance in predicting car prices.  

## Project Overview  
Accurately predicting the price of second-hand cars helps buyers and sellers make informed decisions. This project uses CRISP-DM methodology to ensure a structured approach to data mining and prediction tasks, combined with the power of ANN for achieving accurate price predictions.  

## CRISP-DM Methodology  

1. **Business Understanding**  
   - Objective: Build a predictive model to estimate the price of used cars based on their features.
   - Value: Assist stakeholders in making data-driven decisions for car pricing.  

2. **Data Understanding**  
   - Data Source: Dataset contains features such as car brand, model, age, mileage, fuel type, transmission, and other relevant attributes.
   - Exploratory Analysis: Inspected for patterns, distributions, and missing values.

3. **Data Preparation**  
   - Data cleaning: Handled missing values and outliers.
   - Feature engineering: Transformed categorical variables into numerical values using one-hot encoding.
   - Data scaling: Normalized numerical features for ANN compatibility.
   - Split: Dataset divided into training and test sets.

4. **Modeling**  
   - Architecture: Built a fully connected ANN using TensorFlow/Keras with the following specifications:
     - Input layer matching the number of features.
     - Hidden layers with appropriate activation functions.
     - Output layer for regression tasks (linear activation).
   - Loss function: Mean Squared Error (MSE).  
   - Optimizer: Adam.

5. **Evaluation**  
   - Achieved **89% accuracy on training data** and **93% accuracy on test data**.  
   - Performance metrics: Mean Absolute Error (MAE), R² score.

6. **Deployment**  
   - Not covered in this repository but could be extended to create a web app for predicting car prices.

## Dependencies  
- Python 3.8+
- Libraries:  
  ```
  numpy  
  pandas  
  matplotlib  
  seaborn  
  tensorflow  
  sklearn  
  ```

## Installation  
1. Clone the repository:  
   ```
   git clone https://github.com/your-username/second-hand-car-price-prediction
   cd second-hand-car-price-prediction
   ```
2. Install dependencies:  
   ```
   pip install -r requirements.txt
   ```

## Usage  
1. Place the dataset in the `data` folder.
2. Run the Jupyter Notebook or Python scripts in the `src` folder for each step of the CRISP-DM methodology.
3. Evaluate results and modify hyperparameters for optimization if necessary.  

## Results  
- **Training Accuracy:** 89%  
- **Test Accuracy:** 93%  
- Detailed evaluation metrics and visualizations are included in the notebook.  

## Future Work  
- Improve model performance by experimenting with advanced architectures and hyperparameters.  
- Add deployment pipeline for real-world usability.  
- Expand features by integrating external data sources (e.g., market trends).  

## Contributing  
Feel free to fork this repository, create a feature branch, and submit a pull request for contributions.
