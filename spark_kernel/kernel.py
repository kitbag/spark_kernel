from ipykernel.kernelbase import Kernel
from pexpect import spawn, EOF
from pexpect.replwrap import REPLWrapper
from re import match

class SparkKernel(Kernel):
  implementation = 'IPython'
  implementation_version = '1.0'
  banner = "Spark Kernel"
  language = 'en-us'
  language_version = '0.1'
  language_info = {'mimetype': 'text/plain', 'name': 'python'}

  def __init__(self, **kwargs):
    Kernel.__init__(self, **kwargs)
    self._start_spark()

  def _start_spark(self):
    '''Creates a pexpect.spawn, then passes to the REPLWrapper in order to allow for a larget timeout value.'''
    self.spark_spawn = spawn('spark-shell', timeout=60)
    self.sparkwrapper = REPLWrapper(self.spark_spawn, u'scala>', None)
    # spark_spawn.expect() needs implemented

  def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
    if match('exit.*', code):
      stream_content = {'name': 'stdout', 'text': 'To exit, just shutdown the kernel!'}
      self.send_response(self.iopub_socket, 'stream', stream_content)
      return {'status': 'ok',
              'execution_count': self.execution_count,
              'payload': [],
              'user_expressions': {},
              }
    elif match('%', code):
      stream_content = {'name': 'stdout', 'text': 'No magics :-( ....sorry.'}
      self.send_response(self.iopub_socket, 'stream', stream_content)
      return {'status': 'ok',
              'execution_count': self.execution_count,
              'payload': [],
              'user_expressions': {},
              }
    else:
      output = self.sparkwrapper.run_command(code)
      if not silent:
        try:
          stream_content = {'name': 'stdout', 'text': output}
          self.send_response(self.iopub_socket, 'stream', stream_content)
          return {'status': 'ok',
                  'execution_count': self.execution_count,
                  'payload': [],
                  'user_expressions': {},
                  }
        finally:
          print('finally')
        
        # Need some exception handling here.

  def do_shutdown(self, restart):
    '''Ensure exit command gets sent to the spark-shell.'''
    self.spark_spawn.send('exit\r\n')
    self.spark_spawn.expect(EOF)
    self.spark_spawn.close()
