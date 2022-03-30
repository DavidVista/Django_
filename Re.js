var login, pass;
var user = [];
var names = [];
var n = 0;

function get(){
	login = document.getElementById("a").value;
	pass = document.getElementById("b").value;
	user = [login, pass];
	if (user[0] != "") {
		document.getElementById("a1").style.backgroundColor = "#ebfaca";
		if (user[1] != "") {
		alert(`Добро пожаловать, ${login}!`);
		document.getElementById("b1").style.backgroundColor = "#ebfaca";
		document.getElementById("a").value = null;
		document.getElementById("b").value = null; }
		else {
			alert("Введите пароль!");
			document.getElementById("b1").style.backgroundColor = "red";
		}
	}
	else {
		alert("Введите логин!");
		document.getElementById("a1").style.backgroundColor = "red";
	}
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
		alert("Введите название!");
		document.getElementById("NoteHead").style.color = "red";
	}
}

