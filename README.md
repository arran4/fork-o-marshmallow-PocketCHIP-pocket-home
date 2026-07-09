# PocketCHIP Launcher (Marshmallow Edition)

# How to install
 
## From repository 
 
#### 1. Add https support to apt
    
    sudo apt-get install apt-transport-https

#### 2. Add a source to `sources.list`

    echo "deb https://${YOUR_GITHUB_USERNAME}.github.io/${YOUR_REPOSITORY_NAME}/archive/ jessie main" | sudo tee /etc/apt/sources.list.d/marshmallow-pocket-chip-home.list


#### 3. Add public key to apt

    curl -fsSL https://${YOUR_GITHUB_USERNAME}.github.io/${YOUR_REPOSITORY_NAME}/archive/public.key | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/pocket-home.gpg


#### 4. Fix pocket-home package (which is pinned by NTC)

    echo -e "Package: pocket-home\nPin: version *\nPin-Priority: 1050" | sudo tee /etc/apt/preferences.d/unpin-pocket-home.pref


#### 5. Update the list of available packages

    sudo apt-get update


#### 6. Upgrade `pocket-home`

    sudo apt-get install pocket-home


Note: The previous commands need to be typed once, then, upgrading is easy and is done by typing `sudo apt-get update`

## Building from sources

#### 1. Required Packages

     sudo apt-get install \
     git \
     build-essential \
     libasound2-dev \
     libx11-dev \
     libxrandr-dev \
     libxcursor-dev \
     libxft-dev \
     libxinerama-dev \
     libnm-glib-dev \
     network-manager-dev \
     libi2c-dev \
     libssl-dev \
     libnm-gtk-dev


####  2. Cloning and building
      
      git clone --recursive https://github.com/o-marshmallow/PocketCHIP-pocket-home/
      make
      make devinstall
      sudo systemctl restart lightdm


#### 3. Updating

      git pull
      git submodule update
      make
      make devinstall
      sudo systemctl restart lightdm


### Thanks
Big thanks to [Celti](https://github.com/Celti) who made this repo updated to new JUCE version and easier to compile and @sgentle who made the install by apt repository !

