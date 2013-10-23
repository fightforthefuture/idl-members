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

        'cssmin': {

            'include': {
                'src': [
                    'css/src/include.css'
                ],
                'dest': '../templates/include/css/include.css'
            },

            'idl_launch-modal': {
                'src': [
                    'css/src/reset.css',
                    'campaigns/idl_launch/css/src/modal.css'
                ],
                'dest': 'campaigns/idl_launch/css/modal.css'
            },

            'idl_launch-banner': {
                'src': [
                    'css/src/reset.css',
                    'campaigns/idl_launch/css/src/banner.css'
                ],
                'dest': 'campaigns/idl_launch/css/banner.css'
            },

            'test-modal': {
                'src': [
                    'css/src/reset.css',
                    'campaigns/test/css/src/modal.css'
                ],
                'dest': 'campaigns/test/css/modal.css'
            },

            'test-banner': {
                'src': [
                    'css/src/reset.css',
                    'campaigns/test/css/src/banner.css'
                ],
                'dest': 'campaigns/test/css/banner.css'
            }

        },

        'watch': {
            'js': {
                'files': ['js/src/**/*.js'],
                'tasks': 'uglify'
            },
            'css': {
                'files': ['css/src/*.css'],
                'tasks': 'cssmin'
            }
        }

    });

    grunt.task.loadNpmTasks('grunt-contrib-cssmin');
    grunt.task.loadNpmTasks('grunt-contrib-uglify');
    grunt.task.loadNpmTasks('grunt-contrib-watch');
    // grunt.registerTask('default', ['uglify', 'cssmin']);
    grunt.registerTask('default', [
        // 'cssmin',
        'uglify',
        'watch'
    ]);

};
