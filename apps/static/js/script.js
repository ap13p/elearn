/**
 * Created by Afief on 19/08/2015.
 */
var CKEDITOR = CKEDITOR || {};
CKEDITOR.config = CKEDITOR.config || {};

CKEDITOR.config.extraPlugins = [
    'filetools', 'notificationaggregator',
    'uploadimage', 'uploadwidget', 'widget',
    'lineutils', 'notification'
].join(',');
CKEDITOR.config.uploadUrl = '/upload/';

function delete_this(target) {
    var pr = confirm('Hapus ini?');
    if (pr) {
        window.location = target;
    }
}
