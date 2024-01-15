# ITEP-G-44
# Urban Agriculture System

## Overview

The Urban Agriculture System is a project that integrates weather forecasting, rainwater harvesting, and machine learning for sustainable urban agriculture. It aims to optimize irrigation strategies based on real-time weather data, ensuring efficient water usage and promoting sustainable practices.

## Features

- **Real-Time Sensor Data:** Collects humidity, temperature, and soil moisture data from sensors deployed in the agriculture system.
- **Weather Forecasting:** Utilizes machine learning algorithms to forecast weather patterns and optimize irrigation schedules.
- **Rainwater Harvesting:** Implements rainwater harvesting strategies to supplement irrigation based on predicted rainfall.
- **Dashboard:** Provides a web-based dashboard for monitoring real-time sensor data, historical trends, and system status.

## Project Structure

- **backend:** Flask application for handling sensor data, machine learning, and communication with the database.
- **machine_learning:** Contains scripts for training machine learning models and storing saved models.
- **node_mcu_code:** Arduino code for NodeMCU module to gather sensor data and send it to the backend.
- **react_dashboard:** React-based web application for displaying real-time and historical data through a user-friendly dashboard.

## Getting Started

### Prerequisites

- Python (Flask, Firebase Admin SDK)
- Node.js (for React dashboard)
- Arduino IDE (for NodeMCU code)

### Installation

1. Set up the backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   python run.py
