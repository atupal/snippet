<%def name="buildtable()">
<table>
<tr><td>
${caller.body()}
</td></tr>
</table>
</%def>

<%self:buildtable>
I am the table body.
</%self:buildtable>
