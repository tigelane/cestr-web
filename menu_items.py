
def simple_black_style():
    return '''
    <style>
        ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: #333;
        }

        li {
            float: left;
        }

        li a {
            display: inline-block;
            color: white;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
        }

        li a:hover {
            background-color: #111;
        }
    </style>
    '''

def complex_black_style(m_width):
    html = '''
    <style>
    
    /* Main */

    #menu {
    '''

    html += "        width: {}px;".format(m_width)

    html += '''
        margin: 0 auto;
        padding: 10px 0 0 0;
        list-style: none;  
        background-color: #111;
        background-image: linear-gradient(#444, #111);
        border-radius: 5px;
        box-shadow: 0 2px 1px #9c9c9c;

    }
   

    #menu li {
        float: left;
        padding: 0 0 10px 0;
        position: relative;
        border-right: 2px solid #9c9c9c;
    }

    #menu li:last-child { 
        box-shadow: none;    
        border-right: 0px;
    }

    #menu a {
        float: left;
        height: 25px;
        padding: 0 25px;
        color: #999;
        text-transform: uppercase;
        font: bold 12px/25px Arial, Helvetica;
        text-decoration: none;
        text-shadow: 0 1px 0 #000;
    }

    #menu li:hover > a {
        color: #fafafa;
    }

    *html #menu li a:hover { /* IE6 */
        color: #fafafa;
    }

    #menu li:hover > ul {
        display: block;
    }

    /* Sub-menu */
    #menu ul {
        list-style: none;
        margin: 0;
        padding: 0;    
        display: none;
        position: absolute;
        top: 35px;
        left: 0;
        z-index: 99999;    
        background-color: #444;   
        background-image: linear-gradient(#444, #111);    
        -moz-border-radius: 5px;
        border-radius: 5px;
    }

    #menu ul li {
        float: none;
        margin: 0;
        padding: 0;
        display: block;  
        box-shadow: 0 1px 0 #111111, 
                    0 2px 0 #777777;
    }

    #menu ul li:last-child { 
        box-shadow: none;    
    }

    #menu ul a {    
        padding: 10px;
        height: auto;
        line-height: 1;
        display: block;
        white-space: nowrap;
        float: none;
        text-transform: none;
    }

    *html #menu ul a { /* IE6 */   
        height: 10px;
        width: 150px;
    }

    *:first-child+html #menu ul a { /* IE7 */    
        height: 10px;
        width: 150px;
    }

    #menu ul a:hover {
        background-color: #0186ba;
        background-image: linear-gradient(#04acec, #0186ba);
    }

    #menu ul li:first-child a {
        border-radius: 5px 5px 0 0;
    }

    #menu ul li:first-child a:after {
        content: '';
        position: absolute;
        left: 30px;
        top: -8px;
        width: 0;
        height: 0;
        border-left: 5px solid transparent;
        border-right: 5px solid transparent;
        border-bottom: 8px solid #444;
    }

    #menu ul li:first-child a:hover:after {
        border-bottom-color: #04acec; 
    }

    #menu ul li:last-child a {
        border-radius: 0 0 5px 5px;
    }

    /* Clear floated elements */
    #menu:after {
        visibility: hidden;
        display: block;
        font-size: 0;
        content: " ";
        clear: both;
        height: 0;
    }

    * html #menu             { zoom: 1; } /* IE6 */
    *:first-child+html #menu { zoom: 1; } /* IE7 */

    </style>
    '''

    return html

def project_menu():
    html = '''
    <ul id="menu">
        <li><a class="active" href="#">Home</a></li>
        
        <li><a href="#">Python</a></li>
        
        <li><a href="#">Contact</a></li>

    </ul>
    '''

    return html


def web2aci_menu():
    html = '''
    <ul id="menu">
        <li><a href="#">Home</a></li>
        <li>
            <li><a href="#">Downloads</a>
                <ul>
                    <li><a href="../alvmi">Alvmi</a></li>
                </ul>
            </li>
        <li>
            <a href="#">Testing</a>
            <ul>
                <li><a href="test_python.py">Python</a></li>
                <li><a href="test_php.php">PHP</a></li>
            </ul>
        </li>
        <li><a href="web2aci.py/setuplogin">Login to ACI</a></li>
        <li>
            <a href="#">Show Information</a>
            <ul>
                <li><a href="aci-show-contexts.py">Context</a></li>
                <li><a href="aci-show-contracts.py">Contracts</a></li>
                <li><a href="aci-show-epgs.py">EPGs</a></li>
                <li><a href="aci-show-filter-entries.py">Filters</a></li>
                <li><a href="aci-show-interfaces.py">Interfaces</a></li>
                <li><a href="aci-show-nodes.py">Network Nodes</a></li>
                <li><a href="aci-show-physical-inventory.py">Physical Inventory</a></li>
                <li><a href="aci-show-tenants.py">Tenants</a></li>
                <li><a href="aci-show-connected-end-points.py">End Devices (Servers)</a></li>
            </ul>
        </li>
        <li><a href="web2aci.py/search4host">Search Fabric</a></li>

    </ul>
    '''

    return html