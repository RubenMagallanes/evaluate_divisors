var gulp = require('gulp');

/////////////////////////////////////////////
////             MAIN TASKS              ////
/////////////////////////////////////////////
gulp.task('default', ['serve'], function() {});

gulp.task('serve', function() {
  var express = require('express');
  var app = express();
  app.set('port', (process.env.PORT || 5000));

  app.use(express.static(__dirname + '/app'));

  // views is directory for all template files
  app.set('views', __dirname + '/app');
  app.engine('html', require('ejs').renderFile);
  app.set('view engine', 'html');

  app.get('/', function(request, response) {
    response.render('index');
  });

  app.listen(app.get('port'), function() {
    console.log('Node app is running on port', app.get('port'));
  });
});
