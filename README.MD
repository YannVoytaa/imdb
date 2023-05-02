# [ML in Cloud] IMDb Predictor

The repository contains a Web API wrapper around IBM Cloud's Watson Machine Learning endpoint to IMDb predictor Model created with AutoAI. It can be publicly accessed [here](https://imdb-ibm-yannvoytaa.vercel.app/docs).

## Overview

The following code is a group assignment for the "Machine Learning in Cloud" course at the University of Warsaw. To complete the assignment we performed the following tasks:

- Fetched the IMDb dataset from the cloud,
- Used AutoAI to train the model by applying multiple strategies and selecting the best one that fits our needs,
- Deployed the model in Watson Machine Learning deployment space,
- Built the wrapper around the deployment space

## Installation (Locally)

1. Clone this repository.

2. Install the required dependencies by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Usage

You can run the web interface and access [localhost:8000/docs](localhost:8000/docs) by executing the following command:

```bash
python3 main.py
```

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/)
