---
title: 3DoF AR Tag Following Robot
summary: Homemade robot with 3 degrees of freedom can track and follow an augmented reality tag. The python program uses the open source opencv arucotag standard and demonstares position-based visual servoing and image-based visual servoing
tags:
  - Mechanical
  - AIML
date: '2023-12-16T00:00:00Z'

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  # caption: Delete this but its how to caption
  focal_point: Smart

links:
  - icon: code
    icon_pack: fas
    name: Code
    url: https://github.com/ryanbelmont/EE5271_Project
  - icon: slideshare
    icon_pack: fab
    name: Presentation
    url: https://docs.google.com/presentation/d/1RgNHFKQKeqjjbgmGjgYJjdZ3IuJDmxuOltNXcgrbcHY/edit?usp=sharing
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

Our team engineered a sophisticated 3 Degree of Freedom AR tag tracking robot, featuring a custom-made chassis crafted from 80/20 T-slot aluminum. Every aspect of the robot's design and construction is meticulously tailored, showcasing a commitment to precision and innovation.

The primary objective of this project was to demonstrate the distinctions between position-based visual servoing and image-based visual servoing. The robot incorporated an ELP 8mp USB camera seamlessly interfaced with a custom Python program. Calibration of the camera was performed utilizing OpenCV's integrated calibration function and a dataset comprising 20 sample images of a 9x6 checkerboard.

In the realm of position-based visual servoing, OpenCV transmitted the AR tag coordinates directly to the movement algorithm. The robot, responding with remarkable accuracy, would adjust its position by 30% of the distance towards the target position above the tag. While effective, this method demanded significant computational resources.

Conversely, in the domain of image-based visual servoing, OpenCV identified the four corners of the AR tag. These corner coordinates were then fed into the movement algorithm, leveraging a timestep of 1 and a Jacobian matrix to orchestrate the robot's precise movement to the desired position. This approach, though faster, exhibited a tendency to overshoot and faced challenges when confronted with substantial changes in the AR tag's position.

