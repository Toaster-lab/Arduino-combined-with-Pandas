# Arduino + Pandas Data Analysis

## Project Overview

*Mini weather station*
I build two circuits, one just for testing and seeing if the idea would even work.
The second one is the main one we will actually use to get our data from.
The data will be processed and analyse for a quick overview of the weather where I live.

## Goal

The main goal of this project was to learn more about electrical circuits and electronics by building and experimenting with an Arduino-based system.
I also wanted to learn and apply C++ for Arduino programming, 
reuse my Python and Pandas skills to analyze collected data, 
integrate Git and GitHub into my workflow, 
and combine hardware, programming, and data analysis in one project.

## Hardware

* Arduino: Mega(main circuit), Uno(Prototype)
* temperature/humidity: DHT11
* rain sensor
* light sensor: BH1750

## Software

* VsCode
* Arduino IDE
   * DHT libary
   * BH1750 libary
* Python
   * Pandas
   * Matplotlib
   * Numpy

## How It Works

We read the data from the built circuit and display it with the Serial Monitor,
read that from Python and save it into a text file,
read that data after collection into a Pandas useable Dataframe,
analyze that and create diagrams using Numpy.

### Arduino

The Arduino part of the project focuses on learning how to work with circuits, sensors, inputs and outputs, and collecting data from physical hardware.

I used C++ to program the Arduino and learned how to:
* Read data from sensors
* Work with buttons and other inputs
* Control outputs such as an LCD
* Send data through the Serial connection
* Connect the physical hardware with my Python programs
* Understand basic circuits and wiring

### Python / Pandas

The Python part of the project focuses on receiving and processing the data collected by the Arduino.

I used Python and Pandas to:
* Receive and store Arduino data
* Read and work with datasets
* Clean and filter data
* Organize data using Pandas DataFrames
* Analyze the collected information
* Use the data for further processing and visualization

This allowed me to combine my Python/Pandas knowledge with the hardware side of the project.

## Data
The data I got on the first attempt got pretty quickly to nonsense because the conditions were too much for the sensors too handle.

## Analysis


## Results



## Project Structure


## What I Learned

## Possible Improvements and Errors


