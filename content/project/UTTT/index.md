---
title: Ultimate Tic-Tac-Toe
summary: Artifically intelligent agent optimized for Ultimate Tic-Tac-Toe game. This Python project implemented the Mini-Max algorithm with alpha-beta pruning and Monte-Carlo search
tags:
  - AIML
date: '2023-12-19T00:00:00Z'

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  # caption: Delete this but its how to caption
  focal_point: Smart

links:
  - icon: file
    icon_pack: fas
    name: Report
    url: https://docs.google.com/document/d/1OOaWsup-7BIKx1tJh2bwaORIzThYFjy7K4TnGg2u_sw/edit?usp=sharing
  - icon: code
    icon_pack: fas
    name: Code
    url: https://github.com/AlexanderBesch/Ultimate-Tic-Tac-Toe/tree/main
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

Ultimate Tic-Tac-Toe (UTTT) represents a sophisticated evolution of the traditional Tic-Tac-Toe game, introducing a heightened level of complexity and strategic depth. Departing from the conventional 3x3 grid, UTTT employs a 9x9 playing grid intricately subdivided into a master 3x3 grid, with each of its cells containing a 3x3 original Tic-Tac-Toe game. This innovative structure, as depicted in the accompanying image, challenges players to achieve victory on the larger scale 'master' Tic-Tac-Toe board.

The focal objective of this project was the development of an intelligent agent capable of outperforming publicly available artificial intelligence counterparts in UTTT. The implementation, programmed in Python, leveraged the Mini-Max algorithm enhanced by Alpha-Beta pruning to optimize computational efficiency. The program boasts a diverse set of agents, including those operating on a Monte Carlo search algorithm, random player, and human player interfaces.

A pivotal aspect of the project lay in the design of a robust heuristic to evaluate and score each game state. The heuristic, finely tuned to incentivize or disincentivize the agent's decisions, operated on the following principles:
 - Sub-boards ending in tie recieved no points
 - each path to win a sub-board gained a small number of points
 - each path to lose a sub-board lost a small number of points
 - each path to win master board gained a large number of points
 - each path to lose master board lost a large number of points

