# machineLearning-project2020
<br>

## Overview
This repository contains a the files for a web application *power-app*. Also included within this repository is a jupyter notebook containing the trained regression models that are used by the web app. The The author is Owen Coleman (G00387850@gmit.ie).

## How to run ```model-training.ipynb```
In order to access the <b>model-training.ipynb</b> notebook, it is required that you have the latest version of <a href="https://www.anaconda.com/" target="_blank">Anaconda</a> installed. This will provide you with all of the Python libraries utilized as part of this project, including <a href="https://jupyter.org/install.html" target="_blank">Jupyter Notebook</a>. Should you wish to run this notebook, you will need <a href="https://keras.io/" target="_blank">Keras</a> from <a href="https://www.tensorflow.org/" target="_blank">TensorFlow</a> to interact with the regression models. This does not come with anaconda, but is easily gotten through pip by typing ```pip install tensorflow``` in the command terminal. 

Once installed, simply clone this repository with <a href="https://git-scm.com/" target="_blank">Git</a> then navigate to the location of <b>model-training.ipynb</b>. Once there open a command terminal and type ```jupyter notebook``` and hit enter. A local server should launch, and a browser window will take you to the notebook dashboard. If your browser does not open immediately the console should provide you with a link that you can paste in the URL bar.

## How to run ```power-app```

In order to run this web application, it is highly recommended you install <a href="https://www.docker.com/" target="_blank"> Docker</a>. Once installed, ensure you are in the cloned repository directory and in the command line type the following commands:

```bash
docker build . -t power-app .
docker run -d -p 5000:5000 power-app
```

This will start the web app, which by default can then be accessed at http://127.0.0.1:5000/
