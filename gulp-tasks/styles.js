// packages
const autoprefixer = require("autoprefixer");
const cssnano = require("cssnano");
const gulp = require("gulp");
const postcss = require("gulp-postcss");
const rename = require("gulp-rename");

// CSS task

function stylesBuild() {
  var plugins = [
    autoprefixer,
    cssnano,
  ];

  return gulp
    .src("./src/css/*.css")
    .pipe(gulp.dest("./dist/css/"))
    .pipe(rename({ suffix: ".min" }))
    .pipe(postcss(plugins))
    .pipe(gulp.dest("./dist/css/min"));
}

// exports
module.exports = {
  build: stylesBuild
};
