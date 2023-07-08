const form = document.getElementById('form');
const usuario = document.getElementById('username');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

form.addEventListener('submit', e => {
	
	checkInputs();
});

function checkInputs() {
	// trim to remove the whitespaces
	const usuarioValue = usuario.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();
	/*Validacion de usuario*/
	if(usuarioValue === '') {
		setErrorFor(usuario, "");
	} else {
		setSuccessFor(usuario);
	}
	/*Validacion de contraseña*/
	if(passwordValue === '') {
		setErrorFor(password, "");
	} else {
		setSuccessFor(password);
	}
	
	if(password2Value === '') {
		setErrorFor(password2, "");
	} else if(passwordValue !== password2Value) {
		setErrorFor(password2, "");
	} else{
		setSuccessFor(password2);
	}
}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}

function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}