var log, pass, email, pass1;
var user = [];
var names = [];
var n = 0;
var font;

function load(x){
	document.getElementById("a1").innerText = "Логин " + x;
		
	document.getElementById("a").remove();
	document.getElementById("b").remove();
	document.getElementById("b1").remove();
	document.getElementById("lg-btn").remove();
	document.getElementById("rg").remove();
		
	document.getElementById("log-bl").align = "center";
	var b = document.createElement("button");
	b.className = "btn btn-light";
	b.innerText = "Аккаунт";
	document.getElementById("log-bl").appendChild(b);
		
	if (document.location.href === "file:///C:/Python%2038/PyProjects/Django_/Index.html") {
		document.getElementById("frm").title= "Приятного пользования!";
		
		var lst = document.getElementsByClassName("f");
		for (var i = 0; i < 9; i++) {
				lst[i].disabled = false;
			}
	}
}

function login() {
	log = document.getElementById("a").value;
	pass = document.getElementById("b").value;
	user = [log, pass];
	if (user[0] != "")  {
		document.getElementById("a1").style.backgroundColor = "#ebfaca";
		if (user[1] != "") {
			alert(`Добро пожаловать, ${log}!`);
			document.getElementById("b1").style.backgroundColor = "#ebfaca";
			load(log);
		}
		
		else {
			alert("Введите пароль!");
			document.getElementById("b1").style.backgroundColor = "red";}
		}
	
	else {
		alert("Введите логин!");
		document.getElementById("a1").style.backgroundColor = "red";}
}


function note() {
	var head = document.getElementById("NoteHead").value;
	var t = document.getElementById("NoteText").value;
	var elem = document.getElementById("list");

	if (head != "" && !names.includes(head)) {
		var block = document.createElement("div");
		block.className = "wrapper bl";
		block.id = n;
		n++;
		
		var newP = document.createElement("li");
		newP.innerText = head + " — " + Date();
		
		var newB = document.createElement("button");
		newB.id = n;
		newB.className = "btn btn-danger";
		newB.innerText = "Удалить";

		
		block.appendChild(newP);
		block.appendChild(newB);
		elem.appendChild(block);
		names.push(head);
		
		var obj_button = document.getElementById("" + n);
		var obj_block = document.getElementById("" + (n-1));
		
		obj_button.addEventListener("click", function() {
			x = parseInt(obj_button.id);
			document.getElementById(""+x).remove();
			document.getElementById(""+(x-1)).remove();
			names.pop(x-2);
		})

		document.getElementById("NoteHead").value = null;
		document.getElementById("NoteText").value = null;
		n++;
	}
	else {
		alert("Введите корректное название!");
		document.getElementById("NoteHead").style.color = "red";
	}
}

function reg() {
	email = document.getElementById("e");
	log = document.getElementById("a");
	pass = document.getElementById("b");
	pass1 = document.getElementById("bb");
	
	user = [email.value, log.value, pass.value, pass1.value];
	
	if (user[0] != "") {
		document.getElementById("e1").style.backgroundColor = "#ebfaca";
		if (user[1] != "") {
			document.getElementById("a1").style.backgroundColor = "#ebfaca";
			if (user[2] != "") {
				document.getElementById("b1").style.backgroundColor = "#ebfaca";
				if (user[3] === user[2]) {
					document.getElementById("bb1").style.backgroundColor = "#ebfaca";
					alert(`Добро пожаловать, ${log.value}!`);
					email.value = null;
					log.value = null;
					pass.value = null;
					pass1.value = null;
					document.location.href = "Index.html";
					load(log.value);
				}
				else {
					alert("Пароль не совпадает!")
					document.getElementById("bb1").style.backgroundColor = "red";
					pass1.value = null;
				}
			}
			else {
				alert("Придумайте пароль!")
				document.getElementById("b1").style.backgroundColor = "red";
			}
		}
		else {
			alert("Придумайте логин!")
			document.getElementById("a1").style.backgroundColor = "red";
		}
	}
	else {
		alert("Введите e-mail!");
		document.getElementById("e1").style.backgroundColor = "red";
	}
}

function ChangeFontSize() {
	var size = document.getElementById("f_size").value;
	document.getElementById("NoteText").style.fontSize = size + "px";
}

function ChangeFontWeight() {
	var weight = document.getElementById("f_weight").value;
	document.getElementById("NoteText").style.fontWeight = weight + "px";
}

function SetFont(x) {
	font = x;
	alert(font);
}