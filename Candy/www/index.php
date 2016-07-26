<html>
<head>
<meta charset="UTF-8" />
</head>


<?php

if (isset($_POST['SomeCandy']))
{
exec("sudo python /home/pi/some.py");
}
if (isset($_POST['MoreCandy']))
{
exec("sudo python /home/pi/more.py");
}
if (isset($_POST['EvenMoreCandy']))
{
exec("sudo python /home/pi/evenmore.py");
}
if (isset($_POST['MaxCandy']))
{
exec("sudo python /home/pi/max.py");
}
?>
<form method="post">
<button name="SomeCandy">Some Candy</button>&nbsp;
<button name="MoreCandy">More Candy</button>&nbsp;
<button name="EvenMoreCandy">Even More Candy</button>&nbsp;
<button name="MaxCandy">Max Candy</button><br>



</form>
</html>
