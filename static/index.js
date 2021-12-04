function check()
{
	var pass = document.getElementById('spwd')

	if(pass.type === "password"){
		pass.type = "text"
	}
	else{
		pass.type = "password"
	}
}

function fname_validation()
{
	'use strict';
	var inputxt = document.getElementById('fname');
	var inputtxt = document.getElementById('fname').value;
	var letters = /^[a-zA-Z]+$/
	if (!inputtxt.match(letters))
	{
		document.getElementById('fn').innerHTML = '  cant be empty,only alphabet allowed.';
		inputxt.focus();
		document.getElementById('fn').style.color = "#FF0000";
	}
	else
	{
		document.getElementById('fn').innerHTML ='';
		document.getElementById('fn').style.color = "#00AF33";
	}
}

function lname_validation()
{
	'use strict';
	var inputxt = document.getElementById('lname');
	var inputtxt = document.getElementById('lname').value;
	var letters = /^[a-zA-Z]+$/
	if (!inputtxt.match(letters))
	{
		document.getElementById('ln').innerHTML = 'cant be empty,only alphabet allowed.';
		inputxt.focus();
		document.getElementById('ln').style.color = "#FF0000";
	}
	else
	{
		document.getElementById('ln').innerHTML ='';
		document.getElementById('ln').style.color = "#00AF33";
	}
}

function uname_validation()
{
	'use strict';
	var inputxt = document.getElementById('uname');
	var inputtxt = document.getElementById('uname').value;
	var txt_len = inputtxt.length;
	var letters = /^[0-9a-zA-Z]+$/
	if (txt_len < 6 || !inputtxt.match(letters))
	{
		document.getElementById('un').innerHTML = 'Username must be 6 chracters long and alphanuric chracters only.';
		inputxt.focus();
		document.getElementById('un').style.color = "#FF0000";
	}
	else
	{
		document.getElementById('un').innerHTML ='';
		document.getElementById('un').style.color = "#00AF33";
	}
}



function mobile_validation()
{
	'use strict';
	var inputxt = document.getElementById('mobile');
	var inputtxt = document.getElementById('mobile').value;
	var txt_len = inputtxt.length;
	var numbers = /^[0-9]+$/;
	if (txt_len < 10 || !inputtxt.match(numbers))
	{
		document.getElementById('mob').innerHTML = 'Mobile No. must be 10 chracters long.';
		inputxt.focus();
		document.getElementById('mob').style.color = "#FF0000";
	}
	else if (!txt_len > 10)
	{
		document.getElementById('mob').innerHTML = 'Mobile No. must be 10 chracters long.';
		inputxt.focus();
		document.getElementById('mob').style.color = "#FF0000";
	}
	else
	{
		document.getElementById('mob').innerHTML ='';
		document.getElementById('mob').style.color = "#00AF33";
	}
}


function email_validation()
{
	'use strict';
	var inputxt = document.getElementById('email');
	var inputtxt = document.getElementById('email').value;
	var txt_len = inputtxt.length;
	var mail = /^\w+([\.\-]?\w+)*@\w+([\.\-]?\w+)*(\.\w{2,3})+$/;
	if (txt_len < 0 || !inputtxt.match(mail))
	{
		document.getElementById('em').innerHTML = 'Invalid email id';
		inputxt.focus();
		document.getElementById('em').style.color = "#FF0000";
	}
	else
	{
		document.getElementById('em').innerHTML ='';
		document.getElementById('em').style.color = "#00AF33";
	}
}


function passwd_validation()
{
	'use strict';
	var inputxt = document.getElementById('pwd');
	var inputtxt = document.getElementById('pwd').value;
	var txt_len = inputtxt.length;
	
	if (txt_len < 1)
	{
		document.getElementById('erpwd').innerHTML = 'Can not be empty';
		inputxt.focus();
		document.getElementById('erpwd').style.color = "#FF0000";
	}
	else if (txt_len < 6)
	{
		document.getElementById('erpwd').innerHTML ='Too short,must atleast 6 character';
		inputxt.focus();
		document.getElementById('erpwd').style.color = "#EC7063";
	}

	else if (txt_len < 8)
	{
		document.getElementById('erpwd').innerHTML ='Medium length';
		document.getElementById('erpwd').style.color = "#F39C12";
	}

	else
	{
		document.getElementById('erpwd').innerHTML ='Strong Password';
		document.getElementById('erpwd').style.color = "#58D68D";
	}

	

}

function dob_validation()
{
	'use strict';
	var inputd = document.getElementById('gen').value;
	var inputxt = document.getElementById('dob');
	var inputtxt = document.getElementById('dob').value;
	var year =     inputtxt.slice(0,4);
	console.log(inputd)
	var d = new Date();
	var dte = d.getFullYear();
	var age = dte-year
	
	if (inputd=='female' && age < 18) {


		document.getElementById('db').innerHTML = 'Age must be more than 18';
		inputxt.focus();
		document.getElementById('db').style.color = "#FF0000";

	}
	else if (inputd=='male' && age<21) {


		document.getElementById('db').innerHTML = 'Age must be more than 21';
		inputxt.focus();
		document.getElementById('db').style.color = "#FF0000";

	}
	else
	{
		document.getElementById('db').innerHTML ='';
		document.getElementById('db').style.color = "#00AF33";
	}
}


