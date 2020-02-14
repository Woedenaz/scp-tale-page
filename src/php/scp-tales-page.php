<?php
 
include( "../lib/DataTables.php" );

use
    DataTables\Editor,
    DataTables\Editor\Field,
    DataTables\Editor\Format,
    DataTables\Editor\Mjoin,
    DataTables\Editor\Options,
    DataTables\Editor\Upload,
    DataTables\Editor\Validate,
    DataTables\Editor\ValidateOptions;
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * Easy set variables
 */
 
// DB table to use
$table = 'scp-tales-table';
 
// Table's primary key
$primaryKey = 'id';
 
// Array of database columns which should be read and sent back to DataTables.
// The `db` parameter represents the column name in the database, while the `dt`
// parameter represents the DataTables column identifier. 
$columns = array(
    array( 'db' => 'title_shown', 'dt' => 0 ),
    array(
        'db'        => 'created_at',
        'dt'        => 1,
        'formatter' => getFormatter( Format::dateSqlToFormat( 'Y' ) )
    ),
    array( 'db' => 'created_by',   'dt' => 2 ),
    array( 'db' => 'tags',     'dt' => 3 ),
    array( 'db' => 'rating',     'dt' => 4 )
); 
 
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * If you just want to use the basic configuration for DataTables with PHP
 * server-side, there is no need to edit below this line.
 */
 
require( 'ssp.class.php' );
 
echo json_encode(
    SSP::simple( $_GET, $sql_details, $table, $primaryKey, $columns )
);