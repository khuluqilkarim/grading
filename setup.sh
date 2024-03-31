#!/bin/bash

directory=$(pwd)


echo "#!/bin/bash" > grading
echo "python3 $directory/grading.py" >> grading

chmod +x grading
sudo mv grading /bin/grading

echo "Setup finish!!"