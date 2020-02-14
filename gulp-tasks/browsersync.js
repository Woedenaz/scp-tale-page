// packages
const browsersync = require("browser-sync").create();

// BrowserSync
function init(done) {
  browsersync.init({
    server: {
      baseDir: "../dist/",
    },
    files: [
      "../dist/css/min/*.css",
      "../dist/js/*.js",
      "../*.{html, xml}",
    ],
    port: 3000,
    open: false,
  });

  done();
}

// BrowserSync Reload
function reload(done) {
  browsersync.reload();
  done();
}

// exports
module.exports = {
  init: init,
  reload: reload,
};
