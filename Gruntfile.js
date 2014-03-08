module.exports = function(grunt) {

// Project configuration.
grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    watch: {
        html: {
            files: [
                'static/web/templates/*.html'
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
                sassDir: 'static/web/sass',
                cssDir:  'static/web/css',
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
                "static/web/js/template.js" : ["static/web/templates/*.html"]
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
