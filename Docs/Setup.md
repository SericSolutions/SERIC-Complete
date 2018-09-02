# S.E.R.I.C Raspbian Image From Scratch

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [S.E.R.I.C Raspbian Image From Scratch](#seric-raspbian-image-from-scratch)
	- [Introduction](#introduction)
	- [Step 1 Apt repo](#step-1-apt-repo)
	- [Step 2 Install nodeJS](#step-2-install-nodejs)
	- [Step 3 OpenBR](#step-3-openbr)
	- [Step 4 MJPG streamer](#step-4-mjpg-streamer)
	- [Step 5 Wifi hotspot](#step-5-wifi-hotspot)
	- [Step 6 Set time](#step-6-set-time)

<!-- /TOC -->


## Introduction

These are instructions on how to create a SERIC compatable boot image form Scratch

## Step 1 Apt repo

``` bash
  sudo apt-get update
  sudo apt-get upgrade

  sudo apt-get install
  sudo apt-get install make
  sudo apt-get install cmake
  sudo apt-get install libtool
  sudo apt-get install imagemagick
  sudo apt-get install libjpeg8-dev
  sudo apt-get install cmake-curses-gui
  sudo apt-get install pkg-config
  sudo apt-get install qt5-default
  sudo apt-get install libqt5svg5-dev
  sudo apt-get install git
  sudo apt-get install sqlite3
```
*NOT IN STOCK IMAGE*
```Bash
sudo apt-get install bluetooth libbluetooth-dev
sudo apt-get install python-pip python-dev ipython
```
## Step 2 Install nodeJS
  * ### To install go [link](https://github.com/nodesource/distributions)

  * ### Libraries
  ```bash
	su # IMPORTAT, DO AS ROOT
	npm install express
	npm install cors
	npm install --build-from-source sqlite3 #this can take 1 hour
	npm install sleep
	npm install express-fileupload
  ```
  * ### RUN ON STARTUP [LINK](https://causeyourestuck.io/2016/04/30/run-node-js-script-startup/)


## Step 3 OpenBR
  * ### Install openBR
    - instructions can be found [here](http://openbiometrics.org/docs/install/#raspbian)
  (Pre built OpenBR jessie rpi3 repo in the same folder)

  * ### Python wrapper
    - ```sudo pip install pyopenbr```

## Step 4 MJPG streamer

``` bash
  git clone https://github.com/jacksonliam/mjpg-streamer.git
  cd mjpg-streamer/mjpg-streamer-experimental
  make #(it will fail)
  mkdir _build && cd _build #(if not already built)
  ccmake . #Turn off anything related to openCV
  make #it will work now
  cp ./_build /{wherever DevCam is}/Server/mjpg
```
* Compiled repo in the same folder
## Step 5 Wifi hotspot
  Instructions can be found [Here](https://frillip.com/using-your-raspberry-pi-3-as-a-wifi-access-point-with-hostapd/).

## Step 6 Set time
```bash
sudo raspi-config
```

## Step 7 Bluetooth *NOT IN STOCK IMAGE*
```
sudo pip install pybluez
```
