# Word Hunt Solver
This is a web application developed with React and Flask that helps users improve their skills at the GamePigeon's Word Hunt while learning new words along the way! The application allows you to input letters into a 4x4 grid, find all possible valid words, and display the definitions and paths of those words.

## Features
4x4 Letter Grid: Input letters into a 4x4 grid to form potential words.
Word Finding: Finds all valid words based on the inputted letters.
Word Definitions: Hover over the words to see their definitions and the path they follow on the grid.
Path Visualization: Highlight the positions on the grid where each word is found.
Purpose
The goal of this project is to help players get better at Pigeon's Word Hunt by showing possible words and allowing them to learn new words with ease by seeing their definitions.

## Demo

![](https://github.com/frankliuuu/Word-Hunt-Solver-and-Learner/blob/main/wh_demo.gif)

## How to Use
Clone or download this repository.

Install all required dependencies:

npm install

To start the application, run the following commands in separate terminals:

Start the frontend:

npm run dev

Start the backend:


python -m src.backend.app

Open your browser and go to http://localhost:3000 to access the app.

## How to play:

Input letters into the 4x4 grid.
Press Solve to find all valid words.
Hover over any word to highlight the path on the grid and view the word's definition.

## Credits 
dictionary.json from https://github.com/matthewreagan/WebstersEnglishDictionary
