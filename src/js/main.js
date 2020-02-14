$(document).ready(function() {

    $("#scp-tales-table").DataTable( {
        "ajax": {
            "url": "src/json/tales.json",
            "dataSrc": ""
        },
        "columns": [
            { 
                "data": "title_shown",
                "render": function(data, type, full) {
                    if(type === "display"){
                        data = "<a href=http://www.scp-wiki.net/" + full["fullname"] + ">" + data + "</a>";
                        
                    }        
                    return data;
                }
            },
            { "data": "created_by" },
            { "data": "created_at" },
            { 
                "data": "tags",
                "render": function(data, type, full) {
                    if(type === "display"){
                        data = [];
                        var data_split = full["tags"].toString().split(",");
                        for (var i=0;i<data_split.length;i++) {
                            data = data + "<a href='#' class='tags'>" + data_split[i] + "</a>\r";
                        }
                    }        
                    return data;
                } 
            },
            { "data": "rating" }
        ],
        responsive: true
    } );

    var search = $("#scp-tales-table_filter > label > input");

    $(document).on("click", ".tags", function(event){ 
        $(search).val("");
        $(search).val($(this).html());
        
        var keyboardEvent = document.createEvent('KeyboardEvent');
        delete keyboardEvent.which;
        var initMethod = typeof keyboardEvent.initKeyboardEvent !== 'undefined' ? 'initKeyboardEvent' : 'initKeyEvent';
        keyboardEvent[initMethod](
          'keydown', // event type : keydown, keyup, keypress
          true, // bubbles
          true, // cancelable
          window, // viewArg: should be window
          false, // ctrlKeyArg
          false, // altKeyArg
          false, // shiftKeyArg
          false, // metaKeyArg
          13, // keyCodeArg : unsigned long the virtual key code, else 0
          13 // charCodeArgs : unsigned long the Unicode character associated with the depressed key, else 0
        );
        document.querySelector("#scp-tales-table_filter > label > input").dispatchEvent(keyboardEvent);
        event.preventDefault();
    });
    return search;
} );