from .Web_scrapping import *
import os
from time import sleep


def write_to_html_file(df, title='', filename=''):
    '''
    Write an entire dataframe to an HTML file with nice formatting.
    '''
    from datetime import timedelta
    from time import time, strftime, localtime
    result = '''
<html>
<head>
<script type=text/javascript>
function changecolor(){
var dtable = document.getElementById('Datatable');
var i,j;
var rowLength = dtable.rows.length;


for (i = 0; i < rowLength; i++) {
    for(j=0;j<dtable.rows[i].cells.length;j++){
if (dtable.rows[i].cells[j].innerHTML='FAILED'){
    dtable.rows[i].cells[j].innerHTML="<span style='color: red;'>FAILED</span>";
}
else if(dtable.rows[i].cells[j].innerHTML='PASSED'){
dtable.rows[i].cells[j].innerHTML="<span style='color: green;'>PASSED</span>";
}
}
}
}

</script>
<style>

    h2 {
        text-align: center;
        font-family: Helvetica, Arial, sans-serif;
    }
    table { 
        margin-left: auto;
        margin-right: auto;
    }
    table, th, td {
     
        border: 1px solid black;
        border-collapse: collapse;
    }
    th, td {
        padding: 5px;
        text-align: center;
        font-family: Helvetica, Arial, sans-serif;
        font-size: 90%;
        
        
    }
   td{
   line-height:2.5em;
   }
   
    .wide {
        width: 90%; 
    }

</style>
</head>
<body>
 
    '''
    result += '<h2> %s </h2>\n' % title
    result +='<div id="div1">'
    result +='<img alt ="" src=""/>'
    result += '<table id="Datatable">\
    <td>%s</td></table>'%df.to_html(classes='wide', escape=False)
    result +='</div>'
    result += '''
</body>
</html>
'''
    with open(filename, 'w+') as f:
        f.write(result)
    return filename



