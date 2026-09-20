$(document).ready(
function add(){
   var input1=$("#num1").value()
   var input2=$("#num2").value()
   var total=parseInt(input1)+parseInt(input2)
   $("#add").click(function(){
      alert(total);
      $("#total").value(total);
   });
});
