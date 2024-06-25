# Flood Monitoring and Warning System

![System Overview](https://github.com/ShijiroHikiro/FYP-Machine-Learning/assets/169379608/3991b40a-bb30-4aea-84a9-b2a39ecd573c)

## Overview

Flood monitoring and warning systems are essential in mitigating damage to property and loss of life. These systems can significantly reduce the recovery burden on governments post-flood. This project aims to provide timely warnings to residents and relevant organizations to prepare for imminent floods. The system also monitors and displays critical data that helps identify the causes of floods. Utilizing machine learning, it makes predictions based on rainfall frequency and river water depth data.

## Features

- Real-time flood monitoring
- Early warning notifications
- Data visualization of flood-related metrics
- Prediction models using K-Nearest Neighbor (KNN) and Decision Tree (DT) algorithms

## System Architecture

![System Architecture](https://github.com/ShijiroHikiro/FYP-Machine-Learning/assets/169379608/5ea6dee5-06d2-4808-be62-ebc12e1c514f)

The diagram above illustrates the system's architecture. The process flow is as follows:
1. **Data Input**: The system receives datasets containing rainfall frequency and river water depth.
2. **Machine Learning Models**: Both KNN and DT models process the data simultaneously.
3. **Training and Testing**: The datasets are split into training and testing sets to build accurate models.
4. **Monitoring and Alerts**: If a potential flood is detected, the system sends notifications to citizens and relevant departments.

## Result and Discussion

<p align="center">
  <img src="https://github.com/ShijiroHikiro/FYP-Machine-Learning/assets/169379608/0253c84d-3ac8-4b60-b73e-00800766bfa7" alt="Picture1" width="45%"/>
  <img src="https://github.com/ShijiroHikiro/FYP-Machine-Learning/assets/169379608/6f39bf6d-21e8-42b4-b3de-410d4da1f9d5" alt="Slide3" width="45%"/>
</p>

# Model Performance Comparison

## Accuracy Comparison

**K-Nearest Neighbors (KNN)**

- **Achieved Accuracy:** 87.5%
  - KNN correctly predicts the target variable for 87.5% of the test set instances.

**Decision Tree (DT)**

- **Achieved Accuracy:** 79.17%
  - DT correctly predicts the target variable for 79.17% of the test set instances.

**Conclusion on Accuracy**

- KNN outperforms the Decision Tree model with a higher accuracy of 87.5% compared to DT's 79.17%.
- Despite DT's performance, it struggles with capturing complex relationships or patterns in the data, leading to lower accuracy.

---

## ROC Curve Comparison

**K-Nearest Neighbors (KNN)**

- **ROC Value:** 87.76%
  - Indicates a high true positive rate while maintaining a low false positive rate.
  - Demonstrates KNN's effectiveness in identifying correct positive examples and reducing false positives.

**Decision Tree (DT)**

- **ROC Value:** 69.58%
  - Indicates a moderate true positive rate but with a higher false positive rate.
  - Reflects lower overall performance compared to the KNN model.

**Conclusion on ROC Curve**

- The ROC curve for KNN shows better performance in distinguishing between positive and negative cases compared to the DT model.
- KNN's higher ROC value signifies its superiority in classification performance over the DT model.

---
