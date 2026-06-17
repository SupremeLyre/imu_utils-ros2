clear 
close all

dt = readmatrix('../data/data_ADIS16475_gyr_t.txt');         
data_x = readmatrix('../data/data_ADIS16475_gyr_x.txt'); 
data_y= readmatrix('../data/data_ADIS16475_gyr_y.txt'); 
data_z = readmatrix('../data/data_ADIS16475_gyr_z.txt'); 
data_draw=[data_x data_y data_z] ;

data_sim_x= readmatrix('../data/data_ADIS16475_sim_gyr_x.txt'); 
data_sim_y= readmatrix('../data/data_ADIS16475_sim_gyr_y.txt'); 
data_sim_z= readmatrix('../data/data_ADIS16475_sim_gyr_z.txt'); 
data_sim_draw=[data_sim_x data_sim_y data_sim_z] ;


figure
loglog(dt, data_draw , 'o');
% loglog(dt, data_sim_draw , '-');
xlabel('time[sec]');                
ylabel('\sigma[deg/h]');             
% legend('x','y','z');      
grid on;                           
hold on;                           
loglog(dt, data_sim_draw , '-');
legend('x','y','z','x_{sim}','y_{sim}','z_{sim}')
