---
title: Robotic Tool Sorter
summary: Developed a program to use a Universal Robots UR5 to sort tools. Python program utilizes tensorflow library for deep learning of tool image datasets.
tags:
  - AIML
date: '2022-11-23T00:00:00Z'

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  # caption: Delete this but its how to caption
  focal_point: Smart

links:
  - icon: robot
    icon_pack: fas
    name: UR5
    url: https://universal-robots.com/products/ur5-robot/
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

I successfully implemented a robust tool sorting solution using the Universal Robots UR5, a 6 degree of freedom robotic arm known for its versatility. For this project, precision was achieved by integrating a Robotiq 2-finger gripper and a wrist camera seamlessly to the robot's end. The system was designed to enable users to place a variety of tools such as wrenches, hammers, screwdrivers, or pliers on a table. Leveraging Google's Tensorflow library in a Python program, the system exhibited an outstanding tool detection and sorting accuracy of 99.9%.

The training of the Tensorflow model involved an extensive dataset, comprising over 100 images of each tool captured under similar lighting conditions. Rigorous image augmentation using OpenCV and Numpy Python libraries contributed to the diversification of the dataset. The Tensorflow model was meticulously trained until surpassing a remarkable 95% accuracy threshold. Ultimately, the deployed model achieved an impressive accuracy rate of 99.9%. The robot's manipulation capabilities were orchestrated through the Universal Robots Python library, ensuring seamless and precise control.

Unfortunately, owing to the inclusion of classroom materials in the project, sharing specific code files or reports is not possible.