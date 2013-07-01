module.exports = function(grunt) {

    grunt.initConfig({

        'min': {

            'include': {
                'src': [
                    '../templates/include/js/lib/closure_start.js',
                    '../templates/include/js/lib/cookies.js',
                    '../templates/include/js/lib/querystring.js',
                    '../templates/include/js/lib/addevent.js',
                    '../templates/include/js/lib/classname.js',
                    'js/src/include.js',
                    '../templates/include/js/lib/closure_finish.js'
                ],
                'dest': 'js/include.js'
            },

            'frame': {
                'src': [
                    '../templates/include/js/lib/closure_start.js',
                    '../templates/include/js/lib/querystring.js',
                    '../templates/include/js/lib/addevent.js',
                    '../templates/include/js/lib/classname.js',
                    'js/src/frame.js',
                    '../templates/include/js/lib/closure_finish.js'
                ],
                'dest': 'js/frame.js'
            },

            'customize': {
                'src': [
                    'js/src/jquery.js',
                    'js/src/handlebars.js',
                    'js/src/customize.js'
                ],
                'dest': 'js/customize.js'
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
                'tasks': 'min'
            },
            'css': {
                'files': ['css/src/*.css'],
                'tasks': 'cssmin'
            }
        }

    });

    grunt.task.loadNpmTasks('grunt-css');
    grunt.registerTask('default', 'min cssmin');

};
