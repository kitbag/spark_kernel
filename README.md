# A Scala-based Spark shell wrapper for Jupyter Notebook
Uses the IPython wrapper method for creating a `spark-shell` kernel for use by Jupyter Notebook. You may need to do some initial setup.

# Spark/Scala Installation

Upgrade and install latest Java
```
sudo apt-get update && apt-get upgrade && apt-get install default-jdk
```

Get somewhat latest Spark and Scala
```
curl -O http://downloads.lightbend.com/scala/2.10.6/scala-2.10.6.tgz
curl -O http://d3kbcqa49mib13.cloudfront.net/spark-1.6.2-bin-hadoop2.6.tgz
```

Extract and move them
```
tar -xvf scala-2.10.6.tgz
tar -xvf spark-1.6.2-bin-hadoop2.6.tgz
sudo mv scala-2.10.6 /usr/local/scala
sudo mv spark-1.6.2-bin-hadoop2.6 /usr/local/spark
```

Add to and source bashrc
```
echo "\n\n# Added for spark/scala installation" >> ~/.bashrc
echo "export PATH=$PATH:/usr/local/scala/bin" >> ~/.bashrc
echo "export PATH=$PATH:/usr/local/spark/bin" >> ~/.bashrc
source ~/.bashrc
```

Cleanup by removing files
```
rm scala-2.10.6.tgz
rm spark-1.6.2-bin-hadoop2.6.tgz
```

*AT THIS POINT SPARK/SCALA SHOULD WORK*

# Jupyter Notebook Installation
This should implement most of what is explained [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-jupyter-notebook-to-run-ipython-on-ubuntu-16-04)
```
sudo apt-get update && sudo apt-get -y install python2.7 python-pip python-dev ipython ipython-notebook
sudo -H pip install --upgrade pip
sudo -H pip install jupyter
```

# Install `spark_kernel`

After using `git clone`, you will need to install the `spark_kernel` module; this is what python uses to implement the kernel
```
sudo -H pip install -e spark_kernel/
```

Run the install as a script, which installs the notebook as a kernel
```
python -m spark_kernel.install
```

Run and connect to Jupyter Notebook
```
jupyter notebook --ip 0.0.0.0 --port 8080 --no-browser
```

# References
Where to get more information
- [Jupyter Client](http://jupyter-client.readthedocs.io/en/latest/index.html)
- [Creating Language Kernels for IPython](http://andrew.gibiansky.com/blog/ipython/ipython-kernels/)
- Example kernels
 - [bash_kernel](https://github.com/takluyver/bash_kernel)
 - [redis_kernel](https://github.com/supercoderz/redis_kernel)
- [How To Set Up a Jupyter Notebook to Run IPython on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-jupyter-notebook-to-run-ipython-on-ubuntu-16-04)
- [pexpect module](http://pexpect.readthedocs.io/en/latest/index.html)
