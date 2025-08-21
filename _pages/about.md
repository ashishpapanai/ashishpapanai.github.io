---
permalink: /
title: "Ashish Papanai - Machine Learning Researcher"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

# Ashish Papanai

**Incoming MSc Machine Learning Student**  
*University of Tübingen*  
*ELIZA Master's Scholarship Recipient*

## Overview

I am an incoming MSc Machine Learning student at the University of Tübingen, selected for the prestigious ELIZA Master's Scholarship. Previously, I worked as an Associate ML Scientist at the Wadhwani Institute for Artificial Intelligence, where I specialized in computer vision and agricultural AI applications.

My research focuses on developing innovative solutions for crop monitoring, pest detection, and yield estimation using advanced deep learning techniques. I have extensive experience in computer vision, model optimization, and deploying AI systems in real-world agricultural applications.

## Research Interests

- **AI Security & Trustworthy AI**: Developing robust and secure AI systems
- **Computer Vision**: Advanced deep learning for image analysis
- **Medical Image AI**: Healthcare applications and diagnostic assistance
- **AI for Social Good**: Agricultural technology and assistive technologies
- **Model Explainability**: Interpretable AI for real-world deployment

## Latest Publications

{% assign sorted_publications = site.publications | sort: 'date' | reverse %}
{% for publication in sorted_publications limit:3 %}
### [{{ publication.title }}]({{ publication.url }})
*{{ publication.venue }} - {{ publication.date | date: "%B %Y" }}*

{{ publication.excerpt }}

**Authors:** {{ publication.authors }}

[Read more →](/publications/)
{% unless forloop.last %}
---
{% endunless %}
{% endfor %}

## Latest News & Updates

{% assign sorted_posts = site.posts | sort: 'date' | reverse %}
{% for post in sorted_posts limit:3 %}
### [{{ post.title }}]({{ post.url }})
*{{ post.date | date: "%B %d, %Y" }}*

{{ post.excerpt }}

[Read more →](/posts/)
{% unless forloop.last %}
---
{% endunless %}
{% endfor %}

## Quick Links

- **[Experience & Professional Background](/experience/)** - Detailed work history and achievements
- **[Publications](/publications/)** - Complete research publications
- **[Projects](/projects/)** - Technical projects and implementations
- **[Skills & Expertise](/skills/)** - Technical skills and competencies

## Contact Information

- **Email**: ashishpapanai00 [at] gmail [dot] com
- **Location**: Delhi, India
- **LinkedIn**: [ashishpapanai](https://www.linkedin.com/in/ashishpapanai/)
- **GitHub**: [ashishpapanai](https://github.com/ashishpapanai/)
- **Google Scholar**: [Ashish Papanai](https://scholar.google.com/citations?user=MpzridIAAAAJ&hl=en)
- **X (Twitter)**: [@ashishpapanai1](https://x.com/ashishpapanai1)
