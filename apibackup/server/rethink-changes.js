var r = require(
    '../node_modules/loopback-connector-rethinkdb/node_modules/rethinkdb');

var dataSources = require('../server/dataSources');
var db = dataSources.rethinkdb;

r.connect({
    host: db.host,
    port: db.port
}, function(err, conn) {
    if (err) throw err;

    r.db('Mawto').table('ArticleURL').changes().run(conn, function(err,
        cursor) {
        cursor.each(console.log);
    });
});
