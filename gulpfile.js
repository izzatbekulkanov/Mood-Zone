const browsersync = require('browser-sync').create();
const cached = require('gulp-cached');
const del = require('del');
const fileinclude = require('gulp-file-include');
const gulp = require('gulp');
const gulpif = require('gulp-if');
const npmdist = require('gulp-npm-dist');
const replace = require('gulp-replace');
const uglify = require('gulp-uglify');
const useref = require('gulp-useref-plus');
const rename = require('gulp-rename');
const sass = require('gulp-sass')(require('sass'));
const autoprefixer = require("gulp-autoprefixer");
const sourcemaps = require("gulp-sourcemaps");
const cleanCSS = require('gulp-clean-css');
const rtlcss = require('gulp-rtlcss');
const fs = require('fs'); // Read a file

const isSourceMap = true;
const sourceMapWrite = (isSourceMap) ? "./" : false;

const paths = {
    base: {
        base: {
            dir: './'
        },
        node: {
            dir: './node_modules'
        }
    },
    dist: {
        base: {
            dir: './static',
            assets: './static/'
        },
        libs: {
            dir: './static/libs'
        },
        css: {
            dir: './static/css',
        },
        js: {
            dir: './static/js',
            files: './static/js/pages',
        },
    },
    src: {
        base: {
            dir: './src',
            assets: './src/**/*',
        },
        js: {
            dir: './src/js',
            pages: './src/js/pages',
            files: './src/js/pages/*.js',
            main: './src/js/*.js',
        },
        scss: {
            dir: './src/scss',
            files: './src/scss/**/*',
            main: './src/scss/config/app.scss'
        },
        icon: {
            dir: './src/scss',
            files: './src/scss/icons.scss',
            main: './src/scss/*.scss'
        },
        bootstrap: {
            files: './src/scss/config/bootstrap.scss',
            typeFiles: './src/scss/config/bootstrap.scss',
            components: './src/scss/components/*',
            light: './src/scss/config/_theme*',
            variables: './src/scss/config/_variables*',
        },
        custom: {
            dir: './src/scss/config/custom.scss',
            files: './src/scss/config/custom.scss',
            main: './src/scss/config/custom.scss'
        },
    }
};

gulp.task('browsersync', function (callback) {
        var baseDir = paths.dist.base.dir;
        browsersync.init({
            server: {
                baseDir: [baseDir, paths.src.base.dir, paths.base.base.dir]
            }
        });
        callback();
});

gulp.task('browsersyncReload', function (callback) {

    browsersync.reload();
    callback();

});

gulp.task('watch', async function () {
    gulp.watch([paths.src.scss.files, '!' + paths.src.custom.files, '!' + paths.src.icon.files,  '!' + paths.src.bootstrap.typeFiles, '!' + paths.src.bootstrap.light, '!' + paths.src.bootstrap.variables], gulp.series('scss'));
    gulp.watch([paths.src.bootstrap.typeFiles, '!' + paths.src.bootstrap.components, '!' + paths.src.bootstrap.light], gulp.series('bootstrap'));
    gulp.watch([paths.src.bootstrap.light, paths.src.bootstrap.variables], gulp.series('bootstrap', 'scss'));
    gulp.watch(paths.src.icon.files, gulp.series('icon'));
    gulp.watch(paths.src.custom.files, gulp.series('custom'));
    gulp.watch([paths.src.js.dir], gulp.series('js'));
    gulp.watch([paths.src.js.pages], gulp.series('jsPages'));
});

gulp.task('js', async function () {
        var destPath = paths.dist.js.dir;
        return gulp
            .src(paths.src.js.main)
            .pipe(uglify())
            .pipe(gulp.dest(destPath));
});

gulp.task('jsPages', function () {
    var JsPagePath = paths.dist.js.files;
    return gulp.src(paths.src.js.files).pipe(uglify()).pipe(gulp.dest(JsPagePath));
});

gulp.task('bootstrap', function () {

        var scssFiles = paths.src.bootstrap.files;
    
        var cssDest = paths.dist.css.dir;
    
        // generate ltr
        gulp
            .src(scssFiles)
            .pipe(sourcemaps.init())
            .pipe(sass.sync().on('error', sass.logError))
            .pipe(
                autoprefixer()
            )
            .pipe(gulp.dest(cssDest))
            .pipe(cleanCSS())
            .pipe(
                rename({
                    suffix: ".min"
                })
            )
            .pipe(sourcemaps.write(sourceMapWrite))
            .pipe(gulp.dest(cssDest));

        // generate rtl
        return gulp
            .src(scssFiles)
            .pipe(sourcemaps.init())
            .pipe(sass.sync().on('error', sass.logError))
            .pipe(
                autoprefixer()
            )
            .pipe(rtlcss())
            .pipe(gulp.dest(cssDest))
            .pipe(cleanCSS())
            .pipe(
                rename({
                    suffix: "-rtl.min"
                })
            )
            .pipe(sourcemaps.write(sourceMapWrite))
            .pipe(gulp.dest(cssDest));
});

gulp.task('scss', function () {

        var scssFiles = paths.src.scss.main;

        var cssDest = paths.dist.css.dir;

        // generate ltr  
        gulp
            .src(scssFiles)
            .pipe(sourcemaps.init())
            .pipe(sass.sync().on('error', sass.logError))
            .pipe(
                autoprefixer()
            )
            .pipe(gulp.dest(cssDest))
            .pipe(cleanCSS())
            .pipe(
                rename({
                    suffix: ".min"
                })
            )
            .pipe(sourcemaps.write(sourceMapWrite))
            .pipe(gulp.dest(cssDest));

        // generate rtl
        return gulp
            .src(scssFiles)
            .pipe(sourcemaps.init())
            .pipe(sass.sync().on('error', sass.logError))
            .pipe(
                autoprefixer()
            )
            .pipe(rtlcss())
            .pipe(gulp.dest(cssDest))
            .pipe(cleanCSS())
            .pipe(
                rename({
                    suffix: "-rtl.min"
                })
            )
            .pipe(sourcemaps.write(sourceMapWrite))
            .pipe(gulp.dest(cssDest));
});

gulp.task('custom', async function () {
        var scssFiles = paths.src.custom.main;

        var cssDest = paths.dist.css.dir;

        // generate ltr  
        gulp
            .src(scssFiles)
            .pipe(sourcemaps.init())
            .pipe(sass.sync().on('error', sass.logError))
            .pipe(
                autoprefixer()
            )
            .pipe(gulp.dest(cssDest))
            .pipe(cleanCSS())
            .pipe(
                rename({
                    suffix: ".min"
                })
            )
            .pipe(sourcemaps.write(sourceMapWrite))
            .pipe(gulp.dest(cssDest));
             // generate rtl
        return gulp
        .src(scssFiles)
        .pipe(sourcemaps.init())
        .pipe(sass.sync().on('error', sass.logError))
        .pipe(
            autoprefixer()
        )
        .pipe(rtlcss())
        .pipe(gulp.dest(cssDest))
        .pipe(cleanCSS())
        .pipe(
            rename({
                suffix: "-rtl.min"
            })
        )
        .pipe(sourcemaps.write(sourceMapWrite))
        .pipe(gulp.dest(cssDest));
});

gulp.task('icon', async function () {
        var iconFiles = paths.src.icon.dir;
        var cssDest = paths.dist.css.dir;

        return gulp
            .src(paths.src.icon.main)
            .pipe(sass.sync().on('error', sass.logError))
            .pipe(
                autoprefixer()
            )
            .pipe(gulp.dest(cssDest))
            .pipe(cleanCSS())
            .pipe(
                rename({
                    suffix: ".min"
                })
            )
            .pipe(gulp.dest(cssDest));
});

gulp.task('clean:dist', function (callback) {
    del.sync(paths.dist.base.dir);
    callback();
});

gulp.task('copy:all', function (cb) {
        var destPath = paths.dist.base.assets;
        return gulp
            .src([
                paths.src.base.assets,
                '!' + paths.src.scss.files,
                '!' + paths.src.js.main,
                '!' + paths.src.js.files,
                '!' + paths.src.scss.dir,
            ])
            .pipe(gulp.dest(destPath));
});

gulp.task('copy:libs', function () {
        var destPath = paths.dist.libs.dir;
    
        return gulp
            .src(npmdist({replaceDefaultExcludes: isSourceMap, excludes : ['/**/*.txt']}), {
                base: paths.base.node.dir
            })
            .pipe(rename(function (path) {
                path.dirname = path.dirname.replace(/\/static/, '').replace(/\/dist/, '');
            }))
            .pipe(gulp.dest(destPath));
});

gulp.task('build', gulp.series(gulp.parallel('clean:dist', 'copy:all', 'copy:libs','bootstrap', 'scss', 'js', 'jsPages', 'icon','custom'), gulp.parallel('scss')));

gulp.task('default', gulp.series(gulp.parallel('clean:dist', 'copy:all', 'copy:libs', 'bootstrap', 'scss', 'js', 'jsPages', 'icon','custom'), gulp.parallel('watch')));
