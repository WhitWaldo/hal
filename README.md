# Setup
## Backend
* Install package dependencies
  *  `pacman -S $(< dependencies/pkglist.txt)`
* Install python dependencies
  *  `pip2 install -r dependencies/requirements.txt`
* Configure apache (or other webserver) to use wsgi script

## Frontend

* Setup Node
  * Install it for the platform you're using if you don't already have it.
  * package.json contains the node dependencies we're using. To install all of them at once, simply execute `npm install` in the same directory as package.json
* Setup Bower
  * We're using bower to manage our third party front-end dependencies. The above command should install bower for you. Once it's installed, execute `bower install` to install all the dependencies located in bower.json.
  * If you'd like to add more dependencies, add it to the bower.json file. Look at bower's documentation for information.
  * Bower's configuration is located in .bowerrc
* Grunt + SASS + Compass + JST
  * Grunt is a JS task manager to keep all of our front-end workflow organized and compiled. When working on a project, be sure to have `grunt watch` or just `grunt` running while you edit files. It will execute compilations and other tasks when a particular file changes.
  * This is all configured in Gruntfile.js
  * We're using SASS, and using compass to compile it to CSS.
  * We're using JST to keep our html templates/fragments organized and compiled into a singular JS object. It's directories and behaviors are also found in Gruntfile.js
#Circuit
![](door_controller/Door/design.png?raw=true)
![](door_controller/Door/circuit.png?raw=true)

# Site
![](images/preview_1.png?raw=true)
![](images/preview_2.png?raw=true)