# LeNet-5 CNN Reproduction Project

## Description
This project is a reproduction of the classic LeNet-5 architecture by LeCun et al. (1998) for handwritten digit recognition. The model is built using Python, TensorFlow, and Keras on the MNIST dataset.

## Features
- Classic LeNet-5 architecture implementation.
- Trained and evaluated on the MNIST dataset.
- Achieved a test accuracy of **98.65%**.
- Includes visualization of CNN feature maps to analyze the model's learning process.

## How to Run
1.  **Set up the environment:**
    ```bash
    python -m venv lenet_env
    # For Windows
    lenet_env\Scripts\activate
    # For Mac/Linux
    source lenet_env/bin/activate
    ```
2.  **Install dependencies:**
    ```bash
    pip install tensorflow numpy matplotlib jupyterlab
    ```
3.  **Run the Jupyter Notebook:**
    ```bash
    jupyter lab
    ```
    Then open the `.ipynb` file and run the cells from top to bottom.

## Results
The model successfully achieved a final test accuracy of **98.65%**.

### Training Performance
*(Yahan aap apne accuracy/loss wale graph ka screenshot laga sakte hain)*

### Feature Map Visualization
*(Yahan aap feature map visualization ka ek screenshot laga sakte hain)*
