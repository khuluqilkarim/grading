
#!/bin/bash
pip install -r requirements.txt

directory=$(pwd)
echo "#!/bin/bash" > grading
echo "path=$directory" >> grading
curl https://raw.githubusercontent.com/khuluqilkarim/grading/master/update/update.txt >> grading
sed -i 's/\r//' grading
chmod +x grading
sudo mv grading /bin/grading

echo "Setup finish!!"