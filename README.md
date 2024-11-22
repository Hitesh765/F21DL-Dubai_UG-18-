# F21DL-Dubai_UG-18-
# Image Classification and IPL Winner Prediction
Classifying images of balls into predefined categories.
Predicting the winner of IPL matches based on match data.

## **Group Members**
- Member 1: Daksh Luhana
- Member 2: Yohann Simon
- Member 3: Vinay Nankani
- Member 4: Hitesh Wadhwani
- Member 5: Neola Castelino


---

## **Project Milestones**
| **Milestone**                     | **Expected Completion** |
|------------------------------------|--------------------------|
| Dataset Collection and Cleaning    | Week 2,3                  |
| Exploratory Data Analysis (EDA)    | Week 4                  |
| Clustering Analysis (R3)           | Week 5,6                  |
| Initial Model Implementation (R4) | Week 7                  |
| Neural Network Implementation (R5)| Week 8                  |
| Model Evaluation and Reporting     | Week 9                  |

---

## **Dataset Sources**
### a. **True Source**:
- The dataset is sourced from [Kaggle IPL Dataset](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020).
- The dataset is sourced from [Kaggle Sports Ball Dataset](https://www.kaggle.com/datasets/mdkabinhasan/sports-ball-dataset?resource=download).

### b. **Original License**:
- Database Contents License (DbCL) v1.0
- MIT

### c. **Examples from the Dataset**:
#### IPL DATASET
| Season   | City        | Date       | match_type | Player_of_the_Match | Venue                                       | Team 1                   | Team 2                | Toss_Winner                | Toss_Decision | Winner                   | Result | Result_Margin | Target_Runs |Target_Overs  |Super_Over |Method | Umpire 1| Umpire 2|   
|----------|-------------|------------|------------|---------------------|---------------------------------------------|--------------------------|-----------------------|----------------------------|---------------|--------------------------|----------|------------|----------------|----------------|-------|------------|---------------|------------|
| 2007/08  | Bangalore   | 2008-04-18 | League     | BB McCullum         | M Chinnaswamy Stadium                       | Royal Challengers Bangalore | Kolkata Knight Riders | Royal Challengers Bangalore | field         | Kolkata Knight Riders | runs     | 140        | 223            | 20             | N     | NA         | Asad Rauf     | RE Koertzen |
| 2007/08  | Chandigarh  | 2008-04-19 | League     | MEK Hussey          | Punjab Cricket Association Stadium, Mohali | Kings XI Punjab          | Chennai Super Kings  | Chennai Super Kings       | bat           | Chennai Super Kings    | runs     | 33         | 241            | 20             | N     | NA         | MR Benson     | SL Shastri  |
#### Sports Ball DATASET
![00c69db5-6467-4b3f-a035-6d542dfa2c31](https://github.com/user-attachments/assets/f75ab8d8-db34-42e2-a09b-33b65215a9ca)



![061be72b-99bf-43f5-af05-25f11e471857-2](https://github.com/user-attachments/assets/5805003c-491d-4ded-98f9-fdf2c7746f7a)

---

## **Data Preparation Pipeline**

---

Follow the steps mentioned here: [Python Scripts](https://github.com/Hitesh765/F21DL-Dubai_UG-18-/blob/main/Python%20Scripts/Readme.md)

---

## **Project Description**

---

### *R2: Data Preprocessing, Data Augmentation, and EDA*
In R2, exploratory data analysis (EDA) was performed to understand the structure and quality of the datasets. For the IPL dataset, visualizations such as bar plots, histograms, and correlation heatmaps highlighted key patterns like the impact of toss decisions and venues on match outcomes. For the image dataset, preprocessing involved resizing images to 123px × 100px, cropping a 20px banner, and balancing class distributions to a maximum of 400 images per class. Data augmentation, including horizontal flipping, enriched underrepresented classes. Dummy bounding boxes were merged with metadata. Both EDA and augmentation ensured data readiness for subsequent modeling tasks.

### *R3: Clustering*
Clustering was used as an unsupervised technique to explore patterns in both datasets. In the IPL dataset, k-means clustering segmented venues, teams, and toss dynamics, identifying key groupings like high-scoring venues and dominant teams. For the image dataset, high-dimensional RGB data was analyzed using feature reduction, followed by clustering with methods like k-means and hierarchical clustering. These methods revealed overlaps and separability among classes, providing insights into feature quality. Performance metrics like inertia and clustering accuracy informed preprocessing adjustments and feature selection strategies. This analysis uncovered hidden patterns and relationships in the data, guiding further tasks.

---

### *R4: Fundamental Algorithms*
This stage focused on implementing baseline models to compare performance across datasets. For the IPL dataset, Random Forest, Decision Tree, and KNN models were used to predict match outcomes based on features like venue, toss, and team performance. For the image dataset, Logistic Regression, Decision Trees, and Random Forests were applied to classify images. Both datasets underwent robust evaluation using metrics such as accuracy, precision, recall, and F1 score. Visualizations like confusion matrices and ROC curves analyzed prediction quality. These models served as benchmarks for subsequent deep learning approaches, providing insights into data separability and model robustness.

---

### *R5: Advanced Modeling*
Advanced modeling introduced deep learning techniques for both datasets. For the IPL dataset, a Multi-Layer Perceptron (MLP) with two hidden layers was implemented, leveraging preprocessed features to enhance prediction accuracy. For the image dataset, both MLPs and Convolutional Neural Networks (CNNs) were developed. CNNs utilized spatial hierarchies with convolutional and pooling layers, followed by dense layers for classification. Models were evaluated using metrics like accuracy and loss, demonstrating the power of neural networks in handling complex patterns. This stage highlighted the superiority of deep learning over traditional models for both tabular and image datasets.

## **File/Folder Purpose**

---

| File/Folder | Purpose                                           |
|-------------|---------------------------------------------------|
| `Data/`     | Stores link to the datasets.               |
| `Documents/`  | Contains Weekly updates of the work done. |
| `Notebooks/`   | Contains Machine learning portfolio for both the datasets.        |
| `Python Scripts/`   | Contains the pipeline to download the dataset from Kaggle.        |
| `Report/`  | Containsresults and discussions for the experiments done on our datasets .    |

---
