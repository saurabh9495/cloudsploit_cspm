import os
import time
for root, dirs, files in os.walk('/workspaces/ProjectAWS/cloudsploit/plugins/aws'):
    print(root, dirs, files)
    for file in files:
        if file.endswith('.js'):
            print(os.path.join(root, file))
            # os.system('python3 ' + os.path.join(root, file))
            time.sleep(5)
    time.sleep(1)