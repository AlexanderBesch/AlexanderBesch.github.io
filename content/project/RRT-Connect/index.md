---
title: RRT-Connect Maze Solving Turtlebot
summary: Developed a maze-solving robot using RRT-Connect pathfinding algorithm in Python. This project involved simulating the maze environment in Gazebo, calculating precise motor commands, and successfully implementing the solution to navigate the robot through a real-world maze.
tags:
  - AIML
date: '2024-08-11T00:00:00Z'

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  # caption: Delete this but its how to caption
  focal_point: Smart

links:
  # - icon: file
  #   icon_pack: fas
  #   name: Presentation
  #   url: https://docs.google.com/document/d/1OOaWsup-7BIKx1tJh2bwaORIzThYFjy7K4TnGg2u_sw/edit?usp=sharing
url_pdf: ''
url_slides: 'https://docs.google.com/presentation/d/17QvVM9cHbNQrQKbmGGVxUwiExdmBg5uO/edit?usp=sharing&ouid=114055234090021165868&rtpof=true&sd=true'
url_video: 'https://docs.google.com/presentation/d/17QvVM9cHbNQrQKbmGGVxUwiExdmBg5uO/edit?usp=sharing&ouid=114055234090021165868&rtpof=true&sd=true'

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

The RRT-Connect Maze Solving Robot project represents an advanced application of robotics and pathfinding algorithms to navigate complex environments. This project involves placing a robot in a maze with a known map and leveraging sophisticated computational techniques to guide the robot to its destination.

The core objective was to develop and implement an effective pathfinding solution using the Rapidly-exploring Random Tree (RRT) algorithm, specifically the RRT-Connect variant. The implementation, executed in Python, involved scaling the map and running the RRT-Connect algorithm to generate an efficient path through the maze. Motor commands were then derived from the pathfinding solution to navigate the robot through the maze.

Key aspects of the project included:
 - Algorithm Implementation: Utilized the RRT-Connect algorithm to efficiently explore and connect feasible paths in the maze. This approach ensures rapid convergence to the goal by connecting two rapidly-exploring trees in the search space.
 - Simulation and Testing: Employed the Gazebo simulation environment to model the maze and simulate the robot's movements. This simulation allowed for extensive testing and fine-tuning of the pathfinding algorithm before real-world deployment.
 - Real-World Execution: After validating the pathfinding solution in the simulation, implemented the algorithm on a physical robot. The robot executed the motor commands derived from the simulation to navigate through the actual maze, successfully reaching the destination.
A critical element of the project was ensuring the robot's successful traversal of the maze by accurately translating the algorithm's output into practical motor commands. This involved addressing real-world challenges such as sensor accuracy, motor control, and environment interaction to achieve seamless performance in both simulated and real-world scenarios.

Unfortunately, due to the project being built upon small amounts of classroom materials, code cannot be shared.