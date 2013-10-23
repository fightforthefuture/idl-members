module.exports = function(grunt) {

    grunt.initConfig({

        'uglify': {

            'customize': {
                'files': {
                    'js/customize.js': [
                        'js/src/jquery.js',
                        'js/src/handlebars.js',
                        'js/src/customize.js'
                    ]
                }
            }

        },

        'watch': {
            'js': {
                'files': ['js/src/**/*.js'],
                'tasks': 'uglify'
            }
        }

    });

    grunt.task.loadNpmTasks('grunt-contrib-uglify');
    grunt.task.loadNpmTasks('grunt-contrib-watch');
    grunt.registerTask('default', [
        'uglify',
        'watch'
    ]);

};
