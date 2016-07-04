from distutils.core import setup
from distutils.command.install import install
import json
import os.path
import sys

kernel_json = {"argv":[sys.executable,"-m", 'spark_kernel', "-f", "{connection_file}"],
 "display_name": 'Spark',
 "language": 'scala',
 "codemirror_mode": "shell"
}

class install_with_kernelspec(install):
	def run(self):
		# Regular installation
		install.run(self)

		# Now write the kernelspec
		from IPython.kernel.kernelspec import KernelSpecManager
		from IPython.utils.path import ensure_dir_exists
		destdir = os.path.join(KernelSpecManager().user_kernel_dir, 'scala')
		ensure_dir_exists(destdir)
		with open(os.path.join(destdir, 'kernel.json'), 'w') as f:
			json.dump(kernel_json, f, sort_keys=True)


svem_flag = '--single-version-externally-managed'
if svem_flag in sys.argv:
	# Die, setuptools, die.
	sys.argv.remove(svem_flag)

setup(name = 'spark_kernel',
      version = '0.1.1',
      description= 'Spark Scala Kernel',
      long_description='',
      author='',
      author_email='',
      url='',
      packages=[ 'spark_kernel' ],
      cmdclass={'install': install_with_kernelspec},
      install_requires=[ 'pexpect' ]
)
