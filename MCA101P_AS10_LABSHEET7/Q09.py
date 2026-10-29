"""Q9: Copy file contents"""
import shutil
try: shutil.copyfile('sample.txt', 'copy.txt'); print('Copied to copy.txt')
except FileNotFoundError: print('Source file not found')
