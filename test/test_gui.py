import unittest
import core.gui

class TestGui(unittest.TestCase):
    def test_basic_command_call(self):
        '''
        test if the most basic command can be runned
        '''


import subprocess
process = subprocess.Popen(['echo','More Outputs'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
stdout,stderr = process.communicate()
print([stdout,stderr])