#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Convert</title>'
echo '</head>'
echo '<body>'
echo '<a href="/"><img src="formula.png" width=492 height=109 alt="" border=0></a>'
echo '<span style="display: block !important; width: 180px; text-align: right; float: right; font-family: sans-serif; font-size: 12px;"><a href="http://www.wunderground.com/cgi-bin/findweather/getForecast?query=zmw:94114.1.99999&bannertypeclick=wu_simpleblack" title="San Francisco, California Weather Forecast" target="_blank"><img src="http://weathersticker.wunderground.com/weathersticker/cgi-bin/banner/ban/wxBanner?bannertype=wu_simpleblack&airportcode=KSFO&ForcedCity=San Francisco&ForcedState=CA&zip=94114&language=EN" alt="Find more about Weather in San Francisco, CA" align = right width="160" /></a><br><a href="http://www.wunderground.com/cgi-bin/findweather/getForecast?query=zmw:94114.1.99999&bannertypeclick=wu_simpleblack" title="Get latest Weather Forecast updates" style="font-family: sans-serif; font-size: 12px" target="_blank"></a><br><br></span>'

echo '<table border="0" cellspacing="4" cellpadding="4" bgcolor="#CCCCCC" width=100%>'
echo '<tr align="left" valign="top">'
echo '<td><font size=-1>'
echo '<p><i>This web application is designed to convert various values to different formats.</i></p>'
        
echo '<p>Enter value into the text field and select the mode to convert and hit the <i>convert button</i> to get the value. Hit reset to clear what was entered</p>'
echo '</font> </td>'
echo '</tr>'
echo '</table>'

  echo "<form method=GET action=\"${SCRIPT}\">"\
       '<table nowrap><tr><td>Input</TD><TD><input type="text" name="val_x" size=12></td></tr></table>'


echo '<input type="radio" name="val_z" value="1" checked> Fahrenheit to Celsius<br>'\
     '<input type="radio" name="val_z" value="2"> Fahrenheit to Kelvin<br>'\
	 '<input type="radio" name="val_z" value="3"> Celsius to Fahrenheit<br>'\
     '<input type="radio" name="val_z" value="4"> Celsius to Kelvin'

echo '<br><input type="submit" value="Convert">'\
'<input type="reset" value="Reset"></form>'

if [ "$REQUEST_METHOD" != "GET" ]; then
	echo "<hr>Script Error:"\
	"<br>Usage error, REQUEST_METHOD!=GET."\
	"<br>check declaration use METHOD=\"GET\".<hr>"
	exit 1
fi

if [ -z "$QUERY_STRING" ]; then
	exit 0
else
	saveIFS=$IFS
	IFS='=&'
	parm=($QUERY_STRING)
	IFS=$saveIFS
	
     echo "Input value:" ${parm[1]}
	 echo '<br>'
	 s1="${parm[3]}"
	 s2="${parm[1]}"
	 if [ "$s1" -eq 1 ]
	 then
		s3="$(($s2 - 32))"
		s3="$(($s3*5))"
		z=$((s3 / 9))
		echo "Fahrenheit to Celsius: " $z
		echo $s2 "Fahrenheit to Celsius: " $z >> log.txt
	 fi
	 if [ "$s1" -eq 2 ]
	 then
		s3="$(($s2 + 459))"
		s3="$(($s3*5))"
		z=$((s3 / 9))
		echo "Fahrenheit to Kelvin: " $z
		echo $s2 "Fahrenheit to Kelvin: " $z >> log.txt
	 fi
	 if [ "$s1" -eq 3 ]
	 then
		s3="$(($s2*9))"
		z=$((s3/5))
		echo "Celsius to Fahrenheit: " $(($z + 32))
		echo $s2 "Celsius to Fahrenheit: " $(($z + 32)) >> log.txt
	 fi
	 if [ "$s1" -eq 4 ]
	 then
		echo "Celsius to Kelvin: " $(($s2 + 273))
		echo $s2 "Celsius to Kelvin: " $(($s2 + 273)) >> log.txt
	 fi
fi
  
echo '</body>'
echo '</html>'

exit 0
