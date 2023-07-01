const form = document.getElementById('form');
const email = document.getElementById('email');
const password = document.getElementById('password');
form.addEventListener('submit', e => {
	e.preventDefault();
	
	checkInputs();
});

function checkInputs() {
	// trim to remove the whitespaces
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	/*Validacion de email*/
	if(emailValue === '') {
		setErrorFor(email, "Correo no valido");
	} 
    else if (!isEmail(emailValue)) {
		setErrorFor(email, "");
	} 

    /*Usuario admin*/
    if(emailValue === "admin@gmail.com") {
        if(passwordValue === 'admin123'){
            setSuccessFor(password);
        }
        else{
            setErrorFor(password, "Contraseña incorrecta");
        }
	} 
    else{
        setErrorFor(password, "Contraseña no valida");
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