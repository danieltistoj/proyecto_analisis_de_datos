import subprocess
import socket
from datetime import datetime
cmdCommand = " TASKLIST /V /FI 'STATUS eq running'"   #specify your cmd command
process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)
print((socket.gethostbyname(socket.gethostname())))
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
