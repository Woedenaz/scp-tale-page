// Load plugins
const gulp = require("gulp");
const sync = require("gulp-npm-script-sync");

// import tasks
const img = require("./gulp-tasks/images.js");
const js = require("./gulp-tasks/scripts.js");
const server = require("./gulp-tasks/browsersync.js");
const css = require("./gulp-tasks/styles.js");
const clean = require("./gulp-tasks/clean.js");
const copy = require("./gulp-tasks/copy.js");
const scpperjs = require("./gulp-tasks/scpperjs.js");

// Watch files
function watchFiles() {
  gulp.watch(
    "./src/css/*",
    css.build
  );
  gulp.watch("./src/img/*", gulp.parallel(img.optimise, copy.assets));
}

// define tasks
const watch = gulp.parallel(watchFiles, server.init);
const build = gulp.series(
  clean.dist,
  gulp.parallel(
    copy.assets,
    css.build,
    gulp.series(js.lint, js.build)
  )
);

const scpper = gulp.parallel(scpperjs);

// expose tasks to CLI
exports.images = img.optimise;
exports.watch = watch;
exports.build = build;
exports.scpper = scpper;
exports.default = scpper;

sync(gulp);