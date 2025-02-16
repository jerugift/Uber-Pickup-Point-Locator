# Uber Pick-up Point Locator

## Introduction
The **Uber Pick-up Point Locator** is a Python-based project that analyzes Uber trip data in New York City for April 2014. It uses **K-Means clustering** to identify optimal pickup points based on trip locations. The project is built with **pandas, matplotlib, scikit-learn, folium, and Streamlit** to provide both analytical insights and an interactive visualization of pickup points.

## Features
- **Data Analysis:** Reads Uber trip data and performs clustering on latitude and longitude coordinates.
- **K-Means Clustering:** Uses the elbow method to determine the optimal number of clusters and identifies key pickup points.
- **Visualization:**
  - Scatter plots of trip locations.
  - Clustering results with centroid markers.
  - Interactive maps with folium to visualize pickup points.
- **Streamlit Integration:** Provides a web-based interface for users to interact with the pickup point locator.
- **Closest Pickup Point Finder:** Predicts the nearest Uber pickup point for specific locations like Lincoln Center and Howard Beach.

---

## Requirements

### Libraries
Ensure the following Python libraries are installed:
- **pandas**: For data manipulation
- **matplotlib**: For plotting data
- **streamlit**: For the interactive web interface
- **folium**: For creating interactive maps
- **scikit-learn**: For performing K-Means clustering

To install the required libraries, run:
```bash
pip install pandas matplotlib streamlit folium scikit-learn
```

### Dataset
Download the dataset `uber-raw-data-apr14.csv` and place it in the project directory.

---

## How to Run the Project

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/uber-pickup-point-locator.git
cd uber-pickup-point-locator
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit App**
```bash
streamlit run app.py
```

4. **Interact with the App**
   - The app will open in your default browser.
   - View Uber trip locations and optimized pickup points.
   - Find the nearest pickup point for specific locations.

---

## Application Workflow

1. **Load Data**
   - The dataset `uber-raw-data-apr14.csv` is loaded.
   - The first few rows of the data are displayed.

2. **Visualize Trip Locations**
   - Scatter plots show the distribution of Uber trips across New York.

3. **Cluster Analysis (K-Means)**
   - The elbow method is used to determine the optimal number of clusters.
   - K-Means clustering groups the trip locations into **7 pickup points**.
   - The cluster centroids are displayed on a folium map.

4. **Interactive Pickup Point Locator**
   - The app predicts the closest Uber pickup point for given locations (e.g., Lincoln Center, Howard Beach).
   - The results are visualized on an interactive map.

---

## Folder Structure
```
|-- app.py                 # Main Python script for Streamlit app
|-- uber-raw-data-apr14.csv # Uber trip dataset
|-- README.md              # Documentation
|-- requirements.txt       # List of dependencies
```

---

## Known Limitations
- The dataset is limited to Uber trips from April 2014.
- The clustering results depend on the number of clusters chosen (fixed at 7 for this project).
- The accuracy of pickup points may be affected by noise in the dataset.

---

## Future Enhancements
- **Real-time Data Integration:** Incorporate live Uber trip data.
- **User-defined Clusters:** Allow users to specify the number of clusters dynamically.
- **Enhanced Mapping:** Improve visualization with additional map layers and filters.

---

## License
This project is open-source and licensed under the MIT License.

---



