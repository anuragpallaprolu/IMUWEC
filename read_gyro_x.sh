rm -r *.txt
./miniterm > sensor_out.log
perl tobenizer2_2.pl sensor_out.log
ls -l
perl prepend.pl gyrox.txt > gyrox_n.txt
cat gyrox_n.txt
python py_plot.py 
python theta_integral.py > theta_x.txt
perl prepend.pl theta_x.txt > theta_x_n.txt
python kalman_new.py > milestone1.log
cat milestone1.log


