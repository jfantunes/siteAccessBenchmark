<html>
%if len(valid)>0: 
<h1>Valid Requests:</h1>
<table>
  %i=1
  %for item in valid:
	<tr>
	<th>Rank</th>
    <th>Url</th>
    <th>Size</th> 
    <th>LoadTime</th>
  </tr>	
	<tr>
		<td>{{i}}</td>
		<td>{{item['url']}} </th> 
		<td>{{item['size']}} </th>
		<td>{{item['load_time']}} </th>	
	</tr>
  %i+=1
  %end
</table>
</br>
%end

%if(len(not_valid))>0:
<h1>Not Valid Requests:</h1>
%for item in not_valid:
<table>
	<tr>
	<th>Url</th>
    <th>Error</th>
    </tr>
	<tr>
		<td>{{item['url']}}</td>
		<td> {{item['error']}}</td>
	</tr>
  %end
</table>
</html>
%end
