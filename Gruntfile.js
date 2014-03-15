module.exports = function(grunt) {

// Project configuration.
grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    watch: {
        html: {
            files: [
                'static/templates/*.html'
            ],
            tasks: ['jst']
        },
        css: {
            files: [
                '**/*.sass',
                '**/*.scss'
            ],
            tasks: ['compass']
        }
    },
    compass: {
        dist: {
            options: {
                sassDir: 'static/sass',
                cssDir:  'static/css',
                outputStyle: 'compressed'
            }
        }
    },
    jst: {
        compile: {
            options: {
                templateSettings: {}
            },
            files: {
                "static/js/template.js" : ["static/templates/*.html"]
            }
        }
    }
});

// Load the Grunt plugins.
grunt.loadNpmTasks('grunt-contrib-compass');
grunt.loadNpmTasks('grunt-contrib-watch');
grunt.loadNpmTasks('grunt-contrib-jst');
// Register the default tasks.
grunt.registerTask('build',['compass','jst']);
grunt.registerTask('default', ['watch']);
};
