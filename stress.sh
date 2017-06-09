gettemp(){
   cat /sys/devices/virtual/thermal/thermal_zone0/temp
 };

fulload() { 
    dd if=/dev/zero of=/dev/null |
    dd if=/dev/zero of=/dev/null | 
    dd if=/dev/zero of=/dev/null | 
    dd if=/dev/zero of=/dev/null & }; 
echo CPU temp:
gettemp;
echo stressing CPU, press any key to stop...
fulload; 
read;
echo CPU temp after stress:
gettemp; 
killall dd;
