# edgeScan
## TODO
[x] Hacer funcionar una sóla cámara de Basler y usarla con OpenCV y pypylon

## History

```
1  python3
    2  pip3 install pypylon
    3  sudo apt install pip3
    4  sudo apt install python-pip3
    5  pip
    6  sudo apt install python3-pip
    7  python3
    8  sudo apt update
    9  sudo apt install python3-pip
   10  from pypylon import pylon
   11  camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
   12  camera.Open() new_width = camera.Width.GetValue() - camera.Width.GetInc()
   13  if new_width >= camera.Width.GetMin():
   14  numberOfImagesToGrab = 100
   15  camera.StartGrabbingMax(numberOfImagesToGrab)
   16  while camera.IsGrabbing():
   17  sudo apt install python3-pip
   18  pip3 install pypylon
   19  sudo pip3 install pypylon
   20  git clone https://github.com/basler/pypylon.git
   21  cd pypylon/
   22  pip install .
   23  pip3 install .
   24  sudo apt install python-pip
   25  pip install .
   26  sudo pip install pypylon
   27  cd ..
   28  ls
   29  pip3 install pypylon-1.4.0-cp36-cp36m-linux_x86_64.whl
   30  pip3 install pypylon-1.4.0-cp36-cp36m-linux_armv7l.whl
   31  pip3 install pypylon-1.4.0-cp36-cp36m-linux_aarch64.whl
   32  python3 opencvpypylon.py
   33  sudo shutdown -h now
   34  sudo apt instal openssh-server
   35  sudo apt install openssh-server
   36  python3 opencvpypylon.py
   37  python3
   38  python3 pypylon.py
   39  mv pypylon.py samplepypylon.py
   40  python3 pypylon.py
   41  python3 samplepypylon.py
   42  vi samplepypylon.py
   43  python3 devicespylon.py
   44  vi devicespylon.py
   45  python3 devicespylon.py
   46  vi devicespylon.py
   47  python3 devicespylon.py
   48  cd basler-dart-bcon-mipi-cep_1.0-for-nvidia-jetson-l4t-32.4.x/
   49  ls
   50  sudo ./setup.sh
   51  ./setup.sh
   52  sudo /home/jetson/setup.sh
   53  sudo /home/jetson/basler-dart-bcon-mipi-cep_1.0-for-nvidia-jetson-l4t-32.4.x/setup.sh
   54  ls
   55  cat setup.sh
   56  sudo su
   57  ls
   58  cat README.md
   59  sudo
   60  sudo ./setup.sh
   61  sudo /home/jetson/basler-dart-bcon-mipi-cep_1.0-for-nvidia-jet
   62  chmod +x setup.sh
   63  sudo ./setup.sh
   64  sudo shutdown -r now
   65  python3 opencvpypylon.py
   66  cd basler-dart-bcon-mipi-cep_1.0-for-nvidia-jetson-l4t-32.4.x/
   67  ls
   68  sudo ./setup.sh
   69  sudo vi setup.sh
   70  ls
   71  cat README.md
   72  sudo ./setup.sh
   73  3
   74  sudo ./setup.sh
   75  2
   76  sudo reboot
   77  sudo python3 opencvpypylon.py
   78  cd basler-dart-bcon-mipi-cep_1.0-for-nvidia-jetson-l4t-32.4.x/
   79  ls
   80  dpkg -i basler-dart-bcon-mipi-gentl-producer_1.6.1-nvidia.3-1_arm64.deb
   81  sudo dpkg -i basler-dart-bcon-mipi-gentl-producer_1.6.1-nvidia.3-1_arm64.deb
   82  sudo dpkg -i pylon_6.1.3.20159-deb0_arm64.deb
   83  sudo ./setup.sh
   84  ls
   85  cd devicetree-overlays/
   86  ls
   87  cat tegra210-p3448-0000-p3449-0000-b00-basler-camera-overlay.dts
   88  ls
   89  cd ..
   90  ls
   91  cd basler-camera-driver/
   92  ls
   93  make install
   94  make
   95  cd ..
   96  ls
   97  sudo ./setup.sh
   98  2
   99  cat setup.sh
  100  cat /opt/nvidia/jetson-io/config-by-hardware.py
  101  cat setup.sh 2
  102  sudo ./setup.sh 2
  103  sudo vi /opt/nvidia/jetson-io/config-by-hardware.py
  104  sudo ./setup.sh 2
  105  sudo vi /opt/nvidia/jetson-io/config-by-hardware.py
  106  sudo ./setup.sh
  107  sudo vi /opt/nvidia/jetson-io/config-by-hardware.py
  108  sudo ./setup.sh
  109  sudo reboot
  110  cd basler-dart-bcon-mipi-cep_1.0-for-nvidia-jetson-l4t-32.4.x/
  111  sudo vi /opt/nvidia/jetson-io/config-by-hardware.py
  112  cd ..
  113  sudo python3 opencvpypylon.py
  114  ls *.py
  115  sudo python3 devicespylon.py
  116  sudo python3 samplepylon.py
  117  sudo python3 samplepypylon.py
  118  sudo python3 /opt/nvidia/jetson-io/config-by-hardware.py --help
  119  sudo python3 /opt/nvidia/jetson-io/config-by-hardware.py --l
  120  cd basler-dart-bcon-mipi-cep_1.0-for-nvidia-jetson-l4t-32.4.x/
  121  ls
  122  cat setup.sh
  123  ls /boot/
  124  cat setup.sh
  125  sudo /opt/nvidia/jetson-io/config-by-hardware.py -n "Basler camera overlay"
  126  sudo vi /opt/nvidia/jetson-io/config-by-hardware.py
  127  sudo /opt/nvidia/jetson-io/config-by-hardware.py -n "Basler camera overlay"
  128  cat setup.sh
  129  sudo reboot
  130  sudo python3 devicespylon.py
  131  sudo /opt/nvidia/jetson-io/config-by-hardware.py -l
  132  ls /boot/
  133  cd dtb
  134  ls |more
  135  ls
  136  cat setup.sh
  137  cd basler-dart-bcon-mipi-cep_1.0-for-nvidia-jetson-l4t-32.4.x/
  138  cat setup.sh
  139  cd devicetree-overlays/
  140  ls
  141  cat tegra210-p3448-0000-p3449-0000-b00-basler-camera-overlay.dts
  142  sudo /opt/nvidia/jetson-io/config-by-hardware.py -l
  143  sudo vi tegra210-p3448-0000-p3449-0000-b00-basler-camera-overlay.dts
  144  sudo vi /opt/nvidia/jetson-io/config-by-hardware.py
  145  cd ..
  146  sudo ./setup.sh
  147  sudo vi /opt/nvidia/jetson-io/config-by-hardware.py
  148  sudo /opt/nvidia/jetson-io/config-by-hardware.py -n "Basler camera overlay"
  149  sudo reboot
  150  sudo python3 devicespylon.py
  151  sudo shutdown -h now
  152  sudo python devices
  153  sudo python3 devicespylon.py
  154  sudo python devicespylon.py
  155  sudo python opencvpypylon.py
  156  sudo pip install pypylon-1.4.0-cp36-cp36m-linux_aarch64.whl
  157  ls
  158  cat imagecapture.py
  159  sudo python3 imagecapture.py
  160  sudo vi /opt/nvidia/jetson-io/config-by-hardware.py
  161  sudo /opt/nvidia/jetson-io/config-by-hardware.py -n "Basler camera overlay"
  162  sudo /opt/nvidia/jetson-io/config-by-hardware.py -l
  163  sudo /opt/nvidia/jetson-io/config-by-hardware.py -h
  164  sudo /opt/nvidia/jetson-io/config-by-hardware.py -n 2="Basler camera overlay"
  165  sudo reboot
  166  sudo python3 devicespylon.py
  167  sudo shutdown -h now
  168  ls -l
  169  sudo python devicespylon.py
  170  sudo python3 devicespylon.py
  171  python3 pylongrabtest.py
  172  python pylongrabtest.py
  173  sudo apt install nano
  174  ls -l
  175  cd basler-dart-bcon-mipi-cep_1.0-for-nvidia-jetson-l4t-32.4.x/
  176  ls -l
  177  cat README.md
  178  ```sh
  179      $ /opt/pylon/bin/pylonviewer
  180  ```sh
  181  /opt/pylon/bin/pylonviewer ls -l
  182  ls l- /opt/pylon/bin/pylonviewer
  183  ls -l /opt/pylon/bin/pylonviewer
  184  sh /opt/pylon/bin/pylonviewer
  185  sh
  186  clear
  187  cat README.md
  188  sudo pip3 install  https://github.com/basler/pypylon/releases/download/1.6.0/pypylon-1.6.0-cp36-cp36m-linux_aarch64.whl
  189  nano
  190  clear
  191  cd ..
  192  ls -l
  193  nano pylongrabtest.py
  194  exit
  195  nano pylongrabtest.py
  196  ls -l
  197  rm pylongrabtest.py.save
  198  ls -l
  199  nano pylongrabtest.py
  200  python3 pylongrabtest.py
  201  nano pylongrabtest.py
  202  python3 pylongrabtest.py
  203  nano pylongrabtest.py
  204  python3 pylongrabtest.py
  205  touch test.py
  206  ls -l
  207  nano test.py
  208  python3 test.py
  209  touch opencvtest.py
  210  nano opencvtest.py
  211  ls.l
  212  ls -l
  213  python3 opencvpypylon.py
  214  python3 opencvtest.py
  215  ls -l
  216  python3 devicespylon.py
  217  python3 opencvpypylon.py
  218  clear
  219  python3 devicespylon.py
  220  python3 opencvtest.py
  221  python3 opencvpypylon.py
  222  clear
  223  ls -l
  224  nano imagecapture.py
  225  python3 imagecapture.py
  226  ls -l
  227  nano imagecapture.py
  228  touch imagesave.py
  229  nano imagesave.py
  230  python3 imagesave.py
  231  nano imagesave.py
  232  python3 imagesave.py
  233  nano imagesave.py
  234  python3 imagesave.py
  235  nano imagesave.py
  236  python3 imagesave.py
  237  nano imagesave.py
  238  python3 imagesave.py
  239  nano imagesave.py
  240  python3 imagesave.py
  241  nano imagesave.py
  242  python3 imagesave.py
  243  ls -l
  244  python3 opencvpypylon.py
  245  ls -l
  246  git --version
  247  ls -l
  248  mkdir edgeScan
  249  ls -l
  250  cd edgeScan/
  251  touch README.md
  252  ls -l
  253  nano README.md
  254  ls -l
  255  git remote add https://github.com/julencasazk/edgeScan.git
  256  git remote add origin https://github.com/julencasazk/edgeScan.git
  257  git branch -M main
  258  git push -u origin maingit remote add origin https://github.com/julencasazk/edgeScan.git
  259  git branch -M main
  260  ls -l
	
	
	

```