---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* B.Tech in Computer Science Engineering, Guru Gobind Singh Indraprastha University, Delhi, 2019-2023
  * GPA: 9.6/10

Work experience
======
* January 2025 - Present: Associate ML Scientist - 2
  * Wadhwani Institute for Artificial Intelligence, Delhi, India
  * Developing computer vision models for crop monitoring using Joint Positional Embedding models
  * Applying MAE (Masked Autoencoder) style pretraining strategies for region-specific pest recognition
  * Evaluating and fine-tuning Open Source Vision Language Models (VLMs) for agricultural applications
  * Leading pest monitoring projects with teams of ML analysts and interns

* July 2023 - January 2025: Associate ML Scientist - 1
  * Wadhwani Institute for Artificial Intelligence, Delhi, India
  * Automated image classification model development, reducing development time from 5 hours to under 1 hour
  * Streamlined ML deployment pipeline, accelerating releases from 5 days to under 1 day
  * Enhanced model reliability using dataset cartography techniques and Class Activation Maps (CAMs)
  * Developed and deployed Crop Yield Estimation solution with agronomist-validated feature importance
  * Advanced CottonAce project with synthetic image generation for national deployment

* February 2023 - July 2023: ML Intern
  * Wadhwani Institute for Artificial Intelligence, Delhi, India
  * Developed and evaluated novel model distillation techniques for object detection and counting models
  * Optimized model performance and efficiency through various distillation strategies
  * Analyzed and improved cascade models including OOD detectors for edge devices

* August 2022 - February 2023: Research Intern
  * Indian Institute of Technology Delhi
  * Worked under Prof. Chetan Arora and Prof. M. Balakrishnan on MAVI project
  * Research on gall bladder cancer detection from ultrasonography images
  * Focus on Vision Transformers explainability, Weakly supervised object detection, and Multiple instance learning

* June 2022 - August 2022: Summer Research Fellow
  * Indian Institute of Technology Delhi
  * Optimized deep learning models for scene-text recognition using edge devices
  * Refactored and upgraded existing models to latest firmware versions (OpenVINO 2022, PyCam 2.0)
  * Converted and tested VisionLAN to ONNX and OpenVINO IR formats
  
Skills
======
* **Programming Languages**: Python, C++, Java, JavaScript, C
* **Machine Learning & Deep Learning**: PyTorch, TensorFlow, Keras, TensorFlow.js
* **Computer Vision**: OpenCV, YOLO, Object Detection, Image Classification
* **Web Technologies**: Flask, HTML/CSS, Git, AWS, GCP, Azure
* **Databases**: MySQL, PostgreSQL, LaTeX, Scikit Learn
* **Specialized Areas**: Agricultural AI, Medical Image Analysis, Edge Computing, Model Explainability

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Awards and Honors
======
* **2023**: Finalist, Singapore India Hackathon 2023 [Nanyang Technological University and Ministry of Education India]
* **2022**: Winner, UNESCO India Africa Hackathon 2022 [Ministry of Education of India]
* **2022**: Winner, Smart India Hackathon 2022 (Software Edition) [Ministry of Education of India]
* **2022**: Selected as UG Summer Research Fellow @ IIT Delhi

Service and leadership
======
* Project lead for pest monitoring at Wadhwani Institute for Artificial Intelligence
* Led teams of ML analysts and interns in agricultural AI projects
* Contributed to national deployment of CottonAce project within Ministry of Agriculture and Farmers Welfare's National Pest Surveillance System
