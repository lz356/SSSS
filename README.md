# Sub-keyword Synonym Subtopics Searching (SSSS)
Paper Searching Tool termed as Sub-keyword Synonym Subtopics Searching described in the paper "A review of machine learning in building load prediction", Section 2

Please cite the paper if you use the code for publication:

Zhang, L., Wen, J., Li, Y., Chen, J., Ye, Y., Fu, Y., & Livingood, W. (2021). A review of machine learning in building load prediction. Applied Energy, 285, 116452.

This project is a work-in-progress.

Installation

Download and install [git](https://git-scm.com/download/win)

Download and install the latest version of [Conda](https://docs.conda.io/en/latest/) (version 4.4 or above)

Run Anaconda Prompt as Administrator

Create a new conda environment:

`$ conda create -n <name-of-repository> python=3.6 pip`

`$ conda activate <name-of-repository>`

(If you’re using a version of conda older than 4.4, you may need to instead use source activate <name-of-repository>.)

Ensure that you have navigated to the top level of your cloned repository. You will execute all your pip commands from this location. For example:

`$ cd /path/to/repository`

Install the environment needed for this repository:

`$ pip install -e .[dev]`
