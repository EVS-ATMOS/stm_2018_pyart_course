-------------------------------------------------------------------
Welcome to the install instructions for the ARM Python Radar course
-------------------------------------------------------------------

Introduction
============
Python, by itself, contains only a core set of packages.
Depending on how you wish to use it you install various modules. You can do this by hand by compiling dependencies from
source or you can use a package manager. There are a number of choices for package managers but there are two dominant
ones in the world of scientific Python: Enthought and Anaconda Python distributions. We will be using Anaconda Python
Distribution (APD) for this course.

Step one: Download Anaconda
===========================
Point your browser here: https://www.anaconda.com/downloads

This will automatically direct you to the downloads for your OS. You will see two boxes, one for Python 3.6 and one for
Python 2.7 **we will be using Python 3.6**. For many applications 2.7 is nearing end of life and 3.6 is simply better.

For MacOS click on "Download command line installer." For Windows you will need to either download the 64 bit
graphical installer or 32 bit depending on your windows distribuion.

MacOS instructions
==================
Open a terminal window. We will now complete several steps: install anaconda, fetching the environment file for the
course, installing that environment, activating the environment and finally testing that environment.

Installing
----------
create a directory where you can work for example: tmp.. if you already have tmp you will need to pick another name.

.. code-block:: bash
    cd ~
    mkdir tmp
    cd tmp
    cp ~/Downloads/Anaconda3-5.0.1-MacOSX-x86_64.sh .

Next step is to run the install script

.. code-block:: bash

    chmod +x Anaconda3-5.0.1-MacOSX-x86_64.sh
    ./Anaconda3-5.0.1-MacOSX-x86_64.sh

Follow the prompts, accept the agreement **and when the installer asks if you want to append anaconda to your path select
yes.** Following this you will want to open a new tab in your terminal. Or close and open the terminal window. This
ensures the sourcing of .bashrc which is the final set up step.

Setting up a killer environment for science-ing
-----------------------------------------------

In your new terminal window we will now update conda and
install our environment:

.. code-block:: bash

    cd ~/tmp
    conda update conda
    curl -O https://raw.githubusercontent.com/EVS-ATMOS/stm_2018_pyart_course/master/pyart-2018.yml
    curl -O https://raw.githubusercontent.com/EVS-ATMOS/stm_2018_pyart_course/master/test_install.py
    conda env create -f pyart-2018.yml

this last step will take some time (minutes) as it determines dependencies and downloads all the cool software you need to use
Py-ART and many other apps!

Testing to make sure you will stay sane
---------------------------------------
Final step is to make sure our environment is set up nicely.. This is simple thanks to the test script you downloaded

.. code-block:: bash

    source activate pyart-2018
    python test_install.py

if you see SUCCESS then you are successful.

Windows instructions
==================
Download whatever version (32/64 bit) is appropriate for your system. In your browser, run the .exe file that is downloaded. This will prompt you to install Anaconda into your local directory. You will want to install it for just yourself if you do not have adminstrative access to your machine. 

Setting up your environment
---------------------------
After Anaconda is installed, you should have access to a program called "Anaconda Prompt" in your Start Menu. Click on "Anaconda Prompt" which will give you a modified version of the command prompt with a indicator to the left which shows which enviroment you are in (should be base). In Anaconda, you can set up differing operating environments that include different versions of various packages. For this tutorial, you will be setting up an environment as follows:

First, make a new directory where you will install environments, for example:

.. code-block:: bash

    md tmp
    cd tmp

We will now set up our environment by typing in the command prompt:

.. code-block:: bash

    conda update conda
    curl -O https://raw.githubusercontent.com/EVS-ATMOS/stm_2018_pyart_course/master/pyart-2018.yml
    curl -O https://raw.githubusercontent.com/EVS-ATMOS/stm_2018_pyart_course/master/test_install.py
    conda env create -f pyart-2018.yml

this last step will take some time (minutes) as it determines dependencies and downloads all the cool software you need to use
Py-ART and many other apps!

Testing to make sure you will stay sane
---------------------------------------
Final step is to make sure our environment is working. We can test this with the test script you downloaded. In the Anaconda Prompt, type:

.. code-block:: bash

    activate pyart-2018
    python test_insall.py
    
If you see SUCCESS then you are successful.
