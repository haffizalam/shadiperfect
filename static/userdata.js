/** complete profile data **/

function fathername_validation()
{
	'use strict';
	var inputxt = document.getElementById('faname');
	var inputtxt = document.getElementById('faname').value;
	var letters = /^[a-zA-Z]+$/
	if (!inputtxt.match(letters))
	{
		document.getElementById('fnm').innerHTML = '  cant be empty,only alphabet allowed.';
		inputxt.focus();
		document.getElementById('fnm').style.color = "#ECF0F1";
	}
	else
	{
		document.getElementById('fnm').innerHTML ='';
		document.getElementById('fnm').style.color = "#ECF0F1";
	}
}

function mothername_validation()
{
	'use strict';
	var inputxt = document.getElementById('mname');
	var inputtxt = document.getElementById('mname').value;
	var letters = /^[a-zA-Z]+$/
	if (!inputtxt.match(letters))
	{
		document.getElementById('mnm').innerHTML = '  cant be empty,only alphabet allowed.';
		inputxt.focus();
		document.getElementById('mnm').style.color = "#ECF0F1";
	}
	else
	{
		document.getElementById('mnm').innerHTML ='';
		document.getElementById('mnm').style.color = "#ECF0F1";
	}
}

function height_validation()
{
	'use strict';
	var inputxt = document.getElementById('ht');
	var inputtxt = document.getElementById('ht').value;
	var letters = /^[+-]?\d+(\.\d+)?$/
	if (!inputtxt.match(letters))
	{
		document.getElementById('hei').innerHTML = 'cant be empty,only number allowed.';
		inputxt.focus();
		document.getElementById('hei').style.color = "#ECF0F1";
	}
	else
	{
		document.getElementById('hei').innerHTML ='';
		document.getElementById('hei').style.color = "#ECF0F1";
	}
}

function prof_validation()
{
	'use strict';
	var inputxt = document.getElementById('prof');
	var inputtxt = document.getElementById('prof').value;
	var letters = /^[a-zA-Z]+$/
	if (!inputtxt.match(letters))
	{
		document.getElementById('prf').innerHTML = 'cant be empty,only alphabet allowed.';
		inputxt.focus();
		document.getElementById('prf').style.color = "#ECF0F1";
	}
	else
	{
		document.getElementById('prf').innerHTML ='';
		document.getElementById('prf').style.color = "#ECF0F1";
	}
}

function dist_validation()
{
	'use strict';
	var inputxt = document.getElementById('dist');
	var inputtxt = document.getElementById('dist').value;
	var letters = /^[a-zA-Z]+$/
	if (!inputtxt.match(letters))
	{
		document.getElementById('dis').innerHTML = 'cant be empty,only alphabet allowed.';
		inputxt.focus();
		document.getElementById('dis').style.color = "#ECF0F1";
	}
	else
	{
		document.getElementById('dis').innerHTML ='';
		document.getElementById('dis').style.color = "#ECF0F1";
	}
}

function pin_validation()
{
	'use strict';
	var inputxt = document.getElementById('pin');
	var inputtxt = document.getElementById('pin').value;
	var txt_len = inputtxt.length;
	
	var letters = /^[0-9]+$/
	if (!inputtxt.match(letters) && !txt_len==6)
	{
		document.getElementById('dis').innerHTML = 'cant be empty,only number allowed.';
		inputxt.focus();
		document.getElementById('dis').style.color = "#ECF0F1";
	}
	else
	{
		document.getElementById('dis').innerHTML ='';
		document.getElementById('dis').style.color = "#ECF0F1";
	}
}

