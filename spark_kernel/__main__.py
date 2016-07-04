from ipykernel.kernelapp import IPKernelApp
from .kernel import SparkKernel
IPKernelApp.launch_instance(kernel_class=SparkKernel)
