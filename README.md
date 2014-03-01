# Installation
* Install package dependencies
  *  `pacman -S $(< dependencies/pkglist.txt)`
* Install python dependencies
  *  `pip2 install -r dependencies/requirements.txt`
* Configure apache (or other webserver) to use wsgi script
* Install nodejs dependencies.
  * package.json contains the node dependencies, for now it should just be bower
  * you must install node first but after that all you should have to do is type npm install and the dependencies should be installed automatically
* Generating vendor assets
  * We're using bower to manage our third party front-end assets. Once you install bower using the above npm install, you should be able to type bower install and all our dependencies should be installed to web/bower_components
  * If you'd like to add some vendor assets, add it to the bower.json file. Look at bower's documentation for information 

