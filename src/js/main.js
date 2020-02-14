var editor;

$(document).ready(function() {
    $("#scp-tales-table").DataTable( {
        "ajax": {
            "url": "src/json/tales.json",
            "dataSrc": ""
        },
        "columns": [
            { "data": "title_shown" },
            { "data": "created_by" },
            { "data": "created_at" },
            { "data": "tags" },
            { "data": "rating" }
        ]
    } );
} );