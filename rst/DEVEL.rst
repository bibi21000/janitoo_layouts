==================
Developper's notes
==================

What are layouts ?

 - a house
 - a room
 - but can also be a widget : TV remote control, fish tank
 - a user views, ...

Who use layouts ?

 - web clients
 - Android clients
 ...

Who provide layouts ?

 - core
 - extensions


Layout is like a grid/table :

 - fixed sized or dynamic size
 - colspan

Layout can "embeded" others layouts or values

They must be used with python, java, javascript, ... and transported by mqtt (or http if really necessary)

We can use the table format as templating
<table>
    <tr>
        <td>value_chanel</td>
    </tr>
    <tr>
        <td>value_volume</td>
    </tr>
</table>

We should define templates or use copy/paste to create new layouts

