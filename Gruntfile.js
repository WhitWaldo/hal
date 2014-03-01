module.exports = function(grunt) {

// Project configuration.
grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    watch: {
        html: {
            files: [
                'web/templates/*.html'
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
                sassDir: 'web/sass',
                cssDir:  'web/css',
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
                "web/js/template.js" : ["web/templates/*.html"]
            }
        }
    }
});

// Load the Grunt plugins.
grunt.loadNpmTasks('grunt-contrib-compass');
grunt.loadNpmTasks('grunt-contrib-watch');
grunt.loadNpmTasks('grunt-contrib-jst');
// Register the default tasks.
grunt.registerTask('build',['compass','JST']);
grunt.registerTask('default', ['watch']);
};
